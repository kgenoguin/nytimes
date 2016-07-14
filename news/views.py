from django.shortcuts import render
from bs4 import BeautifulSoup
from django.template.defaulttags import register
import requests as req
import json


def news(request):
    base_url = 'http://www.nytimes.com'
    r = req.get(base_url)
    soup = BeautifulSoup(r.text)
    news = []


    for story_heading in soup.find_all(class_= "story-heading"):
        news_title = ""


        if story_heading.a:
            news_title = story_heading.a.text.replace("\n", " ").strip()
        else:
            news_title = story_heading.contents[0].strip()

        news.append({ 'title': news_title , 'link': story_heading })


    return render(request, 'news.html', {'news' : news})
