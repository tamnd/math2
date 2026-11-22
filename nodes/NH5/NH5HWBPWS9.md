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

The determinant of an alternating matrix of even size is always the square of a polynomial in its entries, and the Pfaffian is that polynomial.
It is a square root of the determinant with a sign that comes from a formula, not from a choice.
For an alternating $2n \times 2n$ matrix $A$ over a commutative ring, which means $a_{ji} = -a_{ij}$ and $a_{ii} = 0$, the Pfaffian is a signed sum over the [[perfect matchings|0NHK9MFFW9]] of $\{1, \dots, 2n\}$:
$$\operatorname{pf}(A) = \sum_{M} \operatorname{sgn}(\pi_M) \prod_{\{i, j\} \in M,\ i < j} a_{ij},$$
where $\pi_M$ is the permutation that lists the pairs of $M$ in order, as the [[definition|C9JJD2AVJR]] explains.
Its two main rules are $\operatorname{pf}(A)^2 = \det A$ and $\operatorname{pf}(B A B^{\mathsf{T}}) = \det(B) \operatorname{pf}(A)$.

## Motivation

The determinant of a real [[skew-symmetric matrix|0PBY4E9GQF]] of even size is never negative, and for integer entries it is always a perfect square.
For size $2$ we see why: $\det \begin{pmatrix} 0 & a \\ -a & 0 \end{pmatrix} = a^2$.
So we expect a square root that is itself a polynomial in the entries, and the Pfaffian is that square root.
It is also much shorter than the determinant: for size $4$ it has $3$ terms, while the [[determinant|00KDZRW4C0]] has $24$.

The Pfaffian appears wherever alternating forms appear.
It decides whether an alternating form is nondegenerate, it shows that symplectic matrices have determinant $1$, and it counts the perfect matchings of planar graphs in the [[FKT algorithm|A6SPEDH8BK]].
In geometry, the Pfaffian of a curvature form gives the [[Euler class|BJX6QS0ANT]] in the [[Chern-Gauss-Bonnet theorem|GG6NYPKMHX]].

## Notation

Books write $\operatorname{pf}(A)$ or $\operatorname{Pf}(A)$.
The standard symplectic matrix is written $J$, but two versions are common: $\begin{pmatrix} 0 & I_n \\ -I_n & 0 \end{pmatrix}$, and the matrix with blocks $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ on the diagonal.
For $n = 2$ their Pfaffians are $-1$ and $1$, as the [[example in two orders|65Q3YWX09Q]] shows, so read the convention of a book before you trust a sign.

## Remarks

### The first two sizes

For a $2 \times 2$ alternating matrix there is one matching, $\{\{1, 2\}\}$, so
$$\operatorname{pf} \begin{pmatrix} 0 & a \\ -a & 0 \end{pmatrix} = a, \qquad \det \begin{pmatrix} 0 & a \\ -a & 0 \end{pmatrix} = a^2.$$
For a $4 \times 4$ alternating matrix there are three matchings, $\{12, 34\}$, $\{13, 24\}$ and $\{14, 23\}$, with signs $+1$, $-1$ and $+1$:
$$\operatorname{pf}(A) = a_{12} a_{34} - a_{13} a_{24} + a_{14} a_{23}.$$
With $a_{12} = 1$, $a_{13} = 2$, $a_{14} = 3$, $a_{23} = 4$, $a_{24} = 5$ and $a_{34} = 6$, this gives $6 - 10 + 12 = 8$.
The [[worked integer example|M0JEPXXWQM]] then checks $\det A = 64 = 8^2$ by a Laplace expansion.

### The rules you can use

The square rule $\operatorname{pf}(A)^2 = \det A$ is the [[theorem on the square of the Pfaffian|473MBZST4D]].
It shows that an alternating matrix over a field is invertible exactly when its Pfaffian is nonzero.

The change of basis rule $\operatorname{pf}(B A B^{\mathsf{T}}) = \det(B) \operatorname{pf}(A)$ holds for every $2n \times 2n$ matrix $B$.
Squaring it gives the familiar $\det(B A B^{\mathsf{T}}) = (\det B)^2 \det A$, so the Pfaffian is the finer invariant.

Scaling is simple, because each term has $n$ factors: $\operatorname{pf}(\lambda A) = \lambda^n \operatorname{pf}(A)$.
Since $A^{\mathsf{T}} = -A$, this gives $\operatorname{pf}(A^{\mathsf{T}}) = (-1)^n \operatorname{pf}(A)$.
For odd size there are no perfect matchings, the Pfaffian is $0$ by convention, and the matrix is [[singular|55RX9C0ZTH]], so the square rule still holds.

### What it is not

The Pfaffian is defined only for alternating matrices.
The symmetric matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ over $\mathbb{R}$ fails the condition $a_{21} = -a_{12}$, and its determinant $-1$ has no real square root, as the [[symmetric non-example|Z172P2ZBQ8]] shows.
A matrix with a nonzero diagonal entry fails the condition $a_{ii} = 0$; over a field of characteristic other than $2$ such a matrix is not skew-symmetric either.

### Counting matchings with signs

Take the square graph with vertices $1, 2, 3, 4$ and edges $12$, $23$, $34$ and $14$.
It has two perfect matchings, $\{12, 34\}$ and $\{14, 23\}$.
Put $a_{ij} = 1$ for each edge $ij$ with $i < j$ and $a_{ij} = 0$ for the other pairs with $i < j$, and complete $A$ to an alternating matrix.
The formula gives
$$\operatorname{pf}(A) = 1 \cdot 1 - 0 \cdot 0 + 1 \cdot 1 = 2,$$
the number of perfect matchings.
If we put $a_{14} = -1$ instead, the formula gives $1 - 0 - 1 = 0$.
So the signs of the entries matter, and for a planar graph the FKT algorithm chooses them so that all matchings count with the same sign.

### Watch out

The Pfaffian is not $\sqrt{\det A}$ with a sign chosen by you.
For $J = \begin{pmatrix} 0 & I_2 \\ -I_2 & 0 \end{pmatrix}$ the determinant is $1$ but the Pfaffian is $-1$.
Its sign changes when two basis vectors are exchanged, because $\det B = -1$ for the permutation matrix $B$ of an exchange.
A second trap is the middle term of the $4 \times 4$ formula: the matching $\{13, 24\}$ comes with the sign $-1$.

### History

The name honors the German mathematician Johann Friedrich Pfaff.

### Try it

First, find the Pfaffian and the determinant of $\begin{pmatrix} 0 & -3 \\ 3 & 0 \end{pmatrix}$.
The Pfaffian is $a_{12} = -3$, and the determinant is $0 \cdot 0 - (-3) \cdot 3 = 9 = (-3)^2$.

Second, a $4 \times 4$ alternating matrix has $a_{12} = 2$, $a_{34} = 3$ and all other entries above the diagonal $0$.
What is the Pfaffian of $5A$?
The Pfaffian of $A$ is $2 \cdot 3 = 6$, and $\operatorname{pf}(5A) = 5^2 \cdot 6 = 150$.

## Explanations

### L1 human

Write the numbers $1$ to $4$ and split them into two pairs.
There are three ways: $\{1, 2\}$ with $\{3, 4\}$, $\{1, 3\}$ with $\{2, 4\}$, and $\{1, 4\}$ with $\{2, 3\}$.
For each way, multiply the two matrix entries that the pairs pick out, and add the three products with the signs $+$, $-$, $+$.
That number is the Pfaffian, and its square is the determinant of the matrix.
For the $2 \times 2$ matrix with entries $0, a, -a, 0$ there is only one pairing, and the Pfaffian is $a$.

### L2 human

Here is a typical use: show that every real $4 \times 4$ symplectic matrix has determinant $1$.
A matrix $B$ is symplectic when $B J' B^{\mathsf{T}} = J'$, where $J'$ has the blocks $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ on its diagonal.
The $4 \times 4$ formula gives $\operatorname{pf}(J') = a_{12} a_{34} = 1 \cdot 1 = 1$.
Take the Pfaffian of both sides and use the change of basis rule:
$$\det(B) \cdot \operatorname{pf}(J') = \operatorname{pf}(B J' B^{\mathsf{T}}) = \operatorname{pf}(J').$$
Since $\operatorname{pf}(J') = 1$, this gives $\det B = 1$.
The determinant alone would only give $(\det B)^2 = 1$, so $\det B = \pm 1$.
The problem shows what the Pfaffian adds: it remembers the sign that the determinant loses.

### L3 human

An alternating matrix $A$ defines the $2$-form $\omega = \sum_{i < j} a_{ij}\, e_i \wedge e_j$ in the [[exterior algebra|0MDMZ965VE]].
Its $n$-th power is $\omega^n = n! \operatorname{pf}(A)\, e_1 \wedge \dots \wedge e_{2n}$, which defines the Pfaffian without matchings and proves the change of basis rule, since $B$ multiplies the top power by $\det B$.
Over a field, an [[alternating bilinear form|0DGDS5XY84]] has a basis in which its matrix is a sum of blocks $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ and zeros, and the square rule follows from this normal form.
On a [[symplectic vector space|PQ7JJY0VPH]] the Pfaffian of the form gives a canonical volume, and for vector bundles the Pfaffian of the curvature gives the Euler class.
The Pfaffian of a matrix of indeterminates has integer coefficients, so it is defined over every commutative ring.
