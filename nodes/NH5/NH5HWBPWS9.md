---
tag: NH5HWBPWS9
kind: concept
name: Pfaffian
msc: [15A15]
topics: [DTBK11SR77]
audience: grad
sources:
  - url: https://en.wikipedia.org/wiki/Pfaffian
  - url: https://en.wikipedia.org/wiki/Pfaffian
    locator: lead section
same_as:
  wikidata: Q1189744
  wikipedia: Pfaffian
---

## Summary

The Pfaffian is a polynomial in the entries of an alternating, or [[skew-symmetric|0PBY4E9GQF]], matrix of even size whose square is the [[determinant|00KDZRW4C0]].
It is a sum over the [[perfect matchings|0NHK9MFFW9]] of the index set, with signs; the [[definition|C9JJD2AVJR]] gives the formula.
It satisfies $\operatorname{pf}(A)^2 = \det A$ and $\operatorname{pf}(B A B^T) = \det(B) \operatorname{pf}(A)$.
It appears in the study of alternating forms and symplectic groups, and in the counting of perfect matchings of planar graphs.

## Motivation

The determinant of a real skew-symmetric matrix of even size is never negative, and for integer entries it is a perfect square.
This suggests a square root that is itself a polynomial in the entries.
The Pfaffian is this square root, with a sign fixed by its formula.
It has about half as many factors per term as the determinant, and far fewer terms.

## Notation

- $\operatorname{pf}(A)$ or $\operatorname{Pf}(A)$ is the Pfaffian of $A$.
- $J$ is a standard alternating matrix with $\operatorname{pf}(J) = \pm 1$; its sign depends on the convention.

## Remarks

### Examples

- $\operatorname{pf} \begin{pmatrix} 0 & a \\ -a & 0 \end{pmatrix} = a$.
- For $4 \times 4$, $\operatorname{pf}(A) = a_{12} a_{34} - a_{13} a_{24} + a_{14} a_{23}$; an integer matrix with Pfaffian $8$ and determinant $64$ is the [[example|M0JEPXXWQM]].
- Two forms of the standard symplectic matrix have Pfaffians $-1$ and $1$: [[example|65Q3YWX09Q]].

### Non-examples

- The symmetric matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ over $\mathbb{R}$ has no Pfaffian, and its determinant $-1$ is not a square: [[non-example|Z172P2ZBQ8]].
- An alternating matrix of odd size has Pfaffian $0$ by convention, because its determinant is $0$; see the [[odd size statement|55RX9C0ZTH]].

### Basic properties

- [[Square identity|473MBZST4D]]: $\operatorname{pf}(A)^2 = \det A$ for every alternating matrix of even size.
- $\operatorname{pf}(B A B^T) = \det(B) \operatorname{pf}(A)$ for every $2n \times 2n$ matrix $B$.
- $\operatorname{pf}(\lambda A) = \lambda^n \operatorname{pf}(A)$ for a $2n \times 2n$ matrix $A$, and $\operatorname{pf}(A^T) = (-1)^n \operatorname{pf}(A)$.
- An alternating matrix over a field is invertible if and only if its Pfaffian is nonzero.
- The number of perfect matchings of a planar graph is a Pfaffian; this is the basis of the [[FKT algorithm|A6SPEDH8BK]].

### History

Cayley first proved $\operatorname{pf}(A)^2 = \det A$ in 1849.
He introduced the term Pfaffian in 1852 and named it indirectly after Johann Friedrich Pfaff.

### Common errors

- Taking $\operatorname{pf}(A) = \sqrt{\det A}$; the Pfaffian can be negative, and its sign depends on the order of the basis.
- Forgetting the minus sign of the middle term in the $4 \times 4$ formula.
- Applying the formula to a matrix that is not alternating.

## Explanations

### L1 human

The determinant of an alternating matrix of even size is always a perfect square of a polynomial in its entries.
The Pfaffian is that square root, with a fixed choice of sign.
Each term of the Pfaffian pairs up the indices $1, \dots, 2n$ and multiplies the matching entries.
For $A = \begin{pmatrix} 0 & a \\ -a & 0 \end{pmatrix}$, the Pfaffian is $a$, and $\det A = a^2$.

### L2 human

For $A = \begin{pmatrix} 0 & 1 & 2 & 3 \\ -1 & 0 & 4 & 5 \\ -2 & -4 & 0 & 6 \\ -3 & -5 & -6 & 0 \end{pmatrix}$:

1. $\operatorname{pf}(A) = 1 \cdot 6 - 2 \cdot 5 + 3 \cdot 4 = 8$.
2. So $\det A = 64$, which a Laplace expansion confirms.

The typical use is to count perfect matchings, as in the dimer model of statistical physics, or to define the Euler class of an oriented vector bundle.
A trap: a reordering of the basis can change the sign of the Pfaffian but never the determinant.

### L3 human

An alternating matrix $A$ defines the $2$-form $\omega = \sum_{i < j} a_{ij}\, e_i \wedge e_j$.
Then $\omega^n / n! = \operatorname{pf}(A)\, e_1 \wedge \dots \wedge e_{2n}$, which gives a definition without matchings.
A symplectic matrix $B$ satisfies $B J B^T = J$, so the rule $\operatorname{pf}(B J B^T) = \det(B) \operatorname{pf}(J)$ gives $\det B = 1$.
In the Chern-Gauss-Bonnet theorem, the Pfaffian of the curvature form gives the Euler class.
