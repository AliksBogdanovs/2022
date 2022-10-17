from bs4 import BeautifulSoup
import requests
 
def apstrada_lapu(url):
    r = requests.get(url) 
    html = r.text
    soup = BeautifulSoup(html, 'html.parser') 
    return soup
 
html = apstrada_lapu("https://vvsprogramm.github.io/B/") 
print(html.second.name.text)
