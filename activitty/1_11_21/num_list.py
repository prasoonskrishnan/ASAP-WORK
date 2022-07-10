numbers=[]
limit=int(input('How many numbers you want to add to list? '))
var=0

while var<limit:
    num=int(input(f'Enter the number {var+1} :'))
    var+=1
    if num%2==0 and num>50:
        numbers+=[num]
print(numbers)
