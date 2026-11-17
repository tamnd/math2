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

Experimental mathematics is the use of computation to explore mathematical objects: to find patterns, to state and test [[conjectures|WMEMMHZ3BH]], and to identify exact values from numerical ones.
A typical experiment computes a quantity to high precision, searches for an exact form that matches it, and tests the match at a higher precision and on new data.
The main tools are arbitrary-precision arithmetic, integer relation algorithms such as PSLQ, inverse symbolic calculators, computer algebra and databases such as the On-Line Encyclopedia of Integer Sequences.
The output of an experiment is a conjecture with strong evidence, and it becomes a theorem only with a [[proof|0B94TKFQJX]].
The method matters because many identities and patterns were found first by computation and then proved, the BBP formula for $\pi$ among them.

## Motivation

Many questions have answers that are hard to guess and easy to check.
A sum, an integral or a sequence may have a closed form, but the form is not visible in the definition.
Computation reverses the order of work: the machine produces the number or the first terms, and the mathematician looks for the form.
Once a precise conjecture exists, a proof is often much easier to find, because its target is known.

The idea is old.
Gauss guessed the [[prime number theorem|0EHBY5Y84N]] from tables of primes, and Euler tested his conjectures with long hand computations.
Electronic computers changed the scale: values to hundreds of digits, sequences with thousands of terms, and searches over millions of candidate formulas.

## Notation

An integer relation for a vector $x = (x_1, \ldots, x_n)$ of real numbers is a nonzero vector $a = (a_1, \ldots, a_n)$ of integers with
$$a_1 x_1 + a_2 x_2 + \cdots + a_n x_n = 0.$$
An integer relation algorithm takes $x$ to a given precision and either finds a relation with small $|a_i|$ or proves that no relation exists with $\|a\|$ below a bound.
The best known algorithms are PSLQ (Helaman Ferguson and David Bailey) and methods based on the LLL lattice reduction algorithm (Arjen Lenstra, Hendrik Lenstra and László Lovász).
To test whether $\alpha$ is algebraic of degree at most $d$, one applies the algorithm to $(1, \alpha, \alpha^2, \ldots, \alpha^d)$.
To test whether $\alpha$ is a rational combination of known constants $c_1, \ldots, c_k$, one applies it to $(\alpha, c_1, \ldots, c_k)$.

## Remarks

### Examples

1. [[Discovery of the BBP formula for pi|ZQWC236CQQ]]: a PSLQ search found $\pi = \sum_{k \geq 0} 16^{-k}\left(\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6}\right)$ in 1995, and a short proof followed.
2. [[Identifying the sum of 1/(n^2 C(2n,n))|SQHXXFTXEY]]: a numerical value $0.5483113556\ldots$ and an integer relation with $\pi^2$ give the conjecture $\pi^2/18$, and a known series for $\arcsin^2$ proves it.
3. Polynomial fitting: the sums $1^3 + \cdots + n^3$ have constant fourth differences, which suggests a polynomial of degree $4$ and then the formula $\left(n(n+1)/2\right)^2$; see [[a conjecture for the sum of the first n cubes|H19P682F8X]].
4. Sequence lookup: the counts $1, 2, 5, 14, 42$ of some new family of objects are the first [[Catalan numbers|0YWZJEABB2]]. A search in the OEIS proposes this match and the known formulas, and the match becomes a conjecture to prove by a bijection.
5. Testing a conjecture: a computer search through all even numbers up to a bound tests Goldbach's conjecture; see [[Goldbach partitions grow with n|RKFZV5NFXE]].

### Non-examples

1. [[Ramanujan's constant is not an integer|7ZM5VCCB7H]]: $e^{\pi\sqrt{163}}$ agrees with an integer to $12$ decimal places. Accepting the match without a test at higher precision is a numerical coincidence, not an experimental result.
2. A computation of a known quantity with no question attached, such as a record computation of digits of $\pi$, is computation but not an experiment. It tests hardware and algorithms, not a conjecture.
3. A proof by exhaustive computer check, such as a check of all cases of a finite statement, is a proof and not an experiment; its acceptance is treated in [[rigour and the acceptance of proofs|1BTHSHST4M]].

### Basic properties

1. An integer relation found at precision $D$ digits is evidence only if it persists when $D$ is increased. A false relation found by chance usually disappears at the next precision.
2. If the precision is $D$ digits and the relation has $n$ coefficients of size at most $10^m$, then a chance relation is unlikely when $nm$ is much smaller than $D$. A relation with large coefficients relative to $D$ is suspect.
3. A failure to find a relation is also data: PSLQ gives a lower bound for the size of any relation, which excludes simple closed forms.
4. Experimental evidence never replaces a proof; there are [[patterns that eventually fail|A2KSJSQSF6]] and equalities that hold to many digits but not exactly, such as the Borwein integrals on the same page.
5. A conjecture from an experiment should be stated with its evidence: the precision, the range checked and the method.

### History

David Epstein, Silvio Levy and Klaus Peters founded the journal "Experimental Mathematics" in 1992.
Its statement of aims names three kinds of papers: results inspired by experiment, conjectures suggested by experiment, and data that support hypotheses.
Ferguson and Bailey described PSLQ in the early 1990s, and the LLL algorithm dates from 1982.
In 1995 Simon Plouffe found the BBP formula with PSLQ; David Bailey, Peter Borwein and Plouffe published it in Mathematics of Computation in 1997.
Neil Sloane began to collect integer sequences in 1964, and his collection became a website, the OEIS, in 1996.
Jonathan Borwein and David Bailey described the method and its tools in the book "Mathematics by Experiment".

### Common errors

1. Trusting low precision. A relation found with $15$ digits and coefficients near $10^4$ can be an accident; recompute with more digits.
2. Searching too many candidate forms. With enough constants in the search, some combination matches any number to the working precision.
3. Calling an experimental result a theorem. The statement must be marked as a conjecture until a proof exists, even if the evidence is overwhelming.

## Explanations

### L1 human

Experimental mathematics means using a computer like a laboratory.
We compute many examples and look for a rule.
For example, a computer can add up $1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \cdots$ and print $1.6449\ldots$.
A mathematician then notices that $\pi \times \pi / 6$ gives the same digits.
The computer did not prove anything, but it told the mathematician what to prove.

### L2 human

We identify $\alpha = \sqrt{2} + \sqrt{3} = 3.1462643699\ldots$ as if we did not know its form.

1. We compute $\alpha$ to $30$ digits.
2. We guess that $\alpha$ is algebraic of degree at most $4$, and we apply an integer relation algorithm to $(1, \alpha, \alpha^2, \alpha^3, \alpha^4)$.
3. The algorithm returns $(1, 0, -10, 0, 1)$, that is, $\alpha^4 - 10\alpha^2 + 1 = 0$.
4. We test at $60$ digits: the relation persists, and the residual is at the level of the rounding error.
5. Proof: $\alpha^2 = 5 + 2\sqrt6$, so $(\alpha^2 - 5)^2 = 24$, which gives $\alpha^4 - 10\alpha^2 + 1 = 0$.

The typical use is this chain: compute, detect, test, prove.
A trap: the degree bound of step 2 is a guess; with degree $3$ the algorithm finds no small relation, and that failure must not be read as "$\alpha$ is transcendental".

### L3 human

Integer relation detection is a lattice problem.
For $x \in \mathbb{R}^n$ known to precision $10^{-D}$, the lattice spanned by the rows $(e_i, \operatorname{round}(10^D x_i))$ contains a short vector when a small relation exists, and LLL finds a short vector in polynomial time.
The same reduction gives algorithms for minimal polynomials, for simultaneous Diophantine approximation and for factoring polynomials over $\mathbb{Q}$.

The method fits the wider view of [[plausible reasoning|8DHD3H1CJ9]]: a relation that holds to many digits is a surprising consequence of the conjecture, and so it adds much credibility.
[[Numerical evidence|JFD3QWCX8Z]] studies how such credibility can mislead, and [[machine-assisted discovery|D1YQW43N3K]] extends the method from formula search to search by learning systems.
The software tools belong to [[tools of experimental mathematics|KY55MDRBEY]] and to [[mathematical databases|956TNX0HG9]].
