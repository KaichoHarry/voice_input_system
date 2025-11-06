# core/microphone_controller.py
import pyaudio
import wave
from utils.logger import get_logger

class MicrophoneController:
    def __init__(self, config):
        self.logger = get_logger(self.__class__.__name__)
        self.config = config
        self.audio = pyaudio.PyAudio()
        self.stream = None

    def microphone_operate(self, status: str):
        """マイクのON/OFF制御"""
        if status == "microphone_on":
            self.logger.info("🎤 マイクを起動します")
            self.start_recording()
        elif status == "microphone_off":
            self.logger.info("🛑 マイクを停止します")
            self.stop_recording()
        else:
            self.logger.warning(f"不明なステータス: {status}")

    def start_recording(self):
        """録音開始"""
        if self.stream is not None:
            self.logger.warning("すでに録音中です。")
            return

        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.config.sample_rate,
            input=True,
            frames_per_buffer=self.config.chunk_size
        )
        self.logger.info("録音を開始しました。")

    def stop_recording(self):
        """録音停止"""
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None
            self.logger.info("録音を停止しました。")

    def record_to_file(self, output_path: str):
        """指定秒数だけ録音してファイルに保存"""
        self.logger.info(f"{self.config.record_seconds}秒間録音を開始します...")
        stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.config.sample_rate,
            input=True,
            frames_per_buffer=self.config.chunk_size
        )

        frames = []
        for i in range(0, int(self.config.sample_rate / self.config.chunk_size * self.config.record_seconds)):
            data = stream.read(self.config.chunk_size)
            frames.append(data)

        stream.stop_stream()
        stream.close()

        wf = wave.open(output_path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(self.config.sample_rate)
        wf.writeframes(b''.join(frames))
        wf.close()

        self.logger.info(f"録音を終了しました。ファイル保存: {output_path}")
        return output_path
