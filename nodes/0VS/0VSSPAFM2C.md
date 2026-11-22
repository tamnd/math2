---
tag: 0VSSPAFM2C
kind: concept
name: Characteristic polynomial
msc: ["15A15", "15A18"]
topics: [6R1D6QPY3S]
audience: ug2
uses: [00KDZRW4C0, 0JXZKX526R, 0Q9EZS90GY, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Formal definition
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: History
  - book: isbn:9780134860244
  - book: isbn:9780135367971
same_as:
  wikidata: Q849705
  wikipedia: Characteristic polynomial
---

## Summary

The characteristic polynomial turns the search for eigenvalues into the search for roots of one polynomial.
You put a variable $t$ on the diagonal, take a determinant, and the eigenvalues are the values of $t$ that make it zero.
Let $K$ be a commutative ring, let $n \ge 1$, and let $A$ be an $n \times n$ matrix over $K$.
The *characteristic polynomial* of $A$ is
$$p_A(t) = \det(t I_n - A),$$
the [[determinant|00KDZRW4C0]] of a matrix with entries in the [[polynomial ring|0Q9EZS90GY]] $K[t]$.
It is monic of degree $n$, and over a field its roots in the field are exactly the [[eigenvalues|0BQAA2BK3Q]] of $A$.
The [[formal definition|039HF58KQ5]] states it.

## Motivation

A scalar $\lambda$ is an eigenvalue of $A$ when $Av = \lambda v$ for some $v \ne 0$.
That equation has two unknowns, and it is not linear in the pair $(\lambda, v)$.
The determinant removes $v$: over a field, a nonzero solution $v$ exists exactly when $\lambda I - A$ is singular, that is, when $\det(\lambda I - A) = 0$.
If we write a variable $t$ in place of $\lambda$, this condition becomes one polynomial equation $p_A(t) = 0$ of degree $n$.

The polynomial carries more than its roots.
Its coefficients give the trace and the determinant, the multiplicities of its roots give the [[algebraic multiplicities|0FY42N02DV]], and by the [[Cayley-Hamilton theorem|0F765KFC2J]] the matrix itself is a root, $p_A(A) = 0$.
The same polynomial measures the stability of linear differential equations and recurrences, through the real parts or the absolute values of its roots.
Later sub-areas use it to decide when a matrix is diagonalizable and to build the Jordan form.

## Notation

Books write $p_A$, $\chi_A$, $c_A$ or $P_A$.
Mathlib writes `Matrix.charpoly A`, and `LinearMap.charpoly f` for an endomorphism.
For a linear map of a finite-dimensional space, the [[characteristic polynomial of the map|0J5EMJRRFM]] is $p_A$ for any matrix $A$ of the map.

Watch out for the sign convention.
We use $\det(t I - A)$, which is monic, and so does Mathlib.
Many textbooks, for example Lay and Strang, use $\det(A - t I)$ instead.
The two differ by a factor $(-1)^n$, because each of the $n$ rows changes sign:
$$\det(A - tI) = (-1)^n \det(tI - A).$$
So they agree for even $n$ and differ in sign for odd $n$, as the [[3 by 3 example of det(A - tI)|BCF4Z6BN0C]] shows.
The roots are the same in both conventions, but the coefficient formulas below hold only for $\det(tI - A)$.

## Remarks

### A first computation

Take $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.
Subtract $A$ from $t I$, which puts $t - a_{ii}$ on the diagonal and $-a_{ij}$ off it, and take the determinant:
$$p_A(t) = \det \begin{pmatrix} t - 1 & -2 \\ -3 & t - 4 \end{pmatrix} = (t - 1)(t - 4) - 6 = t^2 - 5t - 2.$$
The same pattern for a general $2 \times 2$ matrix gives
$$\det \begin{pmatrix} t - a & -b \\ -c & t - d \end{pmatrix} = t^2 - (a + d)\, t + (ad - bc),$$
so $p_A(t) = t^2 - (\operatorname{tr} A)\, t + \det A$.
Check: $\operatorname{tr} A = 5$ and $\det A = 4 - 6 = -2$, which gives $t^2 - 5t - 2$ again.
The roots are $\tfrac{1}{2}(5 \pm \sqrt{33})$, so this $A$ has two real eigenvalues.

### More examples

[[The 3 by 3 matrix with 4 on the diagonal and 1 elsewhere|7XFGVVTZ2X]] has
$$p_A(t) = t^3 - 12t^2 + 45t - 54 = (t - 3)^2 (t - 6),$$
so its eigenvalues are $3$, twice, and $6$.
Check: $(t^2 - 6t + 9)(t - 6) = t^3 - 12t^2 + 45t - 54$.

[[A real matrix with complex eigenvalues|XGRN8RY29P]], with rows $(3, -2)$ and $(4, -1)$, has trace $2$ and determinant $5$, so $p_A(t) = t^2 - 2t + 5$.
Its roots $1 \pm 2i$ are not real, so over $\mathbb{R}$ the matrix has no eigenvalue at all.
In the same way, [[the rotation of the plane by an angle theta|5AE98D7959]] has $p(t) = t^2 - 2 \cos\theta \, t + 1$, with real roots only when $\theta$ is a multiple of $\pi$.

For a [[triangular matrix|NHR1K0GPS1]], $tI - A$ is triangular too, so $p_A(t) = \prod_i (t - a_{ii})$ by the [[determinant of a triangular matrix|0K1KKMFHYH]].
Every monic polynomial of degree $n \ge 1$ arises: the [[companion matrix|0ZCWPNZTQ3]] of $f$ has characteristic polynomial $f$.

### What it is not

The polynomial $\det(A - tI)$ is not $p_A$ for odd $n$.
For $A = \operatorname{diag}(1, 2, 3)$ it is $-t^3 + 6t^2 - 11t + 6$, with leading coefficient $-1$; the [[sign non-example|BCF4Z6BN0C]] works it out.

The product $\prod_i (t - a_{ii})$ of the diagonal factors is $p_A$ for a triangular matrix, but not in general.
For $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ the diagonal gives $t^2$, but $p_A(t) = t^2 - 1$.

### The rules you can use

The polynomial is monic of degree $n$, the coefficient of $t^{n-1}$ is $-\operatorname{tr} A$, and the constant term is $(-1)^n \det A$, by the theorem on the [[coefficients of the characteristic polynomial|0FRYPZ6D0X]].
Similar matrices have the same characteristic polynomial, because $tI - P^{-1}AP = P^{-1}(tI - A)P$; the [[invariance theorem|0TYMASG33Y]] proves it.
A matrix and its transpose have the same polynomial, since $\det$ does not change under transposition.
Over a field, the roots of $p_A$ in the field are the eigenvalues, by the theorem that [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]].
For square $A$ and $B$, the theorem on the [[eigenvalues of AB and BA|MCXV71BY74]] gives $p_{AB} = p_{BA}$.
A block upper triangular matrix has the product of the polynomials of its diagonal blocks, by the theorem on the [[characteristic polynomial of an endomorphism|C98TZ6ZAXC]].

### Watch out

Three mistakes are common.
The first is to subtract $t$ from every entry, or to compute $\det A - t$; only the diagonal entries change.
The second is to "prove" the Cayley-Hamilton theorem by putting $t = A$ into $\det(tI - A)$.
That gives $\det(A - A) = 0$, a scalar, while $p_A(A)$ is a matrix, so the substitution proves nothing.

The third is to think that $p_A$ determines $A$ up to similarity.
The matrices $I_2$ and $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ both have $p(t) = (t - 1)^2$.
They are not similar, since the only matrix similar to $I_2$ is $P^{-1} I_2 P = I_2$.

### History

Cauchy used the term "racine caractéristique", characteristic root, for the roots of this polynomial.
Cayley, in his memoir on matrices of 1858, stated that a matrix satisfies its own characteristic equation.

### Try it

First, find $p_A$ for $A = \begin{pmatrix} 2 & 7 \\ 0 & -3 \end{pmatrix}$.
The matrix is triangular, so $p_A(t) = (t - 2)(t + 3) = t^2 + t - 6$; check: $-\operatorname{tr} A = -(-1) = 1$ and $\det A = -6$.

Second, a $3 \times 3$ matrix has $\det(A - tI) = -t^3 + 4t^2 - t + 7$; find $p_A$.
Multiply by $(-1)^3 = -1$ to get $p_A(t) = t^3 - 4t^2 + t - 7$.

## Explanations

### L1 human

To find the eigenvalues of a square matrix, we look for the numbers $\lambda$ that make $\lambda I - A$ fail to have an inverse.
The determinant is the test, since a matrix fails to have an inverse exactly when its determinant is zero.
If we leave $\lambda$ as an unknown letter $t$, the determinant becomes a polynomial in $t$.
For the matrix with rows $(2, 0)$ and $(0, 5)$ it is $(t - 2)(t - 5)$.
Its roots $2$ and $5$ are the eigenvalues, the factors by which the matrix stretches its two axes.

### L2 human

Here is a typical use: find the eigenvalues of
$$A = \begin{pmatrix} 2 & 0 & 1 \\ 0 & 3 & 0 \\ 1 & 0 & 2 \end{pmatrix}.$$
Expand $\det(tI - A)$ along the second row, which has only one nonzero entry:
$$p_A(t) = (t - 3) \det \begin{pmatrix} t - 2 & -1 \\ -1 & t - 2 \end{pmatrix} = (t - 3)\big((t - 2)^2 - 1\big) = (t - 3)(t - 1)(t - 3).$$
So $p_A(t) = (t - 1)(t - 3)^2$, and the eigenvalues are $1$ and $3$, with $3$ a double root.
Check: the roots add up to $1 + 3 + 3 = 7 = \operatorname{tr} A$, and their product is $9$, while $\det A = 3(4 - 1) = 9$.
For $\lambda = 1$, the vector $(1, 0, -1)$ gives $A(1, 0, -1) = (1, 0, -1)$, as it should.
The typical pattern is to expand along a row or column with many zeros, factor, and then check with the trace and the determinant.

### L3 human

For an endomorphism $T$ of a free module $V$ of rank $n$ over a commutative ring $K$, the characteristic polynomial is the determinant of $t - T$ acting on $K[t] \otimes_K V$, and it needs no basis.
Over a field, $V$ becomes a module over $F[t]$, and $p_T$ is the product of its invariant factors, while the [[minimal polynomial|03NDVCSHSB]] is the largest one; see [[modules over a principal ideal domain|WKJXXX0DYG]].
When $p_A$ splits into linear factors, its coefficients are, up to sign, the [[elementary symmetric polynomials|0X5QVCF06N]] of the eigenvalues.
In field theory, the [[minimal polynomial of an algebraic element|0VX9EP2GS8]] $\alpha$ divides the characteristic polynomial of multiplication by $\alpha$, and the norm and trace of $\alpha$ are coefficients of that polynomial.
