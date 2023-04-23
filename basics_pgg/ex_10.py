"""
Write a program displaying the minimum and maximum number of all numbers entered by the user.
Give the user the ability to finish entering numbers with
the appropriate command (STOP for example).
Make sure the case where the user does not enter any number works properly.

How we can do that?
- let's define two variables where we can store minimum and maximum values from the
  provided numbers
- at the beginning we will assign None to those variables
- we will use infinite WHILE loop for getting data from the user.
    - IF user provides "STOP" value, then we will stop the loop
- convert user input to a number
- check the existing value of minimum/maximum variable - if None, assign a value
  from the user
- check the if the provided number is greater than maximum or lower than minimum
  and then properly assign new value

Sample program output:
Provide a number or STOP: 10
Provide a number or STOP: 15
Provide a number or STOP: 3
Provide a number or STOP: 20
Provide a number or STOP: STOP
Provided minimum = 3, maximum = 20
"""
