#Liest die einfachen Splits, getrennt nach Erst- und Zweitglied, aus der Split-Datei des Compound Splitters aus und schreibt sie in neue Dateien

file = open("noun.txt.versuch.SPLITS.tsv.trees", "r")
lines = file.readlines()
file.close()

for line in lines:
    if line.startswith("2@1#>>>>>>	=T	null	2"):
        components = line.split("\t")
        split = components[6].split(" ")
            #print(split)

        file = open("komposita_split_R.txt", "a")
        file.write(f"{components[6]}\n")
        file.close

        file = open("Erstglied_R.txt", "a")
        file.write(f"{split[0]}\t{components[4]}\n")
        file.close

        file = open("Zweitglied_R.txt", "a")
        file.write(f"{split[1]}\t{components[4]}\n")
        file.close
