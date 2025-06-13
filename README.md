# WhisperX Subtitle Generator

This repository provides an automated pipeline to generate speaker-diarized subtitles (SRT) from audio or video files using [WhisperX](https://github.com/m-bain/whisperX). It is designed for researchers, content creators, and anyone who needs accurate, speaker-attributed subtitles from Turkish or other language sources.

## Example Video

<a href="https://www.youtube.com/shorts/tI354Xu6xRs">
  <img src="https://img.youtube.com/vi/tI354Xu6xRs/maxresdefault.jpg" width="50%"/>
</a>

Suppose you want to generate Turkish subtitles for the following YouTube video:

> https://www.youtube.com/shorts/tI354Xu6xRs

### Step 1: Download the Video (Optional)
You can use the [YoutubeDownloader](https://github.com/Tyrrrz/YoutubeDownloader.git) project to easily download YouTube videos as audio or video files. YoutubeDownloader provides a user-friendly graphical interface—no need to use the command line or install .NET manually. Simply download and run the application, paste the YouTube link, and save the video or audio file to your computer.

This step is optional: you can use any tool or method to obtain your audio/video file.

### Step 2: Configure the Pipeline
Edit `config.py` to set the correct audio file and language:

```python
AUDIO_FILE = "example-audio.mp3"
LANGUAGE = "tr"  # 'tr' for Turkish, 'en' for English, etc.
# SRT_PATH will be set automatically based on AUDIO_FILE
```

### Step 3: Run the Subtitle Generator
Install dependencies (see INSTALL.md), then run:

```bash
python main.py --config config.py
```

This will generate a subtitle file named `subtitle-TR-example-audio.srt` in the same directory.

## Installation (with conda)

1. Clone this repository and navigate to its directory:

```bash
git clone <this-repo-url>
```

2. Create and activate a conda environment (recommended):

```bash
conda create -n whisperx python=3.10
conda activate whisperx
```

3. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

4. (Optional) If you want to download YouTube videos, you can use the [YoutubeDownloader](https://github.com/Tyrrrz/YoutubeDownloader.git) GUI as described above.

## Optional: Add WhisperX as a Git Submodule

If you want to add WhisperX as a git submodule (recommended for development):

```bash
git submodule add https://github.com/m-bain/whisperX.git whisperX
git submodule update --init --recursive
```

If you clone this repository from your own GitHub, the `whisperX` folder will only be present if you (or someone else) has already added it and pushed it to the repo. Otherwise, you can always add it later with the above command.

> **Note:** If you do not need to modify or develop WhisperX itself, you do not need to clone it manually. The code will work with the pip-installed version.

## Optional: Add YoutubeDownloader as a Git Submodule

If you want to add [YoutubeDownloader](https://github.com/Tyrrrz/YoutubeDownloader.git) as a git submodule (for convenient local access to the GUI or CLI):

```bash
git submodule add https://github.com/Tyrrrz/YoutubeDownloader.git YoutubeDownloader
git submodule update --init --recursive
```

This will create a `YoutubeDownloader` folder in your project. You can then use the GUI or CLI directly from this folder to download YouTube videos as audio or video files.

If you clone this repository from your own GitHub, the `YoutubeDownloader` folder will only be present if you (or someone else) has already added it and pushed it to the repo. Otherwise, you can always add it later with the above command.

> **Note:** This step is optional. You can use any tool or method to obtain your audio/video file. YoutubeDownloader is provided for convenience.

## Notes
- If you want to translate the subtitles, set `LANGUAGE` in `config.py` to the target language code (e.g., 'en' for English).
- The pipeline uses GPU by default. Adjust `DEVICE` and `COMPUTE_TYPE` in `config.py` for your hardware.
- All logs and progress will be shown in the terminal.

## Requirements
- Python 3.8+
- CUDA-compatible GPU (recommended for speed)
- WhisperX and dependencies (see [whisperX/README.md](whisperX/README.md) for details)
