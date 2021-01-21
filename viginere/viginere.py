import string
from itertools import product
import numpy as np


def know_key_length(a):
    s = 0
    b = 0.0667
    minn = 100
    for i in range(len(a)):
        ee = abs(a[i] - b)
        if (minn > ee):
            minn = ee
            s = i + 2
    return s


def form_alph():
    alph = []
    for i in range(26):
        alph.append(chr(ord('a') + i))

    return alph

def precombine(a,s):
    b=np.array(a)
    c=np.transpose(b)
    listt=[]
    for i in product(*c):
        lisst=list(i)
        lissst=combine(lisst,s)
        listt.append(''.join(lissst))
    return listt


def combine(a,s):
    list_final=[]
    list_final2=[]


    for i in range(len(''.join(a))):
        list_final.append(0)
    for e in range(len(a)):
        r=0
        for i in a[e]:
            list_final[r*s+e]=i
            r+=1
    strr=''.join(str(i) for i in list_final)
    list_final2.append(strr)
    return list_final2


def get_list_decrypted(a,b,h):
    list_letters=['e','t','a','o','i','n']
    list_good2=[]
    for k in list_letters:
        list_good=[]
        for q in range(len(a)):
            str_temp=""
            for i in a[q]:
                razn=b.index(h[q])-b.index(k)
                sm=b.index(i)-razn
                if(26>sm>=0):
                    str_temp=str_temp+b[b.index(i)-razn]
                if(sm<0):
                    str_temp=str_temp+b[len(b)+(b.index(i)-razn)]
                if(sm>25):
                    str_temp=str_temp+b[sm-26]
            list_good.append(str_temp)
        list_good2.append(list_good)
    return list_good2

def divide_by_key_length(s, a):
    t = 0
    list_shifrov = []
    list_tmp = []
    while (t < len(a)):
        strd = ""
        iss = 0
        while (t + s * iss < len(a)):
            if (t + s * iss not in list_tmp):
                strd = strd + a[t + s * iss]
                list_tmp.append(t + s * iss)
                iss = iss + 1
            else:
                iss = iss + 1
        if (strd != ""):
            list_shifrov.append(strd)
        t = t + 1
    print(list_shifrov)
    return list_shifrov


def most_popular_letter(a):
    h = []
    for i in range(len(a)):
        gg = dict.fromkeys(a[i], 0)
        for ii in a[i]:
            gg[ii] += 1
        u = 0
        max_str = ''
        for iiii in gg:

            if gg[iiii] > u:
                u = gg[iiii]
                max_str = iiii
        h.append(max_str)
        print(max_str)

    return h


def get_list_cisum(a, b):
    c2 = []
    for ii in b:
        st = ""
        t = 0
        while (t < len(a)):
            st = st + a[t]
            t += ii

        d = dict.fromkeys(st, 0)
        for i in st:
            d[i] += 1

        d2 = dict.fromkeys(st, 0)
        for i in d:
            d2[i] = (d[i] * (d[i] - 1)) / (len(st) * (len(st) - 1))

        summ = 0
        for i in d2:
            summ = summ + d2[i]
        c2.append(summ)

    return c2

c=[i for i in range(2,9,1)]
with open('inputtext.txt','r') as myfile:
    e=myfile.read()
myfile.close()
clearstring=''.join(c for c in e.lower() if c in string.ascii_lowercase)
with open('clearedtext.txt','w') as myfile1:
    e1=myfile1.write(clearstring)
myfile1.close()
alphabet='abcdefghijklmnopqrstuvwxyz'
key='hello'
key_len=len(key)
key_as_int=[alphabet.index(i) for i in key]
word_as_int=[alphabet.index(i) for i in clearstring]
cipher=''
for i in range(len(word_as_int)):
    value=(word_as_int[i]+key_as_int[i%key_len])%26
    cipher+=alphabet[value]
print(cipher)
list2=get_list_cisum(cipher,c)
key_len2=know_key_length(list2)
list3=divide_by_key_length(key_len2,cipher)
list4=most_popular_letter(list3)
alph=form_alph()
list5=get_list_decrypted(list3,alph,list4)
list6=precombine(list5,key_len2)
popular_words=['the','be','to','of','and','in','that','have','it','for']
with open('outputted.txt','w') as myfile2:  # type: TextIO
    for i in list6:
        myfile2.write("%s\n" % i)
myfile2.close()
listg=[]
for i in list6:
    m=0
    for b in popular_words:
        m+=i.count(b)
    listg.append(m)

with open('englishwords.txt','w') as myfile3:
    for i in listg:
        myfile3.write("%s\n" %i)
myfile3.close()
print(key_len2)
list_sorted=[]
for i in list6:
    r=listg.index(max(listg))
    list_sorted.append(list6[r])
    listg[r] = 0

with open('possiblewords.txt','w') as myfile4:
    for i in list_sorted:
        myfile4.write("%s\n" %i)

lisd=[]
for i in range(len(cipher)):
    g=alph.index(cipher[i])%26-alph.index(list_sorted[0][i])%26

    if g<0: lisd.append(26+g)
    else: lisd.append(g)
tempp=[]
strr=''
for i in lisd:
    if i not in tempp:
        tempp.append(i)
        strr+=alph[i]

print(strr)
print(lisd)
