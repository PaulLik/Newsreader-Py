import requests
from bs4 import BeautifulSoup
import lxml
import os

allNews = []

def interfax():
    url ="https://www.interfax.ru/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    newsblock = soup.find("div", class_="timeline")
    times = newsblock.find_all("time")
    news = newsblock.find_all("h3")

    for n in range(0, len(news)):
        if "Фотохроника" in news[n].text or "Что произошло в мире науки" in news[n].text:
            continue
        else:
            #print(f"\u2022 {times[n].text} Интерфакс:\t{news[n].text}", end = "\n" * 2)
            allNews.append([times[n].text, "Интерфакс", news[n].text])


def kommersant():
    url="https://www.kommersant.ru/lenta"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    lenta = soup.find("div", class_="rubric_lenta")
    news = lenta.find_all("h2")
    for n in news:
        #print(f"\u2022 Коммерсант:\t{n.text}", end = "\n" * 2)
        allNews.append(["", "Коммерсант", n.text])


def dddnews():
    """
    Выводит новости с 3dnews.ru
    """
    url = "https://3dnews.ru"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    news_hw = soup.find("div", class_="allnews-col lncol")
    news = news_hw.find_all("li", class_ = "header")
    for n in news:
        #if "strong" in n.get("class"):
        #    color = "\033[1;35;40m "
        #else:
        #    color = "\033[0;37;44m"
        article = n.find("a")
        articleTime = article.get("title").split(" ")[1]
        articleText = article.text
        #print(f"\u2022 3D News, {articleTime}, Hardware:\t{articleText}", end = "\n" * 2)
        allNews.append([articleTime, "3D News Hardware", articleText])
    news_hw = soup.find("div", class_="allnews-col rncol")
    news = news_hw.find_all("li", class_ = "header")
    for n in news:
        #if "strong" in n.get("class"):
        #    color = "\033[1;35;40m"
        #else:
        #    color = "\033[0;37;44m"
        article = n.find("a")
        articleTime = article.get("title").split(" ")[1]
        articleText = article.text
        #print(f"\u2022 3D News, {articleTime}, Software:\t{articleText}", end = "\n" * 2)
        allNews.append([articleTime, "3D News Software", articleText])


if __name__ == "__main__":
    clear = lambda: os.system("cls")
    clear()
    interfax()
    #kommersant()
    dddnews()
    
    allNews.sort()

    for n in allNews:
        print(f"\u2022 {n[0]} {n[1]}\t{n[2].center(22)}", end = "\n" * 2)