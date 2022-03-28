from wsgiref import headers
from bs4 import BeautifulSoup
import urllib

username = 'user'
password = 'pass'
url = 'http://192.168.0.1/'

passwordManager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
passwordManager.add_password(None, url, username, password)

#authHandler = urllib.request.HTTPBasicAuthHandler(passman)
authHandler = urllib.request.HTTPDigestAuthHandler(passwordManager)

opener = urllib.request.build_opener(authHandler)
urllib.request.install_opener(opener)

res = urllib.request.urlopen(url)

html = res.read()
print(html.decode('utf-8'))

#soup = BeautifulSoup(html, 'html.parser')

#imgIn = soup.select_one('img')
