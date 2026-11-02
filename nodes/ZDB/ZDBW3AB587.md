---
tag: ZDBW3AB587
kind: statement
role: theorem
name: Bareiss algorithm
msc: [65F40, 15A15, 68W30]
uses: [00KDZRW4C0, 0BT9BYWVRY, 0QVD7WBFGN, 0JVJ2WCXZH, CGDN1X32NQ]
about: [00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Bareiss_algorithm
same_as:
  wikidata: Q4860404
  wikipedia: Bareiss algorithm
---

## Statement

Let $R$ be an [[integral domain|0QVD7WBFGN]] and let $A = (a_{ij})$ be an $n \times n$ matrix over $R$, with $n \ge 2$.
Put $a^{(0)}_{ij} = a_{ij}$.
For $k = 1, \dots, n - 1$ and $k < i, j \le n$, the *Bareiss algorithm* sets
$$a^{(k)}_{ij} = \frac{a^{(k-1)}_{kk} \, a^{(k-1)}_{ij} - a^{(k-1)}_{ik} \, a^{(k-1)}_{kj}}{a^{(k-2)}_{k-1, k-1}},$$
where the denominator is $1$ for $k = 1$.
Assume that the leading principal [[minors|0BT9BYWVRY]] of $A$ of orders $1, \dots, n - 1$ are nonzero.
Then:

1. for each $k$ and each $i, j > k$, the entry $a^{(k)}_{ij}$ equals the determinant of the $(k+1) \times (k+1)$ submatrix of $A$ with rows $1, \dots, k, i$ and columns $1, \dots, k, j$;
2. in particular, every division in the algorithm is exact in $R$, every pivot $a^{(k-1)}_{kk}$ is the leading principal minor of order $k$, and $a^{(n-1)}_{nn} = \det A$.

## Remarks

Clause 1 is proved by induction on $k$ with Sylvester's determinant identity, which expresses a bordered minor of the reduced matrix as a ratio of minors of $A$.
For $k = 1$ it is the direct check $a^{(1)}_{ij} = a_{11} a_{ij} - a_{i1} a_{1j} = \det \begin{pmatrix} a_{11} & a_{1j} \\ a_{i1} & a_{ij} \end{pmatrix}$.
Example: for $A = \begin{pmatrix} 2 & 3 & 1 \\ 4 & 1 & 5 \\ 6 & 2 & 3 \end{pmatrix}$ over $\Z$, step $1$ gives $a^{(1)}_{22} = -10$, $a^{(1)}_{23} = 6$, $a^{(1)}_{32} = -14$, $a^{(1)}_{33} = 0$, and step $2$ gives $a^{(2)}_{33} = \big((-10) \cdot 0 - 6 \cdot (-14)\big)/2 = 42 = \det A$.
Over $\Z$, clause 1 and [[Hadamard's inequality|CGDN1X32NQ]] bound the size of every intermediate entry.
So the bit length of the numbers grows only polynomially, unlike naive fraction-free elimination, where it can double at each step.
If a pivot is zero, rows can be exchanged as in [[Gaussian elimination|0JVJ2WCXZH]], which changes the sign of the [[determinant|00KDZRW4C0]].
The algorithm uses $O(n^3)$ operations in $R$.

## Explanations

### L1 human

To compute a determinant of an integer matrix exactly, one wants to avoid fractions.
Cross-multiplying rows avoids fractions but makes the numbers huge.
The Bareiss algorithm cross-multiplies and then divides by the previous pivot, and a theorem guarantees that this division always leaves no remainder.

### L2 human

It is fraction-free Gaussian elimination: the work is the same order as ordinary elimination, but all intermediate values are minors of the input matrix.
It is a standard method in computer algebra for determinants, ranks and exact solutions of linear systems over $\Z$ or over polynomial rings.
The final pivot is the determinant, and the earlier pivots are the leading principal minors.
