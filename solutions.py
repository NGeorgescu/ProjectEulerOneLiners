from datetime import datetime
import numpy as np
import itertools as it
import re
import collatz
import sympy as sp
from tqdm import tqdm
from scipy import stats
from fractions import Fraction
from string import ascii_uppercase
from decimal import Decimal, getcontext, ROUND_DOWN
from inflect import engine
from treys import Card, Evaluator
import extended as xt
evaluator = Evaluator()
getcontext().prec, getcontext().rounding  = 2000, ROUND_DOWN


#%% Problem 1
#this returns the sum of the list from 0 to 999, divisible by either 3 or 5
np.sum([i for i in range(1000) if i%3==0 or i%5==0])

#%% Problem 2
#the inner brackets do the fibonacci sequence, which is filtered by the outer 
#brackets.  We then find the sum of the filtered list
int(np.sum([j for j in [sp.fibonacci(i) for i in range(1000)] if j<4*10**6 and j%2==0]))

#%% Problem 3
#simple sympy number theory
max(sp.primefactors(600851475143))

#%% Problem 4
#the inner bracket generates the products and the outer checks if the string of 
#that number is equal to its reverse
max([k for k in [i*j for i in range(1,1000) for j in range(1,1000)] \
     if str(k)==str(k)[::-1]])

#%% Problem 5
#numpy has this built in
np.lcm.reduce(range(1,20))

#%% Problem 6
#I used a one-item comprehension to avoid punching in 100 twice.
[np.sum(np.arange(n+1))**2 - np.sum(np.arange(n+1)**2) for n in [100]][0]

#%% Problem 7
#Built-in sympy
sp.prime(10001)

#%% Problem 8
n = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""
#this first converts the problem into a table, j, and then iterates a rolling 
#window through the lines
[np.max(np.prod([j[i:i+13] for i in np.arange(len(j)-12)],axis=1)) for j in 
 [[int(j) for j in re.findall(r'\d',n)]]][0]

#%% Problem 9
# we first find the pythagorian triples, the scecond filters the list
[a*b*c for a,b,c in [[a,b,int(np.sqrt(a**2+b**2))] for a,b in list(it.product(\
   np.arange(1,int(1000)),repeat=2)) if np.sqrt(a**2+b**2)%1==0 and a<b] if \
   a+b+c==1000][0]

#%% Problem 10
#built in 
np.sum(list(sp.primerange(1,2*10**6)))

#%% Problem 11
h="""08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""
#This function first defines n, which is the numerical representation of the table copied as a string
#It then makes four representations of the table,s, the first is the identity, the second is transposed,
#and the last two are zero-padded skews of the table. Each of these four representations is constructed
#such that adjacent horizontal values in the new space represent each of the four directions:
#horizontal, vertical, diagonal up, diagonal down.  Then you loop through each line of each
#representation and find the max of all of these using a four-item window
np.max([np.max([[np.prod(r[j:j+4]) for j in range(len(r)-3)] for r in s]) for \
 s in [[np.array(n), np.array(n).T]+ [np.array([(l + [0*k for k in l])[m:]+ \
 (l + [0*k for k in l])[:m] for m,l in enumerate(o)]).T for o in [n,[[i for i \
 in j[::-1]] for j in np.array(n).T]]] for n in [[[int(j) for j in re.findall(r'\d+',\
 i)] for i in re.findall('.+',h)]]][0]])

#%% Problem 12
# this inner sequence creates b, a list of triangle number,
[c for c,d in [[b,len(sp.divisors(b))] for b in [int(np.sum(np.arange(a+1))) \
 for a in range(1,13000)]]  if d>500][0]

#%% Problem 13
n="""37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690"""
#add them up, convert to string, and get the first 10 items
int(str(np.sum([int(i) for i in re.findall(r'\d+',n)]))[:10])

#%% Problem 14
#I built a library just to one-linerize this problem
np.argmax([collatz.reduce(i,out='dist') for i in range(10**6)])
    
#%% Problem 15
#this is combinatorially huge, so using itertools is out of the question.  
#It's a factorial problem.
[int(sp.factorial(2*n))//int(sp.factorial(n))**2 for n in [20]][0]

#%% Problem 16
# easy
np.sum([int(i) for i in str(2**1000)])

#%% Problem 17
#the inflect engine generates the text.  We just need to count it all up.
len(list(it.chain.from_iterable([re.findall('\w',engine().number_to_words(i)) \
 for i in range(1,1001)])))

#%% Problem 18
t = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
#this uses exactly the combinatorial strategy described in the problem. It generates
#a list of steps to take and then takes them through the entire pyramid, and returns 
#the max
max(np.sum([[[k[n][o] for n,o in enumerate(np.cumsum(m))] for m in list([l for \
 l in it.product([0,1],repeat=len(k)) if l[0]==0])] for k in [[[int(j) for j in \
 re.findall(r'\d+',i)] for i in t.split('\n')]]][0],axis=1))

#%% Problem 19
#find when weekday was equal to 6 (monday is zero-indexed) and return the number 
#of items
len([k for k in [datetime(i, j, 1, 0,0,0,0).weekday() for i in range(1901,2001) \
 for j in range(1,13)] if k==6])

#%% Problem 20
#just uses the built-in factorial method and then gets the digits and adds them up
np.sum([int(j) for j in str(int(sp.factorial(100)))])

#%% Problem 21
# this one finds the list of proper divisors, and then finds where following that 
# index twice gets you back to the same spot without just staying where you are 
# (i.e. perfect numbers) 
[np.sum(np.unique([k for k in j[:10000] if j[j[k]]==k and j[k]!=k])) for j in \
 [[int(np.sum(sp.divisors(i)[:-1])) for i in range(100000)]]][0]

#%% Problem 22
# first create a dictionary of values (there's probably a library for that but I didn't feel
# like searching for it). then it just loops through the names, getting the index i, and value, n,
# and adds up those numbers' products
np.sum([[(n+1)*np.sum([d[j] for j in i]) for n,i in enumerate(sorted(re.findall(\
 r'\w+',open('names.txt').read())))] for d in [{k:v for k,v in \
 zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),np.arange(26)+1)}]][0])

#%% Problem 23
# This one takes like an hour or two to run.  it generates a list of abundant numbers, d,
# and then looks through each number up to 28123 to see if two abundant numbers can add up
# to it
np.sum([[i for i in tqdm(range(28123)) if all([i-k not in d for k in d])] for d \
 in [[j for j in range(28123) if np.sum(sp.divisors(j)[:-1])>j]]][0])

#%% Problem 24
# This works
int(''.join([str(i) for i in list(it.permutations(range(10)))[999999]]))

#%% Problem 25
# This works
min(np.where(np.array([len(str(sp.fibonacci(i))) for i in range(10000)])>=1000)[0])

#%% Problem 26
# you need 2000 decimals of precision.  This block o' text takes each number,
# returns the number and the inverse decimal as i and k respectively, only if k
# is non-terminating.  It then uses the decimal library and checks from the back
# of the string, trying to match the longest repeat sequence.  It then returns 
# the shortest match.  it then sorts the list by the matches and returns the original number
sorted([[i,1+min(np.where([all([k[-1-l]==k[-1-l-m] for l in range(m)]) for m in \
 range(1,getcontext().prec//2)])[0])] for i,k in [[j,str(Decimal(1) / Decimal(j))] \
 for j in range(1,1000)] if len(k)>getcontext().prec//2],key = lambda x:x[1])[-1][0]

#%% Problem 27
# this one takes like an hour to run. it generates a list functions, and then for each of
# these functions it returns the position of the first composite number.  Then it sorts
# the list and returns the product of the values that generated the function with the highest
# index of the first composite number
np.product(sorted([[a,b,min(np.where([not sp.isprime(i**2+a*i+b) for i in \
 range(100)])[0])] for a in tqdm(range(-999,1000)) for b in range(-1000,1001)], \
 key=lambda x:x[-1])[-1][:2])

#%% Problem 28
# this uses the mathematical property that the spiral is composed of four numbers, the lowest
# of which follows a quadratic form.  n keeps track of how far out you are, i the lowest of the
# corner values of the spiral, and then you add 1 at the end because the center is done separately
1+np.sum([[i+j*(2*n+2) for j in range(4)] for n,i in enumerate([3]+ \
 list(np.cumsum(np.cumsum([8 for i in range(1001 //2-1)])+2)+3))])

#%% Problem 29
#simple
len(np.unique([a**b for a in range(2,101) for b in range(2,101)]))

#%% Problem 30
#you just need to split the number into a string and then raise each digit to 
#the fifth power.  Start at 10 to avoid single-digit non-sums
np.sum([i for i in range(10,1000000) if i==np.sum([int(j)**5 for j in list(str(i))])])

#%% Problem 31
#nested iterators up to making 2 pounds given the previous coins.  It's the only 
#way to avoid making 5*10**8 operations.  If you were doing it multiline, you could 
#use a recursive function.
np.sum([a+b+c+d+e+f+g+h==200 for a in range(0,201,200) for b in range(0,201-a,100) \
 for c in range(0,201-a-b,50) for d in range(0,201-a-b-c,20) for e in \
 range(0,201-a-b-c-d,10) for f in range(0,201-a-b-c-d-e,5) for g in \
 range(0,201-a-b-c-d-e-f,2) for h in range(0,201-a-b-c-d-e-f-g,1)])

#%% Problem 32
#generate the product and answer (l and m) of all possible splits (a and b) of 
#all possible pandigital numbers (i), and return the unique answers
int(np.sum(np.unique([m for l,m in [[int(''.join(i[:a]))*int(''.join(i[a:b])),\
 int(''.join(i[b:]))] for a in range(1,8) for b in range(a+1,9) for i in \
 list(it.permutations([str(k) for k in range(1,10)], 9))] if l==m])))

#%% Problem 33
# a and b are the 'simplified' numerator and denominator, d is the canceled digit, 
#and c is the control that distinguishes between 49/98 94/98 94/89 and 49/89. Given 
#all these possibilities, e,f,g,h is just used to filter the list and then np.product 
#multiplies them together and you extract the denominator.
np.product([Fraction(e,f) for e,f,g,h in [[a*c//100+d*(11-c//100),b*(c%100)+d*(11-c%100) \
 ,a,b] for a in range(1,10) for b in range(1,10) for c in [101,110,1001,1010] \
 for d in range(1,10) if a!=b] if e<f and g<h and Fraction(g,h)==Fraction(e,f)]).denominator

#%% Problem 34
#interestingly enough, the only other example is 40585. 
np.sum([a for a in range(3,100000) if a == np.sum([sp.factorial(int(b)) for b in str(a)])])

#%% Problem 35
#we generate the primes with c, check the rotations with the rotation d, and then 
#flatten with e and g. Then we just need the unique values and the total number of items
len(np.unique([e for g in [[int(''.join(c[d:]+c[:d])) for d in range(len(c))] \
 for c in [[b for b in str(a)] for a in sp.primerange(1,10**6)]] for e in g if \
 all([sp.isprime(f) for f in g])]))

#%% Problem 36
#you generate the binary (b) and decimal (c) for the list of numbers a, and then 
#compare them to their reverses
np.sum([int(c) for b,c in [[bin(a)[2:],str(a)] for a in range(10**6)] if b[::-1]==b and c[::-1]==c])

#%% Problem 37
#a is the list of base primes, which get converted to a string (b), and c controls
#the forward and d controls the back truncation.  If they both pass, b gets turned 
#into an int and summed up
np.sum([int(b) for b in [str(a) for a in sp.primerange(10,10**6)] if all([all( \
 [sp.isprime(int(b[:c+1])) for c in range(len(b))]),all([sp.isprime(int(b[d:])) \
 for d in range(len(b))])])])

#%% Problem 38
# we generate a list of number with unique digits, a, which we then create 
#sequential products with b, and accumulate with c.  This gets thrown into a 
#list d if it hits certain criteria, and then the max is found
max([int(d) for d in [''.join([str(a*b) for b in range(1,6)][:c+1]) for a in \
 range(10**5) if len(list(str(a)))==len(np.unique(list(str(a)))) for c in \
 range(4)] if len(d)==9 and '0' not in list(d) and len(np.unique(list(d)))==9])

#%% Problem 39
#we us a and b to generate the two legs, and calculate the perimeter if it makes
#a right triangle, filter with c, and find the mode
stats.mode([c for c in [int(a+b+np.sqrt(a**2+b**2)) for a in range(1,1000) for \
 b in range(1,a+1) if np.sqrt(a**2+b**2)%1==0] if c<1000]).mode[0]

#%% Problem 40
#join the list of string range, set it to a, and look for the bth item in the list, 
#and multiply them up
np.product([[int(a[10**b-1]) for b in range(7)] for a in [''.join([str(a) for a \
 in range(1,1000000)])]][0])

#%% Problem 41
#first we generate the value of n in a, make the digits with b, and then get 
#the permutations in a flattened list with c and d, which we filter for primes with e
max([e for e in [int(''.join(d)) for c in [list(it.permutations([str(b) for b \
 in range(1,a)])) for a in range(2,10)] for d in c] if sp.isprime(e)])

#%% Problem 42
#we get the words with a, the value of each letter with b, filter with c for the 
#triangle numbers found with d
len([c for c in [np.sum([ascii_uppercase.index(b)+1 for b in a]) for a in \
 re.findall('\w+',open('words.txt').read())] if c in [np.sum(range(d)) for \
 d in range(1,21)]])

#%% Problem 43
#find the permutations of a with b, doing some quick filtering to cut down the 
#possibilities by 10x, then check the modulo of the prime and position with d 
#sums to zero, filtering on c.  then join, int, and sum.
sum([int(''.join(c)) for c in tqdm([b for b in it.permutations([str(a) for a in \
 range(10)]) if b[0]!='0' and b[3] in '02468' and b[5] in '05' ],position=0, \
 leave=True) if np.sum([int(''.join(c[d+1:d+4]))%sp.prime(d+1) for d in [1,3,4,5,6]])==0])

#%% Problem 44
#the trick here is to store the list of pentagonal numbers in b, and then check
#it with the solution to the Pn equation for n. The solution to the Pn equation 
#is found with sp.var('Pn n');print(sp.solve(Pn-n*(3*n-1)/2,n)[1]) and you check 
#if n%1==0 i.e. has no decimal component
min([[c-d for c in tqdm(b,position=0) for d in [e for e in b if e<c] if \
 all([(np.sqrt(24*(c+d*f) + 1)+1)/6%1==0 for f in [-1,1]]) ] for b in \
 [[a*(3*a-1)//2 for a in range(1,2200)]]][0])

#%% Problem 45
# find the solutions to the equations with sp.var('Tn, Hn, n');print(sp.solve(
# Tn-n*(n+1)/2,n)[1]);print(sp.solve(Pn-n*(3*n-1)/2,n)[1]) and filter the hexagonal list
min([c for c in [a*(2*a-1) for a in range(145,100000)] if all([b%1==0 for b in \
 [(np.sqrt(8*c+1)-1)/2,(np.sqrt(24*c+1)+1)/6]])])

#%% Problem 46
#list of non primes using a, and then checking if that number, d, is not in the
#list of all possible prime+ 2*squares
min([d for d in tqdm([a for a in range(3,10000,2) if not sp.isprime(a)],position=0)
 if d not in [c+2*b**2 for b in range(1,int(np.sqrt(d))) for c in sp.primerange(1,d)]])

#%% Problem 47
#first this generates a rolling window list (c) which we find the factors (f,l) 
# along with the first number in the sequence (e,k), and we filter the flattened (h,i) 
# list(j) and check that the number of factors is the same, after we check that 
# they all have four factors (g)
min([k for k,l in [[e,f] for e,f in [[c[0],[list(sp.factorint(d).items()) for d in c]] \
 for c in tqdm([[a+b for a in range(4)] for b in range(2,300000)],position=0,leave=True)]\
 if all([len(g)==len(f) for g in f])] if [len(j) == len(np.unique(j,axis=0)) for j in \
 [[h for i in l for h in i]]][0]])

#%% Problem 48
#python handles longs just fine in comprehensions
int(str(np.sum([a**a for a in range(1,1000)]))[-10:])

#%% Problem 49
#we take the digits (a), get all possible combinations (b), get the permutations of 
#those combinations (c), check if they are prime (d), get the 3-fold combinations of 
#the permutations of the digits (e), flatten the list one level (f,g), and then filter
#for the same differences and not being the first answer (h)
['{:04d}{:04d}{:04d}'.format(*h) for h in [sorted(f) for g in [it.combinations(e,3) \
 for e in [[d for d in [int(''.join(c)) for c in np.unique(list(it.permutations(b)),\
 axis=0)] if sp.isprime(d)] for b in list(it.combinations_with_replacement([str(a) \
 for a in range(1,10)],4))] if len(e)>2] for f in g] if np.ediff1d(np.ediff1d(h))==0 \
 if 1487 not in h][0]

#%% Problem 50
#first we make a list of primes (a), length of rolling window (b) and list of windows (c) 
#then we filter the list to just primes (d,e), and store the result in f so that we can grab
#the maximum length (h) for the list and return the list at that index
[f[np.argmax([h for g,h in f])] for f in [[[d,e] for d,e in [[int(np.sum(a[c:c+b])),b]\
 for a in [list(sp.primerange(1,5000))] for b in range(1,1000) for c in range(len(a)-b)]\
 if d<10**6 and sp.isprime(d)]]][0][0]

#%% Problem 51
#A comprehension doozy! a generates a list of digits, b and c inserts those to find the permutations
#with 'x', d and e flatten the list, f and g control the size (i.e. x3 vs xx3 vs x34, etc.)
#i and j control the substitutions into each item h of that list, creating a list of lists
#stored into k, and then the list is partially filtered with l.  HOWEVER, we first
#have to check that the first digit isn't a zero, i.e. 03, 13, 23 is against the rules because
#'03' is really '3'.  You can't just chop the zero from j though because 56003 is valid for 56xx3.  
#So n checks that all the digits in m have the same length, and o does the final filtering of the 
#lists of len 8. Then you get the smallest item from the list starting with the smallest item.
np.unique([o for o in [[n for n in m if len(str(n))==len(str(m[-1]))] for m in \
 [[l for l in k if len(l)>=8] for k in [[[j for j in [int(re.sub('x',str(i),h)) \
 for i in range(10)] if sp.isprime(j)] for h in [''.join(d) for f in range(1,4) \
 for g in range(1,4) for e in [it.permutations([*b,*['x' for c in range(f)]]) \
 for b in list(it.combinations_with_replacement([str(a) for a in range(10)],g))] \
 for d in e]]]][0]] if len(o)>=8],axis=0)[0,0]

#%% Problem 52
#a gives the numbers we're working with.  Obviously it must have a leading 1. then we use b to
#make a list of the multiples, d checks that they are all the same length (no sense in looking
#at numbers of varying length), e and f then sort those digits, and h stores 1x, where g and i
#check that all the digits are the same
np.unique([h for h,g in [[e[0],[int(''.join(sorted(list(str(f))))) for f in e]] \
 for e in [[d for d in c if len(str(d[0]))==len(str(d[-1]))] for c in [[[b*a for \
 b in range(1,7)] for a in range(10**6) if str(a)[0]=='1']]][0]] if all([i==g[0] \
 for i in g])])[0]

#%% Problem 53
#This one seems self-explanatory.  sum of the true values for the function greater than a million
np.sum(np.array([sp.factorial(a)/sp.factorial(b)/sp.factorial(a-b) for a in range(1,101)\
 for b in range(a+1)])>10**6)

#%% Problem 54
#this uses treys.  I know it technically uses an additional line for evaluator = Evaluate(). 
#You can do it with Evaluator().evaluate(hand) but it just adds computational time. a and b get
#you a list of lists of rounds, d and c split it into two hands, and the evaluator from the treys
#library evaluates the hand.  Note: smaller is better.
np.sum([evaluator.evaluate([],[Card.new(d) for d in c[:5]])<evaluator.evaluate([],
 [Card.new(d) for d in c[5:]]) for c in [[b[0]+b[-1].lower() for b in a.split(' ')] 
 for a in open('poker.txt').read().split('\n')[:-1]]])

#%% Problem 55
#here I use my extended library to nest the palindrome addition to a depth of 50.  
#If it comes back a non-palindrome after up to 50 iterations, 1 is added to the summed list
np.sum([1 for b in [xt.nest_while(lambda x: x+int(str(x)[::-1]),a,lambda x: \
 str(x)!=str(x)[::-1],max_iter=50) for a in range(10000)] if str(b)!=str(b)[::-1]])

#%% Problem 56
#pretty straightforward
np.max([np.sum([int(c) for c in str(a**b)]) for a in range(100) for b in range(100)])

#%% Problem 57
#the nest list prints out 1 more than the sqrt(2), and then it's just a matter of 
#comparing the numerators and denominators
np.sum([len(str((a-1).numerator))>len(str((a-1).denominator)) for a in \
  xt.nest_list(lambda x: Fraction(2 + 1/x), 2, 1000)])

#%% Problem 58
#We find the number of primes in a new layer (b,c), add it to an accumulated total 
#(d), and compare that to the running total of all layers (e), and then look for 
#the minimum index of the resulting array of fractions that's over 0.1.  Then we 
# multiply by 2 and add 3 (because we threw away the middle piece)
min(np.where(np.array([[d/e for d,e in zip(np.cumsum([0]+[np.sum([sp.isprime( \
  4*c**2-2*c+1+2*b*c) for b in range(4)]) for c in range(1,a)]),1+4*np.arange(a))] \
  for a in [14000]][0][1:])<.1)[0])*2+3

#%% Problem 59
#First we map (a) an int to the file to read (b) then we try all the possible keys, 
#and then we look at the XORed result for the word 'the'.  
#The text is about Euler, and the key is 'exp'.
np.sum([d for d in [[np.array(b) ^ np.tile(c,len(b)//3)  for c in list(it.product(97+ \
 np.arange(26), repeat=3))] for b in [[int(a) for a in open('cipher.txt').read().split( \
 ',')]]][0]  if ' the ' in ''.join([chr(e) for e in d])])

#%% Problem 60
#This code is highly golfed because a brute force takes forever! First you get a 
#list of primes, then you keep tacking on 4 times, each successive layer checking 
#that the permutations of the numbers are all prime. Each tqdm represents one layer.
#first you stringify the primes (b) and then the nesting starts. for each combination 
#(d) in the previous layer (c), you add on a prime (e) and check if it works for each 
#permutation (f).  The list (h) is converted (g) and the minimum is found.
min([sum([int(g) for g in h]) for h in xt.nest(lambda c: [[str(e),*d] for d in \
 tqdm(c,position=0,leave=True) for e in sp.primerange(3,int(d[0])) if \
 all([sp.isprime(int(''.join(f))) for f in it.permutations([*d,str(e)],2)])], \
 [[str(b)] for b in sp.primerange(3,10000)], 4)])

#%% Problem 61
#the list (a,c) and angularity (b,d) of the numbers is cataloged (f), and recursively (h)
#added (i,j) the original list (g), at each step checking (l,m) that the angularity is new
#and the list is filtered (k) for the last matching the first, and (o,n)
sum([[int(o) for o,n in k] for k in [xt.nest(lambda h: [[j,*i] for i in h for j in \
 f if j[0][-2:]==i[0][0][:2] and j[1] not in [l for m,l in i]],[[g] for g in f],5) \
 for f in [[[str(c),d] for c,d in [[b*((a-2)*b+(4-a))//2,a] for b in range(1,200) \
 for a in range(3,9)] if len(str(c))==4]]][0] if k[0][0][:2]==k[-1][0][2:]][0])

#%% Problem 62
#we gather by the sorted digits, then we look for the min.
min([min(a) for a in xt.gather_by(np.arange(10000)**3,lambda x: str(sorted(str(x)))) if len(a)==5])

#%% Problem 63
#Since 9**99 is 95 digits long, we can stop at 100**x. then we look for the digits 1-9 powers
#we raise the first number (b) to the power (a) and then for each item in the list check
#that the length of the number (c) is equal to the power (d)
np.sum([1 for c,d in [[b**a,a] for a in range(100) for b in range(1,11)] if len(str(c))==d])

#%% Problem 64
#first we construct a list of decimals (a) and for each of them we take the sqrt,
#and then start nesting comprehensions until we reach a repeat of length 5 (i).
#the repeat is calculated by trying every combination (e) up to the amount allowed
#by the length of the list (d), wherein all of the repeats (f) must match.  Once
#this list terminates, that testing algorithm runs again (g) to return the list of
#repeats that work, the minimum repeat for each is taken, and then they are grouped
#by positive and negative.  This code can be golfed some more by running the test
#within the nest and exiting the nestwhile when this has a len.  This is left
#as an excercise to the reader
len(xt.group_by([[[np.where([all([all([g[-e-(f+1)*d]==g[-f*d -e] for f in \
 range(i)]) for e in range(1,d+1)]) for d in range(1,len(g)//(i+1))])[0][0]+1 \
 for g in [xt.nest_while(lambda b: [1/(b[0]-int(b[0])),[*b[1],int(b[0])]],[np.sqrt( \
 Decimal(a)),[]], lambda c: not(any([all([all([c[1][-e-(f+1)*d]==c[1][-f*d -e] \
 for f in range(i)]) for e in range(1,d+1)]) for d in range(6,len(c[1])//(i+1))] \
 )))[1]]][0] for a in tqdm(range(10000), position=0,leave=True) if a not in \
 np.arange(101)**2] for i in [5]][0],xt.odd_q)[True])

#%% Problem 65
#we first make the list of continued fractions (a), and then use the nest
#to chunk it down until (c) the list is gone. add the 1 for out front,
#get the numerator, and then get the sum of the list of integers in the numerator
sum(map(int,list(str((xt.nest_while(lambda b: [b[0][:-1],Fraction(b[0][-1]+ \
 1/b[1])],[list(it.chain(*[[1,1,2*a+2] for a in range(40)]))[:100],np.inf], \
 lambda c: len(c[0]))[-1]+1).numerator))))

#%% Problem 66
#This method really requirest the shortcut that everyone uses off of wikipedia
#for solving pell's equation. I constructed a nest_while which produces three
#parameters (b) for the number you're working on (a), the remainder, the continued
#fraction, and the evaluation of the convergent of the continued fraction at that 
#level which is itself a recursive nestwhile structure that works from the back
#if the convergent num**2-denom**2 evaluates to 1, then the nest_while terminates and
#we return the numerator of the result (g) along with a. We sort and grab the largest
#so you know what you're working with, 661 -> 16421658242965910275055840472270471049
sorted([[[[a,g[0].numerator] for g in [xt.nest_while(lambda b: [1/(b[0]-int(b[0])), \
 [*b[1],int(b[0])],[[f,f.numerator**2-a*f.denominator**2] for f in [xt.nest_while( \
 lambda d: [d[0][:-1], d[0][-1]+Fraction(1/d[1])],[[*b[1],int(b[0])],np.inf], \
 lambda e:len(e[0])>0 )[1]]][0]],[np.sqrt(Decimal(a)),[]], lambda c: c[-1][-1]!=1 \
 if len(c[-1]) else False)[-1]]][0] for a in range(1000) if a not in np.arange(101)**2] \
 for i in [5]][0],key=xt.last)[-1][0]

#%% Problem 67
#just a nest where the last row is added to the preceding row, maxing it at each level
#for every 2.  
xt.nest(lambda c: c[:-2]+[[max(c[-1][d],c[-1][d+1])+e for d,e in enumerate(c[-2])]],
 [[int(b) for b in a.split(' ')] for a in open('triangle.txt').read().split('\n')[:-1]]
 ,99)[0][0]

#%% Problem 68
#We make sure f< all of ghij and the five spokes and the len(l) checks that it's 16
#     f
#       a  g
#     e   b
#   j  d c h
#       i
max([int(l) for l in [''.join([str(k) for k in [f,a,b,g,b,c,h,c,d,i,d,e,j,e,a]]) \
 for a,b,c,d,e,f,g,h,i,j in list(it.permutations(range(1,11))) if all(f<np.array( \
 [g,h,i,j])) and all(0==np.ediff1d([f+a+b,g+b+c,h+c+d,i+d+e,j+e+a]))] if len(l)==16])

#%% Problem 69
#is sympy cheating at this point?
max(range(1,1+10**6),key=lambda a: a/sp.ntheory.factor_.totient(a))

#%% Problem 70
#a checks if it's a permutation, 
min([a for a in tqdm(range(2,10**7),position=0,leave=True) if sorted(str(a))== \
 sorted(str(sp.ntheory.factor_.totient(a)))], key = lambda b: b/sp.ntheory.factor_.totient(b))

#%% Problem 71
#I tried to save a little time with the array math (a).  There's no getting around
#checking with gcd, sorting, and then finding the findal result.  Or maybe there is...
[sorted([[b,c] for b,c in tqdm(zip((a*3//7),a),position=0,leave=True) if 
 sp.gcd(b,c)==1],key=lambda d: d[0]/d[1]) for a in [np.arange(8,10**6)]][0][-1][0]

#%% Problem 72
#The totient tells us how many numbers smaller are relative primes so if you sum them up
#that should be the right answer.
sum([sp.ntheory.factor_.totient(a) for a in tqdm(range(2,1+10**6),position=0,leave=True)])

#%% Problem 73
#simple
len([b for a in tqdm(range(1,12001),position=0,leave=True) for b in \
 np.arange(a//3,int(np.ceil(a/2))) if 1/3<b/a<1/2 and sp.gcd(a,b)==1])

#%% Problem 74
#we nest a function that does the stuff, until a repeat is encountered.
np.sum([len(xt.nest_while(lambda b: [*b,sum([sp.factorial(d) for d in str(b[-1])])],[a],
 lambda c: c[-1] not in c[:-1])[:-1])==60 for a in tqdm(range(3,10**6),position=0,leave=True)])

#%% Problem 75
#a controls the max, b the first parameter, c the second, which generates all
#the primitive triples, which are multiplied by ranges in d. the 'variant' approach
#as described int 'the generating pythagorean triples' wikipedia page is used
#wherein the total length is m*(m+n) and odd triples are used. we use np.unique
#to tally up the values and return tallies of 1 to add up the number
np.sum(np.unique([d*(b**2+b*c) for a in [15*10**5] for b in range(1,2000,2) \
 for c in range(1,b,2) if sp.gcd(c,b)==1 and b*(b+c)<a for d in range(1, \
 int(np.ceil(a/(b**2+b*c)))) if d*(b**2+b*c)<=a],return_counts=True)[1]==1)

#%% Problem 76
#we construct a recursive algorithm with a [done,todo] structure.  We nest it
#(b) adding more length to each item until the todo list is of len 0 (c).
xt.nest_while( lambda b: [b[0]+len([1 for e in range(1,min(b[1][-1])+1) if 
 sum(b[1][-1])+e==100]),b[1][:-1]+[b[1][-1]+[e] for e in range(1,min(b[1][-1])+1)
 if sum(b[1][-1])+e<100]],[0,[[a] for a in list(range(1,100))]],lambda c: len(c[1])!=0)[0]

#%% Problem 77                             
#Same as the last problem but we nest it in another nestwhile structure which
#increments the first term and will terminate only when the number possibilities
#(held in the second term) goes over 5k
xt.nest_while(lambda f: [f[0]+1,[f[0]+1,xt.nest_while( lambda b: [b[0]+len([1 
 for e in sp.primerange(1,min(b[1][-1])+1) if sum(b[1][-1])+e==(f[0]+1)]),b[1][:-1]
 +[b[1][-1]+[e] for e in sp.primerange(1,min(b[1][-1])+1) if sum(b[1][-1])+e<(f[0]+1)]]
 ,[0,[[a] for a in list(sp.primerange(1,f[0]+1))]], lambda c: len(c[1])!=0)[0]]],
 [3,[0,0]],lambda g: not g[1][1]>=5000)[0]
                                        
#%% Problem 78
#so I put problem 76 in a for loop (plus 1 each time) and put that answer in the 
#OEIS and ctrl+F'ed for 'python'. Turns out sympy has number of partitions built in.
#thank goodness because this would have taken FOREVER to calculate.
min(np.where(np.array([sp.ntheory.npartitions(i) for i in range(10**5)])%10**6==0)[0])

#%% Problem 79
#yeah I mean I could go into details but why?
numbers = [319,680,180,690,129,620,762,689,762,318,368,710,720,710,629,168,160,689,
           716,731,736,729,316,729,729,710,769,290,719,680,318,389,162,289,162,718,
           729,319,790,680,890,362,319,760,316,729,380,319,728,716]
min(list(it.chain(*[[[j for j in i if all([re.match('\\d*?'+'\\d*?'.join(list(k)) \
 +'\\d*?',j) is not None for k in b])] for i in [[e[:g]+e[g+1:h]+e[h+1:] for h in \
 range(len(e)) for g in range(h) if h!=g]+[e[:h]+e[h+1:] for h in range(len(e) \
 +1)]]][0] for b in [[str(a) for a in numbers]] for e in tqdm([''.join(d) for d \
 in list(it.chain(*[list(it.permutations(b,c)) for c in range(2,5)]))],leave=True, \
 position=0) if all([re.match('\\d*?'+'\\d*?'.join(list(f))+'\\d*?',e) is not None \
 for f in b])])),key=len)

                     
                     