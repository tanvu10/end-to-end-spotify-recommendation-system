import pandas as pd
import json
import re
from api_request import track_uri_to_features
from dotenv import load_dotenv
import os
import time

load_dotenv()
c_id = os.getenv('CLIENT_ID')
c_secret = os.getenv('CLIENT_SECRET')


def normalize_data(data_path):
    # load json data
    with open(data_path) as f:
        data = json.load(f)
    df = pd.json_normalize(data['playlists'], record_path='tracks', meta=['name'])
    # save to CSV
    df.to_csv('./data/raw.csv', index=False)

def feature_processing(df):
    features_list = []
    sleep_duration = 0.01
    # format track_uri
    df["track_uri"] = df["track_uri"].apply(lambda x: re.findall(r'\w+$', x)[0])

    # add feature from api data
    for index, row in df.iterrows():
        try:
            # fetch the features
            features = track_uri_to_features(row['track_uri'], c_id, c_secret)
            features_list.append(features)

            # respect the rate limit
            time.sleep(sleep_duration)

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(sleep_duration * 5)

    features_df = pd.DataFrame(features_list, index=False)

    # Save the result to a CSV file
    features_df.to_csv('./data/feature_date.csv', index=False)

if __name__ == "__main__":
    data_path = './data/first_1000_playlist.json'

    # normalize json file and save as csv
    # normalize_data(data_path)
    
    track_data = pd.read_csv('./data/raw.csv')
    # fetch the feature of each track from api call
    feature_processing(track_data)


