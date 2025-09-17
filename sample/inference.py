import subprocess, json
from pathlib import Path

# Define input audio file
input_audio = "audio.m4a"

# Save the metadata from the original audio file
meta = json.loads(subprocess.check_output([
    "ffprobe", "-v", "error", "-print_format", "json",
    "-show_format", "-show_streams", input_audio
]))

json.dump(meta, open("metadata.json", "w"), indent=2)

# Convert the audio to .wav with 16-bit PCM and 16kHz fs
output_audio = Path(input_audio).with_suffix(".wav")

subprocess.run(
    f"ffmpeg -y -i {input_audio} -ac 1 -ar 16000 -sample_fmt s16 {output_audio}".split(),
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    check=True
)