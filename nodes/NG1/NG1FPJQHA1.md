---
tag: NG1FPJQHA1
kind: statement
role: theorem
name: Steinhaus theorem on regular methods
msc: [40C05, 40D20]
uses: [RKFB6AHPBE, BXVVXJQV8M, 05FQ3VGAR9]
about: [M6311DWJ1E, 29C7C41A52]
sources:
  - url: https://en.wikipedia.org/wiki/Silverman–Toeplitz_theorem
---

## Statement

Let $A = (a_{nk})_{n, k \ge 0}$ be an infinite complex matrix whose [[matrix method|RKFB6AHPBE]] is [[regular|BXVVXJQV8M]].
Then there is a sequence $s$ with all terms in $\set{0, 1}$ that is not $A$-summable.
In particular, no regular matrix method sums every [[bounded sequence|05FQ3VGAR9]].

## Remarks

Proof idea: a "gliding hump" argument.
By the [[Silverman–Toeplitz theorem|S4J7SRPXMZ]], each fixed column of $A$ fades as $n$ grows, while row sums tend to $1$ and the absolute row sums stay bounded.
So one can pick rows $n_1 < n_2 < \cdots$ and disjoint blocks of columns such that row $n_j$ has almost all its weight on block $j$.
Put $s_k = 1$ on the blocks with odd $j$ and $s_k = 0$ elsewhere.
Then $(As)_{n_j}$ is close to $1$ for odd $j$ and close to $0$ for even $j$, so $(As)_n$ does not converge.
Example: for Cesàro summation, the sequence equal to $1$ for $2^{2j} \le k < 2^{2j+1}$ and $0$ otherwise has Cesàro means that oscillate between values near $\frac13$ and near $\frac23$.

## Explanations

### L1 human

Every reasonable averaging method of matrix type fails on some sequence of zeros and ones.
So there is no single regular matrix method that gives a limit to all bounded sequences.

### L2 human

The theorem shows that the bounded sequences are never all summable by one regular matrix.
Extensions of the limit to all bounded sequences do exist, such as [[Banach limits|SYF2ND6J97]], but they are not given by matrices, and their existence uses the Hahn–Banach theorem.
