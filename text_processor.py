# -*- coding: utf-8 -*-
import sys
import codecs
import unicodedata
from tabulate import tabulate

GURU_LABELS =  ["AA", "AI", "EE", "OO", "II", "AU", "RR", "LL"]

def gana_vibhajana(padyam):
    lines = padyam.split("\n")
    desc = []
    v = False
    ganas = []
    chars = []
    cur_char = []
    for line in lines:
        for c in line:
            unicode_name = unicodedata.name(c)
            if "LETTER" in unicode_name:
                if v:
                    v = False
                    cur_char.append(c)
                    continue
                ganas.append("I")
                cur_char = []
                chars.append(cur_char)
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
    chars = ["".join(x) for x in chars]
    return zip(chars, ganas)

def call_for_data():
    text = open("samples/kandam_sample.txt","r").read()
    f = codecs.open("samples/kandam_sample.txt", "r", "utf-8")
    lines = f.read()
    gana_tuple =  gana_vibhajana(lines)
    table = [[ x[1] for x in gana_tuple], [ x[0] for x in gana_tuple]]
    headers = [x for x in range(0, len(gana_tuple))]
    return tabulate(table, headers, tablefmt="html")
