from bs4 import BeautifulSoup
import urllib.request as ur

def scrape(link):
    sock = ur.urlopen(link)
    soup = BeautifulSoup(sock,"html.parser")

    filters = soup.find("form",{"class":"filter-submissions"}).findAll("ul")

    prizeList = filters[0].findAll("label")
    prizeList = [row.contents[-1] for row in prizeList]

    return prizeList
