# -------- Lists(Arrays) --------

# slice
array = ["this ", "is ", "actually ", "a ", "list!"]
array[0:1] # >>> ['this']
array[1:2] # >>> ["is "]
array[1:3] # >>> ["is ", "actually "]
array[0:] # >>> "this ", "is ", "actually ", "a ", "list!"


del array[index]
len(array)

aray.append("new thing") # append() is push()

numbers = [0,1,1,2,3,5,8,13,21]

# array.count() // counts instances of argument passed to it in an array
numbers.count(0) # >>> 1
numbers.count(1) # >>> 2
numbers.count(2) # >>> 1
numbers.count(13) # >>> 1



# -------- Dictionaries(Hashes or Associative Arrays) --------

students = {'eric': {'name': "eric", 'age': 14},
            'bob': {'name': "bob", 'age': 12},
            'tina': {'name': "tina", 'age': 26}}

In [14]: students
Out[14]:
{'bob': {'age': 12, 'name': 'bob'},
 'eric': {'age': 14, 'name': 'eric'},
 'tina': {'age': 26, 'name': 'tina'}}

In [15]: students['bob']
Out[15]: {'age': 12, 'name': 'bob'}

In [16]: students['bob']['name']
Out[16]: 'bob'

In [17]: students['bob']['age']
Out[17]: 12

In [14]: students
Out[14]:
{'bob': {'age': 12, 'name': 'bob'},
 'eric': {'age': 14, 'name': 'eric'},
 'tina': {'age': 26, 'name': 'tina'}}

In [15]: students['bob']
Out[15]: {'age': 12, 'name': 'bob'}

In [16]: students['bob']['name']
Out[16]: 'bob'

In [17]: students['bob']['age']
Out[17]: 12

In [18]: del students['bob']
In [19]: students
Out[19]: {'eric': {'age': 14, 'name': 'eric'}, 'tina': {'age': 26, 'name': 'tina'}}

{}.keys()
{}.values()
