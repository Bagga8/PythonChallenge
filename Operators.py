bagga_age = 25
bagga_height =1.90
imaginary_number = complex(6,3)

print(bagga_age)
print(bagga_height)
print(imaginary_number)


#Triangle calculations
base= float(input('Please enter the value of the base:'))
height= float(input('Please enter the value of the height:'))
hypotenus= float(input('Please enter the value of the hypotenus:'))

area = base * height * 0.5
perimeter = base + height + hypotenus

print("area of a triangle using", base, "and", height, "= ", area)
print("Perimeter of a triangle using", base, "and", height, "and", hypotenus, "=", perimeter)


#Rectangle calculations
length = float(input('Please Enter the Length of a Rectanlge: '))
width = float(input('Please Enter the Width of a Rectangle: '))

perimeter = 2 * (length + width)

print("Perimeter of a Rectangle using", length, "and", width, " = ", perimeter)


#Circle calculations
radius = float(input('Please Enter the radius of a circle: '))
pi = 3.14

area = pi * radius * radius
circumference = 2 * pi * radius

print("Circumference of cirle", radius, " = ", circumference)
print("Area of circle", radius, " = ", area)

#Equation of a line
x = 0
y_intercept = 2 * x - 2

y = 0
x_intercept = (y + 2) / 2

slope = (y - y_intercept) / (x_intercept - x)
print("The slope is ", slope)
print("The x-intercept is ", x_intercept)
print("The y-intercept is ", y_intercept)

x1, y1 = 2, 2
x2, y2 = 6, 10
m = (y2 - y1) / (x2 - x1)
d = (((y1 - x1) ** 2) + ((y2 - x2) ** 2)) ** 0.5
print("The slope is ", m)
print("The Euclidean distance is ", d)

if slope > m:
    print("slope in task 8 is greater than slope in task 9")
else:
    print("slope in task 8 is less than slope in task 9")

proceed = True
while proceed:
    x = int(input("Enter the value of x: "))
    y = (x ** 2) + (6 * x) + 9
    if y == 0:
        print("y is zero when x is ", x)
        proceed = False

#python and dragon
python = "python"
dragon = "dragon"
print(len(python) > len(dragon))

print('on' in python and 'on' in dragon)

print("jargon" in "I hope this course is not full of jargon")

print('on' not in python and 'on' not in dragon)

(text_len) = len(python)
f_text_len = float(text_len)
s_text_len = str(text_len)

#Modulus
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is not even")

#Floor division
floor_div = 7 // 3
number = 2.7
if floor_div == int(number):
    print("floor division of 7 by 3 is equal to the int converted value of 2.7")
else:
    print("floor division of 7 by 3 is not equal to the int converted value of 2.7")

#Comparisons
if type('10') == type(10):
    print("type of '10' is equal to type of 10")
else:
    print("type of '10' is not equal to type of 10")

if int('9.8') == 10:
    print("int('9.8') is equal to 10")
else:
    print("int('9.8') is not equal to 10")

#Prompt scripts
hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hours: "))
pay = hours * rate
print("The pay of the personis: ", pay)

years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("The number of seconds a person can live is ", seconds)

#Form a table
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)
