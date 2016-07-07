filein = open("final.arff")

fileout = open("optimised.arff","w")

data = filein.readlines()

i = 5

data.remove(data[i+1])

for line in data:
	if "@" not in line:
		x = line.replace("\n","").split(",")
		x.remove(x[i])
		fileout.write(",".join(x)+"\n")
	else:
		fileout.write(line)