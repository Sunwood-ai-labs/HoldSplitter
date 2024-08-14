## HoldSplitter: Unmasking the Wall: Hold by Hold

<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/HoldSplitter.png" width="100%">
<br>
<h1 align="center">HoldSplitter</h1>
<h2 align="center">
  ～ Unmasking the Wall: Hold by Hold ～
<br>
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/HoldSplitter">
<img alt="PyPI - Format" src="https://img.shields.io/pypi/format/HoldSplitter">
<img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/HoldSplitter">
<img alt="PyPI - Status" src="https://img.shields.io/pypi/status/HoldSplitter">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/HoldSplitter">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/HoldSplitter">
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
>This repository's release notes, README, and commit messages are primarily generated using [claude.ai](https://claude.ai/) and [ChatGPT4](https://chatgpt.com/) through [AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), and [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II).

HoldSplitter is a Python tool that revolutionizes climbing route analysis and understanding by separating holds from 3D models of bouldering walls.

## 🎥 Demo

* Demo video will be added later.

## 🚀 Getting Started

To install HoldSplitter, run the following command:

```bash
pip install hold-splitter
```

Example usage:

```python
from hold_splitter.main_script import run_blender_script

run_blender_script(fbx_path="path/to/your/model.fbx", offset=0.1, split_threshold=0.1)
```

## 📝 Features

- Loads 3D models of bouldering walls from FBX files.
- Automatically separates the wall from the holds.
- Individualizes separated holds as separate objects.
- Advanced 3D processing using Blender.

## 🛠 Requirements

- Python 3.10 or later
- Blender 4.2 or later

## 🤝 Contributing

Contributions to the project are welcome! Feel free to contribute bug reports, feature requests, pull requests, etc.

## 📄 License

This project is licensed under the MIT license.

## 🙏 Acknowledgements

This project is built upon the shoulders of the following amazing open-source projects:

- Blender
- NumPy
- Open3D
- PyMeshLab
- Matplotlib
- Loguru
- tqdm

## 🔄 Updates

- **[v0.1.0](https://github.com/Sunwood-ai-labs/HoldSplitter/releases/tag/v0.1.0):** Initial release. Implements basic hold separation functionality from FBX files.
- **[v0.1.1](https://github.com/Sunwood-ai-labs/HoldSplitter/releases/tag/v0.1.1):** Improved Blender scripts. Enhanced hold separation accuracy.
- **[v0.2.0](https://github.com/Sunwood-ai-labs/HoldSplitter/releases/tag/v0.2.0):** Added CLI interface. Improved usability.

```