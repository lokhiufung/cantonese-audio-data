from .downloader import Downloader
from .errors import *


class RthkDownloader(Downloader):
    def __init__(self, name, base_url_dict, download_dir):
        super().__init__(name, base_url_dict, download_dir)

    def download(self, params):
        """
        params: dict with fields: channel(name of channel), date(yyyy-mm-dd)
        """
        channel = params['channel']
        date = self._parse_date_format(params['date'])

        base_url = self.base_url_dict[self.name][channel]
        # 2 possible file name
        filename_m4a = self.download_dir + '/' + channel + date + '.m4a'
        filename_mp3 = self.download_dir + '/' + channel + date + '.mp3'

        if not self._is_file_exist(filename_m4a) or not self._is_file_exist(filename_mp3):
            try:
                url_m4a = base_url + '/m4a/' + date + '.m4a'
                self._handle_request(url_m4a, filename_m4a)
            except EndPointNotFoundException:
                url_mp3 = base_url + '/mp3/' + date + '.mp3'
                self._handle_request(url_mp3, filename_mp3)
            except Exception as exe:
                self._error_handler(exe)
                

    def _handle_request(self, url, filename):
        response = self.sess.get(url)
        if response.status_code == 200:
            print('writing {} to local directory'.format(url))
            with open(filename, 'wb') as f:
                f.write(response.content)
        elif response.status_code == 404:
            raise EndPointNotFoundException
        else:
            raise Exception('unknown exception: response.status_code {} url {}'.format(response.status_code, url))

    
    def _error_handler(self, exe):
        print('Catched exception: {}'.format(exe))

    @staticmethod
    def _parse_date_format(date):
        return date.replace('-', '')
