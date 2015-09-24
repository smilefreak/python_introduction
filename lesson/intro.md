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

I have listed two that I have frequently used to create programs using the commonbioinfomatics data formats variant call files (VCFs) and BAM (binary alignment).

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
    no_tumours = 20
    avg_bmi = 20.0
    print(gene, no_tumours, avg_bmi)
```

You can reassign these variables at wil within your code, even changing the datatype if you want.

```py
    gene = "TP53"
    print(gene)
    gene = 10 
    print(gene)
```

Thes things are not just storage items but can be manipuled also.
 
