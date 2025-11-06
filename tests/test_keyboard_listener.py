import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.config import Config
from core.keyboard_listener import KeyboardListener

def test_keyboard_listener():
    config = Config()
    listener = KeyboardListener(config)
    print("⌨️ Command+Spaceでマイク起動テスト。ESCで終了。")
    listener.keyboard_check()

if __name__ == "__main__":
    test_keyboard_listener()
