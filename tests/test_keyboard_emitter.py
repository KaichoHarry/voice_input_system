# tests/test_keyboard_emitter.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.keyboard_emitter import KeyboardEmitter

def test_keyboard_emitter():
    emitter = KeyboardEmitter()

    print("🧪 テスト: テキストを入力してみます（メモ帳などのフォーカスを当てておくと確認可能）")
    emitter.type_text("こんにちは、テスト入力です！")
    emitter.press_enter()
    print("✅ テスト完了。")

if __name__ == "__main__":
    test_keyboard_emitter()
