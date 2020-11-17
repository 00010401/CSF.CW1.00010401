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


#Dictionary. In dictionaries, unlike lists the indices can be any type of value.
#Moreover, in dictionaries there won't be indices, instead they will have keys, which can be any type value.
#So, we use keys in dictionaries to change the value, not indices.

name_age = {
    'Toby': 30,         # this is called key-value pair
    'Ralph': 8,         #where name is a key, and age is value
    'Megan': 35
}
print(name_age)

name_age['Megan'] = 28     #this will change the value of 'Megan' key.
print(name_age)
