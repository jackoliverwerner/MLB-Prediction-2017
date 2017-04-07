import urllib
from bs4 import BeautifulSoup

fte_url = "https://projects.fivethirtyeight.com/2017-mlb-predictions/games/"

fte_html = urllib.request.urlopen(fte_url).read()
fte = BeautifulSoup(fte_html, "lxml")

a = fte.findAll(attrs={"class":"game js-game"})[0]


print(a)

