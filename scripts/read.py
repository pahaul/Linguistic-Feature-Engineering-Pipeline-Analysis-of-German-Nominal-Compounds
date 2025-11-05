from inspect import classify_class_attrs
from bs4 import BeautifulSoup
import os

count = 1

for file in os.listdir("artikel_rubikon/"):
    file_name = (f"artikel_rubikon/{file}")
    print(file_name)

    file = open(file_name, "rb")
    data = file.read()
    file.close()

    soup = BeautifulSoup(data, 'html.parser')


    file_name = (f"artikel/{str(count) + '.txt'}")
    count += 1

    file = open(file_name, "a")
    if soup.find("h1") != None:
        header1 = soup.find("h1").text
        file.write(header1 + "\n")
        print(header1)
    if soup.find("h2") != None:
        header2 = soup.find("h2").text
        file.write(header2 + "\n")
        print(header2)
   
    paragraphs = soup.find_all("p")
    for paragraph in paragraphs:
        if not paragraph.text.startswith("Foto: ") and paragraph.parent.name != "blockquote":
            if paragraph.find_parent("div", class_ ="article-author-bio") != None or paragraph.text.startswith("Quellen und Anmerkungen:"):
                break
            print(paragraph.text)
            file = open(file_name, "a")
            file.write(paragraph.text)
    file.write("\n\n")  
    file.close()