---
tag: PMYDHW00KF
kind: statement
role: theorem
name: Pentagonal number theorem
msc: [11P81, 05A17]
uses: [033WGN00BF, 0JV30XN73Z, 001CX45SWQ, MX3CVYMNDV]
about: [0JV30XN73Z, 0578PA53VA]
sources:
  - url: https://en.wikipedia.org/wiki/Pentagonal_number_theorem
same_as:
  wikidata: Q282649
  wikipedia: Pentagonal number theorem
---

## Statement

In the ring of [[formal power series|033WGN00BF]] $\Z[\![x]\!]$,
$$\prod_{n=1}^{\infty} (1 - x^n) = \sum_{k=-\infty}^{\infty} (-1)^k x^{k(3k-1)/2} = 1 - x - x^2 + x^5 + x^7 - x^{12} - x^{15} + \cdots.$$
The same identity holds for complex $x$ with $\abs{x} < 1$, both sides converging absolutely.

## Remarks

The exponents $k(3k-1)/2$ for $k = 0, \pm 1, \pm 2, \ldots$ are the generalized pentagonal numbers $0, 1, 2, 5, 7, 12, 15, 22, 26, \ldots$.
Let $E(m)$ and $O(m)$ be the numbers of partitions of $m$ into an even and an odd number of distinct parts.
The coefficient of $x^m$ on the left is $E(m) - O(m)$.
Franklin's bijection pairs these two kinds of partitions, and the only unpaired partitions occur when $m$ is a generalized pentagonal number, with sign $(-1)^k$.
Example: for $m = 3$, the distinct-part partitions are $3$ (one part) and $2 + 1$ (two parts), so the coefficient is $1 - 1 = 0$; indeed $3$ is not a generalized pentagonal number.
The [[generating function for partitions|0578PA53VA]] is $\prod_n (1 - x^n)^{-1} = \sum_m p(m) x^m$.
Multiplying the theorem by it gives the recurrence
$$p(m) = p(m-1) + p(m-2) - p(m-5) - p(m-7) + p(m-12) + p(m-15) - \cdots,$$
with $p(0) = 1$ and $p(j) = 0$ for $j < 0$.

## Explanations

### L1 human

Multiply out $(1 - x)(1 - x^2)(1 - x^3)\cdots$.
One expects a mess, but almost everything cancels: only the powers $0, 1, 2, 5, 7, 12, 15, \ldots$ survive, each with coefficient $+1$ or $-1$.
These exponents are the pentagonal numbers, which count dots in nested pentagons, together with a second family of the same shape.

### L2 human

Euler found the identity, and it gives a fast recurrence for the [[partition function|001CX45SWQ]] $p(m)$.
It is a special case of the Jacobi triple product identity.
The left side is, up to the factor $x^{1/24}$, the [[Dedekind eta function|MX3CVYMNDV]], so the theorem is also a statement about a modular form.
