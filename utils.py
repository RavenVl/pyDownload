import requests, os
from tqdm import tqdm

def download(url):

    eg_link = url
    response = requests.get(eg_link, stream=True)
    file_name = eg_link.split('/')[-1]
    with tqdm.wrapattr(open(file_name, "wb"), "write",
                       miniters=1, desc=eg_link.split('/')[-1],
                       total=int(response.headers.get('content-length', 0))) as fout:
        for chunk in response.iter_content(chunk_size=4096):
            fout.write(chunk)
