from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()

favorite_color = input('What is your favorite color? ') # input takes a prompt, which needs to be a string
print(f'Your favorite color is: {favorite_color}') #output, prints the color given to the console
