import requests
import pprint

api_key = 'AIzaSyCJRXitIZDyOny8iecSVrFRTqZGVKpHFOQ'
channel_id = 'UCKkrzIj3tAzLEVNvbc6PTZA'
sess = requests.Session()
url = 'https://www.googleapis.com/youtube/v3/playlists?part=id&channelId={channel_id}&key={api_key}'.format(channel_id=channel_id, api_key=api_key)
 

def get():
    response = sess.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        error_handler(response)

def parse_playlist_list(json_):
    return [item['id'] for item in json_['items']]

json_ = get().json()
playlist = parse_playlist_list(json_)
print(playlist)