#!/path/to/python3/virtual/env

import os
import getpass

import requests
from lxml import html

# set Downloads folder as img save destination
dest_folder = f'/home/{getpass.getuser()}/Downloads/slackmojis/'

try:
    os.makedirs(dest_folder)
    print('Directory Created')

except FileExistsError:
    print('Directory Already Exists')

# download main html page and convert into tree
html_page = requests.get('https://slackmojis.com/categories/19-random-emojis')
html_tree = html.fromstring(html_page.text)

# select all elements with xpath
elements = html_tree.xpath('//a[@class="downloader"]')

# download each img 
for el in elements:
    url = requests.get(url=el.attrib['href'])
    filename = el.attrib['download']
    filepath = dest_folder + filename
    
    with open(filepath, 'wb') as fout:
        fout.write(url.content)
    
    print(filepath)

print('\nDONE')
