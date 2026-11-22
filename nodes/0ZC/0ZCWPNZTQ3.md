---
tag: 0ZCWPNZTQ3
kind: concept
name: Companion matrix
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
specializes: [0JXZKX526R]
uses: [0JXZKX526R, 0C3QBCR46M, 039HF58KQ5, 03NDVCSHSB]
sources:
  - url: https://en.wikipedia.org/wiki/Companion_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Companion_matrix
    locator: Similarity to companion matrix
  - book: isbn:9780135367971
    locator: Section 7.1
same_as:
  wikidata: Q814361
  wikipedia: Companion matrix
inventory: [EGQ8TF53DJ]
---

## Summary

The companion matrix of a polynomial is the simplest matrix whose characteristic polynomial is that polynomial.
It shifts each basis vector to the next one, and the coefficients of the polynomial say where the last basis vector goes.
Let $F$ be a field and let $p = x^n + c_{n-1} x^{n-1} + \cdots + c_1 x + c_0$ be a [[monic polynomial|0C3QBCR46M]] over $F$ of degree $n \ge 1$.
The [[companion matrix|0VH1TC1PWF]] $C(p)$ is the $n \times n$ [[matrix|0JXZKX526R]]
$$C(p) = \begin{pmatrix} 0 & 0 & \cdots & 0 & -c_0 \\ 1 & 0 & \cdots & 0 & -c_1 \\ 0 & 1 & \cdots & 0 & -c_2 \\ \vdots & & \ddots & & \vdots \\ 0 & 0 & \cdots & 1 & -c_{n-1} \end{pmatrix},$$
with ones just below the diagonal and the negated coefficients in the last column.
Equivalently, $C(p) e_i = e_{i+1}$ for $i < n$ and $C(p) e_n = -c_0 e_1 - c_1 e_2 - \cdots - c_{n-1} e_n$.
Its [[characteristic polynomial|039HF58KQ5]] and its [[minimal polynomial|03NDVCSHSB]] are both $p$.

## Motivation

Suppose a linear map $T$ has a [[cyclic vector|42MMQBTP0M]] $v$, and let $n = \dim V$.
In the basis $v, Tv, \dots, T^{n-1} v$, the map moves each basis vector to the next one.
Only the image $T^n v$ of the last vector needs work, and it is a combination of the basis whose coefficients give a monic polynomial $p$ with $p(T) v = 0$.
So the whole matrix of $T$ is fixed by the $n$ numbers $c_0, \dots, c_{n-1}$, and that matrix is $C(p)$.

The construction also runs the other way.
Every monic polynomial is the characteristic polynomial of some matrix, namely its companion matrix, so questions about roots of polynomials become questions about eigenvalues.
Numerical software uses this: the `roots` command of MATLAB finds the roots of a polynomial as the eigenvalues of its companion matrix.
Later in the sub-area, companion matrices are the blocks of the [[rational canonical form|042JWAR3Q0]], so every matrix is built from them.

## Notation

The column version above has ones below the diagonal and the coefficients in the last column.
Many books use its transpose $C(p)^{\mathsf T}$, the row version, with ones above the diagonal and $-c_0, \dots, -c_{n-1}$ in the last row.
Other books put the coefficients in the first row or the first column and move the ones to match.
All versions are [[similar|0E89HQATM8]] to each other, since each one is cyclic with characteristic polynomial $p$.
The symbols $C(p)$, $C_p$ and $\operatorname{Comp}(p)$ are all common, so check the version before you compute.

## Remarks

### Building one from a polynomial

Take $p = x^3 - 2x^2 + 3x - 4$, so $c_0 = -4$, $c_1 = 3$ and $c_2 = -2$.
The last column is $(-c_0, -c_1, -c_2) = (4, -3, 2)$, and so
$$C(p) = \begin{pmatrix} 0 & 0 & 4 \\ 1 & 0 & -3 \\ 0 & 1 & 2 \end{pmatrix}.$$
Expand $\det(xI - C(p))$ along the first row:
$$\det \begin{pmatrix} x & 0 & -4 \\ -1 & x & 3 \\ 0 & -1 & x - 2 \end{pmatrix} = x \bigl( x(x - 2) + 3 \bigr) - 4 \cdot (-1)(-1) = x^3 - 2x^2 + 3x - 4.$$
So the characteristic polynomial is $p$ again, as the [[theorem on companion matrices|XYR7GPH20K]] promises.

### Small cases to know

For degree $1$, $C(x - c) = (c)$.
For $x^2 + 1$ we get the [[quarter turn of the plane|AK9AABZCZM]], $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, with no real eigenvalue.
For $(x - 1)^2 = x^2 - 2x + 1$ we get $\begin{pmatrix} 0 & -1 \\ 1 & 2 \end{pmatrix}$, which is [[similar to the Jordan block $J_2(1)$|6FE9Q55AV1]] and so is not diagonalizable.
The matrix $C(x^n)$ sends $e_i$ to $e_{i+1}$ and $e_n$ to $0$, a nilpotent shift similar to the [[Jordan block|07PH4RX0X5]] $J_n(0)$.
The matrix $C(x^n - 1)$ is the permutation matrix of the cycle $e_1 \mapsto e_2 \mapsto \cdots \mapsto e_n \mapsto e_1$.

### What is not a companion matrix

The [[identity matrix $I_2$|M135QJH5NQ]] is not similar to any companion matrix.
Its minimal polynomial $x - 1$ is shorter than its characteristic polynomial $(x - 1)^2$, while a companion matrix has the two equal.
In the same way $\operatorname{diag}(1, 1, 2)$ fails, because its minimal polynomial $(x - 1)(x - 2)$ has degree $2 < 3$.
A matrix can also fail to be a companion matrix only in form.
For example, $\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ has first column $(1, 1) \ne e_2$, but it is cyclic with cyclic vector $e_1$, so it is similar to $C((x - 1)^2)$.

### The rules you can use

By construction $e_1$ is a cyclic vector, and the [[characteristic and minimal polynomials of $C(p)$ are both $p$|XYR7GPH20K]].
A matrix is similar to a companion matrix [[exactly when its minimal and characteristic polynomials are equal|RK1QVMYW7H]], and then it is similar to $C(\chi_A)$.
The determinant is $\det C(p) = (-1)^n c_0$, so $C(p)$ is invertible exactly when $p(0) \ne 0$.
The eigenvalues of $C(p)$ in $F$ are the roots of $p$ in $F$, and for a root $\lambda$ the row vector $(1, \lambda, \lambda^2, \dots, \lambda^{n-1})$ is a left eigenvector.
Check this for the last column: the row vector times that column is $-c_0 - c_1 \lambda - \cdots - c_{n-1} \lambda^{n-1}$, which equals $\lambda^n$ because $p(\lambda) = 0$.

### Watch out

Do not mix the row and the column versions in one computation, for example the column version for $C(p)$ and the eigenvector formula of the row version.
Do not forget the minus signs.
For $p = x^3 - 2x^2 + 3x - 4$, putting $(c_0, c_1, c_2) = (-4, 3, -2)$ itself into the last column gives the characteristic polynomial $x^3 + 2x^2 - 3x + 4$, which is wrong.
If the polynomial is not monic, divide by its leading coefficient first.

### History

The rational canonical form, whose blocks are companion matrices, is also called the Frobenius normal form, after Georg Frobenius.

### Try it

First, write down $C(x^2 - 5x + 6)$ and find its eigenvalues.
The matrix is $\begin{pmatrix} 0 & -6 \\ 1 & 5 \end{pmatrix}$, with trace $5$ and determinant $6$, so its eigenvalues are the roots $2$ and $3$ of $x^2 - 5x + 6$.

Second, is $C(x^3 + 2x)$ invertible?
No, since $c_0 = 0$ and so $\det C = (-1)^3 \cdot 0 = 0$; indeed $0$ is a root of $x^3 + 2x$ and so an eigenvalue.

## Explanations

### L1 human

A companion matrix is a matrix built from a polynomial.
It pushes each basis vector to the next one, and it sends the last one to a mixture that the coefficients of the polynomial fix.
For the polynomial $x^2 + 1$, the matrix turns the plane by a quarter turn.
Turning twice gives minus the identity, so the matrix satisfies its own polynomial: its square plus the identity is zero.
In this way every polynomial is the characteristic polynomial of some matrix.

### L2 human

Here is a typical use: write the recurrence $u_{k+2} = u_{k+1} + u_k$ of the Fibonacci numbers with a matrix.
The polynomial of the recurrence is $p = x^2 - x - 1$, so $c_0 = -1$ and $c_1 = -1$.
Put the state $(u_k, u_{k+1})$ in a row vector; one step multiplies it on the right by the column version
$$C(p) = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}, \qquad (u_k, u_{k+1}) \, C(p) = (u_{k+1}, u_k + u_{k+1}).$$
Starting from $(0, 1)$ we get $(1, 1)$, then $(1, 2)$, then $(2, 3)$, the Fibonacci numbers.
Check: the characteristic polynomial of $C(p)$ is $x^2 - (\operatorname{tr}) x + \det = x^2 - x - 1 = p$.
So the growth of the sequence is governed by the eigenvalues of $C(p)$, the roots $(1 \pm \sqrt{5})/2$ of $p$.

### L3 human

The companion matrix is the matrix of multiplication by $x$ on $F[x]/(p)$ in the basis $1, x, \dots, x^{n-1}$.
So it is the matrix of a cyclic $F[x]$-module, and the [[cyclic decomposition theorem|R3Z20J19BR]] says that every finite-dimensional $F[x]$-module is a direct sum of such modules.
When $p$ is irreducible, $F[x]/(p)$ is the field $F(\alpha)$ with $p(\alpha) = 0$, and $C(p)$ is the matrix of multiplication by $\alpha$ in the power basis.
In that language the trace and the determinant of $C(p)$ are the field trace and the field norm of $\alpha$.
