# utils/config.py
import os
from dataclasses import dataclass

@dataclass
class Config:
    """音声入力システム全体の設定クラス"""
    # 音声設定
    sample_rate: int = 16000
    chunk_size: int = 1024
    record_seconds: int = 5
    
    # Whisper モデル設定
    whisper_model: str = "base"
    
    # ログ設定
    log_dir: str = os.path.join(os.path.dirname(__file__), "..", "logs")
    log_level: str = "INFO"
    
    # NLP 設定
    use_japanese: bool = True
    language: str = "ja"
    
    # キーボード設定
    trigger_key: str = "f8"

    def ensure_log_dir(self):
        """ログディレクトリが存在しない場合は作成"""
        os.makedirs(self.log_dir, exist_ok=True)
