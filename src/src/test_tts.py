from TTS.api import TTS

# Load English TTS model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

# Generate audio file
tts.tts_to_file(text="Hello world, this is a test.", file_path="hello.wav")
print("Audio generated successfully!")
