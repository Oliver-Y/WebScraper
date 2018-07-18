import requests
from BeautifulSoup import BeautifulSoup
url = "http://webscraper.io/test-sites/e-commerce/allinone"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
captions = soup.findAll('div', attrs = {'class' : 'caption'});
with open("Output.txt", "w") as text_file:
    ##text_file.write("Purchase Amount: {}".format(soup.prettify()))
    text_file.write("header: {}".format(captions))
