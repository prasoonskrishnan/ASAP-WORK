foods = []



def display():
    print('1.PIZZA--->250\t2.BURGER--->150\t3.KFC--->100\t4.PEPSI--->50\t5.QUIT')
    opt = int(input('Enter the option: '))
    
    if opt==5:
        tabled(foods)
    else:
        qty = int(input('How much? '))
        cal(opt,qty)
              
    return opt



def cal(opt,qty):
    if opt == 1:
        createfood('pizza',qty,250)
    if opt == 2:
        createfood('burger',qty,150)
    if opt == 3:
        createfood('kfc',qty,100)
    if opt == 4:
        createfood('pepsi',qty,50)
        
    

def createfood(food,n,price):
    dic1={'Name':food,'Qty':n,'Total':n*price}
    foods.append(dic1)

def tabled(food):
    gross = 0
    print('\nName\t\tQty\t\tPrice')
    print('_'*40)
    for i in food:
        gross = gross + int(i['Total'])
        print(f"{i['Name']}\t\t{i['Qty']}\t\t{i['Total']}")
    print('_'*40)
    print(f'Total\t\t   \t\t{gross}')
    










