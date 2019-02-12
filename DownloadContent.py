from bs4 import BeautifulSoup
import os
import urllib.request as urllib2

url = 'https://www.daniyadenia.com'
folderName = 'site'
def download_site(url, level):
    if not os.path.exists(folderName):
        os.makedirs(folderName)
    response = urllib2.urlopen(url)
    webContent = response.read().decode('utf-8')
    f = open(folderName + '/' + url.rsplit('/', 1)[-1] , 'w')
    f.write(webContent)
    f.close
    webcontents=[webContent]

    for i in range(level):
        links = []
        for linkContent in webcontents:
            print("CONTENT: " + str(len(webcontents)))
            soup = BeautifulSoup(linkContent)
            for link in soup.findAll('a'):
                links.append(link.get('href'))
        webcontents = download_page(links)

def download_page(links):
    webcontents = []
    for link in links:
        if link is not None:
            if link.endswith('/'):
                link = link[:-1]
            if len(link) > 1:
                if link.startswith('/'):
                    linkUrl = url+link
                else:
                    linkUrl = link
                try:
                    response = urllib2.urlopen(linkUrl)
                    if response.getcode() == 200:
                        webcontent = response.read()
                        f = open(folderName + '/' + link.rsplit('/', 1)[-1], 'wb')
                        f.write(webcontent)
                        f.close
                        webcontents.append(webcontent)
                except Exception as e:
                    print(e)

    return webcontents

if __name__ == '__main__':
    download_site(url, 2)
