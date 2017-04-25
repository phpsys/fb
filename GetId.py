# hotfix - update!
import urllib.request
from bs4 import BeautifulSoup

link = "https://www.facebook.com/apple"
html_page = urllib.request.urlopen(link)
soup = BeautifulSoup(html_page , "lxml")

for link in soup.findAll('a'):
    a = str(link.get('href'))
    if 'ref_page_id' in a:
        print((a.strip().split("&"))[0].strip().split("=")[1])


print("ok")