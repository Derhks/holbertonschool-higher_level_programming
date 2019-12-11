# Python - Hello, World

- Who created Python?
- Who is Guido van Rossum?
- Where does the name ‘Python’ come from?
- What is the Zen of Python?
- How to use the Python interpreter?
- How to print text and variables using `print`?
- How to use strings?
- What are indexing and slicing in Python?
- What is the official Holberton Python coding style and how to check your code with `PEP 8`?



![img](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263.jpg)



## Who created Python?

Python was born out of the need to have a programming language that was extensible, so at Christmas 1989 it began its development until 1991 when the first version created by Guido van Rossum was released.



## Who is Guido van Rossum?

Guido van Rossum is a Dutch programmer and is best known as the creator of the Python programming language. In the Netherlands he obtained a master's degree in mathematics and computer science from the University of Amsterdam in 1982. During his career as a programmer he worked at Google and currently works for Dropbox.



## Where does the name ‘Python’ come from?

Python's name comes from the comedy show "Monty Python's Flying Circus" on the BBC television network, which was a show from the 1970s.



## What is the Zen of Python?

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```



## How to use the Python interpreter?

The Python interpreter can be used in the following ways:

To invoke the interpreter we execute at the command line

```
vagrant@vagrant-ubuntu-trusty-64:~$ python3
Python 3.4.3 (default, Nov 12 2018, 22:25:49)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
When we press Ctrl + D on Unix we leave the Python interpreter.

```
vagrant@vagrant-ubuntu-trusty-64:~$ python3
Python 3.4.3 (default, Nov 12 2018, 22:25:49)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>>vagrant@vagrant-ubuntu-trusty-64:~$
```

But if this method does not work we can exit the interpreter by executing the command quit()

```
vagrant@vagrant-ubuntu-trusty-64:~$ python3
Python 3.4.3 (default, Nov 12 2018, 22:25:49)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
>>> vagrant@vagrant-ubuntu-trusty-64:~$
```

We can also execute commands directly in interactive mode

```
>>> for cnt in range(97, 123): print("{:s} ".format(chr(cnt)), end='')
>>> ...
```

When the three consecutive points appear we must press enter again

```
>>> for cnt in range(97, 123): print("{:s} ".format(chr(cnt)), end='')
>>> ...
>>> a b c d e f g h i j k l m n o p q r s t u v w x y z >>>
```



## How to print text and variables using `print`?

To print text we can do it in the following ways:

To print a variable

```
vagrant@vagrant-ubuntu-trusty-64:~$ python3
Python 3.4.3 (default, Nov 12 2018, 22:25:49)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> str1 = "Holberton School Bogota"
>>> print("{:s}".format(str1), end='')
Holberton School Bogota>>>
```

```
vagrant@vagrant-ubuntu-trusty-64:~$ python3
Python 3.4.3 (default, Nov 12 2018, 22:25:49)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> dgt = 209481
>>> print("{:d} ".format(dgt), end='')
209481 >>>
```


To print text

```
vagrant@vagrant-ubuntu-trusty-64:~$ python3
Python 3.4.3 (default, Nov 12 2018, 22:25:49)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Holberton School Bogota")
Holberton School Bogota
>>>
```

```
vagrant@vagrant-ubuntu-trusty-64:~$ python3
Python 3.4.3 (default, Nov 12 2018, 22:25:49)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("209481")
209481
>>>
```



## How to use strings?

**The strings can be used in the following way:**

````
>>> print('spam eggs') # single quotes
>>> spam eggs
>>>
````

````
>>> print('doesn\'t') # use \' to escape the single
doesn't
>>>
````

````
>>> print("doesn't") # or use double quotes instead
doesn't
>>>
````

````
>>> print('C:\some\name') # here \n means newline!
C:\some
ame
>>>
````

````
>>> print(r'C:\some\name') # note the r before the quote
C:\some\name
>>>
````

**Concatenate strings:**

````
>>> str1 = "Holberton"
>>> str2 = "School"
>>> str3 = "Bogota"
>>> str4 = str1 + ' ' + str2 + ' ' + str3
>>> print("{:s}".format(str4), end='')
Holberton School Bogota>>>
````

**Repeat string:**

````
>>> str1 = "Holberton"
>>> print("{:s} ".format(3 * str1), end='')
HolbertonHolbertonHolberton >>>
````



## What are indexing and slicing in Python?

**Indexing:** 

This method allows us to extract a single character from a string indicating the index of the desired character surrounded by square brackets "[]".

````
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'
````

Negative Numbers: These always start from -1

````
>>> word[-1]  # last character
'n'
>>> word[-2]  # second-last character
'o'
>>> word[-6]
'P'
````

**Slicing:**

This method allows us to extract a character string, that is, a slice of the string, indicating the index from which the first cut will be made to the string, followed by two points, and the index in which the second cut will be made to the string, thus generating a string of the string.

````
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'

>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'

>>> word[:2]  # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:]  # characters from position 4 (included) to the end
'on'
>>> word[-2:] # characters from the second-last (included) to the end
'on'
````



## What is the official Holberton Python coding style and how to check your code with `PEP 8`?

The official Holberton Python coding style is `pep8`, been the currently Python coding style `pycodestyle`, but pycodestyle is based on `pep8`.

**Examples:**

This is an example in which we did not find any error in the Python coding style

````
vagrant@vagrant-ubuntu-trusty-64:~/python/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ pep8 0-positive_or_negative.py
/usr/local/lib/python3.4/dist-packages/pep8.py:2124: UserWarning:

pep8 has been renamed to pycodestyle (GitHub issue #466)
Use of the pep8 tool will be removed in a future release.
Please install and use `pycodestyle` instead.

$ pip install pycodestyle
$ pycodestyle ...

  '\n\n'
````

This is an example in which we find errors in the Python coding style

````
vagrant@vagrant-ubuntu-trusty-64:~/python/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ pep8 12-fizzbuzz.py
/usr/local/lib/python3.4/dist-packages/pep8.py:2124: UserWarning:

pep8 has been renamed to pycodestyle (GitHub issue #466)
Use of the pep8 tool will be removed in a future release.
Please install and use `pycodestyle` instead.

$ pip install pycodestyle
$ pycodestyle ...

  '\n\n'
12-fizzbuzz.py:7:5: E112 expected an indented block
12-fizzbuzz.py:9:9: E901 IndentationError: unindent does not match any outer indentation level
````

## Authors

* **Julián Sandoval** [<img src="https://i.blogs.es/3c991e/twitter-bird/450_1000.png" alt="Resultado de imagen para logo twitter" width="40px"/>](https://twitter.com/Derhks)



## Acknowledgments

I thank the following pages for the information I have extracted from them to make this README.md.

- https://en.wikipedia.org/wiki/Guido_van_Rossum
- https://docs.python.org/2/faq/general.html
- https://docs.python.org/3/tutorial/interpreter.html
- https://www.stat.berkeley.edu/~spector/extension/python/notes/node19.html

