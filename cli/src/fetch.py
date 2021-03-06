import requests
import json


def make_request(args):
    # sending get request and saving the response as response object
    r = requests.request(method=args.method, url=args.url, params=args.params)
    # extracting data in json format

    print(json.dumps({
        'status': r.status_code,
        'results': r.json()
    }))
