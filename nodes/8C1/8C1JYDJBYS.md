---
tag: 8C1JYDJBYS
kind: statement
role: theorem
name: van der Waerden conjecture on permanents
msc: [15A15, 15B51, 15A45]
uses: [X9B1XETBPF, JJA90EB2PS]
about: [X9B1XETBPF, JJA90EB2PS]
sources:
  - url: https://en.wikipedia.org/wiki/Permanent_(mathematics)
---

## Statement

Let $n \ge 1$, and let $A$ be an $n \times n$ [[doubly stochastic matrix|JJA90EB2PS]].
This means that its entries are nonnegative real numbers and that each row and each column sums to $1$.
Then
$$\operatorname{perm}(A) \ge \frac{n!}{n^n},$$
where $\operatorname{perm}$ is the [[permanent|X9B1XETBPF]].
Equality holds if and only if every entry of $A$ equals $1/n$.

## Remarks

The statement was conjectured by B. L. van der Waerden and proved independently by G. P. Egorychev and D. I. Falikman.
Egorychev's proof uses the Alexandrov–Fenchel inequality for mixed discriminants.
A later short proof by L. Gurvits uses real stable polynomials.

Example: for $n = 2$, every doubly stochastic matrix has the form $\begin{pmatrix} t & 1 - t \\ 1 - t & t \end{pmatrix}$ with $0 \le t \le 1$.
Its permanent is $t^2 + (1-t)^2$, whose minimum on $[0, 1]$ is $1/2 = 2!/2^2$, reached only at $t = 1/2$.

The value $n!/n^n$ is the permanent of the matrix with all entries $1/n$.
By Stirling's formula it is about $e^{-n} \sqrt{2 \pi n}$.

## Explanations

### L1 human

A doubly stochastic matrix spreads one unit of mass in each row and each column.
The theorem says that its permanent cannot be very small, and that the most evenly spread matrix gives the smallest value.

### L2 human

For a $k$-regular bipartite graph with $n$ vertices on each side, the biadjacency matrix divided by $k$ is doubly stochastic.
So the theorem gives at least $k^n n!/n^n$ perfect matchings.
In particular, every doubly stochastic matrix has a positive permanent, so it has a permutation pattern of positive entries.
