#Einzelen Artikel des Rubikon werden angesteuert und in einem Ordner als html-Datei abgelegt.

import urllib.request
from bs4 import BeautifulSoup

urls = set()
urlnumber = 0
count = 0

for page_number in range(64, 131): #sollten 1320 sein -4 aus 2020 -14 aus 2022
    url = "https://www.rubikon.news/artikel/page/" + str(page_number)
    urlnumber += 1
    print ("    Seite " + str(urlnumber)+" "+url)

    response = urllib.request.urlopen(url)
    data = response.read()

    soup = BeautifulSoup(data, 'html.parser')

    links = soup.find_all("a")

    for link in links:
       url = link.get("href")
       if url != None:

            if url.startswith("/artikel/") and not url.startswith("/artikel/suche")and not url.startswith("/artikel/page"):
                urls.add(url)
                #print("     " + url)

for url in urls:
    count += 1
    print("Der " + str(count) +" Artikel "+ url + " wird heruntergeladen...")

    response = urllib.request.urlopen("https://www.rubikon.news" + url)
    data = response.read()

    file = open("artikel_rubikon/" + str(count) + ".html", "w")
    file.write(data.decode("utf-8"))
    file.close()
    
    