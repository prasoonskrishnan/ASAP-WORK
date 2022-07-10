# Input from user and multiplication
print('I, Multiplication')
num_1=float(input('Enter the first value:'))
num_2=float(input('Enter the second value:'))
result=num_1*num_2
print(num_1,'x',num_2,'=',result)
print('\n\n')
print('II, Recatngle')

# Calculation of area and perimeter of rectangle
length=float(input('Enter the length:'))
breadth=float(input('Enter the breadth:'))
Area=length*breadth
b=length+breadth
Perimeter=2*b
print('Area of rectangle:', Area,
      'Perimeter of rectangle:', Perimeter)
print('\n\n')

# Calculating area and perimeter of a circle
print('III, Circle')
radius=float(input('Enter the radius of circle:'))
pi=3.14
radius_sqr=radius**2
Area=pi*radius_sqr
perimeter=2*pi*radius
print('Area of circle:',Area,
      'Perimeter of circle:',perimeter)
print('\n\n')

# Adding first two numbers and then multiply with a third number
print('IV, Operation')
num_1=float(input('Enter first value:'))
num_2=float(input('Enter the second value:'))
num_3=float(input('Enter the third value:'))
result=(num_1+num_2)*num_3
print('(',num_1,'+',num_2,')','x',num_3,'=',result)
print('\n\n')

# Coversion of celsius into fahrenheit scale
print('V, Temp.')
celsius=float(input('Enter the temp. in celsius:'))
fahr=(celsius*9/5)+32
print(celsius,'C is', fahr,'F')
print('\n\n')

#Calculate the volume of cube
print('VI, Cube')
side=float(input('Enter the length of the side of cube:'))
volume=6*(side**3)
print('Volume of cube is', volume)
print('\n\n')

# Calculation of volume of sphere
print('VII, Sphere')
radius=float(input('Enter the radius of sphere:'))
volume=4/3*3.14*(radius**3)
print('The volume of sphere is:',volume)
print('\n\n')
print('THANK YOU')
