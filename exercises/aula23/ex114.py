from time import sleep
import urllib
import urllib.error
import urllib.request

for i in range (100):
    sleep(0.2)
    try:
        site = urllib.request.urlopen('http://www.google.com')
    except urllib.error.URLError:
        print('Deu errro')
    else:
        print("deu certo")