# -*- coding: utf-8 -*-
import codecs
import unicodedata

GURU_LABELS =  ["AA", "AI", "EE", "OO", "II", "AU", "RR", "LL"]

def gana_vibhajana(padyam):
    lines = padyam.split("\n")
    desc = []
    v = False
    ganas = []
    chars = []
    cur_char = []
    for line in lines:
        print line
        for c in line:
            unicode_name = unicodedata.name(c)
            print unicode_name
            if "LETTER" in unicode_name:
                if v:
                    v = False
                    cur_char.append(c)
                    continue
                ganas.append("I")
                cur_char = []
                chars.append(cur_char)
                print "".join(cur_char)
                #cur_chars = []
                cur_char.append(c)
            if "VOWEL" in unicode_name:
                label = unicode_name.split()[-1]
                if label in GURU_LABELS:
                    ganas.pop()
                    ganas.append("U")
                cur_char.append(c)
            if "VIRAMA" in unicode_name:
                ganas.pop()
                ganas.pop()
                ganas.append("U")
                ganas.append("I")
                v = True
                cur_char.append(c)
            if ("ANUSVARA" in unicode_name) or ("VISARGA" in unicode_name):
                ganas.pop()
                ganas.append("U")
                cur_char.append(c)
    for ch in chars:
        print "".join(ch)
    return ganas

text = open("samples/kandam_sample.txt","r").read()
f = codecs.open("samples/kandam_sample.txt", "r", "utf-8")
lines = f.read()
gana_dict =  gana_vibhajana(lines)
#print "".join(lines.split("\n"))
print gana_dict
