import re
from typing import Tuple, List


class LyricParser:
    TIME_PATTERN = re.compile(r'\[(\d+):(\d+)\.(\d+)\]')

    @classmethod
    def parse(cls, lrc_text: str) -> Tuple[List[int], List[str]]:
        times, lyrics = [], []
        for line in lrc_text.splitlines():
            line = line.strip()
            matches = cls.TIME_PATTERN.findall(line)
            lyric = cls.TIME_PATTERN.sub("", line).strip()
            if matches and lyric:
                for m, s, ms in matches:
                    times.append(int(m) * 60000 + int(s) * 1000 + int(ms))
                    lyrics.append(lyric)
        combined = sorted(zip(times, lyrics))
        if combined:
            return list(zip(*combined))
        return [], []

    @classmethod
    def load_from_file(cls, file_path: str) -> Tuple[List[int], List[str]]:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return cls.parse(f.read())
        except Exception:
            return [], []