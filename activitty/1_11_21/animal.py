animals=[]
limit=int(input('Enter the number of item you want to add to list: '))
var=0

while var<limit:
    item=input(f'Enter a animal {var+1}: ')
    var+=1
    if len(item)<=4:
        animals+=[item]
var2=0
while var2<=len(animals)-1:
    print(animals[var2])
    var2+=1
