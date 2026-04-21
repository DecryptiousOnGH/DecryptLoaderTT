@echo off
title DecryptLoaderTT - TikTok Downloader
color 0B
cls

echo.
echo  ========================================
echo   DecryptLoaderTT
echo   TikTok Video Downloader v1.0
echo.
echo   Developer: Decryptious_ on Discord
echo              Punchborn on IG
echo  ========================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [-] Python not found!
    echo     Install from: https://python.org/downloads
    pause
    exit /b 1
)

REM Check/Install yt-dlp
echo [*] Checking yt-dlp...
python -m pip show yt-dlp >nul 2>&1
if errorlevel 1 (
    echo [*] Installing yt-dlp...
    python -m pip install -U yt-dlp -q
)

REM Run
if "%1"=="" (
    echo.
    echo Drag and drop TikTok URLs onto this batch file
    echo Or run: DecryptLoaderTT.bat "URL"
    echo.
    set /p url="Enter TikTok URL: "
    python "%~dp0DecryptLoaderTT.py" -u "%url%"
) else (
    python "%~dp0DecryptLoaderTT.py" -u "%1"
)

echo.
pause
