sub1=int(input('Enter the mark of first subject:'))
sub2=int(input('Enter the mark of second subject:'))
sub3=int(input('Enter the mark of third subject:'))

total=sub1+sub2+sub3
average=total/3
percentage=(total/300)*100

if percentage<50:
    print('You failed in exam')
elif percentage>50:
    if percentage<75:
        print('3rd rank')
    elif percentage>75 and percentage<90:
        print('2nd rank')
    elif percentage>90:
        print('1st rank')
    
    
