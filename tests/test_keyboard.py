# tests/test_keyboard.py
from pynput import keyboard

def on_press(key):
    try:
        print(f"キーが押されました: {key.char}")
    except AttributeError:
        print(f"特殊キーが押されました: {key}")

def on_release(key):
    print(f"キーが離されました: {key}")
    if key == keyboard.Key.esc:
        # ESCキーで終了
        print("終了します。")
        return False

print("キーボード入力を監視中...(ESCで終了)")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
