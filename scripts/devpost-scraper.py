from bs4 import BeautifulSoup
import urllib.request as ur
from functools import reduce 

def scrape(link):
    sock = ur.urlopen(link)
    soup = BeautifulSoup(sock,"html.parser")

    #Find the prizes
    filters = soup.find("form",{"class":"filter-submissions"}).findAll("ul")
    prizeList = filters[0].findAll("label")
    prizeList = [row.contents[-1] for row in prizeList]

    #How many pages of projects are there? 
    pageInfo = soup.find("div",{"class":"pagination-info"}).find("ul",{"class":"pagination"})
    maxPage = int(pageInfo.findAll("li")[-2].text)

    allLinks = []

    #Find the link to each of the projects
    for i in range(1,maxPage+1):
        linkPage = link+"?page="+str(i)
        sock = ur.urlopen(linkPage)
        soup = BeautifulSoup(sock,"html.parser")

        submissionLinks = soup.find("div",{"id":"submission-gallery"})
        submissionLinks = submissionLinks.findAll("div",{"class":"row"})

        for i in range(len(submissionLinks)):
            submissionLinks[i] = submissionLinks[i].findAll("a")

        submissionLinks = reduce(lambda x,y: x+y,submissionLinks)
        submissionLinks = [j['href'] for j in submissionLinks]

        #Add the links found to all links
        allLinks+=submissionLinks


    
    return allLinks
