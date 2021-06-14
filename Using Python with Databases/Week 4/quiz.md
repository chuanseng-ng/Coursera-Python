# Week 4 Quiz

1. How do we model a many-to-many relationship between two database tables? (We add a table with two foreign keys)

2. In Python, what is a database "cursor" most like? (A file handle)

3. What method do you call  in an SQLIte cursor object in Python to run an SQL command? (execute())

4. In the following SQL, what is the purpose of the "?"? (It is a placeholder for the contents of the "org" variable)
```
1   cur.execute('SELECT count FROM Counts WHERE org = ?', (org, ))
```

5. In the following Python code sequence (assuming cur is a SQLite cursor object),  what is the value in row if no rows match the WHERE clause? (None)
```
1   cur.execute('SELECT count FROM Counts WHERE org = ?', (org, ))
2   row = cur.fetchone()
```

6. What does the LIMIT clause in the following SQL accomplish? (It only retrieves the first 10 rows from the table)
```
1   SELECT org, count FROM Counts
2       ORDER BY count DESC LIMIT 10
```

7. What does the executescript() method in the Python SQLite cursor object do that the normal execute() method does not do? (It allows multipled SQL statements separated by semicolons)

8. What is the purpose of "OR IGNORE" in the following SQL? (It makes sure that if a particular title is already in the table, there are no duplicate rows inserted)
```
1   INSERT OR IGNORE INTO Course (title) VALUES (?)
```

9. What do we generally avoid in a many-to-many junction table? (An AUTOINCREMENT primary key column, A logical key)