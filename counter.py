filein = open("docs/idioms_14_4_16.csv")

tags = filein.readlines()

opinion = 0
fact = 0
o= [0,0,0,0]
f= [0,0,0,0,0]

for line in tags:
	line = line.split(",")
	if len(line)>1 and (line[1]=="o" or line[1] is "0"):
		opinion += 1
		try:
			if len(line) > 2:
				o[int(line[2])-1] += 1
		except:
			print line[0]
	elif len(line) > 1 and line[1] is "f":
		fact += 1
		try:
			if len(line) > 2:
				f[int(line[2].replace("\n",""))-1] += 1
		except:
			print line[0]


print opinion, fact, o[0],o[1],o[2],o[3],f[0],f[1],f[2],f[3],f[4]