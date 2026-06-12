AI with liqirui1145-create开发，由本人输入提示词，doubao模型
默认封面：https://commons.wikimedia.org/wiki/File:Xinjiang_Old_and_young_(Populus_diversifolia_%E8%83%A1%E6%9D%A8)_(4973519309).jpg
# 多媒体播放器 (Media Player)

基于 PyQt6 + VLC 的多媒体播放器，支持音频/视频播放、LRC歌词同步、封面显示等功能。

## 功能特性

- 🎵 支持多种音视频格式（MP3、FLAC、MP4、MKV等）
- 🎤 音频元数据读取（艺术家、专辑、采样率等）
- 📖 LRC歌词自动加载与同步显示
- 📷 专辑封面显示（支持内嵌封面和自定义默认封面）
- ⚡ 倍速播放（0.5x - 2.0x）
- ⌨️ 丰富的键盘快捷键

## 安装依赖

```bash
pip install pyqt6 python-vlc mutagen pillow
```

## 运行

```bash
python p2.py
```

## 快捷键

| 按键 | 功能 |
|------|------|
| 空格 | 播放/暂停 |
| ← | 回退10秒 |
| → | 快进10秒 |
| ↑ | 音量+5 |
| ↓ | 音量-5 |
