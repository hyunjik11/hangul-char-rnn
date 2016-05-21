#!/usr/bin/python
# -*- coding: utf-8 -*-

#  leave same till we have consonant followed by a vowel (c,v).
#  In this case add the two into buffer.
#  - case 1: next is (c',c'') -> join&output(c,v,c'), and go back to 2.
#  - case 2: next is (c,v) -> add u'' to buffer, replace chars in buffer with syllable, add next two to buffer and go back to 3.
#  - case 3: next is v -> add u'' to buffer, replace chars in buffer with syllable, leave v same, go back to 3.
import codecs
import korean

filename="test.txt" #file that needs to be post-processed
savefile="post_test.txt" #post-processed file

def inrange(char,unicode_dec):
    if unicode_dec[0]<=ord(char)<=unicode_dec[1]:
        return True
    else:
        return False

letter=[ord(u'ㄱ'),ord(u'ㅣ')]
consonant=[ord(u'ㄱ'),ord(u'ㅎ')]
vowel=[ord(u'ㅏ'),ord(u'ㅣ')]
output=u''
with codecs.open(filename,encoding='utf-8') as f:
    for line in f:
        i=0;
        while i<len(line)-1:
            if inrange(line[i],consonant) and inrange(line[i+1],vowel):
                if i==len(line)-2: #line[i+1] is last character
                    output+=korean.hangul.join_char((line[i],line[i+1],u''))
                    i+=2
                elif inrange(line[i+2],consonant):
                    if i==len(line)-3: #line[i+2] is last character
                        output+=korean.hangul.join_char((line[i],line[i+1],line[i+2]))
                        i+=3
                    elif inrange(line[i+3],vowel):
                        output+=korean.hangul.join_char((line[i],line[i+1],u''))
                        i+=2
                    else: #line[i+3] a consonant or not a letter
                        output+=korean.hangul.join_char((line[i],line[i+1],line[i+2]))
                        i+=3
                else: #line[i+2] is a vowel or not a letter
                    output+=korean.hangul.join_char((line[i],line[i+1],u''))+line[i+2]
                    i+=3
            else: #search until we get a consonant followed by a vowel
                output+=line[i]
                i+=1
        if i==len(line)-1: #clear up last character - could be new line
            output+=line[i]

with open(savefile, "a") as f:
    f.write(output.encode("UTF-8"))




        