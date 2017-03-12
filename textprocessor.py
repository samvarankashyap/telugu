# -*- coding: utf-8 -*-
import codecs
import unicodedata

GURU_LABELS =  ["AA", "AI", "EE", "OO", "II", "AU", "RR", "LL"]

def gana_vibhajana(padyam):
    lines = padyam.split("\n")
    desc = []
    v = False
    ganas = []
    for line in lines:
        for c in line:
            if c == " ":
                continue
            unicode_name = unicodedata.name(c)
            if "LETTER" in unicode_name:
                if v:
                    v = False
                    continue
                ganas.append("I")
            if "VOWEL" in unicode_name:
                label = unicode_name.split()[-1]
                if label in GURU_LABELS:
                    ganas.pop()
                    ganas.append("U")
            if "VIRAMA" in unicode_name:
                ganas.pop()
                ganas.pop()
                ganas.append("U")
                ganas.append("I")
                v = True
            if ("ANUSVARA" in unicode_name) or ("VISARGA" in unicode_name):
                ganas.pop()
                ganas.append("U")
    return " ".join(ganas)

text = open("samples/kandam_sample.txt","r").read()
f = codecs.open("samples/kandam_sample.txt", "r", "utf-8")
lines = f.read()
print gana_vibhajana(lines)
print "".join(lines.split("\n"))
