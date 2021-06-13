# Week 7 (Chapter 5) Quiz

1. What is wrong with this Python loop? (This loop will run forever)
```
1   n = 5
2   while n > 0:
3       print(n)
4   print('All done')
```

2. What does the break statement do? (Exits the currently executing loop)

3. What does the continue statement do? (Jumps to the "top" of the loop and starts next iteration)

4. What does the following Python program print out? (5)
```
1   tot = 0
2   for i in [5, 4, 3, 2, 1]:
3       tot = tot + 1
4   print(tot)
```

5. What is the iteration variable in the following Python code? (friend)
```
1   friends = ['Joseph', 'Glenn', 'Sally']
2   for friend in friends:
3       print('Happy New Year:', friend)
4   print('Done!')
```

6. What is a good description of the following bit of Python code? (Sum all elements of list)
```
1   zork = 0
2   for thing in [9, 41, 12, 3, 74, 15]:
3       zork = zork + thing
4   print('After', zork)
```

7. What will the following code print out? (-1)
```
1   smallest_so_far = -1
2   for the_num in [9, 41, 12, 3, 74, 15]:
3       if the_num < smallest_so_far:
4           smallest_so_far = the_num
5   print(smallest_so_far)
```

8. What is a good statement to describe the is operator as used in the following if statement? (matches both type and value)
```
1   if smallest is None:
2       smallest = value
```

9. Which reserved word indicates the start of an "indefinite" loop in Python? (while)

10. How many times will the body of the following loop be executed? (0)
```
1   n = 0
2   while n > 0:
3       print('Lather')
4       print('Rinse')
5   print('Dry off!')
```