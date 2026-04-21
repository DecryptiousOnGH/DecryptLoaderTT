# DecryptLoaderTT

**Developer:** Decryptious_ on Discord / Punchborn on IG

A lightweight command-line tool for downloading TikTok videos in high quality. Built for Windows Command Prompt using Python and yt-dlp.

---

## Features

- Download TikTok videos in best available quality
- Batch download multiple URLs at once
- Auto-detects browser cookies (Chrome, Firefox, Edge, Brave, Opera) for private/restricted videos
- Custom output directory support
- Clean, minimal terminal interface
- No bloat — just works

---

## Requirements

- **Python 3.8+** ([Download](https://python.org/downloads))
- **Windows** (Linux/macOS compatible with minor adjustments)
- **yt-dlp** (auto-installed on first run)

---

## Installation

### Method 1: Quick Start (Windows)

1. Download all files from the repository
2. Double-click `DecryptLoaderTT.bat`
3. Paste a TikTok URL when prompted

### Method 2: Manual Setup

```bash
# Clone or download the repository
git clone https://github.com/yourusername/DecryptLoaderTT.git
cd DecryptLoaderTT

# Install dependencies
pip install -r requirements.txt

# Run
python DecryptLoaderTT.py -u "https://www.tiktok.com/@user/video/1234567890"
```

---

## Usage

### Download a Single Video

```bash
python DecryptLoaderTT.py -u "https://www.tiktok.com/@username/video/1234567890123456789"
```

### Download Multiple Videos

```bash
python DecryptLoaderTT.py -u "URL1" -u "URL2" -u "URL3"
```

### Custom Output Folder

```bash
python DecryptLoaderTT.py -u "URL" -o "my_videos"
```

### Specify Quality

```bash
python DecryptLoaderTT.py -u "URL" -q "best"     # Best quality (default)
python DecryptLoaderTT.py -u "URL" -q "worst"    # Lowest quality (fastest)
```

---

## Command Line Arguments

| Argument | Short | Description | Default |
|----------|-------|-------------|---------|
| `--url` | `-u` | TikTok video URL (required, can use multiple) | None |
| `--output` | `-o` | Output directory | `downloads` |
| `--quality` | `-q` | Video quality selector | `best` |

---

## File Structure

```
DecryptLoaderTT/
├── DecryptLoaderTT.py      # Main script
├── DecryptLoaderTT.bat     # Windows launcher
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## How It Works

1. **yt-dlp** handles all the heavy lifting — video extraction, format selection, downloading
2. Browser cookies are auto-detected to bypass login walls on restricted content
3. Videos are saved with descriptive filenames: `username_title_videoID.mp4`
4. Downloads go to the `downloads/` folder by default

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "yt-dlp not found" | Run `pip install -U yt-dlp` or let the auto-installer handle it |
| "Invalid TikTok URL" | Make sure the URL starts with `https://www.tiktok.com/` or `https://vm.tiktok.com/` |
| Download fails / private video | Log into TikTok in Chrome/Firefox so cookies can be used |
| Slow download | Try `-q "worst"` for lower quality, faster download |
| SSL certificate error | The script uses `--no-check-certificates` — should be handled automatically |

---

## Updating yt-dlp

TikTok changes their API frequently. Keep yt-dlp updated:

```bash
yt-dlp -U
```

Or:

```bash
pip install -U yt-dlp
```

---

## Disclaimer

This tool is for **personal use only**. Respect content creators' rights and TikTok's Terms of Service. Do not redistribute downloaded content without permission.

---

## Credits

- **Developer:** Decryptious_ on Discord / Punchborn on IG
- **Powered by:** [yt-dlp](https://github.com/yt-dlp/yt-dlp) — the best video downloader on the planet

---

## License

MIT License — do whatever you want, just don't blame me if TikTok bans your IP.
