# core/nlp_processor.py
import re
from utils.logger import get_logger

class NLPProcessor:
    """
    音声認識結果を自然な日本語文に整形するクラス。
    句読点や文末表現を自動補正する。
    """
    def __init__(self, config=None):
        self.config = config
        self.logger = get_logger(self.__class__.__name__)

    def process_text(self, text: str) -> str:
        self.logger.info(f"🧠 NLP整形開始: {text}")
        # 簡易的に句読点を付与
        if not text.endswith(("。", "！", "？")):
            text += "。"
        self.logger.info(f"✅ NLP整形完了: {text}")
        return text

    def nlp_process(self, text: str) -> str:
        """
        テキストを整形して返す。
        例: "今日はいい天気ですね" → "今日はいい天気ですね。"
        """
        self.logger.info(f"🧠 NLP整形開始: {text}")
        if not text or not isinstance(text, str):
            self.logger.warning("⚠️ 入力テキストが空または不正です。")
            return ""

        # 空白や改行を除去
        text = text.strip()

        # 文末に句点がなければ追加
        if not text.endswith(("。", "！", "？", ".", "!", "?")):
            text += "。"

        # 不要なスペースの正規化
        text = re.sub(r"\s+", " ", text)

        # 句読点の調整（例：", " → "、"）
        text = text.replace(",", "、").replace(".", "。")

        self.logger.info(f"✅ NLP整形完了: {text}")
        return text
