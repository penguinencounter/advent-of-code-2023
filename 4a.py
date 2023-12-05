# Part 1 fits on a card.
import re;s=0
try:
    while 1:s+=int(2**(len((x:=list(map(lambda x:set(re.findall(r'(\d+)',x)),
input().split(':')[1].split('|'))))[0].intersection(x[1]))-1))
except: print(s)