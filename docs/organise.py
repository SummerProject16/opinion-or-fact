filein = open("idioms_14_4_16.csv")

data = filein.readlines()

opinion_count = 0

fact_count = 0

for x in data:
	parsed = x.split(",")

	if parsed[1].lower() == "o" or parsed[1].lower() == "0" :
		opinion_count += 1
	elif parsed[1].lower() == "f":
		fact_count += 1

division1 = opinion_count/2

if division1*2 != opinion_count:
	division1 += 1

division2 = fact_count/2

if division2*2 != fact_count:
	division2 += 1

file1 = open("file1.csv","w")

file2 = open("file2.csv","w")

for x in data:
	parsed = x.split(",")

	if parsed[1].lower() == "o" or parsed[1].lower() == "0":
		if division1 > 0:
			division1 -= 1
			file1.write(x.replace("\n","")+"\n")
		else:
			file2.write(x.replace("\n","")+"\n")

for x in data:
	parsed = x.split(",")

	if parsed[1].lower() == "f":
		if division2 > 0:
			division2 -= 1
			file1.write(x.replace("\n","")+"\n")
		else:
			file2.write(x.replace("\n","")+"\n")

file1.close()
file2.close()