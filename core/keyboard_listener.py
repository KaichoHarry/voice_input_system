# core/keyboard_listener.py
import time
import pyautogui
from pynput import keyboard
from utils.logger import get_logger
from utils.config import Config

class KeyboardListener:
    def __init__(self, config: Config):
        self.config = config
        self.logger = get_logger(self.__class__.__name__)
        self.is_pressed = False
        self.status = "microphone_off"

    def _is_text_input_focused(self) -> bool:
        """アクティブウィンドウが入力欄を持つか（Macでは簡易判定）"""
        try:
            active_window = pyautogui.getActiveWindow()
            if active_window and "Notes" in active_window.title or "Text" in active_window.title:
                return True
            return True  # 仮で常にTrue（実機で調整）
        except Exception as e:
            self.logger.warning(f"ウィンドウ情報の取得に失敗: {e}")
            return True

    def on_press(self, key):
        """ホットキー押下時の処理"""
        try:
            if key == keyboard.Key.space and self.is_pressed is False:
                # Mac用: Commandキーとの組み合わせを判定
                if self._is_text_input_focused():
                    self.status = "microphone_on"
                    self.is_pressed = True
                    self.logger.info("🎹 ホットキー検出: マイク起動要求")
                    print("→ microphone_on")
                else:
                    self.logger.warning("入力可能なウィンドウではありません。")
        except Exception as e:
            self.logger.error(f"キー押下処理でエラー: {e}")

    def on_release(self, key):
        """ホットキー離された時の処理"""
        if key == keyboard.Key.space and self.is_pressed:
            self.status = "microphone_off"
            self.is_pressed = False
            self.logger.info("🛑 ホットキー解除: マイク停止要求")
            print("→ microphone_off")

        if key == keyboard.Key.esc:
            self.logger.info("ESCキーが押されました。リスナーを終了します。")
            return False  # Listener停止

    def keyboard_check(self):
        """キー入力を監視（無限ループ）"""
        self.logger.info("⌨️ キーボード入力の監視を開始します（ESCで終了）")
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
