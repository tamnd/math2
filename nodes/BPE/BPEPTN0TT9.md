---
tag: BPEPTN0TT9
kind: concept
name: Experimental mathematics
aliases: [mathematical-experiment, integer-relation-detection]
msc: ["00A35", "11Y60", "68V99"]
topics: [DME0TPC348]
audience: research
uses: [8DHD3H1CJ9, WMEMMHZ3BH, 0B94TKFQJX]
sources:
  - url: https://en.wikipedia.org/wiki/Experimental_mathematics
    locator: Tools and techniques
  - url: https://en.wikipedia.org/wiki/Experimental_Mathematics_(journal)
    locator: History
  - url: https://en.wikipedia.org/wiki/Integer_relation_algorithm
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Inverse_Symbolic_Calculator
    locator: lead section
  - url: https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences
    locator: lead section
---

## Summary

Experimental mathematics uses the computer as a laboratory.
You compute many cases or many digits, look for a pattern or an exact form, and test it on new data before you try to prove it.

Here is a small experiment that you can repeat.
Add the first terms of
$$S = \sum_{n=1}^{\infty} \frac{1}{n^2 \binom{2n}{n}} = \frac{1}{2} + \frac{1}{24} + \frac{1}{180} + \cdots.$$
The terms shrink by a factor near $4$ each time, so $40$ terms give $S = 0.54831135561607547882\ldots$ to more than $25$ digits.
A search for a simple relation between $S$ and known constants finds $18 S = \pi^2$, and $\pi^2/18$ agrees with $S$ in every computed digit.
That agreement is a [[conjecture|WMEMMHZ3BH]] with very strong evidence.
It becomes a theorem only through a [[proof|0B94TKFQJX]], which here comes from the power series of $\arcsin^2 x$.

In general, an experiment computes a quantity to high precision, searches for an exact form that matches it, and tests the match at higher precision and on new data.
The main tools are arithmetic with many digits, integer relation algorithms such as PSLQ, inverse symbolic calculators, computer algebra, and databases such as the On-Line Encyclopedia of Integer Sequences (OEIS).

## Motivation

Many questions have answers that are hard to guess and easy to check.
A sum, an integral or a sequence may have a closed form that is not visible in its definition.
Computation reverses the order of work: the machine produces the number or the first terms, and the mathematician looks for the form.
Once a precise conjecture exists, a proof is often much easier to find, because its target is known.

The idea is old.
Gauss guessed the [[prime number theorem|0EHBY5Y84N]] from tables of primes, and Euler tested his guesses with long hand computations.
Electronic computers changed the scale: values to thousands of digits, sequences with thousands of terms, and searches over millions of candidate formulas.
The output is evidence in the sense of [[plausible reasoning|8DHD3H1CJ9]], and the sub-area weighs that evidence in [[numerical evidence for conjectures|JFD3QWCX8Z]].

## Notation

An integer relation for real numbers $x_1, \ldots, x_n$ is a list of integers $a_1, \ldots, a_n$, not all zero, with
$$a_1 x_1 + a_2 x_2 + \cdots + a_n x_n = 0.$$
An integer relation algorithm takes the $x_i$ to a given precision and either finds a relation with small $|a_i|$ or shows that no relation exists with coefficients below a bound.
The best known algorithms are PSLQ, by Helaman Ferguson and David Bailey, and methods based on the LLL lattice reduction algorithm of Arjen Lenstra, Hendrik Lenstra and László Lovász.
To test whether $\alpha$ is algebraic of degree at most $d$, run the algorithm on $(1, \alpha, \alpha^2, \ldots, \alpha^d)$.
To test whether $\alpha$ is a rational combination of constants $c_1, \ldots, c_k$, run it on $(\alpha, c_1, \ldots, c_k)$.

## Remarks

### The chain of an experiment

Every good experiment follows the same chain: compute, detect, test, prove.
[[Identifying the sum of 1/(n^2 C(2n,n))|SQHXXFTXEY]] runs the chain for the sum $S$ above.
The relation $18 S - \pi^2 = 0$ survives when the precision grows, and the constants $\ln 2$ and $\zeta(3)$ in the search get the coefficient $0$.
The proof then uses the series
$$2 \arcsin^2 x = \sum_{n \ge 1} \frac{(2x)^{2n}}{n^2 \binom{2n}{n}}$$
at $x = 1/2$, where $\arcsin(1/2) = \pi/6$ gives $S = 2 \cdot \pi^2/36 = \pi^2/18$.

[[The discovery of the BBP formula for pi|ZQWC236CQQ]] is the classic case.
An integer relation search in 1995 found
$$\pi = \sum_{k \ge 0} \frac{1}{16^k} \left( \frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6} \right),$$
and a proof with first-year calculus followed.

### Fitting and lookup

Not every experiment needs many digits.
The sums $1^3 + \cdots + n^3$ are $1, 9, 36, 100, 225, \ldots$, and their fourth differences are constant.
That suggests a polynomial of degree $4$, and fitting gives $\left(n(n+1)/2\right)^2$; see [[a conjecture for the sum of the first n cubes|H19P682F8X]].
In the same way, counts $1, 2, 5, 14, 42$ of a new family of objects match the first [[Catalan numbers|0YWZJEABB2]].
A search in the OEIS proposes the match and the known formulas, and the match becomes a conjecture to prove by a bijection.
A computer search can also test a conjecture directly, as in [[Goldbach partitions grow with n|RKFZV5NFXE]].

### What it is not

[[Ramanujan's constant is not an integer|7ZM5VCCB7H]] shows a match without the test.
At $29$ significant digits $e^{\pi \sqrt{163}}$ prints as $262537412640768744.00000000000$, and at $30$ digits it prints as $\ldots 743.999999999999$.
Accepting the first output skips the test step, so it is a coincidence, not an experimental result.

A record computation of the digits of $\pi$ is computation without a question, so it is not an experiment in this sense.
A proof by an exhaustive check of all cases of a finite statement is a proof, not an experiment; its status belongs to [[rigor and the acceptance of proofs|1BTHSHST4M]].

### The rules you can use

A relation found at $D$ digits counts as evidence only if it persists when $D$ grows, because a chance relation usually disappears at the next precision.
A relation with $n$ coefficients of about $m$ digits each is suspect unless $n m$ is well below $D$, since with that many free digits some relation fits almost any numbers.
A failure to find a relation is also data: PSLQ gives a lower bound on the size of any relation, and so it rules out simple closed forms.
A conjecture from an experiment should be stated with its evidence: the precision, the range checked and the method.

### Watch out

A pattern that holds to many digits is not a proof.
The Borwein integrals are the standard warning.
With $\operatorname{sinc} x = \sin x / x$, the integral
$$\int_0^\infty \operatorname{sinc}(x) \operatorname{sinc}\!\left(\frac{x}{3}\right) \cdots \operatorname{sinc}\!\left(\frac{x}{2m+1}\right) dx$$
equals $\pi/2$ for every product up to the factor $\operatorname{sinc}(x/13)$.
With the next factor $\operatorname{sinc}(x/15)$ it falls below $\pi/2$ by about $2.31 \cdot 10^{-11}$, so a test with $10$ digits sees no change; see [[patterns that eventually fail|A2KSJSQSF6]].

The second error is to search too many forms.
With enough constants in the basis, some combination matches any number to the working precision.
The third error is to call an experimental result a theorem; mark it as a conjecture until a proof exists.

### History

David Epstein, Silvio Levy and Klaus Peters founded the journal *Experimental Mathematics* in 1992.
Ferguson and Bailey described PSLQ in the early 1990s, and the LLL algorithm dates from 1982.
In 1995 Simon Plouffe found the BBP formula with an integer relation search, and David Bailey, Peter Borwein and Plouffe published it in 1997.
Neil Sloane began to collect integer sequences in 1964, and the collection became the OEIS website in 1996.
Jonathan Borwein and David Bailey described the method and its tools in the book *Mathematics by Experiment*.

### Try it

Compute the first three terms of $S$ and their sum.
The terms are $1/(1 \cdot 2) = 1/2$, $1/(4 \cdot 6) = 1/24$ and $1/(9 \cdot 20) = 1/180$, and the sum is $0.547222\ldots$, already within $0.0011$ of $\pi^2/18 = 0.548311\ldots$.

An integer relation search on $(1, \alpha, \alpha^2)$ for $\alpha = 1.6180339887\ldots$ returns $(1, 1, -1)$; what is the conjecture?
It is $1 + \alpha - \alpha^2 = 0$.
The roots of $t^2 - t - 1 = 0$ are $(1 \pm \sqrt 5)/2$, and only the positive root $1.6180339887\ldots$ matches, so the conjecture is that $\alpha$ is the golden ratio.

## Explanations

### L1 human

Experimental mathematics means using a computer like a laboratory.
We compute many examples and look for a rule.
For example, a computer can add $1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \cdots$ and print $1.6449\ldots$.
A mathematician notices that $\pi \times \pi / 6$ gives the same digits.
The computer proved nothing, but it told the mathematician what to prove.

### L2 human

We identify $\alpha = \sqrt{2} + \sqrt{3} = 3.1462643699\ldots$ as if we did not know its form.
We compute $\alpha$ to $30$ digits and guess that it is algebraic of degree at most $4$.
An integer relation search on $(1, \alpha, \alpha^2, \alpha^3, \alpha^4)$ returns $(1, 0, -10, 0, 1)$, that is,
$$\alpha^4 - 10 \alpha^2 + 1 = 0.$$
At $60$ digits the relation persists, and the remainder is at the level of the rounding error.
Now the proof is short.
Since $\alpha^2 = 5 + 2\sqrt{6}$, we get $(\alpha^2 - 5)^2 = 24$, which expands to the relation above.

The typical use is this chain: compute, detect, test, prove.
Watch out for the degree bound, which was a guess.
With degree at most $3$ the search finds no small relation, and that failure must not be read as "$\alpha$ is transcendental".

### L3 human

Integer relation detection is a lattice problem.
For $x \in \mathbb{R}^n$ known to precision $10^{-D}$, the lattice spanned by the rows $(e_i, \operatorname{round}(10^D x_i))$ contains a short vector when a small relation exists, and LLL finds a short vector in polynomial time.
The same reduction gives algorithms for minimal polynomials, for simultaneous Diophantine approximation and for factoring polynomials over $\mathbb{Q}$.

A relation that holds to many digits is a surprising consequence of the conjecture, and in the language of [[plausible reasoning|8DHD3H1CJ9]] it adds much credibility.
[[Numerical evidence|JFD3QWCX8Z]] studies how such credibility can mislead, and [[machine-assisted discovery|D1YQW43N3K]] extends the method from the search for one formula to searches by learning systems.
The software belongs to [[tools of experimental mathematics|KY55MDRBEY]] and to [[mathematical databases|956TNX0HG9]].
