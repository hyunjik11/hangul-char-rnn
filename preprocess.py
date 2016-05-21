#!/usr/bin/python
# -*- coding: utf-8 -*-

import ijson
import korean
from konlpy.utils import pprint
filename="namuwiki_20160425.json"
#has between 513000 and 514000 entries
savefile="test_n.txt"

def inrange(char,unicode_dec):
    if unicode_dec[0]<=ord(char)<=unicode_dec[1]:
        return True
    else:
        return False

range_valid=[ord(u' '),ord(u'~')]
range_letter=[ord(u'ㄱ'),ord(u'ㅣ')]
range_syllable=[ord(u'가'),ord(u'힣')]

with open(filename,'r') as f:
    i=0
    final=u''
    for item in ijson.items(f,"item"):
        text=item['text']
        for char in text:
            if inrange(char,range_syllable):
                t=u''.join(korean.hangul.split_char(char))
                final+=t
            elif inrange(char,range_valid) or inrange(char,range_letter) or char=u'\n':
                #note ord(u'\n')=10
                final+=char
        i+=1
        if i==100:
        #if i%5140==0:
            #save to file and clear buffer final
            with open(savefile, "a") as f:
                f.write(final.encode("UTF-8"))
                final=u''
            break
            #print i/5140,"% complete"
    
