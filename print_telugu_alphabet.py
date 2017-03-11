# -*- coding: utf-8 -*-
achulu = {}
hallulu = {}
gudinthalu = {}
ankelu = {}
telugu_alphabet = {}

# 3073 to 30183 
def unicode_store(alphabet_type,start, end, skip =[]):
    for i in xrange(start, end+1):
        if i in skip:
            continue
        print(hex(i))
        print(unichr(i))
        if alphabet_type in telugu_alphabet:
            telugu_alphabet[alphabet_type][i] = unichr(i)
        else:
            telugu_alphabet[alphabet_type] = {}

unicode_store("achulu", 3073, 3092, skip=[3076,3085,3089])
unicode_store("achulu", 3168, 3169)
unicode_store("hallulu", 3093, 3129, skip=[3113, 3124])
telugu_alphabet["hallulu"]["309331493127"] = unichr(3093)+unichr(3149)+unichr(3127)
unicode_store("ankelu", 3174, 3183)
for k in telugu_alphabet:
    for k2 in  telugu_alphabet[k]:
        print telugu_alphabet[k][k2]
