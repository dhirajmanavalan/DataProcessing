import pandas as pd

s1=pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1,3,5,7,9])

add = s1+s2
sub = s1-s2
mul = s1*s2
div = s1/s2

print("add",add)
print("sub",sub)
print("mul",mul)
print("div",div)