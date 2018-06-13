# -*- coding: utf-8 -*-

import requests
import re
import sys


def download_html(url):
    
    s = requests.Session()
    s.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        })
    r = s.get(url)
    with open('test.html', 'w') as output:
        output.write(r.text.encode('cp1251'))

def find_tel_number():
    with open('test.html') as f:
        data = f.read()
        result = re.findall(r'''\b8\s*\D?\d{3}\D?\s*\d{3}[-,\s]?\d{2}[-,\s]?\d{2}\b|
                                [\b,\+]7\s*\D?\d{3}\D?\s*\d{3}[-,\s]?\d{2}[-,\s]?\d{2}\b|
                                \b\d{3}[-,\s]?\d{2}[-,\s]?\d{2}\b''', 
                                data,
                                re.VERBOSE)
        return result

def main(urls):
    if not  urls:
        urls = ['https://repetitors.info']
    with open('tel.txt','w') as output_tel:
        for url in urls:
            output_tel.write(url)
            download_html(url)
            output_tel.write('\n'.join(find_tel_number()))
            output_tel.write("\n-----------------\n")

if __name__ == '__main__':
    main(sys.argv[1:])
