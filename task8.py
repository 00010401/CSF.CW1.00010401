def fruits_color():                                   #this is the void function which can be only exectued
    print('blueberry is blue')                        #and do not return the value
    print('banana is yellow')                         #so, from this function we cannot return values
    print('raspberry is pink')                        #it will return none

print('This is the list of fruits and their color')
fruits_color()                                        #in this case it only executes the function
print('Done!')


animals = ['lion', 'penguin', 'rabbit']               #this is a list
type = ('wild', 'mammal', 'domestic')                 #this is a tuple

def animals_type(animals, type):                      #this function returns a value, as it has return statement
    animals_type = tuple(zip(animals, type))
    return animals_type                               #this is the return statement
print(animals_type(animals, type))
