a = 3
b = 5.4
c = input('enter any value: ')
enter any value: 1.5
type(a)
<class 'int'>
type(b)
<class 'float'>
type(c)
<class 'str'>
float(a)
3.0
a
3
aa = float(a)
bb = int(b)
type(bb)
<class 'int'>
c_int = int(c)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    c_int = int(c)
ValueError: invalid literal for int() with base 10: '1.5'
c_float = float(c)
c
'1.5'
c_float
1.5
c_int + int(c_float)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    c_int + int(c_float)
NameError: name 'c_int' is not defined. Did you mean: 'print'?
c_int = int(c_float)
c
'1.5'
c_int
1
c_int = int(float)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    c_int = int(float)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'type'
c_int = int(float(c))
c_int
1
name = a
int(name)
3
name = 'a'
int(name)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int(name)
ValueError: invalid literal for int() with base 10: 'a'
float(name)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    float(name)
ValueError: could not convert string to float: 'a'

#If you want to perform arithmatic operations with values stored in variables created using the input function. We must first cast them to a numeric value.
#Convert miles into kilometers.

miles = input('Enter the number of miles: ')
Enter the number of miles: 10
type(miles)
km = miles * 1.60934
