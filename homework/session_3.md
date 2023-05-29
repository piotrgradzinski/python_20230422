## 4. Classes

### Exercise 4.1 | Advertisements

Create a class where you will store information about advertisements (just like on a portal where you want to sell a car or apartment).

Class `Advertisement` should store information about: title, price, contact details of the seller.

### Exercise 4.2 | List of advertisements

Create a program, where you create a list od car Advertisements, and then you create a sample code to search through them and return matches, for example by price or any other advertisement attribute.

### Exercise 4.3 | Train

Create a `Train` class. Train has two attributes: speed (initial value is 10) and amount of fuel (initial value is 1000).

Add `__str__` method to the `Train` class. This method should return (not print) "My speed is XYZ. I have XYZ fuel in my tank."

Add method `speed_up`. This method should accept an argument describing how much you should increase the speed. This method should also decrease the fuel level by the given formula: `(new_speed - old_speed) * (old_speed / 100)`.

Once you shouldn't be able to increase the speed by more than 75% of the current speed. 

Create several tests using pytest to check if the behaviour is correct.

### Exercise 4.4 | Tank

Create `Tank` class. It should have `water_amount` attribute with initial value 0.

Add methods `fill` and `drain` with `how_much` argument. You shouldn't be able to drain more than is in the tank.

Implement `__str__` method that will return a string describing how much water is in the tank.

### Exercise 4.5 | Turtle

Create `Turle` class with methods `go` and `rotate`. Turtle has a position express by two coordinates and a course expressed in degrees.

While creating a turtle object, we provide its initial position (x, y). Course should be set to 0.

`rotate` method changes the course by the given number of degrees clockwise.

`move` method changes the position of the turtle.

Example:

```python
t = Turtle(100, 100)
t.go(50)

print(t)  # x=150, y=100 

t.rotate(90)
t.move(50)

print(t)  # x=150, y=50
```

### Exercise 4.6 | Tic Tac Toe

Create a class `BoardXO` - it will represent the state of the game.

Implement the following methods:
`add_element(x: int, y: int, element_type: str)`
This method should accept only strings `"x"` and `"y"`. When other string is provided, raise an error.

`game_state()` - this method should return the string representing the state of the game (in progress, Xs won, Os won). 

`whose_move()` - this method should tell whose move is next (x or o).

`__str__` - should return a string with a board representation.

Use this class to create interactive (using console/input) game.


### Exercise 4.7 | Advertisements / inheritance

Add two classes to the exercise with advertisements that inherit from `Advertisement` class.
`CarAdvertisement` - with additional attributes: model, brand, year of production, milage, type of fuel.
`ApartmentAdvertisement` – with additional attributes: city, apartment size, number of rooms.


## 5. Files

### Exercise 5.1 | Data of ski jumpers (3 hours)

CSV data file: https://students.alx.pl/~pgradzinski/kpython/zawodnicy.csv

Using a CSV file with data of ski jumpers, write programs that load this file and:

1. lists the tallest, lowest, heaviest and lightest jumper; if several had the same weight or height, just list one of them.
2. counts how much the Polish representatives weigh in total (e.g. to see if they will fit in the elevator to the hill ;)). Let the user specify the country (does not necessarily have to be Poland).
3. (more difficult) for all countries, it calculates how many athletes are from that country; i.e. it is supposed to list, perhaps in a different order:

```
AUT – 2
FIN – 3
GER – 5
NOR – 3
POL – 3
USA – 1
```

4. as above, but still counts for each country the average height of the players.

### Exercise 5.2 | Count the word of your choice (1 hour)

Downloadable file of the "Pan Tadeusz": https://students.alx.pl/~pgradzinski/kpython/pan-tadeusz.txt

Let the program, for a given text file name and for a given word, count how many times that word occurs in the file.

### Exercise 5.3 | Count all the words (trudne) (2 hours)

Basic functionality:
Write a program that reads a text file and enumerates and prints out, without repetition, all the words occurring in the file, along with how many times the word occurs. For example, like this:

```
Zosia -> 34
Asesor -> 35
dwóch -> 35
Tadeusz -> 107
```

Possible simplification (in case of problems with listing): list only the single most common word.

Further extensions (optional):
- sort the extracted words
- in addition to the number of individual words, count and output the number of all words, the total number of all characters.