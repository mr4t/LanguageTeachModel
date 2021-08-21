import re
import requests
from bs4 import BeautifulSoup as bs


categry_urls = []
news_urls = []
blackList = []
url_location = 0
site = ""
categry = ""
news = ""

def connect_page(url):
    header ={"User-Agent" :
            ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")}


    r = requests.get(url, headers = header)
    if r.status_code != 200:
        return 0
    soup = bs(r.content, "lxml")
    return soup

def save_urls(soup): # get urls from page source and save
    def check(url):
        if re.findall("^"+site, url): # check url is belong to website
            pass
        else:
            return 0
        if re.findall("^"+site+categry, url):
            return 1  # category
        if re.findall("^"+site+news, url):
            return 2  # news




    a = soup.find_all("a", attrs={"href": re.compile("^https://")})

    global categry_urls, news_urls, url_location

    for i in a:
        state = check(i.get("href"))
        if i.get("href") in categry_urls or i.get("href") in news_urls or not state: # if url saved already or url not belong website
            continue
        if state == 1: #category
            categry_urls.append(i.get("href"))
        if state == 2: #news

            news_urls.append(i.get("href"))

            # url_location += 1
def find_urls():
    global categry_urls, url_location
    check = True
    for url in range(url_location, len(categry_urls)):
        for _ in range(10):
            soup = connect_page(categry_urls[url])
            if soup:
                save_urls(soup)
                print(url, ":", categry_urls[url])
                url_location += 1
                check = True
                break
            else:
                print(str(_)+" Not Connected to Page. Trying again.")
                check = False

        if not check:
            print("Not Connected to Page :", categry_urls[url])
            blackList.append(categry_urls[url])  # not connected pages

def run(home, topic, article):
    global site, categry, news
    site = home
    categry = topic
    news = article
    categry_urls.append(site)
    while len(news_urls):
        try:
            if categry_urls[url_location]:
                print("-"*100)
                find_urls()
            else:
                break
        except IndexError:
            break
    return news_urls