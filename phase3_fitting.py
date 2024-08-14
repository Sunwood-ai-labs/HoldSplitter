# phase3_fitting.py
import bpy
import numpy as np
from mathutils import Vector, Matrix
from utils import log, offset_vertices
import bmesh

def create_wall_aligned_plane(vertices, normal, offset=0):
    log("壁に沿った平面を作成しています...")
    
    # 頂点をZ軸周りに90度回転
    rotation_matrix = Matrix.Rotation(np.radians(0), 4, 'Z')
    rotated_vertices = [rotation_matrix @ Vector(v) for v in vertices]
    rotated_normal = rotation_matrix @ normal
    
    # 頂点をオフセット
    offset = -0.2
    if offset != 0:
        rotated_vertices = offset_vertices(rotated_vertices, rotated_normal, offset)
    
    # 点群の中心を計算
    center = sum((Vector(v) for v in rotated_vertices), Vector()) / len(rotated_vertices)
    log(f"点群の中心: {center}")

    # 主成分分析（PCA）を使用して平面の向きを計算
    points = np.array(rotated_vertices) - center
    cov_matrix = np.cov(points.T)
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    
    # 最小の固有値に対応する固有ベクトルが法線方向
    pca_normal = eigenvectors[:, np.argmin(eigenvalues)]
    
    # 元の法線との向きを合わせる
    if np.dot(pca_normal, rotated_normal) < 0:
        pca_normal = -pca_normal
    
    log(f"PCAによる法線: {pca_normal}")
    log(f"元の法線: {rotated_normal}")

    # 平面の回転を計算
    rotation = Vector(pca_normal).to_track_quat('-Z', 'Y')
    
    # 平面のサイズを計算
    projected_points = points @ eigenvectors
    min_coords = np.min(projected_points, axis=0)
    max_coords = np.max(projected_points, axis=0)
    size = max_coords - min_coords
    size = [5, 5]
    log(f"平面のサイズ: 幅={size[0]:.2f}, 高さ={size[1]:.2f}")

    # 平面メッシュを作成
    bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, location=center)
    plane_obj = bpy.context.active_object
    plane_obj.name = "Wall_Aligned_Plane"
    plane_obj.rotation_euler = rotation.to_euler()
    plane_obj.scale = Vector((size[0], size[1], 1))
    
    # 平面を半透明にする
    mat = bpy.data.materials.new(name="Transparent_Wall")
    mat.use_nodes = True
    mat.node_tree.nodes.clear()
    
    node_principled = mat.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
    node_output = mat.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    
    mat.node_tree.links.new(node_principled.outputs['BSDF'], node_output.inputs['Surface'])
    
    node_principled.inputs['Base Color'].default_value = (0, 1, 0, 1)  # 緑色
    node_principled.inputs['Alpha'].default_value = 0.3
    
    mat.blend_method = 'BLEND'
    
    plane_obj.data.materials.append(mat)
    
    log("壁に沿った平面の作成が完了しました。")
    
    return plane_obj

def fit_plane_least_squares(points):
    """
    最小二乗法を使用して点群に最適な平面を計算します。
    """
    log("最小二乗法で平面をフィッティングしています...")
    
    # 点群の中心を計算
    centroid = np.mean(points, axis=0)
    
    # 中心を原点に移動
    centered_points = points - centroid
    
    # 共分散行列を計算
    cov = np.cov(centered_points.T)
    
    # 固有値と固有ベクトルを計算
    eigenvalues, eigenvectors = np.linalg.eig(cov)
    
    # 最小の固有値に対応する固有ベクトルが法線方向
    normal = eigenvectors[:, np.argmin(eigenvalues)]
    
    # 法線ベクトルを正規化
    normal = normal / np.linalg.norm(normal)
    
    # 平面の方程式: ax + by + cz + d = 0
    d = -np.dot(normal, centroid)
    
    log(f"フィッティングされた平面の方程式: {normal[0]:.4f}x + {normal[1]:.4f}y + {normal[2]:.4f}z + {d:.4f} = 0")
    
    return normal, centroid, d

def create_least_squares_plane(vertices, offset=0):
    log("最小二乗法で算出した平面を作成しています...")
    
    # 頂点をZ軸周りに90度回転
    rotation_matrix = Matrix.Rotation(np.radians(0), 4, 'Z')
    rotated_vertices = [rotation_matrix @ Vector(v) for v in vertices]
    
    # NumPy配列に変換
    points = np.array(rotated_vertices)
    
    # 最小二乗法でフィッティング
    normal, center, _ = fit_plane_least_squares(points)
    # 頂点をオフセット
    if offset != 0:
        points = offset_vertices(points, normal, offset)
        center += Vector(normal) * offset
    
    # 平面の回転を計算
    rotation = Vector(normal).to_track_quat('-Z', 'Y')
    
    # 平面のサイズを計算
    projected_points = points - center
    projected_points = np.dot(projected_points, rotation.to_matrix().transposed())
    min_coords = np.min(projected_points, axis=0)
    max_coords = np.max(projected_points, axis=0)
    size = max_coords - min_coords
    
    log(f"平面のサイズ: 幅={size[0]:.2f}, 高さ={size[1]:.2f}")

    # 平面メッシュを作成
    bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, location=center)
    plane_obj = bpy.context.active_object
    plane_obj.name = "Least_Squares_Fitted_Plane"
    plane_obj.rotation_euler = rotation.to_euler()
    plane_obj.scale = Vector((size[0], size[1], 1))
    
    # 平面を半透明にする
    mat = bpy.data.materials.new(name="Transparent_LS_Plane")
    mat.use_nodes = True
    mat.node_tree.nodes.clear()
    
    node_principled = mat.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
    node_output = mat.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    
    mat.node_tree.links.new(node_principled.outputs['BSDF'], node_output.inputs['Surface'])
    
    node_principled.inputs['Base Color'].default_value = (1, 0, 0, 1)  # 赤色
    node_principled.inputs['Alpha'].default_value = 0.3
    
    mat.blend_method = 'BLEND'
    
    plane_obj.data.materials.append(mat)
    
    log("最小二乗法で算出した平面の作成が完了しました。")
    return plane_obj

def separate_mesh_by_plane(obj, plane_obj):
    log("平面を使用してメッシュを分離しています...")
    
    # plane_objをZ軸で-90度回転
    rotation_matrix = Matrix.Rotation(np.radians(90), 4, 'Z')
    plane_obj.rotation_euler.rotate(rotation_matrix)
    plane_obj.location = rotation_matrix @ plane_obj.location

    # オブジェクトをアクティブにし、編集モードに入る
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
    
    # BMeshを取得
    bm = bmesh.from_edit_mesh(obj.data)
    
    # 平面の法線と中心点を取得
    plane_normal = plane_obj.rotation_euler.to_matrix() @ Vector((0, 0, 1))
    plane_point = plane_obj.location
    
    # 平面の法線と点を使用して、頂点を分類
    above_plane = set()
    for v in bm.verts:
        if (v.co - plane_point).dot(plane_normal) > 0:
            above_plane.add(v)
    
    # 面を選択
    for f in bm.faces:
        if any(v in above_plane for v in f.verts):
            f.select = True
        else:
            f.select = False
    
    # 選択された部分を分離
    bpy.ops.mesh.separate(type='SELECTED')
    
    # オブジェクトモードに戻る
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # 新しく作成されたオブジェクトを取得
    new_obj = [obj for obj in bpy.context.selected_objects if obj != bpy.context.active_object][0]
    
    # plane_objをZ軸で-90度回転
    rotation_matrix = Matrix.Rotation(np.radians(0), 4, 'Z')
    plane_obj.rotation_euler.rotate(rotation_matrix)
    
    log("メッシュの分離が完了しました。")
    return new_obj

def main(vertices, dominant_normal, offset=0):
    log("壁に沿った平面を作成しています...")
    wall_plane, wall_normal, wall_center = create_wall_aligned_plane(vertices, dominant_normal, offset)

    log("最小二乗法で算出した平面を作成しています...")
    ls_plane = create_least_squares_plane(vertices, offset)

    return wall_plane, ls_plane, wall_normal, wall_center

if __name__ == "__main__":
    # テスト用のコード
    pass
