# nemoone vooroodi:
#                 4 (tedad jomle)
#                 man I je ich
#                 kheili very très sehr
#                 alaghemand interested intéressé interessiert 
#                 barnamenevisi programming laprogrammation Programmierung
#                 I am very interested in programming(baiad tarjome she)

#nemoone khoorooji:
#                 man am kheili alaghemand in barnamenevisi



n = int(input())
d = dict()
for i in range(n):
    words = input().split()
    persian = words[0]

    for word in words[1:]:
        d[word] = persian


sentence = input().split()
str = ''
for word in sentence:
    if word in list(d.keys()):
        str +=  d[word] + ' '
    else:
        str += word + ' '
   
        

print(str)

