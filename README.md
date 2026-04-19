# VIP-DOWNLOADER

**The Ultimate Media Downloader** for YouTube, Spotify, Instagram, Pinterest, Twitter, and WhatsApp Status.

## ✨ Features
- 🎬 **YouTube** – Videos, playlists, audio (MP3)
- 🎵 **Spotify** – Tracks, playlists, albums (MP3)
- 📸 **Instagram** – Reels, posts
- 📌 **Pinterest** – Videos
- 🐦 **Twitter/X** – Videos
- 💬 **WhatsApp** – Status saver (Android/Termux)

## 🚀 One-Line Installation & Run

### Windows (PowerShell)
```
pip install yt-dlp spotdl instaloader rich
winget install --id Gyan.FFmpeg -e && pip install yt-dlp spotdl instaloader rich

python Desktop\vipd.py
```

### Termux 

```
pkg update
pkg upgrade -y
pkg install -y apt
pkg install -y dpkg
pkg update && pkg install python ffmpeg && pip install yt-dlp spotdl instaloader rich && wget https://github.com/toolsbyvipin/VIP-DOWNLOADER.git -O vipdl.py && python vipdl.py
```
