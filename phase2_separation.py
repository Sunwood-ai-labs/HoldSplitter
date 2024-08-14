# phase2_separation.py
import bpy
import bmesh
import numpy as np
from mathutils import Vector
from utils import log, export_to_csv, create_vertices_mesh
import os
def find_dominant_normal(bm, angle_threshold=np.radians(10)):
    normal_groups = {}
    for face in bm.faces:
        normal = tuple(round(n, 2) for n in face.normal)
        if normal not in normal_groups:
            normal_groups[normal] = []
        normal_groups[normal].append(face)
    
    dominant_normal = max(normal_groups, key=lambda n: len(normal_groups[n]))
    dominant_faces = normal_groups[dominant_normal]
    
    # 角度閾値内の面も含める
    for normal, faces in normal_groups.items():
        if normal != dominant_normal:
            dot_product = np.dot(dominant_normal, normal)
            # ドット積を-1から1の範囲に制限
            dot_product = max(-1, min(1, dot_product))
            angle = np.arccos(dot_product)
            if angle < angle_threshold:
                dominant_faces.extend(faces)
    
    return Vector(dominant_normal), set(dominant_faces)

def separate_wall_and_holds(obj, output_dir):
    if obj.type != 'MESH':
        raise ValueError("選択されたオブジェクトはメッシュではありません。")

    log(f"オブジェクト '{obj.name}' の壁とホールドを分離しています...")
    
    bpy.ops.object.mode_set(mode='EDIT')
    bm = bmesh.from_edit_mesh(obj.data)
    bm.faces.ensure_lookup_table()
    bm.verts.ensure_lookup_table()

    log("主要な法線を検出しています...")
    dominant_normal, wall_component = find_dominant_normal(bm)
    log(f"検出された主要な法線: {dominant_normal}")
    
    total_area = sum(f.calc_area() for f in bm.faces)
    wall_area = sum(f.calc_area() for f in wall_component)
    
    log(f"検出された壁の面積比: {wall_area / total_area:.2%}")
    
    vertices = [v.co.to_tuple() for f in wall_component for v in f.verts]
    normals = [f.normal.to_tuple() for f in wall_component for _ in range(len(f.verts))]
    
    csv_path = os.path.join(output_dir, "wall_points_and_normals.csv")
    export_to_csv(vertices, normals, csv_path)
    
    vertices_mesh = create_vertices_mesh(vertices, dominant_normal, name="Wall_Vertices")
    
    bpy.ops.mesh.select_all(action='DESELECT')
    for face in wall_component:
        face.select = True

    log("オブジェクトを分離しています...")
    bpy.ops.mesh.separate(type='SELECTED')
    bpy.ops.object.mode_set(mode='OBJECT')

    wall_obj = [obj for obj in bpy.context.selected_objects if obj != bpy.context.active_object][0]
    hold_obj = bpy.context.active_object

    wall_obj.name = "Wall"
    hold_obj.name = "Holds"

    log(f"壁のオブジェクト: {wall_obj.name}")
    log(f"ホールドのオブジェクト: {hold_obj.name}")

    return wall_obj, hold_obj, vertices_mesh, dominant_normal

def main(imported_obj, output_dir):
    wall_obj, hold_obj, vertices_mesh, dominant_normal = separate_wall_and_holds(imported_obj, output_dir)
    return wall_obj, hold_obj, vertices_mesh, dominant_normal

if __name__ == "__main__":
    # テスト用のコード
    pass
