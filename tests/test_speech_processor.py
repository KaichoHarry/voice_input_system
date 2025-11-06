# tests/test_speech_processor.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.config import Config
from core.speech_processor import SpeechProcessor

def test_speech_to_text():
    config = Config()
    processor = SpeechProcessor(config)

    audio_path = "tests/test_voice.wav"
    print(f"🎙️ テスト音声: {audio_path}")

    text = processor.speech_to_text(audio_path)
    print(f"🧠 認識結果: {text}")

    assert isinstance(text, str)
    assert len(text) > 0, "認識結果が空です"

if __name__ == "__main__":
    test_speech_to_text()
