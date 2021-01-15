#this is an example of object oriented programming
#encapsulates functionality using classes
class Fruit:                               #Self is automatically assigned to the new piece of Fruit class
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def fruits_color(self):
        fruits_color = self.name, self.colour
        return fruits_color

    def displayFruits(self):
        print(self.fruits_color())

if __name__ == '__main__':
    fruit1 = Fruit('kiwi', 'green')
    fruit1.displayFruits()

    fruit2 = Fruit('pomegranate', 'red-pink')
    fruit2.displayFruits()


#functional approach
#pure functions will be used
def recipe_function(Recipe):            #here the Recipe function will not change the input recipe
    new_recipe = []                     #however will return new recipe
    for i in Recipe:
        new_recipe.append(i+'+sugar')
    return new_recipe

raw_Recipe = ['coffee', 'tea', 'lemonade']
sweet_Recipe = recipe_function(raw_Recipe)

print(raw_Recipe)
print(sweet_Recipe)
