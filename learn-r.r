## Learning R 

# This script will serve as a notepad for all that is to learn for R programming 
# from the online Coursera module: R Programming by Johns Hopkins University 

x <- 5 # assign value to vector 
as.numeric(x)     # 'as' command changes the class of the input to a given one e.g. integer, logial, character, complex etc. 

list <- c(a, "a", TRUE, 1+0i)     # as opposed to vectors, lists can have elements of different classes 

m <- matrix(nrow = a, ncol = b)     # a, b are integers 
dim(m)
[1] a b 

m <- 1:10
dim(m) <- c(2,5) # change m from vector to matrix of 2x5 dimension 

x <- 1:3
y <- 10:12
m <- rbind(x,y)    # constructs a 2x3 matrix by putting the vectors side-by-side as rows 
m <- cbind(x,y)    # constructs a 3x2 matrix by putting the vectors side-by-side as columns 

# Factors - can be thought of as vectors where each integer has a label
x <- factor(c("yes","no","yes","yes","yes"))
x <- factor(c("yes","no","yes","yes","yes"), levels = c("yes","no"))   # sometimes might be better to put 'level'
# unclass(x) will strip the vector down to numerics 

i.na(x) OR is.nan(x)    # checks whether NA or NaN entries are present in the vector 

# dataframes are like matrices of lists i.e. can have different class data 
# typically created from read.csv() OR read.table()
x <- data.frame(foo = 1:4, bar = c(T,T,F,T))     # first column 'foo' will contain 1:4 and 2nd column, the logical values

# names attribute 
> x <- 1:3
> names(x)
NULL
> names(x) <- c("a","b","c")
> x
a b c 
1 2 3 

x <- list(a=1, b=2, c=2)    # using names in list 
> x
$a
[1] 1
$b
[1] 2
$c
[1] 2

> m <- matrix(1:4,nrow = 2, ncol = 2)     # label the matrix rows and columns 
> dimnames(m) <- list(c("a","b"),c("c","d"))
> m
  c d
a 1 3
b 2 4

# reading data
read.csv() OR read.table()     # imports data as data.frame
source()     # important for importing codes containing your written functions 

> x <- list(foo=1:4, bar=0.6, baz="hello")
> x$foo         # to summon one label at a time 
[1] 1 2 3 4
> x[c(1,3)]     # to summon different labels from a list 
$foo
[1] 1 2 3 4
$baz
[1] "hello"

