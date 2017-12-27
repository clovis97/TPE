#!/usr/bin/env python
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import random
import sys
from threading import Thread
import time

class Afficheur(Thread):

    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre
        
    def run(self):
        my_url = 'https://play.google.com/store/search?q=camerounais'
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        containers = page_soup.findAll("div",{"class":"card no-rationale square-cover apps small"})
        container = containers[0]
    
        for container in containers:
            brand = container.div.div.a["aria-label"]
            infos = container.findAll("a",{"class":"subtitle"})
            info = infos[0]
        
            print("apk: " + brand)
            print("info: " +info.text)

for i in range(4):             
    thread_1 = Afficheur("10")
    thread_1.start()
    thread_1.join()

