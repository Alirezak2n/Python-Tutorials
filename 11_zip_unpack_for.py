list1 = [1,2,3,4,5,6]
list2 = ['one','two','three','four','five']

zipped = list(zip(list1,list2))
#ye list dorost mikone az item haye har do list
#age andaze item ha barabar nabashe un kamtara ro misaze
print(zipped)

#ye list ro migire be 2 ta list tabdil mikone
#faghat ba ye * jolosh
unzipped = list(zip(*zipped))

print(unzipped)

#in unpack kardane o jalebe
#tuple haye 2tayie tu list o har kodumo joda mide
for (l1,l2) in zip (list1,list2):
    print(l1)
    print(l2)
print(8*"***")
for i in range(len(list2)):
    print(list1[i])
    print(list2[i])

items = ['apple','banaana','orange']
counts = [3,6,4]
prices = [0.99,0.25,0.25]
sentences = []
for (i,c,p) in zip(items,counts,prices):
    i,c,p = str(i),str(c),str(p)
    sentence = 'I bought ' + c + ' ' + i + 's at ' + p + '.'
    sentences.append(sentence)
print(sentences)

