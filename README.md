<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/HoldSplitter.png" width="100%">
<br>
<h1 align="center">HoldSplitter</h1>
<h2 align="center">
  ～ Unmasking the Wall: Hold by Hold ～
<br>
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/hold-splitter">
<img alt="PyPI - Format" src="https://img.shields.io/pypi/format/hold-splitter">
<img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/hold-splitter">
<img alt="PyPI - Status" src="https://img.shields.io/pypi/status/hold-splitter">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/hold-splitter">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/hold-splitter">
<a href="https://github.com/Sunwood-ai-labs/HoldSplitter" title="Go to GitHub repo"><img src="https://img.shields.io/static/v1?label=HoldSplitter&message=Sunwood-ai-labs&color=blue&logo=github"></a>
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Sunwood-ai-labs/HoldSplitter">
<a href="https://github.com/Sunwood-ai-labs/HoldSplitter"><img alt="forks - Sunwood-ai-labs" src="https://img.shields.io/github/forks/HoldSplitter/Sunwood-ai-labs?style=social"></a>
<a href="https://github.com/Sunwood-ai-labs/HoldSplitter"><img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/Sunwood-ai-labs/HoldSplitter"></a>
<a href="https://github.com/Sunwood-ai-labs/HoldSplitter"><img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/Sunwood-ai-labs/HoldSplitter"></a>
<img alt="GitHub Release" src="https://img.shields.io/github/v/release/Sunwood-ai-labs/HoldSplitter?color=red">
<img alt="GitHub Tag" src="https://img.shields.io/github/v/tag/Sunwood-ai-labs/HoldSplitter?sort=semver&color=orange">
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/HoldSplitter/publish-to-pypi.yml">
<br>
<p align="center">
  <a href="https://hamaruki.com/"><b>[🌐 Website]</b></a> •
  <a href="https://github.com/Sunwood-ai-labs"><b>[🐱 GitHub]</b></a>
  <a href="https://x.com/hAru_mAki_ch"><b>[🐦 Twitter]</b></a> •
  <a href="https://hamaruki.com/"><b>[🍀 Official Blog]</b></a>
</p>

   <br>

   <a href="https://github.com/Sunwood-ai-labs/HoldSplitter/blob/main/README.md"><img src="https://img.shields.io/badge/ドキュメント-日本語-white.svg" alt="JA doc"/></a>
   <a href="https://github.com/Sunwood-ai-labs/HoldSplitter/blob/main/docs/README.en.md"><img src="https://img.shields.io/badge/english-document-white.svg" alt="EN doc"></a>

</h2>

</p>

>[!IMPORTANT]
>このリポジトリのリリースノートやREADME、コミットメッセージの9割近くは[claude.ai](https://claude.ai/)や[ChatGPT4](https://chatgpt.com/)を活用した[AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II)で生成しています。

HoldSplitterは、ボルダリング壁面の3Dモデルからホールドを分離し、クライミングルートの分析と理解を革新的に支援するPythonツールです。

## 🎥 Demo

※デモ動画は後日追加予定です。

## 🚀 Getting Started

HoldSplitterをインストールするには、以下のコマンドを実行してください：

```bash
pip install hold-splitter
```

使用例：

```python
from hold_splitter.main_script import run_blender_script

run_blender_script(fbx_path="path/to/your/model.fbx", offset=0.1, split_threshold=0.1)
```

## 📝 Features

- FBXファイルからのボルダリング壁面3Dモデルの読み込み
- 壁面とホールドの自動分離
- 分離されたホールドの個別オブジェクト化
- Blenderを利用した高度な3D処理
- Blenderファイル(.blend)形式での出力
- Unreal Engine 5 (UE5)などの3Dソフトウェアへの簡単なインポート
  
## 🛠 Requirements

- Python 3.10以上
- Blender 4.2以上

## 🤝 Contributing

プロジェクトへの貢献を歓迎します！バグレポート、機能リクエスト、プルリクエストなど、お気軽にご参加ください。

## 📄 License

このプロジェクトはMITライセンスで公開されています。

## 🙏 Acknowledgements

このプロジェクトは、以下の素晴らしいオープンソースプロジェクトに支えられています：

- Blender
- NumPy
- Open3D
- PyMeshLab
- Matplotlib
- Loguru
- tqdm

## 🔄 Updates

- **[v0.1.0](https://github.com/Sunwood-ai-labs/HoldSplitter/releases/tag/v0.1.0):** 初期リリース。FBXファイルからのホールド分離基本機能を実装。
- **[v0.1.1](https://github.com/Sunwood-ai-labs/HoldSplitter/releases/tag/v0.1.1):** Blenderスクリプトの改善。ホールド分離の精度向上。
- **[v0.2.0](https://github.com/Sunwood-ai-labs/HoldSplitter/releases/tag/v0.2.0):**  PyPI パッケージ名を "HoldSplitter" から "hold-splitter" に変更し、README を更新。 
- **[v0.3.2](https://github.com/Sunwood-ai-labs/HoldSplitter/releases/tag/v0.3.2):**  README の更新、PyPI パッケージ名を "HoldSplitter" から "hold-splitter" に変更しました。 

## 🎮 UE5 Integration

HoldSplitterは、処理結果をBlenderファイル(.blend)形式で出力することで、Unreal Engine 5 (UE5)などの3Dソフトウェアやゲームエンジンへの簡単なインポートを可能にしています。この設計により以下の利点があります：

1. **直接インポート**: UE5を含む多くの3D制作ソフトウェアでBlenderファイルを直接インポートできます。

2. **データ保持**: 3Dモデルのジオメトリだけでなく、マテリアル、テクスチャ、階層構造なども保持されます。

3. **整理された構造**: 分離されたホールドは個別のコレクション内に整理され、UE5でインポート時に自動的に整理された状態で取り込めます。

4. **柔軟な編集**: 必要に応じて、後からBlenderで追加の編集や調整を行うことが容易です。

5. **ゲーム開発向け**: クライミングシミュレーターやVR体験の開発など、多様な応用シナリオをサポートします。

これにより、HoldSplitterは3Dモデル処理から実際のゲーム開発まで、シームレスなワークフローを提供します。