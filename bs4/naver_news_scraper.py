from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&listType=title&sid1=100&date=20171022")
    bsObj = BeautifulSoup(html, "html.parser")
    count_page = bsObj.select("#main_content > div.paging")
    print("Page Count is %d"%len(count_page))
    for page in count_page:
        newslist_page = bsObj.find("div", {"class": "list_body newsflash_body"}).findAll("ul")
        print("News list count: %d"%len(newslist_page))
        for i in range(len(newslist_page)):
            newslist = newslist_page[i].findAll("a")
            for news_link in newslist:
                article_link = news_link['href']
                pages.add(article_link)
                
            print ("section end")

def getArticle():
    article =[]
    for article_link in pages:
        bsObj = BeautifulSoup(urlopen(article_link), "html.parser")
        contents = bsObj.find(id = "articleBodyContents").stripped_strings
        print(contents.text)
        # for string in contents:
        #     if re.search(r'(_flash_removeCallback() {})', string):
        #         contents = re.split(r'(_flash_removeCallback() {})', contents)[1]

        #     if re.search(r'(\s)+기자', string):
        #         contents = re.split(r'(\s)+기자', contents)[0]

        #     if re.search(r'(기자단)$', string):
        #         contents = re.split(r'(기자단)$', contents)[0]

        #     print (string)

        print('-------------------------------------------------------------')
        article.append({"title": bsObj.find(id = "articleTitle").get_text() , "contents": bsObj.find(id = "articleBodyContents").get_text()})

getLinks("")
getArticle()
