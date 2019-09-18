#!/usr/bin/python3.7
from flask import Flask, request, jsonify
from pyfy import ClientCreds as ClientCreds, Spotify
import requests, os, time, json, pprint

client = ClientCreds(
    client_id='634a89ab0e2e4ec2b59dff7bfcbfca3d',
    client_secret='541bf8cfdced4f01896b3d4f7551ece9'
)
spt = Spotify(client_creds=client)
spt.authorize_client_creds()
pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)

@app.route('/api/v1/convert', methods=['POST'])
def convert_csv():
    playlist_id = str(request.data).split(":", 2)[2].strip("'")
    #print(playlist_id)

    results = []
    num_offset = 1
    response = spt.playlist_tracks(playlist_id, fields='items(track(name,artists(name),total))', offset=num_offset)
    pp.pprint(response)

    #while "\"next\" : null" not in response.values():
        #pp.pprint(response)
        #num_offset = num_offset + 100
        #response = spt.playlist_tracks(playlist_id, fields='items(track(name,artists(name)))', offset=num_offset)

    return "TEST"

@app.route('/api/v1/image', methods=['GET'])
def get_artist_image():
    return "TEST"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)