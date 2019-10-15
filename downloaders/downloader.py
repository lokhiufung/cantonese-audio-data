import requests
import os


class Downloader(object):
    def __init__(self, name, base_url_dict, download_dir):
        self.name = name
        self.download_dir = download_dir
        self.base_url_dict = base_url_dict
        self.sess = requests.Session()
        
    def download(self, params):
        """
        return a response object with resources from the source
        """
        pass
    
    def _error_handler(self, exe):
        """
        handle errrors
        """
        pass

    
    @staticmethod
    def _is_file_exist(filename):
        return os.path.exists(filename)
        
