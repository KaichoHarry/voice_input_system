# tests/test_whisper.py
import whisper

model = whisper.load_model("small")
result = model.transcribe("tests/ai_irasyaimase.wav", language="ja")
print("認識結果:", result["text"])
