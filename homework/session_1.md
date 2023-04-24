## 1. Interaction with the user

### Exercise 1.1 | Interaction with the user and simple calculations
Ask user (using `input()` function) to provide the number of kilograms of potatoes he'd like to buy and how much 1-kilogram costs. The program should display how much user have to pay.

### Exercise 1.2 | Shoemaker

Ask the user to provide a number of days of the week (Monday=1, Sunday=7) when he left his shoes at the shoemaker shop for a repair. Ask him also how many days the repair will take. As an output, inform the user at which day of the week he should get back his shoes. For example, leaving shoes on Tuesday with 3 days needed for the repair, should output Friday. 

### Exercise 1.3 | BMI

Write a program that will ask the user for his height (in cm) and body weight, and as a result will present his BMI and recommendations. Take a look at BMI definition in wikipedia. 

### Exercise 1.4 | Hotel fee

Write a program, where the user provides his age and the number of nights he wants to stay at the hotel. Based on that values calculate the fee for his stay. The rules are:

- minor (below 18 years old) will pay 100 PLN per night
- adults (of age 18 but less than 65) will pay:
    - 200 PLN if they are staying for one night
    - 180 PLN if they are staying for at least 2 nights but less than 5
    - 150 PLN if they are staying for 5 and more nights
- pensioners (65 and older) will pay the same rate as adults but with a 10% discount

For example, if a user is 70 years old and will spend 10 nights at the hotel, he will pay 150 PLN - 10% discount = 135 PLN per night, so for the whole stay, he will pay 1350 PLN.

### Exercise 1.5 | Triangle area

Write a program that will ask a user for the lengths of the sides of a triangle. Check if it's possible to create a triangle from those lengths and if so, calculate the area of the triangle. 

To calculate squre root use:
```
import math

x = math.sqrt(10)
```

### Exercise 1.6 | Tickets

Assumptions:
	- 0-6   - kindergarten - ticket price: 0
	- 7-17  - school       - ticket price: 2.28
	- 18-64 - adult        - ticket price: 3.80
	- +65   - pensioner    - ticket price: 1.90

Write a program that will ask a user for his age and a number of tickets he'd like to buy.

Based on the assumptions above calculate the price he should pay for the tickets.

### Exercise 1.7 | Counting prices

Ask a user for a product he'd like to byt, its quantity and price. Based on that display proper information.

Example:
What would you like to buy? - tomatoes
Provide a price - 5
Provide quantity - 10

For tomatoes, you'd like to buy, you have to pay 50 PLN.

### Exercise 1.8 | Dog age calculator

Let's assume that 1 dog year equals 5 human years.

Ask a user what is the name of his dog and how old is he and calculate dogs age, if he would be a human. 

Example:
Provide name of the dog - Lassie
Provide dogs age - 3

If Lassie was a human, would have 15 years.

### Exercise 1.9 FizzBuzz

Write a Python program which iterates the integers from 1 to 100. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

Example:
fizzbuzz
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
 ..... 
 
41
fizz
43
44
fizzbuzz
46
47
fizz
49
buzz

## 2. Loops and data structures

### Exercise 2.1 | Math quiz 

Write a program that will draw two numbers from the range from 0 do 99. Display those numbers and ask the user what is the
sum of them (do not display the result). Ask user for a correct answer till he provides a correct one. 

### Exercise 2.2 | Christmas tree

Write a program that reads from the user an integer and then displays a Christmas tree with that many levels with provided
number of levels.

For example, for 3 display:

```
    *
  * * *
* * * * *
```

### Exercise 2.3

Write a program that will read numbers from the user, use `STOP` as a command to stop reading numbers.
Then, display the following stats:
- number of provided numbers, how many
- sum, 
- average, 
- minimum
- maximum

In one version use build-in functions in the other not.

### Exercise 2.4 | Guess a number

Write a program that will draw a number from a range from 0 to 999. The users task is to guess that number.
When the user provides wrong number, give him a hint, whether the number he is looking for is bigger or smaller from the one he gave.