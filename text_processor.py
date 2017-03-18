# -*- coding: utf-8 -*-
import sys
import codecs
import unicodedata
from tabulate import tabulate

GURU_LABELS =  ["AA", "AI", "EE", "OO", "II", "AU", "RR", "LL"]

def gana_vibhajana(padyam, linewise=False):
    lines = padyam.split("\n")
    desc = []
    v = False
    ganas = []
    chars = []
    cur_char = []
    newline = False
    for i in range(0, len(padyam)):
        #print c 
        c = padyam[i]
        if padyam[i] =="\n":
            if linewise:
                ganas.append("\n")
                chars.append("\n")
            newline = True
            continue
        next_c = padyam[i+1] if i < len(padyam)-1 else ""
        prev_c = padyam[i-1] if i > 0 else ""
        prev_c2 = padyam[i-2] if i > 0 else ""
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
                if next_c == "\n" or next_c == " ":
                    cur_char.append(c)
                    chars[-2].extend(chars[-1])
                    chars.pop()
                    ganas.pop()
                    ganas.pop()
                    ganas.append("U")
                    v = False
                else:
                    ganas.pop()
                    ganas.pop()
                    ganas.append("U")
                    ganas.append("I")
                    cur_char.append(c)
                    v = True
        if ("ANUSVARA" in unicode_name) or ("VISARGA" in unicode_name):
            ganas.pop()
            ganas.append("U")
            cur_char.append(c)
    for x in chars:
         print("".join(x))
    chars = ["".join(x) for x in chars]
    return zip(chars, ganas)

def call_for_data(filename=None, linewise=False):
    f = codecs.open("samples/kandam_sample.txt", "r", "utf-8")
    lines = f.read()
    gana_tuple =  gana_vibhajana(lines, linewise)
    print gana_tuple
    indexes = [i for i,x in enumerate(gana_tuple) if x == ('\n','\n')]

    print indexes
    if linewise:
        gana_tuple.append(('\n','\n'))
        htmls = []
        g_t = []
        for elem in gana_tuple:
            print elem
            if elem == ('\n','\n'):
                table = [[ x[1] for x in g_t], [ x[0] for x in g_t]]
                headers = [x for x in range(0, len(g_t))]
                htmls.append(tabulate(table, headers, tablefmt="html"))
                g_t = []
            else:
                g_t.append(elem)
        print htmls
        return htmls
    else:
        table = [[ x[1] for x in gana_tuple], [ x[0] for x in gana_tuple]]
        headers = [x for x in range(0, len(gana_tuple))]
        return tabulate(table, headers, tablefmt="html")
