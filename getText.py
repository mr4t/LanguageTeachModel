import requests
from bs4 import BeautifulSoup as bs


def getText(url):
    header = {"User-Agent":
              ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")}
    r = requests.get(url, headers = header)
    if r.status_code != 200:
        print("Not Connected to Website")

    soup = bs(r.content, "lxml")
    texts = soup.find_all("p") #paragraph
    # links = soup.find_all("a") #links
    # spans = soup.find_all("span") #spans

    text = lambda x:x.text
    texts = list(map(text, texts))

    # links = list(map(text, links))
    # spans = list(map(text, spans))

    if len(texts) == 0:
        return 0
    else:
        return texts
