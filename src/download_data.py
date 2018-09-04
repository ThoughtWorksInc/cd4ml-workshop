import os
from google.cloud import storage

def load_data():
    gcsBucket = "continuous-intelligence"
    key = "store47-2016.csv"

    if not os.path.exists('data/raw'):
        os.makedirs('data/raw')

    if not os.path.exists("data/" + key):
        client = storage.Client()
        bucket = client.get_bucket(gcsBucket)
        blob = bucket.get_blob(key)
        blob.download_to_filename('data/raw/store47-2016.csv')


def main():
    print("Loading data...")
    load_data()
    print("Finished downloading")


if __name__ == "__main__":
    main()
