from math import sqrt,pi

result = sqrt(9) * pi
print(result) # output : 9.424

"""from math import *
result = sqrt(9) * pi
print(result) """
# but this is importing everything 
# this is *wildcard
# but generally not recommended as it can lead to confusion and make it harder to understand

from math import pi, sqrt as s
result = s(9) * pi
print(result) #output : 9.424

#if ypu want to know how many functions math have you can use...
import math
print(dir(math))

#from sam import welcome, Sam
from sam import welcome, Sam
from sam import *
welcome()
print(Sam)