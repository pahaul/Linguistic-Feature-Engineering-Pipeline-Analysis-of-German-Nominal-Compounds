file = open("Erstglied_freq.txt", "r")
lines = file.readlines()
file.close()

datei = open("Erstglied_R.txt", "r")
zeilen = datei.readlines()
datei.close()
count = 0

for line in lines:
    components = line.split(" ")
    ref_glied = str(components[0])
    #print(ref_glied)
    frequencies = {}
    count += 1

    for zeile in zeilen:
        bestandteil = zeile.split("\t")
        bestandteil_clean = bestandteil[1].split("\n")                #bereinigt Begriffe von \n, das aus irgendeinem Grund in den strings sichtbar ist
   # print(str(bestandteil[0]))
        vgl_glied = bestandteil[0]
        target = bestandteil_clean[0]
        #print(vgl_glied)
        

        if ref_glied == vgl_glied:

            old_freq = frequencies.get(target)
            if old_freq == None:
                frequencies[target] = 1
            else:
                frequencies[target] += 1
                        
    print(f"{ref_glied}     << {components[2]} Äußerungen >>   << {len(frequencies)} Varietäten >> \n {frequencies}")
    file = open("EG_evaluation.txt", "a")
    file.write(f"{count}.    {ref_glied}     << {components[2]} Äußerungen >>   << {len(frequencies)} Varietäten >> \n {frequencies}\n\n")
    file.close()


file = open("Zweitglied_freq.txt", "r")
lines = file.readlines()
file.close()

datei = open("Zweitglied_R.txt", "r")
zeilen = datei.readlines()
datei.close()
count = 0

for line in lines:
    components = line.split(" ")
    ref_glied = str(components[0])
    #print(ref_glied)
    frequencies = {}
    count += 1

    for zeile in zeilen:
        bestandteil = zeile.split("\t")
        bestandteil_clean = bestandteil[1].split("\n")                #bereinigt Begriffe von \n, das aus irgendeinem Grund in den strings sichtbar ist
   # print(str(bestandteil[0]))
        vgl_glied = bestandteil[0]
        target = bestandteil_clean[0]
        #print(vgl_glied)
        

        if ref_glied == vgl_glied:

            old_freq = frequencies.get(target)
            if old_freq == None:
                frequencies[target] = 1
            else:
                frequencies[target] += 1
                        
    print(f"{ref_glied}     << {components[2]} Äußerungen >>   << {len(frequencies)} Varietäten >> \n {frequencies}")
    file = open("ZG_evaluation.txt", "a")
    file.write(f"{count}.   {ref_glied}     << {components[2]} Äußerungen >>   << {len(frequencies)} Varietäten >> \n {frequencies}\n\n")
    file.close()