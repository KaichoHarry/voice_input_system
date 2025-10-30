# tests/test_pyautogui.py
import pyautogui

print("画面サイズ:", pyautogui.size())
print("マウスの現在位置:", pyautogui.position())
# pyautogui.moveTo(100, 100, duration=1)  # コメント外すとマウスが移動します
