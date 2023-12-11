a = [1, 2, 3, 4, 5]

a[0] = "foo"

print("CHECK a is:", a) # check your work

a[3] = "bar"

print("CHECK a is:", a) # check your work

print(5)

print("CHECK a[-1] is:", a[-1]) # check your work (don't just write this for your answer!)

a[2:3] = ["hello", "world"]

print("CHECK a is:", a) # check your work

b = a
b[2] = "small"

print("small")

print("CHECK a[2] is:", a[2]) # check your work (don't just write this for your answer!)

c = [x for x in range(2, 10)] # this is a list comprehension!

print(5)

print("CHECK c[3] is:", c[3]) # check your work (don't just write this for your answer!)

d = [8, 7, 6, 5, 4]

d = [x-1 for x in d]
print(d)
