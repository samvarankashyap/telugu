# -*- coding: utf-8 -*-
import codecs
import unicodedata
text = open("samples/kandam_sample.txt","r").read()
f = codecs.open("samples/kandam_sample.txt", "r", "utf-8")
#print f.readline()

def ganav(desc):
    "gana vibhajana"
    ganas = []
    v = False
    for d in desc:
        if "LETTER" in d:
            if v:
                v = False
                continue
            ganas.append("I")
        if "VOWEL" in d:
            sign = d.split()[-1]
            if sign in ["AA", "AI", "EE", "OO", "II"]:
                ganas.pop()
                ganas.append("U")
        if "VIRAMA" in d:
            ganas.pop()
            ganas.pop()
            ganas.append("U")
            ganas.append("I")
            v = True
            
    return ganas

lines = f.readlines()
letters = []
gana = []

desc = []
for line in lines:
    print line
    for word in line.split():
        desc.extend([ unicodedata.name(c) for c in word])
    print desc

print ganav(desc)
