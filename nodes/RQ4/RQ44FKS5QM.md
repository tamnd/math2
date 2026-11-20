---
tag: RQ44FKS5QM
kind: concept
name: Dodgson condensation
msc: ["15A15", "65F40"]
topics: [DTBK11SR77]
audience: grad
sources:
  - url: https://en.wikipedia.org/wiki/Dodgson_condensation
  - url: https://en.wikipedia.org/wiki/Dodgson_condensation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Dodgson_condensation
    locator: Desnanot–Jacobi identity and proof of correctness of the condensation algorithm
same_as:
  wikidata: Q4230490
  wikipedia: Dodgson condensation
---

## Summary

Dodgson condensation is a method to compute the [[determinant|00KDZRW4C0]] of an $n \times n$ matrix over a field by $n - 1$ steps of condensation.
Each step replaces the current matrix by the smaller matrix of its connected $2 \times 2$ minors, and divides each of them by the matching interior entry of the matrix from two steps before.
The method is defined when no divisor is zero, and then the last $1 \times 1$ matrix is the determinant; the [[definition|F7D849A4RZ]] gives the exact recursion.
It matters because it uses only $2 \times 2$ determinants and exact divisions, and it rests on the [[Desnanot-Jacobi identity|KWW7519E58]].

## Motivation

Expansion by cofactors needs about $n!$ operations, and elimination brings fractions into integer computations.
Dodgson looked for a method that a person can run by hand with small integers.
The Desnanot-Jacobi identity expresses a determinant through four minors of size $n - 1$ and one of size $n - 2$, and repeated use gives the recursion.

## Remarks

### Examples

- A $3 \times 3$ matrix with central entry $5$: the [[definition|F7D849A4RZ]] works it out, with result $-3$.
- A $4 \times 4$ condensation with result $21$, checked by Laplace expansion: [[worked example|FZJMAYK2DN]].
- A $4 \times 4$ case with the negative divisor $-1$ and result $-14$: [[second example|WHN8H0777X]].

### Non-examples

- A matrix with a zero interior entry: the method gives $0/0$ and stops; see the [[non-example|AD6GEXKCB1]].
- A matrix over a ring with zero divisors: the divisions need not be defined, even when the divisors are nonzero.

### Basic properties

- The entries after step $k$ are the connected minors of order $k + 1$ of the original matrix.
- Over $\mathbb{Z}$, every division is exact when the divisors are nonzero, since the quotients are minors.
- The method is the repeated use of the case $k = n - 2$ of [[Sylvester's determinant identity|7SSKBQYFW1]].

### History

Charles Dodgson, better known as Lewis Carroll, discovered the method in 1866.
Its proof of correctness rests on the Desnanot-Jacobi identity of 1841.

### Common errors

- Dividing by the interior of the previous matrix, and not by the interior of the matrix from two steps before.
- Reading $0/0$ as the value $0$.

## Explanations

### L1 human

Start with an $n \times n$ matrix and replace each $2 \times 2$ block of neighbouring entries by its determinant.
This gives an $(n-1) \times (n-1)$ matrix.
Repeat, but now divide each new entry by the matching inner entry of the matrix two steps back.
After $n - 1$ steps a single number is left, and it is the determinant.

### L2 human

For $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}$:

1. The connected $2 \times 2$ minors give $\begin{pmatrix} -3 & -3 \\ -3 & 2 \end{pmatrix}$.
2. The second step gives $((-3)(2) - (-3)(-3))/5 = -15/5 = -3$.
3. Laplace expansion along row 1 gives $1 \cdot 2 - 2 \cdot (-2) + 3 \cdot (-3) = -3$, which agrees.

The typical use is a hand computation with small integers.
A trap: a zero interior entry stops the method, even when the determinant is not $0$.

### L3 human

The recursion is the octahedron recurrence, and its terms are Laurent polynomials in the entries.
This Laurent property is a first case of the phenomena studied in cluster algebras.
