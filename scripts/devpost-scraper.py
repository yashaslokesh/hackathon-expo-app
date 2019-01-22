from bs4 import BeautifulSoup
import urllib.request as ur
from functools import reduce 

def getChallenges(link):
    sock = ur.urlopen(link)
    soup = BeautifulSoup(sock,"html.parser")

    #Find the prizes
    filters = soup.find("form",{"class":"filter-submissions"}).findAll("ul")
    prizeList = filters[0].findAll("label")
    prizeList = [row.contents[-1] for row in prizeList]

    #Split it up into challenge and company
    
    prizeList = [tuple(row.split(" - ")) for row in prizeList
                 if len(row.split(" - "))==2]
    
    return prizeList

print(getChallenges("https://bitcamp2018.devpost.com/submissions"))
