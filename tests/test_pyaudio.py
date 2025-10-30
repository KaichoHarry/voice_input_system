# tests/test_pyaudio.py
import pyaudio

p = pyaudio.PyAudio()
print("マイクデバイス一覧:")
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"{i}: {info['name']}")
