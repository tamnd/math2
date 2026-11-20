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

Let $F$ be a field and let $p = x^n + c_{n-1} x^{n-1} + \cdots + c_1 x + c_0$ be a [[monic polynomial|0C3QBCR46M]] over $F$ of degree $n \ge 1$.
The [[companion matrix|0VH1TC1PWF]] $C(p)$ is the $n \times n$ [[matrix|0JXZKX526R]] with $1$ in each position $(i + 1, i)$ just below the diagonal, with last column $(-c_0, -c_1, \dots, -c_{n-1})^{\mathsf T}$, and with $0$ elsewhere.
So $C(p) e_i = e_{i+1}$ for $i < n$, and $C(p) e_n = -c_0 e_1 - \cdots - c_{n-1} e_n$.
Its [[characteristic polynomial|039HF58KQ5]] and its [[minimal polynomial|03NDVCSHSB]] are both $p$.
Companion matrices are the matrices of cyclic endomorphisms, and they are the blocks of the rational canonical form.

## Motivation

Let $T$ have a [[cyclic vector|42MMQBTP0M]] $v$, and let $n = \dim V$.
In the basis $v, Tv, \dots, T^{n-1} v$, the map $T$ moves each basis vector to the next one.
The image $T^n v$ of the last one is a combination of the basis, and the coefficients of this combination give a monic polynomial $p$ with $p(T) v = 0$.
So the whole matrix of $T$ is fixed by the $n$ coefficients of $p$, and this matrix is $C(p)$.
Conversely, every monic polynomial is the characteristic polynomial of a matrix, namely its companion matrix.

## Notation

This page uses the column version: ones below the diagonal and the coefficients in the last column.
Other books use the transpose $C(p)^{\mathsf T}$, the row version, with ones above the diagonal and the coefficients in the last row.
Further variants put the coefficients in the first row or the first column, with the ones moved to match.
All versions are [[similar|0E89HQATM8]] to each other, since each one is cyclic with characteristic polynomial $p$.
The symbols $C(p)$, $C_p$ and $\operatorname{Comp}(p)$ are common.

## Remarks

### Examples

- $C(x - c) = (c)$, a $1 \times 1$ matrix.
- $C(x^2 + 1) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, the [[rotation by a quarter turn|AK9AABZCZM]].
- $C((x - 1)^2) = \begin{pmatrix} 0 & -1 \\ 1 & 2 \end{pmatrix}$, which is [[similar to the Jordan block $J_2(1)$|6FE9Q55AV1]].
- $C(x^n)$ is the nilpotent matrix with $e_i \mapsto e_{i+1}$ and $e_n \mapsto 0$, similar to the [[Jordan block|07PH4RX0X5]] $J_n(0)$.
- $C(x^n - 1)$ is the permutation matrix of the cycle $e_1 \mapsto e_2 \mapsto \cdots \mapsto e_n \mapsto e_1$.

### Non-examples

- The [[identity matrix $I_2$|M135QJH5NQ]] is not similar to any companion matrix, since its minimal polynomial $x - 1$ differs from its characteristic polynomial $(x - 1)^2$.
- $\operatorname{diag}(1, 1, 2)$ is not similar to a companion matrix: its minimal polynomial $(x - 1)(x - 2)$ has degree $2 < 3$.
- The matrix $\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ is not itself a companion matrix in the column version, since its first column is not $e_2$. It is similar to $C((x - 1)^2)$, since it is cyclic with cyclic vector $e_1$.

### Basic properties

- [[The characteristic and the minimal polynomial of $C(p)$ are both $p$|XYR7GPH20K]], and $e_1$ is a cyclic vector.
- If $v$ is a cyclic vector of $T$, the matrix of $T$ in the basis $v, Tv, \dots, T^{n-1} v$ is $C(\chi_T)$, by the [[lemma on cyclic subspaces|5VYBJYPYMW]].
- A matrix is similar to a companion matrix [[if and only if its minimal and characteristic polynomials are equal|RK1QVMYW7H]].
- $C(p)$ is invertible if and only if $c_0 = p(0) \ne 0$, since $\det C(p) = (-1)^n c_0$.
- The eigenvalues of $C(p)$ in $F$ are the roots of $p$ in $F$; for a root $\lambda$, the row vector $(1, \lambda, \lambda^2, \dots, \lambda^{n-1})$ is a left eigenvector.
- Every [[matrix is similar to a block diagonal matrix of companion matrices|042JWAR3Q0]], its rational canonical form.

### History

The rational canonical form, whose blocks are companion matrices, is also called the Frobenius normal form.
Numerical software, for example the `roots` function of MATLAB, computes the roots of a polynomial as the eigenvalues of its companion matrix.

### Common errors

- Mixing the row and the column versions in one computation, for example the column version for $C(p)$ and the row version for its eigenvectors.
- Forgetting the minus signs: the last column is $-c_0, \dots, -c_{n-1}$, not $c_0, \dots, c_{n-1}$.
- Using a polynomial that is not monic: first divide by the leading coefficient.

## Explanations

### L1 human

A companion matrix is a matrix built from a polynomial.
It pushes each basis vector to the next one, and it sends the last one to a mixture that is fixed by the coefficients of the polynomial.
For the polynomial $x$ squared plus one, the matrix turns the plane by a quarter turn.
Its characteristic polynomial is the polynomial that we started with.
So every polynomial "is" the characteristic polynomial of some matrix.

### L2 human

We build $C(p)$ for $p = x^3 - 2x^2 + 3x - 4$ and check its characteristic polynomial.

1. The coefficients are $c_0 = -4$, $c_1 = 3$, $c_2 = -2$, so the last column is $(4, -3, 2)$.
2. So $C(p) = \begin{pmatrix} 0 & 0 & 4 \\ 1 & 0 & -3 \\ 0 & 1 & 2 \end{pmatrix}$.
3. $\det(xI - C(p)) = \det \begin{pmatrix} x & 0 & -4 \\ -1 & x & 3 \\ 0 & -1 & x - 2 \end{pmatrix}$.
4. Expanding along the first row gives $x\,(x(x - 2) + 3) - 4\,((-1)(-1) - 0) = x^3 - 2x^2 + 3x - 4$.

The typical use is to turn a polynomial question into a matrix question, for example to find the roots of $p$ as eigenvalues.
The trap is the sign: with the coefficients $c_i$ in place of $-c_i$, the characteristic polynomial becomes $x^3 + 2x^2 - 3x + 4$ for this example.

### L3 human

The companion matrix is the matrix of multiplication by $x$ on $F[x]/(p)$ in the basis $1, x, \dots, x^{n-1}$.
So it is the matrix of a cyclic $F[x]$-module, and every finite-dimensional $F[x]$-module is a direct sum of such modules by the [[cyclic decomposition theorem|R3Z20J19BR]].
When $p$ is irreducible, $F[x]/(p)$ is the field $F(\alpha)$, and $C(p)$ is the matrix of multiplication by $\alpha$ in the power basis.
Linear recurrences $u_{k+n} = -c_{n-1} u_{k+n-1} - \cdots - c_0 u_k$ are governed by the row version of $C(p)$, and the shift on the solution space is cyclic.
