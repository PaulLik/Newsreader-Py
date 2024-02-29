import requests
from bs4 import BeautifulSoup
import lxml
import os
import msvcrt
import sys

allNews = []

def hyphen(string: str, identation: int = 22) -> str:
    txt = ""
    if len(string) > 57:
        words = string.split()
        txtLines = 1
        for w in words:
            if len(txt + w) > 70 * txtLines:
                txt = txt + "\n" + " " * (identation + 6) + "\t" + w
                txtLines += 1
            else:
                txt = txt + " " + w
    else:
        txt = string
    return txt.lstrip()


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
            allNews.append([times[n].text, "Интерфакс", hyphen(news[n].text, 16)])


def kommersant():
    url="https://www.kommersant.ru/lenta"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    lenta = soup.find("div", class_="rubric_lenta")
    news = lenta.find_all("h2")
    for n in news:
        allNews.append(["", "Коммерсант", hyphen(n.text, 17)])


def dddnews():
    url = "https://3dnews.ru"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    news_hw = soup.find("div", class_="allnews-col lncol")
    news = news_hw.find_all("li", class_ = "header")
    for n in news:
        #if ["strong"] in n.get("class"):
        #    color = "\033[1;35;40m"
        #else:
        #    color = "\033[0;37;44m"
        article = n.find("a")
        articleTime = article.get("title").split(" ")[1]
        articleText = article.text
        allNews.append([articleTime, "3D News Hardware", hyphen(articleText)])
    news_hw = soup.find("div", class_="allnews-col rncol")
    news = news_hw.find_all("li", class_ = "header")
    for n in news:
        #if ["strong"] in n.get("class"):
        #    color = "\033[1;35;40m"
        #else:
        #    color = "\033[0;37;44m"
        article = n.find("a")
        articleTime = article.get("title").split(" ")[1]
        articleText = article.text
        allNews.append([articleTime, "3D News Software", hyphen(articleText, 22)])


if __name__ == "__main__":
    clear = lambda: os.system("cls")
    clear()
    interfax()
    #kommersant()
    dddnews()
    
    allNews.sort()

    if len(sys.argv) == 2:
        breakOutput = True
        linesOut = int(sys.argv[1])
    else:
        breakOutput = False

    i = 0
    for n in allNews:
        print(f"\u2022 {n[0]} {n[1]}\t{n[2]}", end = "\n" * 2)
        i+=1
        if breakOutput == True:
            if (i % linesOut) == 0:
                print("\x1b[92mДля продолжения любую клавишу, \"Esc\" - выход\x1b[0m\n\n")
                keypressed = msvcrt.getch()
                if keypressed == b'\x1b':
                    sys.exit()