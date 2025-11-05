import spacy
import os

count = 1

for file in os.listdir("artikel/"):
    file_name = (f"artikel/{file}")
    print("Tokenisiere den     " + str(count) + "      Artikel       "+ file_name)

    file = open(file_name, "r")
    text = file.read()
    file.close

    print(str(len(text)) + "Zeichen")

    nlp = spacy.load("de_dep_news_trf")  #"de_dep_news_trf" oder "de_core_news_sm"
    doc = nlp(text)

    file = open("spacypos.txt", "a")

    for token in doc:
        line = (str(token.text) + "\t" + str(token.lemma_) + "\t" + str(token.pos_))
        #print(line)
        file = open("spacypos.txt", "a")
        file.write(f"{line}\n")
    file.close

    count += 1
    