import boto3
import spotipy
from spotipy.oauth2 import SpotifyOAuth

boto3.setup_default_session(profile_name="default")
dynamodb_client = boto3.client("dynamodb")
table_name = "music_lucas_da_silva_santos"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

tracks = sp.current_user_top_tracks(limit=10)

for track in tracks['items']:
    duration = track['track']['duration_ms'] // 1000
    minutes, seconds = divmod(duration, 60)

    response = dynamodb_client.put_item(
        TableName=table_name,
        Item={
            "nome_musica": {"S": track['track']['name']},
            "artista": {"S": track['track']['artists'][0]['name']},
            "album": {"S": track['track']['album']['name']},
            "ano": {"N": track['track']['album']['release_date'][:4]},
            "duracao": {"S": "{:02d}:{:02d}".format(minutes, seconds)},
        }
    )