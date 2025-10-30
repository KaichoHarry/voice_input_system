# utils/logger.py
import logging
import os
from datetime import datetime
from .config import Config

def get_logger(name: str = "voice_input_system") -> logging.Logger:
    """共通のロガーを返す"""
    config = Config()
    config.ensure_log_dir()

    # ログファイル名を日付付きで作成
    log_filename = os.path.join(config.log_dir, f"{datetime.now():%Y-%m-%d}.log")

    # ロガー設定
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, config.log_level.upper(), logging.INFO))

    # 重複防止
    if not logger.handlers:
        # コンソール出力
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s"
        ))
        logger.addHandler(console_handler)

        # ファイル出力
        file_handler = logging.FileHandler(log_filename, encoding="utf-8")
        file_handler.setFormatter(logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
        ))
        logger.addHandler(file_handler)

    return logger
