#List. List is a mutable set of data and the set of data can be any type of value. Ordered.

l1 = ['Raspberry', 10401, 15.36, 'fruit']
print(l1)


#mutable means that we can change any value in the list,
#by referring to its index, and giving the value on the right side:

l1[2] = 'fifteen'
print(l1)


#Tuple. Unlike lists, tuples are immutable, meaning that we cannot change its values.

t45 = ('bee', 'giraffe', 'horse', 'penguin')
print(t45)
#t45[2] = 'dolphin'   -- if you do like this, it will show error.
