## 3. Functions

When writing functions for the following exercises remember to add `type-hinting` and `docstring` and creating proper tests to make sure that the function is working properly.

### Exercise 3.1 Numerical functions

Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.
Crete the following functions. Each should take an numerical argument and return a value.

1. `feets_to_meters` - converts the length in feets to meters,
2. `maximum` - returns a bigger number, try not to use `max` built-in function,
3. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)
podpowiedź: wartość PI jest dostępna jako `Math.PI`
4. `bmi` - calculates BMI for height in meters and weight
5. `traingle_area` - calculates the triangle area, use Heron formula
6. `kilometers_to_miles` - converts kilometers to miles
7. `miles_to_kilometers` - converts miles to kilometers

### Exercise 3.2 | Months

Create a function that accepts the name of the month, optional year and returns the number of days for that month.

### Exercise 3.3 | Operations on lists

In addition to writing functions, write tests as well.

```
numbers = [10, 20, 30, 40]
result = average(numbers)
```

- `average(numbers)` - returns the average for the numbers in the list
- `maximum(numbers)` – returns maximum number from the list, don't user built-in `max` function
- `diff_min_max(numbers)` – returns the difference between max and min number in the list. 
- `print_greater_than(numbers, x)` – prints (on the console) numbers greater than x from the list
- `first_bigger_then(numbers, x)` – returns first number bigger than x; None otherwise
- `sum_greater_than(numbers, x)` – returns a sum of numbers from the list greater than x
- `how_many_greater_than(numbers, x)` – returns how many numbers in the list are greater than x