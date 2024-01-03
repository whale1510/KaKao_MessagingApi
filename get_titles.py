import requests
from bs4 import BeautifulSoup

def get_titles():
    url = "https://sco.skku.edu/sco/community/major_info.do"
    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')
    tag = soup.find_all(['span'])
    for s in tag:
        s.extract()

    titles = soup.select('dt.board-list-content-title')
    return titles

titles = get_titles()
cnt = 0
for i in titles:
    if cnt == 0:
        title1 = str(i.text.strip())
        cnt += 1
    elif cnt == 1:
        title2 = str(i)
        cnt += 1
    elif cnt == 2:
        title3 = str(i)
        cnt += 1
    else:
        break