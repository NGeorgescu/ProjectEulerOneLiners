# Project Euler One-Liners

## What is this?

This is an attempt to solve as many problems as possible on [Project Euler](https://www.projecteuler.net) using a single line of python

## Why?

Why not?  Who doesn't like a block of code that reads:

    np.max([np.max([[np.prod(r[j:j+4]) for j in range(len(r)-3)] for r in s]) 
     for s in [[np.array(n), np.array(n).T]+ [np.array([(l + [0*k for k in l])[m:]+
     (l + [0*k for k in l])[:m] for m,l in enumerate(o)]).T for o in [n,[[i for 
     i in j[::-1]] for j in np.array(n).T]]] for n in [[[int(j) for j in re.findall(
     r'\d+',i)] for i in re.findall('.+',h)]]][0]])

which incidentally is the solution for Problem 11 (where h is the text copied from the page).  In all seriousness, one-liner comprehensions
in python are very useful because it lets you condense this:

    l = []
    for i in range(10):
        l.append(i**2)
    print(l)

into this:

    print([i**2 for i in range(10)])

which I would argue is more readable.  Obviously if you force an entire program into one line, you start to get closer and closer to that
pinnacle of modern programming: the write-only language.

## The rules

I didn't include environment-setting lines as part of the constraint (so like imports or setting the precision used in an arbitrary package).
Also, anything that takes longer than like a minute to run has a tqdm statement associated with it.

## What are some one-linerizing tricks I can use?

### Managing Embeddings

So the first trick is managing your embeddings.  The following two lines of code return the same thing:

    list(it.chain.from_iterable([[a*b for a in range(10)] for b in range(20)]))
    [a*b for b in range(20) for a in range(10)]

(Note the position of a and b).  So there are a few useful tricks there. 

### Setting local variables

The second is to do an iteration with a single item when you need to use that item more than once.  Consider joining a list to its own divisor:

    i = [1,2,3]
    i+[j//2 for j in i]

This can be turned into:

    [i+[j//2 for j in i] for i in [[1,2,3]]][0]

In the latter case, you get exactly one iteration, i = [1,2,3], and run a list comprehension, and then out of that comprehension you get a one-item
list, which you then return the zeroth index of.  So it's almost like setting a variable i.

### iterable modifiers

The other thing you can do is wrap iterables in modifiers.  The first is zip, e.g.:

    [f(a,b) for a,b in zip(list_a,list_b)]

which returns [f(a_0,b_0), f(a_1,b_1), etc. ...].  The second is enumerate, which adds an index to your iterable:

    [f(n,a) for n,a in enumerate(list_a)]

returns [f(0,a_0), f(1,a_1), etc. ...]. 

### knowing your sympy and numpy functions

a lot of the one-linerizing wouldn't be possible if not for functions like sp.primefactors() or np.sum().  Running through these is enormously useful
because it's hard to google for them, you get a lot of people just reimplementing there own LCM algorithm if you search 'python least common multiple'.





