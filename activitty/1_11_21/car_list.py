cars=[]
limit=int(input('How many cars do you want add to list: '))
var=0
while var<limit:
    item=input(f'Enter the item {var+1} :')
    var+=1
    if item[0]=='l' or item[0]=='L':
        cars+=[item]
        
print(cars)
