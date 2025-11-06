# core/speech_processor.py
import whisper
import time
from utils.logger import get_logger

class SpeechProcessor:
    """音声ファイルをテキストに変換するクラス"""

    def __init__(self, config):
        self.logger = get_logger(self.__class__.__name__)
        self.config = config
        self.logger.info(f"Whisperモデルをロード中: {self.config.whisper_model}")
        start = time.time()
        self.model = whisper.load_model(self.config.whisper_model)
        self.logger.info(f"モデルロード完了（{time.time() - start:.2f}秒）")

    def speech_to_text(self, audio_path: str) -> str:
        """音声ファイルをテキストに変換"""
        self.logger.info(f"🎧 音声認識を開始: {audio_path}")

        start_time = time.time()
        result = self.model.transcribe(
            audio_path,
            language=self.config.language if self.config.use_japanese else "en"
        )

        text = result.get("text", "").strip()
        elapsed = time.time() - start_time

        if text:
            self.logger.info(f"✅ 音声認識結果: {text}")
        else:
            self.logger.warning("⚠️ 認識結果が空です。")

        self.logger.info(f"処理時間: {elapsed:.2f}秒")
        return text
