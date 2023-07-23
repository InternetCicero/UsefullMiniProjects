from collections import Counter


#Text Datei definieren
Datei_Name = "TextScan.txt"

#Text Datei Öffnen
with open(Datei_Name,'r', encoding='UTF-8') as datei:
	text = datei.read()

#Text in Wörter splitten
replacers = [",",".","!"]

for i in range(len(replacers)):
	text = text.replace(replacers[i], "")

text = text.replace("\n", " ")
text_liste = text.split(" ")

removes = []
for i in text_liste:
	if len(i) < 5:
		removes.append(i)

for i in removes:
	text_liste.remove(i)


Counter = Counter(text_liste) 
H_Woerter = Counter.most_common(20)

print(H_Woerter)

#datei.count()

