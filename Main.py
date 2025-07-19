import re 

text = "data.txt"
fichier = open(text, "r",encoding="utf8")
lines = fichier.readlines()
lines = [line.strip() for line in lines if line.strip() != " "]
lines = [line.strip(",number of verticesedges''"": \n") for line in lines ]
lines = [line.strip() for line in lines if line.strip() != "''"]
dalinesta = [[int(x) for x in lines[i].split(' ')] for i in range(len(lines)) if lines[i] != ""]


print("lines: ", dalinesta)