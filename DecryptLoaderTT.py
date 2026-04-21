#!/usr/bin/env python3
"""
DecryptLoaderTT - TikTok Video Downloader
Developer: Decryptious_ on Discord / Punchborn on IG
A command-line tool to download TikTok videos
"""

import os
import sys
import subprocess
import argparse
import re


def check_yt_dlp():
    """Check if yt-dlp is installed"""
    try:
        result = subprocess.run(
            ["yt-dlp", "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"[+] yt-dlp version: {version}")
            return True
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return False


def install_yt_dlp():
    """Install yt-dlp via pip"""
    print("[*] yt-dlp not found. Installing...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-U", "yt-dlp"],
            capture_output=False,
            check=True
        )
        print("[+] yt-dlp installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("[-] Failed to install yt-dlp.")
        print("    Try: python -m pip install yt-dlp")
        return False


def validate_tiktok_url(url):
    """Validate TikTok URL"""
    patterns = [
        r'tiktok\.com',
        r'vm\.tiktok\.com',
        r'vt\.tiktok\.com',
        r'tiktok\.com/t/\w+',
    ]
    return any(re.search(p, url, re.IGNORECASE) for p in patterns)


def download_tiktok(url, output_dir="downloads", quality="best"):
    """Download TikTok video with yt-dlp"""

    if not validate_tiktok_url(url):
        print(f"[-] Invalid TikTok URL: {url}")
        return False

    os.makedirs(output_dir, exist_ok=True)

    cmd = [
        "yt-dlp",
        "--no-warnings",
        "--no-check-certificates",
        "--add-header", "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "--add-header", "Referer:https://www.tiktok.com/",
        "-f", quality,
        "-o", os.path.join(output_dir, "%(uploader)s_%(title).80s_%(id)s.%(ext)s"),
        url
    ]

    print(f"[*] Downloading: {url}")
    print(f"[*] Output: {os.path.abspath(output_dir)}")

    try:
        result = subprocess.run(cmd, capture_output=False, text=True)
        if result.returncode == 0:
            print("[+] Download complete!")
            return True
        else:
            print("[-] Download failed. Video may be private or region-locked.")
            return False
    except Exception as e:
        print(f"[-] Error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="DecryptLoaderTT - TikTok Video Downloader",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python DecryptLoaderTT.py -u "https://www.tiktok.com/@user/video/1234567890"
  python DecryptLoaderTT.py -u URL1 -u URL2 -u URL3
  python DecryptLoaderTT.py -u "URL" -o "my_videos" -q "best"
        """
    )

    parser.add_argument("-u", "--url", action="append", required=True,
                        help="TikTok video URL")
    parser.add_argument("-o", "--output", default="downloads",
                        help="Output folder (default: downloads)")
    parser.add_argument("-q", "--quality", default="best",
                        help="Video quality: best, worst, or format code")

    args = parser.parse_args()

    print()
    print("========================================")
    print("  DecryptLoaderTT")
    print("  TikTok Video Downloader v1.0")
    print()
    print("  Developer: Decryptious_ on Discord")
    print("             Punchborn on IG")
    print("========================================")
    print()

    if not check_yt_dlp():
        if not install_yt_dlp():
            sys.exit(1)
        if not check_yt_dlp():
            sys.exit(1)

    success = 0
    for url in args.url:
        if download_tiktok(url, args.output, args.quality):
            success += 1
        print("-" * 50)

    print(f"\n[*] Done! {success}/{len(args.url)} videos downloaded.")
    print(f"[*] Saved to: {os.path.abspath(args.output)}")

    if success < len(args.url):
        print("[!] Some downloads failed. Possible reasons:")
        print("    - Video is private or deleted")
        print("    - Video is region-locked")
        print("    - TikTok API changed (update yt-dlp: yt-dlp -U)")


if __name__ == "__main__":
    main()
