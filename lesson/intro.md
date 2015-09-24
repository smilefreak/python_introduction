# Introduction to Python and programming.

Python is primarily a programming language, not a statistical package with some programming
tacked on. Like R.

It is old, concieved in the late 1980s and implemented in 1989, thats 26 years ago. 

Currently still has 2 major version python2 and python3. The transition has been slow. 
This is because some changes to the code would have meant important 3rd party libriaries would have needed a rewrite,

It has some core pholosophies.

- Beautful is better than ugly
- Explicit is better than implicit
- Simple is better than complext
- Complex is better than comppilacted
- Readability counts


Python is a programming language that I think is useful, however, it presents
an oppourtunity to teach some core programming concepts.

In this lesson I will cover briefly, with exercises, 3 core programming concepts.

- variables
- loops
- data structures
- functions 

And finally showing will work through some boiler plate code for creating Python command-line programs 

## Why python for me? 

DNA is essentially a string of letters, SNPs are changes in letters. 
All the sequence data farmots I work with are mostly full of strings and numbers.

Python has lot's of small prgramming libraries for everything. People will
say yea but R has lot's of packages as well. These libraries differ in that 
they are designed for creating programs to interface with commonly known datasets.

I have listed two that I have frequently used to create programs the need to interface with the common sequencing formats variant call files (VCFs) and BAM (binary alignment).

- pysam https://pysam.readthedocs.org/en/latest/
- pyvcf https://pyvcf.readthedocs.org/en/latest/


One can also do tasks commonly done in R with python using packages such as pandas (for DFs), with numpy and other packages from scipy (for math and stats), matplotlib and seaborn for plotting.

- pandas http://pandas.pydata.org/
- scipy http://www.scipy.org/
- matplotlib http://matplotlib.org/
- seaborn http://stanford.edu/~mwaskom/software/seaborn/

## Variables.

The most basic thing you can do in any programming language is store information in variables. 

These can take the form of the major datatypes in Python.

These are strings, integers, and decimals.

In other programming languages you sometimes need to declare the
datatype before assigning to the varibale, not in python, this is
known as dynamic typing. Why would you want to type the type in advance?
It is faster because the computer knows before runnning the program what kind of
things can exist. More *hardcore* languages, such as JAVA and C#, require you to specific the types. And even more *hardcore* languases, like C, require you to actually manage the memory your program uses. More flexibility = faster code, but also requires a significant amount more time to program and debug.


```py
    gene = "ABCG2"
    odds_ratio = 20
    avg_bmi = 20.0
    print(gene, odds_ratio,  avg_bmi)
```

You can reassign these variables at wil within your code, even changing the datatype if you want. Can assign them to other variables also.

```py
    gene = "TP53"
    print(gene)
    gene = 10 
    print(gene)
    gene = avg_bmi
    print(avg_bmi, gene)
```

Thes variables are not just storage items but can be manipuled also using commonly known arithmetic operations, such as multiplication plus etc.


```py
    n = 100
    print("samples size times 100", n * 100)
    print("sample size dividied by 10", n/10)
    name = "James"
    print(name/10)
    print(name*10)
```

Stings are essentially list of characters and have a few more
default functions associated with them.

Slicing, which is analagous to subsetting a df or vector, is probably one of the most usefuls bits of syntax in python.


```py
    file1_id = "NZGL_54000"
    print("ID ", file1_id[0:3])
    print("ID ", file1_id[:3])
    print("ID ", file1_id[5:9])
    print("ID ", file1_id[:9])

``` 

# String functions 

Python has various inbuilt functions for operating on strings specifically. 

What is a function? In simplest terms a function is a thing that takes inputs
and gives output. Sometimes that output may be a number, sometimes it may print something, sometimes it may change the value of a variable?. Basically takes something and does something to it, and may output something. That's about as vague as it get's.

You can also write your own functions, but we will briefly look now some string functions. 


You can split strings
```py
    car = "Red blue car"
    print(car.split())
```
You can reverse strings.
```py
    print(car.reverse())
```
Turn things to uppercase

```py
    print(car.upper())
``` 

# Basic data structures

Python has a few very basic data structures Lists, Tuples, and Dictionaries.

Lists are usually used to store lists of similar things - numbers, strings etc.

Create a empty list
```py
    l = []
    print l
```

Add a number to the list.

```py
    l.append(0)
    print l
```

Can also store strings, pull out specific items, and slice.

```py
    l = ['one','ten','twelve','ninenty']
    print(l[0])
    print(l[:1])
    print(l[2:]) 
```

Can add a list to another list 

```py
    l.extend(['ten thousand', 'fiev])
    print(l)
```

# Loops

If you want to do the same thing many times only changing a few things, loops
are your friend. Almost every programming language provides a loop of some kind. 
in python it is very easy to loop across a list.


```py
    l = [1,2,3,4]
    for item in l:
        print(l)
```

Same syntax applies to any iterable (files, lists, dictionaries etc)

Sometimes you may want to get the index at every iteraction easily.

Bad way.

```py
    i = 0 
    for item it l:
        print(l[i])
        i += 1
```

Pythonic good way.

```py
    i = 0
    for i, item in enumerate(l):
        print(l[i])
        print(item) 
        print(i)
```

# Conditionals.

You can also evaluate logical statements using the if statement.

# Functions 

You can also create your own functions.

This example function will take a number add 10 to it and return 
the result.

```py
    def add_ten(x):
        return(x+10)

```

# Conditionals 
    
# File input and output

One way to ope na file in python is save the filename as string, then use
the open function to read the file, and a loop to process each line. 

Reading from a file.

```py
    file_name = "files.txt"
    with open(file_name) as f:
        for line in f:
            print line
```

Writing to a file.

```py
    output_name = "output.txt"
    with open(output_name) as f:
        f.write("test\n")         
```

# Command-line arguments.

BASH scripts are nasty, and for many purposes that don't need to perform analysis
but rather just convert columns or derive new columns etc.

In contrast, python scripts are clean, and testable.

# Future sessions?

    - Writing packages
    - Test driven development
    - Object orientated programming
    - Web-programming in python
    - More focused sessions on some of the topics, such as functions and conditionals.
