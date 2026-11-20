---
tag: 0NEGN5CRSC
kind: concept
name: Self-adjoint operator
aliases: [hermitian-operator]
msc: ["47B15", "15B57"]
topics: [3YM9EK6VMB]
audience: ug1
specializes: [0C8BR8XRTR]
uses: [0R9NMSM1ZP, 0ST8QF9T3T, 0J7H0YBFDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Self-adjoint_operator
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780134860244
    locator: Section 6.4
same_as:
  wikidata: Q6500908
  wikipedia: Self-adjoint operator
---

## Summary

A self-adjoint operator on a finite-dimensional inner product space is a linear map $T \colon V \to V$ that equals its [[adjoint|0R9NMSM1ZP]], so $T^* = T$.
The [[formal definition|0MB8HQW495]] states this condition.
Self-adjoint operators are the operators that are the same on both sides of the inner product: $\ip{Tv}{w} = \ip{v}{Tw}$.
They matter because the real spectral theorem describes them completely: they have real eigenvalues and an orthonormal basis of eigenvectors.

## Motivation

A real symmetric matrix $A$ satisfies $(Ax) \cdot y = x \cdot (Ay)$ for all vectors $x$ and $y$.
Symmetric matrices appear as Hessians, as covariance matrices and as matrices of quadratic forms.
In all these cases, the important facts are that the eigenvalues are real and that the eigenvectors can be chosen orthonormal.
The self-adjoint operator is the version of a symmetric matrix that needs no basis.
Over $\mathbb{C}$, the same role belongs to the [[Hermitian matrices|0P17NGQQMQ]] $A^* = A$, and in quantum mechanics the observables are self-adjoint operators.

## Notation

- An operator with $T^* = T$ is called self-adjoint or Hermitian. In Mathlib, `LinearMap.IsSymmetric` is the condition $\ip{Tv}{w} = \ip{v}{Tw}$.
- Terms for matrices. A real matrix with $A^T = A$ is [[symmetric|0VR671PHE5]], and a complex matrix with $A^* = A$ is [[Hermitian|0P17NGQQMQ]].
- Warning: some books call a self-adjoint operator on a complex space "symmetric", and some call complex Hermitian matrices "symmetric". A complex matrix with $A^T = A$ is a different thing, see [[a complex symmetric matrix that is not Hermitian|DAZBNZXZK7]].
- Warning: in functional analysis, a [[symmetric operator|H971WGMV6C]] is an unbounded operator with $\ip{Tv}{w} = \ip{v}{Tw}$ only on a domain. It need not be self-adjoint.
- An operator with $T^* = -T$ is skew-adjoint. A real matrix with $A^T = -A$ is skew-symmetric, and a complex matrix with $A^* = -A$ is skew-Hermitian.

## Remarks

### Examples

- [[The Hermitian matrix with entries $1$, $2i$, $-2i$, $1$|4119199XBW]] has the real eigenvalues $3$ and $-1$ and an orthonormal eigenbasis.
- [[A real symmetric $3 \times 3$ matrix|2P021RCC4Y]] with the eigenvalues $3$, $4$ and $6$.
- [[A Hermitian $2 \times 2$ matrix|GGFA8S4NZ2]] and its real eigenvalues.
- Every [[orthogonal projection|0Q8HZTJC7G]] $P$ onto a subspace $U$ is self-adjoint. Indeed, $\ip{Pv}{w} = \ip{Pv}{Pw} = \ip{v}{Pw}$, because $v - Pv$ and $w - Pw$ are orthogonal to $U$.
- For every linear map $S \colon V \to W$, the operators $S^* S$ on $V$ and $S S^*$ on $W$ are self-adjoint, since $(S^* S)^* = S^* S^{**} = S^* S$.

### Non-examples

- [[The rotation by a right angle|1CF483TZZA]] has $R^* = -R$. It is normal, but not self-adjoint, and its eigenvalues are $\pm i$.
- [[The complex symmetric matrix|DAZBNZXZK7]] with $A^T = A$ but $A^* \neq A$ is not self-adjoint for the standard inner product on $\mathbb{C}^2$.
- [[The real rotation with zero quadratic form|VMHPYDZERM]] has only real values $\ip{Rv}{v} = 0$, but it is not self-adjoint. Over $\mathbb{R}$, real values of the quadratic form do not imply self-adjointness.
- A symmetric matrix is not self-adjoint for every inner product. [[The weighted inner product example|CPQB5HABC6]] shows this.

### Basic properties

- If $S$ and $T$ are self-adjoint and $a \in \mathbb{R}$, then $S + T$ and $aT$ are self-adjoint. So the self-adjoint operators form a real vector space. Over $\mathbb{C}$ it is not a complex vector space, because $(iT)^* = -iT$.
- If $S$ and $T$ are self-adjoint, then $ST$ is self-adjoint if and only if $ST = TS$. The reason: $(ST)^* = T^* S^* = TS$.
- Over $\mathbb{C}$, $T$ is self-adjoint if and only if $\ip{Tv}{v}$ is real for all $v$. This is [[the quadratic form statement|WAYMK9GR5S]], which fails over $\mathbb{R}$.
- [[The eigenvalues are real|0C4NT4GT3X]], and [[eigenvectors for distinct eigenvalues are orthogonal|0JHGAV9H25]].
- [[The real spectral theorem|06J4PXRG22]]: on a real space, $T$ is self-adjoint if and only if $V$ has an orthonormal basis of eigenvectors of $T$. On a complex space, $T$ is self-adjoint if and only if it has an orthonormal eigenbasis and all eigenvalues are real.
- [[The Rayleigh quotient|06WHP8SE98]] of $T$ has the largest eigenvalue as its maximum and the smallest eigenvalue as its minimum, by [[the extreme value statement|T7MFPSY009]].
- Cartesian decomposition. Over $\mathbb{C}$, every operator is $T = A + iB$ with $A = \tfrac{1}{2}(T + T^*)$ and $B = \tfrac{1}{2i}(T - T^*)$ both self-adjoint. The pair $A$, $B$ is unique, and $T$ is [[normal|0C8BR8XRTR]] if and only if $AB = BA$.
- An operator $T$ is skew-adjoint if and only if $iT$ is self-adjoint, because $(iT)^* = -iT^*$.

### History

Hermitian matrices are named after Hermite, who showed in 1855 that they have real eigenvalues, like real symmetric matrices.
This fact is from the Wikipedia article on Hermitian matrices.
The general [[spectral theorem|06J4PXRG22]] has its own history, and the [[spectral theorem for unbounded self-adjoint operators|18KPYRRPZY]] belongs to functional analysis.

### Common errors

- Students think that a complex matrix with $A^T = A$ is self-adjoint. For the standard inner product on $\mathbb{C}^n$ the condition is $A^* = A$, with conjugation.
- Students test self-adjointness with the matrix in a basis that is not orthonormal. The matrix of a self-adjoint operator in such a basis need not be symmetric.
- Students conclude $T = 0$ from $\ip{Tv}{v} = 0$ for all $v$ on a real space. This needs $T$ self-adjoint, as [[the rotation counterexample|VMHPYDZERM]] shows.
- Students think that the product of two self-adjoint operators is self-adjoint. This holds only when they commute. For example, $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, which is not symmetric.

## Explanations

### L1 human

A self-adjoint operator gives the same number when it acts on either vector of an inner product.
For real matrices and the dot product, these are the symmetric matrices, which equal their mirror image across the diagonal.
For example, $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ is symmetric.
It stretches the direction $(1, 1)$ by $3$ and the direction $(1, -1)$ by $1$.
These two directions are perpendicular, and this always happens for symmetric matrices.

### L2 human

Worked example: we check self-adjointness of an operator on polynomials.

1. Let $V$ be the [[space of real polynomials|0JGZCDT5DN]] of degree at most $2$, with $\ip{p}{q} = \int_{-1}^{1} p(x) q(x) \, dx$.
2. Let $T(p)(x) = p(-x)$. For $p$ and $q$ in $V$, substitute $y = -x$: $\ip{Tp}{q} = \int_{-1}^{1} p(-x) q(x) \, dx = \int_{-1}^{1} p(y) q(-y) \, dy = \ip{p}{Tq}$.
3. So $T$ is self-adjoint.
4. The eigenvalues are $1$ on the even polynomials $1$ and $x^2$, and $-1$ on the odd polynomial $x$.
5. Every even polynomial is orthogonal to every odd polynomial for this inner product, because the product is odd and the interval is symmetric. This agrees with the orthogonality of eigenspaces.

The typical use is to recognize a self-adjoint operator and then apply the real spectral theorem.
A trap: the standard basis $1, x, x^2$ is not orthonormal here, so we checked the definition directly and not with a matrix.

### L3 human

Self-adjoint operators are the real elements of the algebra of operators with the involution $T \mapsto T^*$, just as real numbers are the fixed points of complex conjugation.
The Cartesian decomposition $T = A + iB$ is the analogue of $z = x + iy$.
The map $T \mapsto e^{iT}$ sends self-adjoint operators to unitary operators, and the self-adjoint operators form the Lie algebra of the unitary group, up to the factor $i$.
In a $C^*$-algebra, self-adjoint elements have real spectrum, which is [[the real spectrum theorem|NXV8S3145K]] of functional analysis.
For unbounded operators, the difference between symmetric and self-adjoint is essential, and self-adjoint extensions are a separate theory.
