import argparse

def add_request_args(parser):
    parser.add_argument('-m', '--method', required=False, default='get', help='Method to make request')
    parser.add_argument('-u', '--url', required=True, help='Url to make request')
    parser.add_argument('-p', '--params', required=False, default={}, help='Url to make request')

def create_request_parser(parent):
    parser = parent.add_parser('fetch', help='fetch module')
    add_request_args(parser)
def parse_args():
    parser = argparse.ArgumentParser(description='CLI with some awesome things')

    subparser = parser.add_subparsers(title='commands',
                                       dest='commands',
                                       help='Provided source specific subparsers')
    create_request_parser(subparser)

    return parser.parse_args()
