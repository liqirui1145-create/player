from config import DEFAULT_METADATA

try:
    from mutagen import File as MutagenFile
except ImportError:
    MutagenFile = None


class MetadataReader:
    @staticmethod
    def read(file_path: str, is_video: bool = False) -> dict:
        metadata = DEFAULT_METADATA.copy()
        if not MutagenFile or is_video:
            return metadata

        try:
            audio = MutagenFile(file_path)
            if not audio:
                return metadata

            if hasattr(audio.info, 'sample_rate'):
                metadata["sample_rate"] = f"{audio.info.sample_rate} Hz"
            if hasattr(audio.info, 'channels'):
                metadata["channels"] = f"{audio.info.channels} 声道"
            if hasattr(audio.info, 'bitrate'):
                metadata["bitrate"] = f"{audio.info.bitrate // 1000} kbps"

            tags = audio.tags
            if tags:
                metadata["artist"] = tags.get('artist', tags.get('ARTIST', ['--']))[0]
                metadata["album"] = tags.get('album', tags.get('ALBUM', ['--']))[0]
                metadata["title"] = tags.get('title', tags.get('TITLE', ['--']))[0]

        except Exception:
            pass

        return metadata

    @staticmethod
    def extract_cover(file_path: str):
        if not MutagenFile:
            return None

        try:
            from mutagen.mp3 import MP3
            from mutagen.flac import FLAC
            from io import BytesIO
            from PIL import Image

            audio = MutagenFile(file_path)
            cover_data = None

            if isinstance(audio, MP3):
                for tag in audio.tags.values():
                    if tag.FrameID == "APIC":
                        cover_data = tag.data
                        break
            elif isinstance(audio, FLAC):
                for pic in audio.pictures:
                    cover_data = pic.data

            if cover_data:
                img = Image.open(BytesIO(cover_data)).convert("RGBA")
                return img
        except Exception:
            pass

        return None