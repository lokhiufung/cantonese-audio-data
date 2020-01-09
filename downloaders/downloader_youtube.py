# import youtube_dl
import subprocess
from .downloader import Downloader


class YoutubeDownloader(Downloader):
    def __init__(self, name, base_url_dict, download_dir, api_key):
        super().__init__(name, base_url_dict, download_dir)
        self.api_key = 'AIzaSyCJRXitIZDyOny8iecSVrFRTqZGVKpHFOQ'
        self.api_url = 'https://www.googleapis.com/youtube/v3/playlists?part=id&key={api_key}'.format(api_key=api_key) 
        self.playlist_ids = []

    def download(self, channel_id):
        playlist_ids = self._get_playlist_ids(channel_id)
        for playlist_id in playlist_ids:
            url = self.base_url_dict['youtube']['playlist'] + playlist_id
            cmd = ['youtube-dl', '--extract-audio', '--audio-format', 'wav', '-o', '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s', '--prefer-ffmpeg', '--sub-lang', 'zh-hk', '--write-sub', '--write-auto-sub',  url]
            subprocess.Popen(cmd)
            
    
    def _get_playlist_ids(self, channel_id):
        url = self.api_url + '&channelId={channel_id}'.format(channel_id=channel_id)
        response = self.sess.get(url)
        if response.status_code == 200:
            json_ = response.json()
            return self._parse_playlist_ids(json_)
        else:
            self._error_handler(response)


    # @staticmethod
    # def _prepare_download_playlist(self, channel_ids):
    #     playlist_ids = []
    #     for channel_id in channel_ids:
    #         self.playlist += self._get_playlist_ids(channel_id)
    #     return playlist_ids

    @staticmethod
    def _error_handler(response):
        josn_ = response.json() 
        print(josn_['error'])

    @staticmethod
    def _parse_playlist_ids(json_):
        return [item['id'] for item in json_['items']]
