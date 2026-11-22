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

A self-adjoint operator is a linear map that can move from one side of the inner product to the other without any change.
It is the basis-free form of a symmetric matrix, and it is the class of operators that the spectral theorems describe most completely.
Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$.
A linear operator $T \colon V \to V$ is *self-adjoint* when it equals its [[adjoint|0R9NMSM1ZP]]:
$$T^* = T, \qquad \text{that is,} \qquad \ip{Tv}{w} = \ip{v}{Tw} \quad \text{for all } v, w \in V.$$
The [[formal definition|0MB8HQW495]] states this and shows that the two forms agree.
In an orthonormal basis, $T$ is self-adjoint exactly when its matrix is symmetric over $\mathbb{R}$ or Hermitian over $\mathbb{C}$.

## Motivation

Symmetric matrices appear wherever a quantity depends on two directions in the same way.
The Hessian of a smooth function, the [[covariance matrix|0V7G6WMFK0]] of a list of random variables and the matrix of a quadratic form are all symmetric.
In each case, the facts that we use are the same: the eigenvalues are real, and the eigenvectors can be chosen perpendicular to each other.
A self-adjoint operator is the setting where these facts hold without any choice of coordinates, so they also apply to spaces of polynomials or functions.

Over $\mathbb{C}$ the same role belongs to the [[Hermitian matrices|0P17NGQQMQ]], with $A^* = A$.
In quantum mechanics, each measurable quantity is a self-adjoint operator, and its eigenvalues are the possible results of a measurement.
Later pages show that the eigenvalues are [[real|0C4NT4GT3X]], that [[eigenspaces for different eigenvalues are orthogonal|0JHGAV9H25]], and that $V$ has an orthonormal basis of eigenvectors by [[the real spectral theorem|06J4PXRG22]].

## Notation

Books say *self-adjoint* or *Hermitian* for an operator with $T^* = T$, and many say *symmetric* when the space is real.
For matrices, a real matrix with $A^{\mathsf{T}} = A$ is [[symmetric|0VR671PHE5]], and a complex matrix with $A^* = A$ is [[Hermitian|0P17NGQQMQ]].
Watch the word "symmetric" over $\mathbb{C}$: some books use it for Hermitian matrices, while others mean $A^{\mathsf{T}} = A$, which is [[a different condition|DAZBNZXZK7]].
In functional analysis, a [[symmetric operator|H971WGMV6C]] is an unbounded operator with $\ip{Tv}{w} = \ip{v}{Tw}$ on a domain only, and it need not be self-adjoint.
Mathlib writes `LinearMap.IsSymmetric` for the condition $\ip{Tv}{w} = \ip{v}{Tw}$.
An operator with $T^* = -T$ is *skew-adjoint*, and its matrices are [[skew-symmetric|0PBY4E9GQF]] over $\mathbb{R}$ and skew-Hermitian over $\mathbb{C}$.

## Remarks

### A first check

Take $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ on $\mathbb{R}^2$ with the dot product, and take $x = (1, 0)$ and $y = (0, 3)$.
Move $A$ to the first vector, and then to the second vector:
$$(Ax) \cdot y = (2, 1) \cdot (0, 3) = 3, \qquad x \cdot (Ay) = (1, 0) \cdot (3, 6) = 3.$$
The two numbers agree, and they agree for every $x$ and $y$, because $(Ax) \cdot y = x^{\mathsf{T}} A^{\mathsf{T}} y$ and $A^{\mathsf{T}} = A$.
This operator stretches $(1, 1)$ by $3$ and $(1, -1)$ by $1$, and these two directions are perpendicular.
That is the pattern for every self-adjoint operator.

Over $\mathbb{C}$ the test needs the conjugate.
For [[the Hermitian matrix with entries 1, 2i, -2i, 1|4119199XBW]], conjugating and transposing gives back the same matrix, so the operator is self-adjoint.
Its eigenvalues are $3$ and $-1$, both real, and its eigenvectors $(i, 1)$ and $(1, i)$ are orthogonal.
The [[real symmetric 3 by 3 matrix|2P021RCC4Y]] with eigenvalues $3$, $4$ and $6$ shows the same pattern in three dimensions.

### Self-adjoint operators without matrices

Every [[orthogonal projection|0Q8HZTJC7G]] $P$ onto a subspace $U$ is self-adjoint.
The reason is that $w - Pw$ is orthogonal to $U$, and $Pv$ lies in $U$:
$$\ip{Pv}{w} = \ip{Pv}{Pw} + \ip{Pv}{w - Pw} = \ip{Pv}{Pw},$$
and the same computation gives $\ip{v}{Pw} = \ip{Pv}{Pw}$.

For every linear map $S \colon V \to W$, the operators $S^* S$ on $V$ and $S S^*$ on $W$ are self-adjoint, because $(S^* S)^* = S^* S^{**} = S^* S$.
These operators lead to the singular values in a later sub-area.

On the [[polynomials of degree at most 2|0JGZCDT5DN]] with $\ip{p}{q} = \int_{-1}^{1} p(x) q(x) \, dx$, the reflection $(Tp)(x) = p(-x)$ is self-adjoint.
The substitution $y = -x$ gives
$$\ip{Tp}{q} = \int_{-1}^{1} p(-x) q(x) \, dx = \int_{-1}^{1} p(y) q(-y) \, dy = \ip{p}{Tq}.$$
Its eigenvalue $1$ has the even polynomials as eigenvectors, and its eigenvalue $-1$ has the odd ones.

### What it is not

[[The rotation of the complex plane by a right angle|1CF483TZZA]] has $R^* = -R$, so it is skew-adjoint and not self-adjoint.
It is still normal, and its eigenvalues $i$ and $-i$ are not real.
[[The complex symmetric matrix|DAZBNZXZK7]] has $A^{\mathsf{T}} = A$, but $A^* \ne A$, so it is not self-adjoint for the standard inner product on $\mathbb{C}^2$.
The [[real rotation with zero quadratic form|VMHPYDZERM]] has $\ip{Rv}{v} = 0$ for all $v$, so every value of its quadratic form is real, and yet $R$ is not self-adjoint.
So the test by real values of $\ip{Tv}{v}$ works over $\mathbb{C}$ only.

### The rules you can use

If $S$ and $T$ are self-adjoint and $a$ is real, then $S + T$ and $aT$ are self-adjoint, so the self-adjoint operators form a real vector space.
Over $\mathbb{C}$ they do not form a complex vector space, because $(iT)^* = -i T^* = -iT$.
A product $ST$ of self-adjoint operators is self-adjoint exactly when $ST = TS$, since $(ST)^* = T^* S^* = TS$.
Every self-adjoint operator is [[normal|0C8BR8XRTR]], because $T^* T = T^2 = T T^*$.

Over $\mathbb{C}$, [[the quadratic form test|WAYMK9GR5S]] says that $T$ is self-adjoint exactly when $\ip{Tv}{v}$ is real for every $v$.
The same test also shows that $\ip{Tv}{v} = 0$ for all $v$ forces $T = 0$ over $\mathbb{C}$, while over $\mathbb{R}$ it forces $T = 0$ only for self-adjoint $T$.
The eigenvalues of a self-adjoint operator are [[real|0C4NT4GT3X]], and the [[Rayleigh quotient|06WHP8SE98]] $\ip{Tv}{v} / \ip{v}{v}$ has the largest and smallest eigenvalue as its maximum and minimum.
By [[the real spectral theorem|06J4PXRG22]], a real operator is self-adjoint exactly when it has an orthonormal basis of eigenvectors.
Over $\mathbb{C}$, self-adjoint means an orthonormal eigenbasis with real eigenvalues.

### Skew-adjoint operators and the Cartesian decomposition

An operator is skew-adjoint when $T^* = -T$.
Over $\mathbb{C}$, $T$ is skew-adjoint exactly when $iT$ is self-adjoint, because $(iT)^* = -iT^* = iT$ in that case.
Every operator on a complex space splits as
$$T = A + iB, \qquad A = \tfrac{1}{2}(T + T^*), \qquad B = \tfrac{1}{2i}(T - T^*),$$
with $A$ and $B$ self-adjoint.
Check: $A + iB = \tfrac{1}{2}(T + T^*) + \tfrac{1}{2}(T - T^*) = T$.
The pair $A$, $B$ is unique, just as $z = x + iy$ has one real part and one imaginary part, and $T$ is normal exactly when $AB = BA$.

### Watch out

The first trap is the plain transpose over $\mathbb{C}$.
The matrix $\begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}$ equals its transpose, but its conjugate transpose is $\begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}$, so it is not Hermitian.
The test is $A^* = A$.

The second trap is a basis or an inner product that is not the standard one.
On $\mathbb{R}^2$ with $\ip{x}{y} = 2x_1 y_1 + x_2 y_2$, the symmetric matrix $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ gives
$$\ip{B e_1}{e_2} = \ip{e_2}{e_2} = 1, \qquad \ip{e_1}{B e_2} = \ip{e_1}{e_1} = 2.$$
So $B$ is not self-adjoint for this inner product, and a symmetric matrix proves self-adjointness only in an orthonormal basis; [[the weighted inner product example|CPQB5HABC6]] computes such an adjoint.

The third trap is a product.
The two symmetric matrices $\operatorname{diag}(1, -1)$ and $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ have the product $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, which is not symmetric, because they do not commute.

### History

Hermitian matrices carry the name of Hermite, who showed in 1855 that their eigenvalues are real, as for real symmetric matrices.
The infinite-dimensional theory, with the [[spectral theorem for unbounded self-adjoint operators|18KPYRRPZY]], belongs to functional analysis.

### Try it

First, for which real $c$ is $\begin{pmatrix} 1 & c \\ 2 & 0 \end{pmatrix}$ self-adjoint on $\mathbb{R}^2$ with the dot product?
The matrix must equal its transpose, so $c = 2$.

Second, is $\begin{pmatrix} 3 & 1 - i \\ 1 + i & -1 \end{pmatrix}$ self-adjoint on $\mathbb{C}^2$?
Yes: the diagonal is real, and the conjugate of the entry $1 - i$ is the entry $1 + i$ in the mirror position.

Third, show that $T^* + T$ is self-adjoint for every operator $T$.
We get $(T^* + T)^* = T^{**} + T^* = T + T^*$.

## Explanations

### L1 human

A self-adjoint operator gives the same number when it acts on either vector of an inner product.
For real matrices with the dot product, these are the symmetric matrices, which look the same in a mirror along the diagonal.
For example, $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ is symmetric.
It stretches the direction $(1, 1)$ by $3$ and the direction $(1, -1)$ by $1$.
These two directions are perpendicular, and symmetric matrices always have such perpendicular stretch directions.

### L2 human

Here is a typical use: show that the reflection $(Tp)(x) = p(-x)$ on the polynomials of degree at most $2$ has an orthonormal eigenbasis for $\ip{p}{q} = \int_{-1}^{1} p q \, dx$.
We proved above that $T$ is self-adjoint, so the real spectral theorem gives such a basis at once.
To find it, note that $T1 = 1$, $Tx = -x$ and $Tx^2 = x^2$, so the eigenvalue $1$ has the eigenspace spanned by $1$ and $x^2$, and $-1$ has the eigenspace spanned by $x$.
The two eigenspaces are orthogonal, since an even times an odd polynomial is odd and its integral over $[-1, 1]$ is $0$.
Inside the first eigenspace we still need Gram-Schmidt, because $\ip{1}{x^2} = \tfrac{2}{3} \ne 0$.
The polynomial $x^2 - \tfrac{1}{3}$ is orthogonal to $1$:
$$\ip{1}{x^2 - \tfrac{1}{3}} = \tfrac{2}{3} - \tfrac{2}{3} = 0.$$
So $1$, $x$ and $x^2 - \tfrac{1}{3}$ are orthogonal eigenvectors, and dividing by their norms gives the basis.
Watch out: the basis $1, x, x^2$ is not orthonormal here, so we checked self-adjointness with the definition and not with a matrix.

### L3 human

Self-adjoint operators are the real elements of the algebra of operators with the involution $T \mapsto T^*$, just as the real numbers are the fixed points of complex conjugation.
The Cartesian decomposition $T = A + iB$ is the operator form of $z = x + iy$, and the map $T \mapsto e^{iT}$ sends self-adjoint operators to unitary ones.
So the self-adjoint operators, times $i$, form the Lie algebra of the unitary group.
In a $C^*$-algebra, self-adjoint elements have [[real spectrum|NXV8S3145K]].
For unbounded operators on Hilbert space, the difference between symmetric and self-adjoint is essential, and self-adjoint extensions are a theory of their own.
The sub-area on positive operators and singular values builds on the operators $S^* S$.
