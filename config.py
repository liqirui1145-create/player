DEFAULT_COVER_SIZE = 550
TIMER_INTERVAL = 50
SPACE_LONG_PRESS_THRESHOLD = 200
VOLUME_STEP = 5
SEEK_STEP = 10000

SUPPORTED_FORMATS = {
    'audio': ('mp3', 'flac', 'wav', 'm4a', 'aac', 'ogg', 'opus', 'wma', 'alac', 'aiff', 'ape'),
    'video': ('mp4', 'mkv', 'avi', 'mov', 'flv', 'webm', 'mpeg', 'mpg'),
    'image': ('jpg', 'jpeg', 'png', 'bmp', 'gif')
}

DEFAULT_METADATA = {
    "sample_rate": "--", "channels": "--", "artist": "--",
    "album": "--", "title": "--", "bitrate": "--"
}