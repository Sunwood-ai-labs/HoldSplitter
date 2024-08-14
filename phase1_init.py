# phase1_init.py
import bpy
import os
import sys
from utils import log, clear_scene

def import_fbx(file_path):
    log(f"FBXファイルをインポートしています: {file_path}")
    bpy.ops.import_scene.fbx(filepath=file_path)
    
    mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH']
    
    if not mesh_objects:
        raise ValueError("FBXファイルにメッシュオブジェクトが含まれていません。")
    
    log(f"インポートされたメッシュオブジェクト数: {len(mesh_objects)}")
    
    bpy.ops.object.select_all(action='DESELECT')
    mesh_objects[0].select_set(True)
    bpy.context.view_layer.objects.active = mesh_objects[0]
    
    log(f"アクティブオブジェクト: {mesh_objects[0].name}")
    return mesh_objects[0]

def main():
    if "--" in sys.argv:
        argv = sys.argv[sys.argv.index("--") + 1:]
    else:
        argv = []
    
    if len(argv) < 1:
        log("エラー: FBXファイルのパスが指定されていません。")
        return

    fbx_path = argv[0]
    log(f"処理を開始します: {fbx_path}")

    clear_scene()
    imported_obj = import_fbx(fbx_path)
    
    # 次のフェーズのために必要な情報を返す
    return imported_obj, os.path.dirname(fbx_path)

if __name__ == "__main__":
    main()
