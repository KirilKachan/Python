import math
from math import*
def func1(x1,x2):
    s=cos(x1)*tan(x2)+math.log(exp(x1)+4,5)+(1/(sqrt(abs(x1)+0.1)))
    return(s)
x=float (input ( "Введіть x: "))
y=float (input ( "Введіть у: "))
s=func1(x,y)
print (s)