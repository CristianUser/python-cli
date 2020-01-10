import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='This make get requests')
    parser.add_argument('-m', '--method', required=False, default='get', help='Method to make request')
    parser.add_argument('-u', '--url', required=True, help='Url to make request')
    parser.add_argument('-p', '--params', required=False, default={}, help='Url to make request')

    return parser.parse_args()
