#!/usr/bin/env python

'''Exectuion Command: spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ dataset/output'''

import sys
from pyspark import SparkConf, SparkContext
import re

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]
delimiters = ""

with open(stopWordsPath) as f:
    data = f.read()
    stopwords = re.split("\\n|\\s",data)
	#TODO

with open(delimitersPath) as f:
    delimiters=",|;|\.|\?|!|-|:|@|\[|\]|\(|\)|\{|\}|_|\*|\/|\\n| "
    #TODO

conf = SparkConf().setMaster("local").setAppName("TitleCount")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[3],1)


def titlecountmap(line):
    retval = list()
    words=re.split(delimiters,line.lower());
    for word in words:
        if word not in stopwords and word != '':
            retval.append((word,1))
    



wc = lines.flatMap(lambda x: titlecountmap(x))

reduce = wc.reduceByKey(lambda a, b: a + b)


#TODO

outputFile = open(sys.argv[4],"w")

print(reduce)


#TODO
#write results to output file. Foramt for each line: (line +"\n")

sc.stop()
