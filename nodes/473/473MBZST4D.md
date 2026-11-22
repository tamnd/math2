---
tag: 473MBZST4D
kind: statement
role: theorem
name: The square of the Pfaffian is the determinant
msc: ["15A15"]
topics: [DTBK11SR77]
audience: grad
uses: [C9JJD2AVJR, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Pfaffian
  - url: https://en.wikipedia.org/wiki/Pfaffian
    locator: lead section
---

## Statement

The determinant of an alternating matrix of even size is the square of its Pfaffian, so it is the square of a polynomial in the entries.

Let $K$ be a commutative ring, let $n \ge 1$, and let $A$ be an alternating $2n \times 2n$ matrix over $K$, which means $a_{ji} = -a_{ij}$ and $a_{ii} = 0$ for all $i, j$.
Then
$$\operatorname{pf}(A)^2 = \det A,$$
where $\operatorname{pf}$ is the [[Pfaffian|C9JJD2AVJR]] and $\det$ is the [[determinant|0C3CFHDN6R]].

## Remarks

### Two quick checks

For size $2$ the theorem says $a^2 = \det \begin{pmatrix} 0 & a \\ -a & 0 \end{pmatrix}$, and the determinant is $0 \cdot 0 - a \cdot (-a) = a^2$.
For size $4$, the [[integer example|M0JEPXXWQM]] with entries $1, 2, 3, 4, 5, 6$ above the diagonal has
$$\operatorname{pf}(A) = 1 \cdot 6 - 2 \cdot 5 + 3 \cdot 4 = 8,$$
and a Laplace expansion gives $\det A = 64 = 8^2$.
The [[proof for sizes 2 and 4|5G56J9G502]] does the size $4$ case with letters.

### Why each hypothesis is needed

The matrix must be alternating, since the Pfaffian is defined only for such matrices, and the conclusion fails for other matrices.
The symmetric matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ over $\mathbb{R}$ has determinant $-1$, which is not the square of any real number, as the [[symmetric non-example|Z172P2ZBQ8]] shows.

The size must be even for the theorem to say something.
For odd size the Pfaffian is $0$ by convention, and an alternating matrix of odd size has determinant $0$ by the [[theorem on odd size|55RX9C0ZTH]], so the identity holds there as $0 = 0$.

### What it gives you

Over $\mathbb{R}$, the determinant of a skew-symmetric matrix is a square, so it is never negative.
Over $\mathbb{Z}$, the determinant of an alternating integer matrix is a perfect square, such as $64$ above.
Over a field, an alternating matrix is invertible exactly when its Pfaffian is nonzero, and the Pfaffian is a polynomial of degree $n$ rather than $2n$.

### The converse

A matrix whose determinant is a square need not be alternating.
For example, $I_2$ has $\det I_2 = 1 = 1^2$, but its diagonal entries are not $0$.

### Generalizations

For every $2n \times 2n$ matrix $B$ over $K$, the Pfaffian satisfies $\operatorname{pf}(B A B^{\mathsf{T}}) = \det(B) \operatorname{pf}(A)$.
Let $J$ be the matrix with blocks $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ on the diagonal, so that $\operatorname{pf}(J) = 1$.
Then the rule gives $\operatorname{pf}(B J B^{\mathsf{T}}) = \det B$, and squaring gives back the theorem for every matrix of the form $B J B^{\mathsf{T}}$.

## History

The Pfaffian is named after Johann Friedrich Pfaff.

## Explanations

### L1 human

The determinant of an alternating matrix of even size is always a perfect square.
It is the square of a shorter formula in the same entries, the Pfaffian.
For the $2 \times 2$ matrix with entries $0, a, -a, 0$, the Pfaffian is $a$ and the determinant is $a^2$.

### L2 human

Here is a typical use: is the matrix $A$ with entries $a_{12} = 1$, $a_{13} = 2$, $a_{14} = 3$, $a_{23} = 4$, $a_{24} = 6$, $a_{34} = 8$ above the diagonal, and the negatives below, invertible over $\mathbb{R}$?
The $4 \times 4$ Pfaffian formula gives
$$\operatorname{pf}(A) = a_{12} a_{34} - a_{13} a_{24} + a_{14} a_{23} = 8 - 12 + 12 = 8.$$
So $\det A = 64 \ne 0$, and $A$ is invertible.
If we change $a_{24}$ to $10$, the Pfaffian becomes $8 - 20 + 12 = 0$, so the new matrix is singular.
Three products of two numbers replace a $4 \times 4$ determinant, and that is the typical gain.
Watch out: $\operatorname{pf}(A)$ is not $\sqrt{\det A}$ with a sign of your choice, since its sign is fixed by the formula and can be negative.

### L3 human

A general proof works with the alternating matrix of indeterminates over $\mathbb{Z}[x_{ij} : i < j]$.
Over its field of fractions, a nondegenerate alternating form has a symplectic basis, so the matrix equals $B J B^{\mathsf{T}}$ for an invertible $B$, and both sides equal $(\det B)^2$.
This proves the identity of polynomials, and it then holds over every commutative ring by substitution.
In the exterior algebra, the Pfaffian is the coefficient in $\omega^n = n! \operatorname{pf}(A)\, e_1 \wedge \dots \wedge e_{2n}$ for the $2$-form $\omega = \sum_{i < j} a_{ij}\, e_i \wedge e_j$, and the theorem compares this top power with the determinant of the form.
