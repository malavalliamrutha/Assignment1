import unittest
def classify_triangle(a,b,c):
    if a==b==c:
        print('It is an Equilateral Triangle')
    elif a==b or b==c or c==a:
        print('It is an Isosceles Triangle')
    elif (a*a)+(b*b)==(c*c) or (b*b)+(c*c)==(a*a) or (a*a)+(c*c)==(b*b) :
        print('It is an Right Angled Triangle')
    else:
        print('It is an Scalene Triangle')
try:   
    a = int(input('Enter the first side of a triangle: '))
    b = int(input('Enter the second side of a triangle: '))
    c = int(input('Enter the third side of a triangle: '))
except:
    print('Invalid Input')
classify_triangle(a,b,c)