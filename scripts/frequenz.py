file = open("Erstglied_R.txt", "r")
lines = file.readlines()
file.close()

länge = len(lines)

frequencies = {}
compounds = []

for line in lines:
    lines = line.rstrip()

    components	=	line.split("\t")

    part	=	components[0]
    kompositum	=	components[1]

    old_freq = frequencies.get(part)

    if old_freq == None:
        frequencies[part] = 1
    else:
        frequencies[part] += 1    

frequencies_sorted = sorted(frequencies.items(), key=lambda item : item[1], reverse=True)

for part, frequency in frequencies_sorted[0:100]:
    print(f"{part} : {frequency}      ({frequency*100/länge}%)")
    file = open("Erstglied_freq.txt", "a")
    file.write(f"{part} : {frequency}      ({frequency*100/länge}%)\n")
    file.close



file = open("Zweitglied_R.txt", "r")
lines = file.readlines()
file.close()

länge = len(lines)

frequencies = {}
compounds = []

for line in lines:
    lines = line.rstrip()

    components	=	line.split("\t")

    part	=	components[0]
    kompositum	=	components[1]

    old_freq = frequencies.get(part)

    if old_freq == None:
        frequencies[part] = 1
    else:
        frequencies[part] += 1    

frequencies_sorted = sorted(frequencies.items(), key=lambda item : item[1], reverse=True)

for part, frequency in frequencies_sorted[0:100]:
    print(f"{part} : {frequency}      ({frequency*100/länge}%)")
    file = open("Zweitglied_freq.txt", "a")
    file.write(f"{part} : {frequency}      ({frequency*100/länge}%)\n")
    file.close