count = 0

with open("spacypos.txt") as f_in:
    lines = filter(None, (line.rstrip() for line in f_in))  #verhindert das Auslesen von Leerzeilen aus Datei, die zu Problemen beim Splitten der Zeilen führen würden

    for line in lines:
        if not ("SPACE") in line:
            components = line.split("\t")

            if components[2].startswith("NOUN"):
                    if not "http" in components[0]:
                        if not "www" in components[0]:
                            print(line)
                            count += 1

                            file = open("noun.txt", "a")
                #file.write(f"{line}\n")
                            file.write(f"{components[1]}" + "\n")
                            file.close
                            count += 1

print(str(count) + " Nomen")