import requests
import os
from urllib.parse import urlparse

def download_page(url):
    response = requests.get(url)
    with open('pagina.html', 'wb') as file:
        file.write(response.content)

    parsed_url = urlparse(url)
    folder_path = parsed_url.netloc + parsed_url.path
    if folder_path.endswith('/'):
        folder_path = folder_path[:-1]

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    os.system(f'curl {url} --output {folder_path}/index.html --create-dirs --remote-name-all')
    os.rename('pagina.html', os.path.join(folder_path, 'pagina.html'))

url = 'link-da-pagina'
download_page(url)
