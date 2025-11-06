# main.py
import time
from core.keyboard_listener import KeyboardListener
from core.microphone_controller import MicrophoneController
from core.speech_processor import SpeechProcessor
from core.nlp_processor import NLPProcessor
from utils.config import Config
from utils.logger import get_logger

def main():
    logger = get_logger("Main")
    config = Config()

    keyboard = KeyboardListener(config)
    mic = MicrophoneController(config)
    stt = SpeechProcessor(config)
    nlp = NLPProcessor(config)

    logger.info("🎯 音声入力システムを起動しました。")
    print("⌨️ スペースキー長押しで録音、ESCで終了します。\n")

    while True:
        # ステータス確認ループ
        if keyboard.status == "microphone_on":
            logger.info("🎙️ 録音開始")
            wav_path = mic.record(duration=config.RECORD_DURATION)

            if wav_path:
                text = stt.transcribe(wav_path)
                processed = nlp.process_text(text)
                print(f"🧠 出力: {processed}")

            keyboard.status = "microphone_off"
            logger.info("🛑 録音完了・待機状態へ")

        elif keyboard.status == "exit":
            logger.info("👋 終了処理を実行します。")
            break

        time.sleep(0.3)

if __name__ == "__main__":
    main()
