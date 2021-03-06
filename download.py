import argparse
import time
import traceback

from config import *
from downloaders import mapper
import utils

def main():
    """
    e.g.
    python download.py -n rthk -s 2019-09-01 -e 2019-09-30
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', type=str, help='name of source', required=True)
    parser.add_argument('-c', '--channels', type=str, help='name of auido channels', default='all')
    parser.add_argument('-d', '--dir', type=str, help='directory for downloaded files')
    # only for rthk
    parser.add_argument('-s', '--start', type=str, help='start date')
    parser.add_argument('-e', '--end', type=str, help='end date')

    parser.add_argument('--n_speaker', type=int, help='number of speakers in the youtube channel', default=2)

    arg = parser.parse_args()
    name = arg.name

    if arg.channels == 'all':
        channels = list(BASE_URL[name].keys())
    else:
        channels = arg.channels.split(',')

    if arg.dir is None:
        download_dir = DEFAULT_DIR_ROOT + '/' + name + '/wav'
    else:
        download_dir = arg.dir

    n_speaker = arg.n_speaker

    params = {}
    if name == 'rthk':
        download_helper = mapper[name](name, BASE_URL, download_dir)
        start_date = arg.start
        end_date = arg.end
        dates = utils.get_dates(start_date, end_date)

        for channel in channels:
            params['channel'] = channel
            for date in dates:
                params['date'] = date
                done = False
                while not done:
                    try:
                        start_time = time.perf_counter()
                        download_helper.download(params)
                        print('Time needed for this sample: {}'.format(time.perf_counter() - start_time))
                        done = True  # turn off the loop
                    except ConnectionResetError:
                        print('Sleep for 5 secs to avoid from blocking...')
                        time.sleep(5)
                    except Exception as exe:
                        print('download.py')
                        traceback.print_tb(exe.__traceback__)
    elif name == 'youtube':
        download_helper = mapper[name](name, BASE_URL, download_dir, api_key=GOOGLE_API_KEY, n_per_playlist=N_PER_PLAYLIST)
        playlist_ids = MULTI_SPEAKER_PLAYLIST if n_speaker > 1 else SINGLE_SPEAKER_PLAYLIST
        for playlist_id in playlist_ids:
            download_helper.download(playlist_id)
              


if __name__ == '__main__':
    main()

    