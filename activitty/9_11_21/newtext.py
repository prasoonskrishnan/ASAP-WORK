import os
myfile = open('text2.txt','w')
matter = 'Python is a awesome programming language'
myfile.write(matter)
myfile.close()
myfile = open('text2.txt')
text = myfile.read()
myfile.close()
text = text.lower()
total = len(text)
list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.',',']
dict1 = {}

for items in list1:
    if items in text:
        dict1[items] = text.count(items)
    else:
        dict1[items] = text.count(items)
print('Letters\t\tPercentage')
print('_'*30)
for i in dict1:
    print(f'{i}\t\t{(dict1[i]/total*100):.2f}')
