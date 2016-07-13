from django.shortcuts import render
from bs4 import BeautifulSoup
import requests as req


def news(request):
    base_url = 'http://www.nytimes.com'
    r = req.get(base_url)
    soup = BeautifulSoup(r.text)
    news_title = []


    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            news_title.append(story_heading.a.text.replace("\n", " ").strip())
        else:
            news_title.append(story_heading.contents[0].strip())

    news_title.sort()
    return render(request, 'news.html', {'news' : news_title})
