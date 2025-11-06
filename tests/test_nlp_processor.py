# tests/test_nlp_processor.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.nlp_processor import NLPProcessor

def test_nlp_process():
    nlp = NLPProcessor()

    samples = [
        "今日はいい天気ですね",
        "Pythonの勉強をしています",
        "これでどうかな？",
        "明日は休みだね。",
        "えっ！そうなの"
    ]

    for text in samples:
        result = nlp.nlp_process(text)
        print(f"🧠 入力: {text} → 整形後: {result}")

if __name__ == "__main__":
    test_nlp_process()
