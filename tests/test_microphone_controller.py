import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.config import Config
from core.microphone_controller import MicrophoneController

def test_microphone_recording():
    config = Config()
    mic = MicrophoneController(config)
    
    print("🎤 5秒間録音を開始します…")
    output_file = "tests/test_voice.wav"
    mic.record_to_file(output_file)
    
    if os.path.exists(output_file):
        print(f"✅ 録音成功: {output_file}")
    else:
        print("❌ 録音に失敗しました")

if __name__ == "__main__":
    test_microphone_recording()
