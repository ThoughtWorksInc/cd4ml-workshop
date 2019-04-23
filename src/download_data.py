import os
import urllib.request
import argparse

def load_data(path, key):
    gcsBucket = "continuous-intelligence"

    if not os.path.exists(path):
        os.makedirs(path)

    if not os.path.exists(os.path.join(path, key)):
        url = "https://storage.googleapis.com/%s/%s" % (gcsBucket, key)
        urllib.request.urlretrieve(url, os.path.join(path, key))


def main():
    parser = argparse.ArgumentParser(description='Download files from Google Storage.')
    parser.add_argument('--model', action='store_true', default=False, help='Downloads model (data/decision_tree/model.pkl) instead of input file (data/raw/store47-2016.csv)')
    args = parser.parse_args()

    if args.model:
        print("Loading model...")
        load_data(path='data/decision_tree', key='model.pkl')
    else:
        print("Loading input data...")
        load_data(path='data/raw', key='store47-2016.csv')
    print("Finished downloading")


if __name__ == "__main__":
    main()
