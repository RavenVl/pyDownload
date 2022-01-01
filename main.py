from utils import download, find_links

if __name__ == '__main__':
    url = 'http://xn----7sbb4ab0aeerjehf9j.xn--p1ai/products/stojkoe-serdtse-1-4'
    for elem in find_links(url):
        download(elem)
