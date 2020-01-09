from .downloader_rthk import RthkDownloader
from .downloader_youtube import YoutubeDownloader


mapper = {
    'rthk': RthkDownloader,
    'youtube': YoutubeDownloader
}