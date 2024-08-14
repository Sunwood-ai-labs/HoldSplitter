import subprocess
import sys
import os

# Blenderの実行ファイルへのパス
# Windowsの場合の例: r"C:\Program Files\Blender Foundation\Blender 3.6\blender.exe"
# MacOSの場合の例: "/Applications/Blender.app/Contents/MacOS/Blender"
BLENDER_PATH = r"C:\Program Files\Blender Foundation\Blender 4.2\blender.exe"

def run_blender_script(fbx_path):
    # Blender内で実行するスクリプトのパス
    blender_script_path = os.path.join(os.path.dirname(__file__), "blender_script.py")
    # blender_script_path = os.path.join(os.path.dirname(__file__), "refine_wall_hold_separation.py")
    
    # Blenderをバックグラウンドモードで実行
    subprocess.run([
        BLENDER_PATH,
        "--background",
        "--python", blender_script_path,
        "--", fbx_path  # "--" 以降の引数はBlenderスクリプトに渡される
    ])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法: python main_script.py <fbx_file_path>")
        sys.exit(1)

    fbx_path = sys.argv[1]
    run_blender_script(fbx_path)
