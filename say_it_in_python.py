# # Fizz Buzz
#
# for i in range(1,101):
#     if i%15 == 0:
#         print("FizzBuzz")
#     elif i%3 == 0:
#         print("Fizz")
#     elif i%5 == 0:
#         print("Buzz")
#     else:
#          print(i)

# --------------------------------------
#
# dict = {'name': 'Miguel'}
#
# for key,val in dict.iteritems():
#     # print "My {} is {}".format(key,val)
#     print("My %(key)s is %(val)s" %locals())
#
#
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# my_list_sq = [num*num for num in my_list]
# print(my_list_sq)

 # --------------------------------------

# def fib(num):
#     a,b = 0,1
#     for i in range(0,num):
#         yield("{}: {}".format(i+1, a))
#         a,b = b, a+b
#
# for num in fib(10):
#     print(num)

# --------------------------------------

cities = ["Miami", "Tampa", "Orlando"]

i=0
for city in cities:
    print(i,city)
    i += 1


# BETTER WAY
for i,city in enumerate(cities):
    print(i, city)

# --------------------------------------


x_list = [1,2,3]
y_list = [2,4,6]

for i in range ( len(x_list)):
    x = x_list[i]
    y = y_list[i]
    print(x, y)


# BETTER WAY
for x, y in zip(x_list, y_list):
    print(x, y)


# --------------------------------------

x = 10
y = -10

print("Before: x = %d, y = %d" %(x,y))
tmp = y

y = x
x = tmp

print("After: x = %d, y = %d" %(x,y))

# BETTER WAY
x,y = y,x  # tuple unpacking


# --------------------------------------
ages = {"Miguel": 27, "Steve": 42}

if 'Dick' in ages:
    age = ages['Dick']
else:
    age = "Unknown"
print("Dick is %s years old" %age)

# BETTER WAY
age = ages.get("Dick", "Unknown")
print("Dick is %s years old" %age)


# --------------------------------------
needle = 'd'

haystack = ['a', 'b', 'c']
# haystack = ['a', 'b', 'c', 'd']

found = False
for letter in haystack:
    if needle == letter:
        print("Found!")
        found = True
        break
    if not found:
        print("Not found!")


# BETTER WAY
for letter in haystack:
    if needle == letter:
        print("Found!")
        break
else: # if no break occured
    print("Not found!")




# --------------------------------------
f = open("pimpin-aint-easy.txt")
text = f.read()
for line in text. split("\n"):
    print(line)
f.close()


# BETTER WAY
f = open("pimpin-aint-easy.txt")
for line in f:
    print(line)
f.close()

# EVEN BETTER WAY
# 'with' automaticly closes file
with open("pimpin-aint-easy.txt") as f:
    for line in f:
        print(line)




# --------------------------------------
print("Converting!")
try:
    print(int("1"))
except:
    print("ERROR: Conversion Failed!")
print("Done!")


# BETTER WAY
print("Converting!")
try:
    print(int("1"))
except:
    print("ERROR: Conversion Failed!")
else: # if no except is raised
    print("Conversion Successful!")
finally: # ALWAYS do this regardless of except
    print("Done!") # this is still returned even if try fails
