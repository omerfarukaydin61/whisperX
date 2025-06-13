import whisperx
import warnings
from importlib.metadata import version
import argparse
from util import write_srt, load_config, log

def main(config):
    if version("whisperx") != "3.3.4":
        warnings.warn(f"Recommended to use whisperx==3.3.4, but found version {version('whisperx')}")

    log(f"Loading model on device: {config.DEVICE} (compute_type={config.COMPUTE_TYPE})")
    model = whisperx.load_model("large-v3", config.DEVICE, compute_type=config.COMPUTE_TYPE)

    log(f"Loading audio file: {config.AUDIO_FILE}")
    audio = whisperx.load_audio(config.AUDIO_FILE)

    log(f"Transcribing audio (batch_size={config.BATCH_SIZE}, language={config.LANGUAGE})")
    result = model.transcribe(audio, batch_size=config.BATCH_SIZE, language=config.LANGUAGE)
    log("Transcription complete.")

    log("Loading alignment model and aligning segments...")
    model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=config.DEVICE)
    result = whisperx.align(result["segments"], model_a, metadata, audio, config.DEVICE, return_char_alignments=False)
    log("Alignment complete.")

    log("Running diarization...")
    diarize_model = whisperx.diarize.DiarizationPipeline(use_auth_token=config.HF_TOKEN, device=config.DEVICE)
    diarize_segments = diarize_model(audio)
    result = whisperx.assign_word_speakers(diarize_segments, result)
    log("Diarization and speaker assignment complete.")

    log(f"Writing SRT to: {config.SRT_PATH}")
    write_srt(result["segments"], config.SRT_PATH)
    log(f"SRT file created: {config.SRT_PATH}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WhisperX ile ses dosyasından SRT oluşturucu.")
    parser.add_argument("--config", default="config.py", help="Kullanılacak config dosyası (varsayılan: config.py)")
    args = parser.parse_args()
    config = load_config(args.config)
    main(config)
