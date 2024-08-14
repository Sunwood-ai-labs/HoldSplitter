# utils.py
import bpy
import bmesh
import numpy as np
import time
import csv
from mathutils import Vector, Matrix

def log(message):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}")

def clear_scene():
    log("シーンをクリアしています...")
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    log("シーンのクリアが完了しました。")

def export_to_csv(vertices, normals, output_path):
    log(f"点群と法線情報をCSVに出力しています: {output_path}")
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['X', 'Y', 'Z', 'Normal_X', 'Normal_Y', 'Normal_Z'])
        for vertex, normal in zip(vertices, normals):
            writer.writerow([vertex[0], vertex[1], vertex[2], normal[0], normal[1], normal[2]])
    log("CSV出力が完了しました。")

def offset_vertices(vertices, normal, offset):
    """頂点を法線方向に指定した距離だけオフセットする"""
    offset_vector = Vector(normal) * offset
    return [Vector(v) + offset_vector for v in vertices]

def create_vertices_mesh(vertices, normal, name="Vertices_Mesh", offset=0):
    log(f"頂点メッシュを作成しています: {name}")
    mesh = bpy.data.meshes.new(name=f"{name}_Mesh")
    
    # 頂点をZ軸周りに90度回転
    rotation_matrix = Matrix.Rotation(np.radians(-90), 4, 'Z')
    verts = [rotation_matrix @ Vector(v) for v in vertices]
    
    mesh.from_pydata(verts, [], [])
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    log(f"頂点メッシュの作成が完了しました: {name}")
    return obj

# その他のユーティリティ関数をここに追加
