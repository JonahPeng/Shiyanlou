#!/usr/bin/env python3
import requests

def download(url):
    '''
    from selected URL download requested files into current content.
    URL: the site of downloading files.
    '''
    #check the URL
    try:
        req = requests.get(url)
    except requests.exceptions.MissingSchema:
        print('Invalid URL"{}"'.format(url))
        return
    #check if the website accessible
    if req.status_code == 403:
        print("you dont have the authority to access the page")
        return
    filename = url.split('/')[-1]
    with open(filename,'w') as fobj:
        fobj.write(req.content.decode('utf-8'))
    print("Download over.")

if __name__ == '__main__':
    url = input ("Enter a URL: ")
    download(url)

