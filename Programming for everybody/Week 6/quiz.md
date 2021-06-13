# Week 6 (Chapter 4) Quiz

1. Which Python keyword indicates the start of a function definition? (def)

2. In Python, how do you indicate the end of the block of code that makes up the function? (You de-indent a line of code to the same indent level as the def keyword)

3. In Python what is the input() feature best described as? (A built-in function)

4. What does the following code print out? (There)
```
1   def thing():
2       print('Hello')
3   
4   print('There')
```

5. In the following Python code, which of the following is an "argument" to a function? (x)

6. What will the following Python code print out? (10 20)
```
1   def func(x):
2       print(x)
3   
4   func(10)
5   func(20)
```

7. Which line of the following Python program will never execute? (print('World'))
```
1   def stuff():
2       print ('Hello')
3       return
4       print('World')
5   
6   stuff()
```

8. What will the following Python program print out? (Bonjour Michael)
```
1   def greet(lang):
2       if lang == 'es':
3           return 'Hola'
4       elif lang == 'fr':
5           return 'Bonjour'
6       else:
7           return 'Hello'
8   
9   print(greet('fr'),'Michael')
```

9. What does the following Python code print out? (2)
```
1   def addtwo(a, b):
2       added = a + b
3       return a
4   
5   x = addtwo(2, 7)
6   print(x)
```

10. What is the most important benefit of writing your own functions? (Avoiding writing the same non-trival code more than once in your program)