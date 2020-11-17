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


#Dictionary + Items method. items method -- in dictionaries will return the answer in form of multiple tuples.
name_age = {
    'Toby': 30,         # this is called key-value pair
    'Ralph': 8,         #where name is a key, and age is value
    'Megan': 35
}
for key, value in name_age.items():    #in this for loop "name_age.items()" -- will iterate the key-value pairs.
    print(key, value)


    
#zip function    
#combining list and tuple into a tuple of tuples, using zip function
fruits = ['strawberry', 'raspberry', 'blueberry']    #this is a list
color = ('red', 'pink', 'purple')                    #this is a tuple

def fruits_color(fruits, color):
    fruits_color = tuple(zip(fruits, color))         #zip function is used in order to combine a tuple and a list
    return fruits_color
print(fruits_color(fruits, color))                   #the result will be in the form of "tuple of tuples"
