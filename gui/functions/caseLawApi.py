import concurrent
import time
from concurrent.futures import as_completed, ProcessPoolExecutor

import requests
from PySide6.QtCore import QThreadPool
from bs4 import BeautifulSoup
from requests_futures.sessions import FuturesSession

from gui.functions.caseLawThread import Worker
from gui.uis.windows.main_window import UI_MainWindow


class CaseLawApi:
    def __init__(self):
        super().__init__()

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    def download_from_zimlii(self):
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

        url = "https://zimlii.org/judgments/Supreme-Court-of-Zimbabwe/2022"
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        links = soup.find_all(class_='field-content')
        for link in links:
            proper_link = f"https://zimlii.org/{link.find('a')['href']}"

            req = requests.get(proper_link, headers)
            soup = BeautifulSoup(req.content, 'html.parser')

            pdf_links = soup.find_all(class_='file-download-pdf')

            for new_open_link in pdf_links:
                print(link.text, new_open_link['href'])
                file_name = f'gui/documents/{link.text}.pdf'

                with FuturesSession() as session:
                    futures = [session.get(new_open_link['href']) for _ in
                               range(10)]
                    for future in as_completed(futures):
                        response = future.result()
                with open(file_name, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=1024 * 1024):
                        if chunk:
                            f.write(chunk)

                print("%s downloaded!\n" % file_name)

    def thread_download_from_zimlii(self):
        self.threadpool = QThreadPool()
        worker = Worker(CaseLawApi.download_from_zimlii, self)

        self.threadpool.start(worker)
