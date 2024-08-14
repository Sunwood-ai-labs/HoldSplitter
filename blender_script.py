# main.py
import bpy
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from utils import log
import phase1_init
import phase2_separation
import phase3_fitting

def main():
    if "--" in sys.argv:
        argv = sys.argv[sys.argv.index("--") + 1:]
    else:
        argv = []
    
    if len(argv) < 1:
        log("エラー: FBXファイルのパスが指定されていません。")
        return

    fbx_path = argv[0]
    offset = float(argv[1]) if len(argv) > 1 else 0  # オフセット値を引数から取得

    log(f"処理を開始します: {fbx_path}")
    log(f"オフセット値: {offset}")

    # Phase 1: 初期化とインポート
    imported_obj, output_dir = phase1_init.main()

    # Phase 2: 壁とホールドの分離
    wall_obj, hold_obj, vertices_mesh, dominant_normal = phase2_separation.main(imported_obj, output_dir)

    # Phase 3: 平面フィッティングと可視化
    wall_plane = phase3_fitting.create_wall_aligned_plane(
        [v.co for v in vertices_mesh.data.vertices], dominant_normal, offset
    )
    # ls_plane = phase3_fitting.create_least_squares_plane(
    #     [v.co for v in vertices_mesh.data.vertices], offset
    # )

    # Wall_Aligned_Planeを使用してホールドと壁を分離
    separated_hold = phase3_fitting.separate_mesh_by_plane(imported_obj, wall_plane)
    separated_hold.name = "Separated_Holds"
    hold_obj.name = "Remaining_Wall"

    # 結果の保存
    output_path = os.path.join(output_dir, "separated_model.blend")
    bpy.ops.wm.save_as_mainfile(filepath=output_path)
    log(f"結果を保存しました: {output_path}")

    log("処理が完了しました。")

if __name__ == "__main__":
    main()
