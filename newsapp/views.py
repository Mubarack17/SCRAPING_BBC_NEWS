from django.shortcuts import render
from .news_scraper import get_bbc_news

def index(request):
    mylist = get_bbc_news()
    return render(request, "newsapp/index.html", {"mylist": mylist})
