---
tag: M24H4GJPPW
kind: statement
role: theorem
name: Rogers–Ramanujan identities
msc: [11P84, 05A17, 05A19]
uses: [033WGN00BF, 0JV30XN73Z]
about: [0JV30XN73Z]
sources:
  - url: https://en.wikipedia.org/wiki/Rogers%E2%80%93Ramanujan_identities
same_as:
  wikidata: Q7359380
  wikipedia: Rogers–Ramanujan identities
---

## Statement

For an integer $n \ge 0$, let $(q; q)_n = (1 - q)(1 - q^2) \cdots (1 - q^n)$, the q-Pochhammer symbol, with $(q; q)_0 = 1$.
In the ring of [[formal power series|033WGN00BF]] $\Z[\![q]\!]$, the following two identities hold.

1. $$\sum_{n=0}^{\infty} \frac{q^{n^2}}{(q; q)_n} = \prod_{n=0}^{\infty} \frac{1}{(1 - q^{5n+1})(1 - q^{5n+4})}.$$
2. $$\sum_{n=0}^{\infty} \frac{q^{n^2 + n}}{(q; q)_n} = \prod_{n=0}^{\infty} \frac{1}{(1 - q^{5n+2})(1 - q^{5n+3})}.$$

## Remarks

In terms of [[integer partitions|0JV30XN73Z]], the identities say the following for each $m \ge 0$.
The partitions of $m$ whose parts differ pairwise by at least $2$ are as many as the partitions of $m$ into parts congruent to $1$ or $4$ modulo $5$.
Consider the partitions of $m$ whose parts differ by at least $2$ and are all at least $2$.
They are as many as the partitions of $m$ into parts congruent to $2$ or $3$ modulo $5$.
The term $q^{n^2} / (q; q)_n$ counts the partitions of the first kind with exactly $n$ parts, since $n^2 = 1 + 3 + \cdots + (2n - 1)$ is the smallest such sum.

Example: for $m = 6$, the partitions with parts differing by at least $2$ are $6$, $5 + 1$ and $4 + 2$.
The partitions into parts from $\set{1, 4, 6, 9, \ldots}$ are $6$, $4 + 1 + 1$ and $1 + 1 + 1 + 1 + 1 + 1$.
Both counts are $3$.

A standard proof transforms the sum side and then applies the Jacobi triple product to reach the product side.
The identities were found by Leonard James Rogers and later found again by Srinivasa Ramanujan.

## Explanations

### L1 human

Count the ways to write a number as a sum of parts that are far apart, each two parts differing by at least $2$.
Count also the ways to write it as a sum of parts that end in $1, 4, 6$ or $9$.
The theorem says that the two counts always agree.
Nothing in the two rules suggests the connection, which is why the identities are famous.

### L2 human

The identities are the prototype of partition identities of Rogers–Ramanujan type, where a difference condition on the parts matches a congruence condition.
Their sum sides are basic hypergeometric series and their product sides are, up to a power of $q$, quotients of theta functions.
They appear in the theory of modular forms, in the hard hexagon model of statistical mechanics, and in the representation theory of affine Lie algebras.
Compare with [[Euler's partition theorem|0XFZ1BMF5Q]], where parts are distinct on one side and odd on the other.
