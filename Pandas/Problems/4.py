import pandas as pd

s = pd.Series([0,1,2,3,4,5,6])
s2 = pd.Series([3, 3, 3, 3, 3, 3, 3])


ans = s**s2

print(s.values)
print(ans.values)