The task is to write a web service with endpoints defined below and corresponding test pack (preferably in pytest).

Part 1. Sequence
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Assume that all starting numbers eventually finish at 1.
The endpoints:
1)     \sequence\elem\{n}
a.       Returns the value of the sequence for “n”

2)     \sequence\longest\{n}
a.     Returns the value smaller than n, that has the longest chain.

Part 2. Iris & pandas
On service start get iris data set from https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv.

1)     \iris\group\sepal_length\{max}
a.     Returns the number of each species with the maximum sepal_length of {max}

2)     \iris\describe	
a.     Returns the basic statistics about the columns in data set, like min, max, count, mean etc.