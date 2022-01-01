import requests, os
from tqdm import tqdm
from requests_html import HTMLSession
from urllib.parse import urlparse


def download(url):
    eg_link = url
    response = requests.get(eg_link, stream=True)
    file_name = eg_link.split('/')[-1]
    with tqdm.wrapattr(open(file_name, "wb"), "write",
                       miniters=1, desc=eg_link.split('/')[-1],
                       total=int(response.headers.get('content-length', 0))) as fout:
        for chunk in response.iter_content(chunk_size=4096):
            fout.write(chunk)


def find_links(url):
    u = urlparse(url)
    prefix_url = f'{u.scheme}://{u.netloc}'
    session = HTMLSession()
    r = session.get(url)
    url_list = [prefix_url+elem.attrs['src'] for elem in r.html.find('source')]
    return url_list


if __name__ == '__main__':
    find_links('http://xn----7sbb4ab0aeerjehf9j.xn--p1ai/products/stojkoe-serdtse-1-4')
