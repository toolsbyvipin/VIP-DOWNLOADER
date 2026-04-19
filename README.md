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

Dependencies 
```
pip install yt-dlp spotdl instaloader rich
winget install --id Gyan.FFmpeg -e && pip install yt-dlp spotdl instaloader rich
python -m pip install yt-dlp rich
```
```
Invoke-WebRequest -Uri "https://github.com/toolsbyvipin/VIP-DOWNLOADER/archive/refs/heads/main.zip" -OutFile "$env:USERPROFILE\Downloads\VIP-DOWNLOADER.zip"
Expand-Archive -Path "$env:USERPROFILE\Downloads\VIP-DOWNLOADER.zip" -DestinationPath "$env:USERPROFILE\Downloads\" -Force
cd Downloads
cd VIP-DOWNLOADER--main
python vipdl.py
```

### Termux 

```
pkg update
pkg upgrade -y
pkg install -y apt
pkg install -y dpkg
pkg update && pkg install python ffmpeg && pip install yt-dlp spotdl instaloader rich && wget https://github.com/toolsbyvipin/VIP-DOWNLOADER.git -O vipdl.py && python vipdl.py
```
Download any video from here it will not save on local device , to save it  copy to download section 

```
cp -r ~/VIP_Downloads/* /sdcard/Download/
```
