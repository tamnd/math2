---
tag: R587SR9GNV
kind: statement
role: theorem
name: Euler's pentagonal number theorem
msc: [11P81, 05A17, 05A19]
uses: [033WGN00BF, 0JV30XN73Z, 0CV69WDRXW]
about: [0JV30XN73Z, 0CV69WDRXW]
sources:
  - url: https://en.wikipedia.org/wiki/Pentagonal_number_theorem
same_as:
  wikidata: Q282649
  wikipedia: Pentagonal number theorem
---

## Statement

In the ring of [[formal power series|033WGN00BF]] $\Z[\![x]\!]$,
$$\prod_{n=1}^{\infty} (1 - x^n) = \sum_{k=-\infty}^{\infty} (-1)^k x^{k(3k-1)/2} = 1 - x - x^2 + x^5 + x^7 - x^{12} - x^{15} + \cdots.$$
The same identity holds for complex numbers $x$ with $\abs{x} < 1$, where both sides converge absolutely.

## Remarks

The exponents $k(3k - 1)/2$ for $k = 1, -1, 2, -2, 3, -3, \ldots$ are $1, 2, 5, 7, 12, 15, \ldots$, the generalised pentagonal numbers.
Franklin's bijective proof reads the identity as a statement on [[integer partitions|0JV30XN73Z]] of $m$ into distinct parts.
The partitions with an even number of parts and those with an odd number of parts are equinumerous, except when $m = k(3k \pm 1)/2$.
In that case the difference, even minus odd, is $(-1)^k$.
Franklin's involution moves the smallest part onto the largest parts, or back, and it changes the number of parts by one.

Example: for $m = 5$, the partitions into distinct parts are $5$, $4 + 1$ and $3 + 2$.
One has an odd number of parts and two have an even number, so the coefficient of $x^5$ is $2 - 1 = 1$, as in the series.

Multiplying by the [[generating function for partitions|0578PA53VA]] $\prod_n (1 - x^n)^{-1}$ gives a recurrence for the [[partition function|0CV69WDRXW]]:
$$p(m) = \sum_{k \ne 0} (-1)^{k+1}\, p\big(m - k(3k - 1)/2\big),$$
with $p(0) = 1$ and $p(j) = 0$ for $j < 0$.
For example, $p(5) = p(4) + p(3) - p(0) = 5 + 3 - 1 = 7$.
The theorem is a special case of the Jacobi triple product.

## Explanations

### L1 human

Multiply out $(1 - x)(1 - x^2)(1 - x^3)\cdots$ without end.
One expects a messy series, but almost everything cancels.
Only the powers $x^1, x^2, x^5, x^7, x^{12}, x^{15}, \ldots$ survive, with signs in the pattern $-, -, +, +, -, -, \ldots$, and every coefficient is $0$ or $\pm 1$.
The surviving exponents are the pentagonal numbers and their close relatives.

### L2 human

The product $\prod (1 - x^n)$ is the reciprocal of the partition generating function, so the theorem controls the partition numbers $p(m)$.
The recurrence above computes $p(m)$ with about $\sqrt{m}$ terms, which was the standard method for tables of $p(m)$.
The bijective proof by Franklin is a model of a sign-reversing involution.
The identity is the simplest of a family of product-sum identities that includes the Jacobi triple product and the [[Rogers–Ramanujan identities|M24H4GJPPW]].
