
import os, requests, csv, re
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

BASE_URL = 'https://www.football-data.co.uk/'
LEAGUES = [{'name': 'premier-league', 'path': 'englandm.php', 'key': 'E0'}]

def fetch_and_save():
    headers = {'User-Agent': generate_user_agent()}
    for league in LEAGUES:
        res = requests.get(BASE_URL + league['path'], headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        # المنطق هنا يعتمد على كيفية تخزينك للبيانات
        print(f"تمت معالجة {league['name']}")

if __name__ == "__main__": fetch_and_save()
