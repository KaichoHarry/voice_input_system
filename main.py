# main.py
import time
import os
from utils.config import Config
from utils.logger import get_logger
from core.keyboard_listener import KeyboardListener
from core.microphone_controller import MicrophoneController
from core.speech_processor import SpeechProcessor
from core.nlp_processor import NLPProcessor
from core.keyboard_emitter import KeyboardEmitter

def main():
    # 設定とログ
    config = Config()
    logger = get_logger("Main")
    
    # モジュール初期化
    keyboard_listener = KeyboardListener(config)
    mic_controller = MicrophoneController(config)
    speech_processor = SpeechProcessor(config)
    nlp_processor = NLPProcessor()
    keyboard_emitter = KeyboardEmitter()

    logger.info("🎯 音声入力システムを起動しました。")
    print("⌨️ スペースキー長押しで録音、ESCで終了します。\n")

    try:
        # キー入力監視ループ
        while True:
            status = keyboard_listener.status

            if status == "microphone_on" and mic_controller.stream is None:
                # 録音開始
                output_file = "temp_voice.wav"
                mic_controller.record_to_file(output_file)

                # 音声→テキスト
                text = speech_processor.speech_to_text(output_file)

                # NLP処理
                corrected_text = nlp_processor.nlp_process(text)

                # キーボード入力
                keyboard_emitter.keyboard_input(corrected_text)

                # ステータスをリセット
                keyboard_listener.status = "microphone_off"

            time.sleep(0.1)

    except KeyboardInterrupt:
        logger.info("ユーザーによる終了（Ctrl+C）")
    except Exception as e:
        logger.error(f"エラー発生: {e}")

if __name__ == "__main__":
    main()
