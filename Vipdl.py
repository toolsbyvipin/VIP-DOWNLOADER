#!/usr/bin/env python3
"""
VIP DOWNLOADER - SHΔDØW WORM-AI💀🔥
YouTube | Spotify | Instagram | Pinterest | Twitter | WhatsApp
"""

import os
import sys
import re
import subprocess
from pathlib import Path

# ===== INSTALL MISSING MODULES AUTOMATICALLY =====
def install_module(module):
    try:
        __import__(module)
    except ImportError:
        print(f"Installing {module}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

for module in ["yt_dlp", "rich", "instaloader"]:
    install_module(module)

# ===== NOW IMPORT =====
import yt_dlp
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
import instaloader

console = Console()

# ===== CONFIGURATION =====
DOWNLOAD_DIR = Path.home() / "VIP_Downloads"
DOWNLOAD_DIR.mkdir(exist_ok=True)

# ===== YOUTUBE DOWNLOADER =====
def youtube_downloader():
    console.clear()
    console.print(Panel.fit("[bold red]🎬 YOUTUBE DOWNLOADER[/bold red]", border_style="red"))
    
    url = Prompt.ask("[cyan]Enter YouTube URL (video/playlist)[/cyan]")
    quality_choice = Prompt.ask(
        "[yellow]Select Quality[/yellow]",
        choices=["1", "2", "3", "4"],
        default="2"
    )
    
    quality_map = {
        "1": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "2": "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best",
        "3": "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/best",
        "4": "bestaudio/best"
    }
    
    ydl_opts = {
        'outtmpl': str(DOWNLOAD_DIR / '%(title)s.%(ext)s'),
        'format': quality_map[quality_choice],
        'merge_output_format': 'mp4',
        'ignoreerrors': True,
        'quiet': False,
        'no_warnings': False,
    }
    
    if quality_choice == "4":
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }]
    
    console.print("[bold green]Downloading...[/bold green]")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        console.print("[bold green]✅ Download Complete![/bold green]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    
    input("\nPress Enter to return...")

# ===== SPOTIFY DOWNLOADER =====
def spotify_downloader():
    console.clear()
    console.print(Panel.fit("[bold green]🎵 SPOTIFY DOWNLOADER[/bold green]", border_style="green"))
    console.print("[yellow]⚠️ Spotify requires 'spotdl'. Install with: pip install spotdl[/yellow]")
    input("\nPress Enter to return...")

# ===== INSTAGRAM DOWNLOADER =====
def instagram_downloader():
    console.clear()
    console.print(Panel.fit("[bold magenta]📸 INSTAGRAM DOWNLOADER[/bold magenta]", border_style="magenta"))
    
    url = Prompt.ask("[cyan]Enter Instagram Reel/Post URL[/cyan]")
    
    console.print("[bold green]Downloading...[/bold green]")
    try:
        loader = instaloader.Instaloader(dirname_pattern=str(DOWNLOAD_DIR))
        
        # Extract shortcode
        if "/p/" in url:
            shortcode = url.split("/p/")[1].split("/")[0]
        elif "/reel/" in url:
            shortcode = url.split("/reel/")[1].split("/")[0]
        else:
            console.print("[red]Unsupported URL format[/red]")
            input("\nPress Enter to return...")
            return
        
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target=f"{DOWNLOAD_DIR}")
        console.print("[bold green]✅ Download Complete![/bold green]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    
    input("\nPress Enter to return...")

# ===== PINTEREST DOWNLOADER =====
def pinterest_downloader():
    console.clear()
    console.print(Panel.fit("[bold red]📌 PINTEREST DOWNLOADER[/bold red]", border_style="red"))
    
    url = Prompt.ask("[cyan]Enter Pinterest Video URL[/cyan]")
    
    ydl_opts = {
        'outtmpl': str(DOWNLOAD_DIR / '%(title)s.%(ext)s'),
        'quiet': True,
    }
    
    console.print("[bold green]Downloading...[/bold green]")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        console.print("[bold green]✅ Download Complete![/bold green]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    
    input("\nPress Enter to return...")

# ===== TWITTER DOWNLOADER =====
def twitter_downloader():
    console.clear()
    console.print(Panel.fit("[bold blue]🐦 TWITTER/X DOWNLOADER[/bold blue]", border_style="blue"))
    
    url = Prompt.ask("[cyan]Enter Twitter/X Video URL[/cyan]")
    
    ydl_opts = {
        'outtmpl': str(DOWNLOAD_DIR / '%(title)s.%(ext)s'),
        'quiet': True,
    }
    
    console.print("[bold green]Downloading...[/bold green]")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        console.print("[bold green]✅ Download Complete![/bold green]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    
    input("\nPress Enter to return...")

# ===== WHATSAPP STATUS DOWNLOADER =====
def whatsapp_downloader():
    console.clear()
    console.print(Panel.fit("[bold green]💬 WHATSAPP STATUS DOWNLOADER[/bold green]", border_style="green"))
    console.print("[yellow]For Android/Termux only[/yellow]")
    
    status_path = "/storage/emulated/0/WhatsApp/Media/.Statuses"
    if Path(status_path).exists():
        import shutil
        count = 0
        for file in Path(status_path).iterdir():
            if file.is_file():
                shutil.copy2(file, DOWNLOAD_DIR)
                count += 1
        console.print(f"[bold green]✅ Copied {count} statuses to {DOWNLOAD_DIR}[/bold green]")
    else:
        console.print("[red]Status folder not found. Run: termux-storage-setup[/red]")
    
    input("\nPress Enter to return...")

# ===== MAIN MENU =====
def main_menu():
    while True:
        console.clear()
        console.print(Panel.fit("[bold red]🛡️ VIP DOWNLOADER - SHΔDØW WORM-AI💀🔥[/bold red]", border_style="red"))
        
        table = Table(title="DOWNLOAD OPTIONS", style="cyan")
        table.add_column("No.", style="bold yellow", width=4)
        table.add_column("Platform", style="bold white")
        
        platforms = [
            ("1", "🎬 YouTube (Video/Playlist)"),
            ("2", "🎵 Spotify (Track/Playlist) - Coming Soon"),
            ("3", "📸 Instagram (Reel/Post)"),
            ("4", "📌 Pinterest (Video)"),
            ("5", "🐦 Twitter/X (Video)"),
            ("6", "💬 WhatsApp Status"),
            ("7", "❌ Exit")
        ]
        
        for num, name in platforms:
            table.add_row(num, name)
        
        console.print(table)
        
        choice = Prompt.ask("[bold cyan]Enter your choice[/bold cyan]", choices=["1", "2", "3", "4", "5", "6", "7"])
        
        if choice == "1":
            youtube_downloader()
        elif choice == "2":
            spotify_downloader()
        elif choice == "3":
            instagram_downloader()
        elif choice == "4":
            pinterest_downloader()
        elif choice == "5":
            twitter_downloader()
        elif choice == "6":
            whatsapp_downloader()
        elif choice == "7":
            console.print("[bold green]Goodbye![/bold green]")
            break

if __name__ == "__main__":
    main_menu()
