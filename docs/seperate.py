
filein = open("idioms_14_4_16.csv")

fileout1 = open("idioms_14_4_16tags.txt","w")
fileout2 = open("idioms_14_4_16type.txt","w")

data = filein.readlines()

for line in data:
	line = line.split(",")
	line[0] = line[0].split()[0]
	if line[1].replace("\n","")!="":
		fileout1.write(line[0].replace("\n","")+"\n")
		if line[1].replace("\n","") is "0":
			line[1]="o"
		fileout2.write(line[1].replace("\n","")+"\n")

fileout1.close()
fileout2.close()

filein.close()