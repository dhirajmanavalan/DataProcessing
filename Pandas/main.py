import pandas as pd

# s = pd.Series([1, 2, 3, 4, 5])
# # print(s)
# # print(s.index)
# # print(s.values)
# s.name = "numbers"
# # print(s.name)
# print(s)


# s=pd.Series([12,32,14,441])
# s.name = "Numbers_dhiru"
# print(s)
# print(s.index)
# print(s.values)
# print(s.name)

# s = pd.Series([1,2,3,4,5])
# print(s[1:4])

# s = pd.Series([10, 20, 30, 40, 50])
# print(s.iloc[[1, 2, 3]])

# s = pd.Series([100, 120, 200, 270, 300])
# index = ["apple", "banana", "grape", "orange", "mango"]
# s.index = index
# s.name = "calories"
# # print(s)

# # print(index[1:3])
# # print(s.iloc[[2,4]])
# print(s.loc["grape"])

# s = pd.Series([100, 120, 130, 140, 150])

# index = ["a", "b", "c", "d", "e"]

# s.index = index
# s.name = "calories"

# # print(s)

# # print(s.iloc[1:4])
# # print(s.loc["a":"d"])

# print(s.loc["a"])


fruit_protein = {
    "lemon" : 20,
    "apple" : 2,
    "orange" :4
}

print(pd.Series(fruit_protein, name="protein"))


fruits = {"mango": 1.0, "orange": 2.3, "apple": 0.49, "pineapple": 3.9, "avacoda": 3}

s = pd.Series(fruits, name="proteins")
# print(s)

print(s > 1)

print(s[s>1])


fruits = {
    "apple": 0.2,
    "banana": 1.2,
    "orange": 2.4,
    "mango": 3.4,
    "pineapple": 1.9,
}

s = pd.Series(fruits, name="proteins")
print(s)

print(s[(s > 1) & (s < 3)])

s['orange'] = 2.33

print(s)

