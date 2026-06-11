from PyQt6.QtGui import QPixmap, QPainter, QColor, QFont, QImage
from PyQt6.QtCore import Qt
from PIL import Image
import os
from config import DEFAULT_COVER_SIZE
from metadata_reader import MetadataReader


class CoverManager:
    DEFAULT_COVER_FILENAME = "Xinjiang_Old_and_young_(Populus_diversifolia_胡杨)_(4973519309).jpg"

    def __init__(self, parent):
        self.parent = parent
        self.custom_default_cover = None
        self.load_default_cover_from_file()

    def load_default_cover_from_file(self):
        """自动加载项目目录中的默认封面图片"""
        cover_path = os.path.join(os.path.dirname(__file__), self.DEFAULT_COVER_FILENAME)
        if os.path.exists(cover_path):
            try:
                pix = QPixmap(cover_path)
                self.custom_default_cover = pix.scaled(
                    DEFAULT_COVER_SIZE, DEFAULT_COVER_SIZE,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
            except Exception:
                self.custom_default_cover = None

    def set_custom_default_cover(self, file_path: str):
        try:
            pix = QPixmap(file_path)
            self.custom_default_cover = pix.scaled(
                self.parent.video_label.width(), self.parent.video_label.height(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            return True
        except Exception:
            return False

    def get_default_cover(self) -> QPixmap:
        if self.custom_default_cover is not None:
            return self.custom_default_cover

        pix = QPixmap(DEFAULT_COVER_SIZE, DEFAULT_COVER_SIZE)
        pix.fill(QColor("#2c3e50"))
        painter = QPainter(pix)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(QColor("#ffffff"))
        painter.setFont(QFont("微软雅黑", 20, QFont.Weight.Bold))
        painter.drawText(pix.rect(), Qt.AlignmentFlag.AlignCenter, "🎵 暂无封面\n请点击【设置默认封面】上传图片")
        painter.end()
        return pix

    def get_audio_cover(self, file_path: str) -> QPixmap:
        img = MetadataReader.extract_cover(file_path)
        if img:
            img = img.resize((DEFAULT_COVER_SIZE, DEFAULT_COVER_SIZE), Image.Resampling.LANCZOS)
            qimg = QImage(img.tobytes(), img.width, img.height, QImage.Format.Format_RGBA8888)
            return QPixmap.fromImage(qimg)
        return self.get_default_cover()

    def clear(self):
        self.custom_default_cover = None