import operator
from fractions import gcd
from functools import reduce


value = "dlcoepvccxkjswfdivdwmmmcdcnbiqorrzeqdelnjsdypoelisloafyvckhqypbkrbwmbnpcorevmqrpgdipkvwdivdwuspjlidkqgvmybagdlrrikshzbsuxzmvykowmpxfoicdwusxfdlcccklsjyjyvjpohhoacviklsqcibyrrridbsldgmfipwsqdsddlcgspuwydxpsfsdibdsisrekpdbibyvryecvjpsgyvslqagdlqyqcyjrrsqofwlmqrsngyjpwrkryxhkegfkrmxckyyqzvmciyxhtovqojpyqrrinbiayroeiqdtcbmmnepoxmlidyylnagdlgxxfowmmmcdcrrvcowcbmccejvsddlccypfmtsrewibsitkpbbekkqmcxmpxfoqgnhjoilqpgclpyqyxgccqsmlpopgqmmewyxhqogsvepzvmciyxhtovqomlmpsnmlqxfoilqpgcluyvicsdtsfxkmgipdlmweqrsampcfiyxhkywryjakbryrnbmldwyvpdsrbdlcsvnveaomldlczyzvmakxgyrqgmrrssdicdwcnmrsslcwrehwyjkohgozyvilqpgclrobrcamepbrepnpwlinywqsfjo"
value_len=len(value)
diff=[]
i=0
c=0
while i+2<value_len:
    g=i+2
    while g+2<value_len:
        if(value[i]+value[i+1]+value[i+2]==value[g]+value[g+1]+value[g+2]):
            print(value[i]+value[i+1]+value[i+2]," ",value[g]+value[g+1]+value[g+2]," ",i," ",g)
            c=c+1
            diff.append(g-i)
        g=g+1
    i=i+1
    
res = gcd(*diff[:2])
for x in diff[2:]:
    res=gcd(res,x)
print(res)


            
    
