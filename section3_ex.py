# -------- Ex. 1 --------
print("This is exercise 1")

age = 27
for num in range(0, age):
    if num % 2 == 0:
        print(num)


# -------- Ex. 2 --------
print("This is exercise 2")

day = "Tuesday"

if day == "Monday" or day == "Tuesday":
    print("Today is sunny!!!")
else:
    print("Today it will rain...")


# -------- Ex. 3 --------
print("This is exercise 3")

myWeight = 145

for year in range(2016,2027):
    moonWeight = myWeight / 6.0
    if year == 2016:
        print("My weight in %(year)i is %(myWeight)i lbs" %locals())
        print("and my weight on the moon would be %(moonWeight)f lbs" %locals())
    else:
        print("My weight in %(year)i will be %(myWeight)i lbs" %locals())
        print("and my weight on the moon would be %(moonWeight)f lbs" %locals())
    year += 1
    myWeight += 1
