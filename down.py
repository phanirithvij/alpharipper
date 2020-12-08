import signal
import sys

import requests
from tqdm import tqdm


# to prevent ctrl+c traceback
signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

# https://stackoverflow.com/a/51812486/8608146


def fetch_or_resume(url, filename, progress=True):
    with open(filename, 'ab') as file:
        pos = file.tell()
        headers = {}
        if pos:
            headers['Range'] = f'bytes={pos}-'
        # print('sending request')
        response = requests.get(url, headers=headers, stream=True)
        # print('got response')

        total_size = 0
        if response.status_code in [200, 206]:
            total_size = int(response.headers.get('content-length'))
        # if pos:
        #     validate_as_paranoid_as_you_want_to_be_(pos, response)
        # try:
        #     total_size = int(response.headers.get('content-length'))
        # except TypeError as e:
        #     if response.headers['content-type'] == 'text/html':
        #         print(response.content)
        #         print("No content-length header possibly fully downloaded")
        if progress:
            for data in tqdm(iterable=response.iter_content(chunk_size=1024), total=total_size//1024, unit='KB', ascii=True):
                file.write(data)
        else:
            for data in response.iter_content(chunk_size=1024):
                file.write(data)
            print(filename, "done")


if __name__ == "__main__":
    print(sys.argv)
    fetch_or_resume(sys.argv[1], sys.argv[2])
