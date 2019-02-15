#steps
#copied 2 folders to JHWNL_1_2
#then extract JHWNL.jar and made it to custom folder
#then modify example.java file and make jar file 
#then create python code to extract data.

from py4j.java_gateway import JavaGateway #connect to jar file
from py4j.java_gateway import java_import #shiva reddy is doing this work on python
import matplotlib.pyplot as plt
import csv
import string
from collections import Counter

# https://github.com/gayatrivenugopal/gnuNify2019/blob/master/Example.py
# http://www.cfilt.iitb.ac.in/wordnet/webhwn/
# http://www.cfilt.iitb.ac.in/wordnet/webhwn/downloaderInfo.php
# shiva reddy [also have bigbucket account]

gateway = JavaGateway.launch_gateway(classpath="MyJar2.jar")

#import the java class
java_import(gateway.jvm,'Examples2')
dict_words = {}

def get_senses():
	out = gateway.jvm.Examples2.demonstration()
	python_output = open('output2.txt','w', encoding='utf-8')
	python_output.write(out)

def get_roots(word):
	roots = gateway.jvm.Examples2.getRoot(word)
	return roots
def analyse_file():
	file = open("story.txt", "r", encoding = "utf-8")
	for line in file:
		for word in line.split():
			for ch in string.punctuation:
				word = word.replace(ch,'')
			if word != '':
				root = get_roots(word)
				if root == '':
					store(word)
				else:
					store(root)

def store(root):
	if root in dict_words.keys():
		dict_words[root] = dict_words[root] + 1
	else:
		if root != '':
			dict_words[root] = 1
	
def visualize():
	plt.rc('font', family='Mangal') #run command
	frequency_dist = Counter(dict_words) #for counting objects - keys (elements) and count(values)
	most_common = dict(frequency_dist.most_common(10))
	#plt.bar(most_common.keys(), most_common.values(), color='#FF4500')
	
	plt.bar(range(1,11), list(most_common.values()), color='#FF4500')
	plt.bar(list(most_common.keys()))
	#plt.xticks(range(len(most_common)), list(most_common.keys()))
	#plt.rcParams["figure.figsize"] = [16,9]
	plt.show()

get_senses()
analyse_file()
visualize()

