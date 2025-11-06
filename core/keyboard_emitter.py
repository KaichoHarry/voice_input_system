# core/keyboard_emitter.py
import pyautogui
import time
from utils.logger import get_logger

class KeyboardEmitter:
    """音声認識結果などをキーボード入力として出力するクラス"""

    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)

    def type_text(self, text: str, delay: float = 0.02):
        """指定したテキストを1文字ずつ入力"""
        if not text:
            self.logger.warning("入力文字列が空です。スキップします。")
            return
        
        self.logger.info(f"🧠 テキスト入力を開始: {text}")
        for char in text:
            pyautogui.typewrite(char)
            time.sleep(delay)
        self.logger.info("✅ テキスト入力完了。")

    def press_enter(self):
        """Enterキーを押す"""
        pyautogui.press('enter')
        self.logger.info("↩️ Enterキーを送信しました。")
