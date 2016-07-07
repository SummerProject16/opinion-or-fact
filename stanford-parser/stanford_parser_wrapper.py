import subprocess as sp
import shlex


CMD = "java -mx150m -cp \"./*\": edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat \"penn,typedDependencies\" edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz"


def get_dependency_data(filenames,cmd=CMD):

	for filename in filenames:
		cmd += " "+filename
	data = sp.Popen(shlex.split(cmd),stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.PIPE)
	raw_data = data.communicate()[0]
	return format_data(raw_data)


def format_data(data):
	data = data.split("\n\n")
	i = 0
	dependencies = []
	while (i+1) < len(data):
		dependencies.append(data[i+1].split("\n"))
		i += 2
	strdependencies = []
	for dependency in dependencies:
		strdependency = {
				'amod' : 0,
				'advmod' : 0,
				'nummod' : 0,
				'quantmod' : 0,
				'acomp' : 0,
				'xcomp' : 0
			}
		for line in dependency:
			if "amod(" in line:
				strdependency['amod'] = 1
			elif "advmod(" in line:
				strdependency['advmod'] = 1
			elif "nummod(" in line:
				strdependency['nummod'] = 1
			elif "quantmod(" in line:
				strdependency['quantmod'] = 1
			elif "acomp(" in line:
				strdependency['acomp'] = 1
			elif "xcomp(" in line:
				strdependency['xcomp'] = 1
		strdependencies.append(strdependency)
	return strdependencies

#print get_dependency_data(["idioms.txt"])

fileout = open("idioms1.arff","w")

filein = open("idioms_output.txt")
data = filein.read()

retdata = format_data(data)

for d in retdata:
	for x,y in d.iteritems():
		fileout.write(str(y)+",")
	fileout.write("\n")