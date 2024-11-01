from Objects.polynomial import *
from Objects.operations import *

p1 = Polynomial([5,4,2])
p2 = Polynomial([2,1])
print("t4")
d=division_recursive(p1,p2)
print(d[0].get(), d[1].get())
