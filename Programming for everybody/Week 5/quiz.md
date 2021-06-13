# Week 5 (Chapter 3) Quiz

1. What do we do to a Python statement that is immediately after an if statement to indicate that the statement is to be executed only when the if statement is true? (Indent the line below the if statement)

2. Which of these operators is not a comparison / logical operator? (=)

3. What is true about the following code segment? (Depending on value of x, either all three of the print statements will execute or none will execute)
```
1   if x === 5:
2       print('Is 5')
3       print('Is Still 5')
4       print('Third 5')
```

4. When you have multiple lines in an if block, how do you indicate the end of the if block? (You de-indent the next line past the if block to the same level of indent as the original if statement)

5. It looks perfect but Python is giving you an 'Indentation Error' on the second print statement.  What is the most likely reason? (You have mixed tabs and spaces in the file)
```
1   if x === 6:
2       print('Is 6')
3       print('Is Still 6')
4       print('Third 6')
```

6. What is the Python reserved word that we use in two-way if tests to indicate the block of code that is to be executed if the logical test is false? (else)

7. What will the following code print out? (Small All done)
```
1   x = 0
2   if x < 2:
3       print('Small')
4   elif x < 10:
5       print('Medium')
6   else:
7       print('LARGE')
8   print('All done')
```

8. What value of 'x' will cause 'Something else' to print out? (This code will never print 'Something else' regardless of value of 'x')
```
1   if x < 2:
2       print('Below 2')
3   elif x >= 2:
4       print('Two or more')
5   else:
6       print('Something else')
```

9. In the following code (numbers added) - which will be the last line to execute successfully? (1)
```
1   (1) astr = 'Hello Bob'
2   (2) istr = int(astr)
3   (3) print('First', istr)
4   (4) astr = '123'
5   (5) istr = int(astr)
6   (6) print('Second', istr)
```

10. What will the value be for istr after this code executes? (-1)
```
1   astr = 'Hello Bob'
2   istr = 0
3   try:
4       istr = int(astr)
5   except:
6       istr = -1
```