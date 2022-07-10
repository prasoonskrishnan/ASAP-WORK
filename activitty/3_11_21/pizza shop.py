def display():
    print('1.PIZZA\t 2.BURGER\t 3.FRENCH_FRIES\t 4.SANWICH\t 5.QUIT')
    opt=int(input())
    return opt

def pizza(n):
    unit=100
    total1=n*unit
    return total1
def burger(n):
    unit=150
    total2=n*unit
    return total2
def french(n):
    unit=30
    total3=n*unit
    return total3
def sanwich(n):
    unit=50
    total4=n*unit
    return total4
def quantity():
    n=int(input('How much do you want? '))
    return n

gross=0
while True:
    opt=display()
    if opt==1:
        n=quantity()
        a=pizza(n)
        gross+=a
    elif opt==2:
        n=quantity()
        b=burger(n)
        gross+=b
    elif opt==3:
        n=quantity()
        c=french(n)
        gross+=c
    elif opt==4:
        n=quantity()
        d=sanwich(n)
        gross+=d
    elif opt==5:
        break
print(f'Gross Total = Rs.{gross:.2f}')
