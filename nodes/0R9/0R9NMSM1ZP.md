---
tag: 0R9NMSM1ZP
kind: concept
name: Adjoint of a linear map
msc: ["15A04", "47A05"]
topics: [3YM9EK6VMB]
audience: ug1
specializes: [0NRYHJPQG2]
uses: [0QVNCJXRY3, 0NRYHJPQG2, 04GYPXDXNH]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_adjoint
    locator: Definition for bounded operators between Hilbert spaces
  - url: https://en.wikipedia.org/wiki/Hermitian_adjoint
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Hermitian_adjoint
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780134860244
    locator: Section 6.3
same_as:
  wikidata: Q1509647
  wikipedia: Hermitian adjoint
---

## Summary

An inner product pairs two vectors and gives a number, and a linear map can act on either vector of the pair.
The adjoint of a map $T$ is the map that acts on the second vector and gives the same number that $T$ gives on the first vector.
For a real matrix and the dot product the adjoint is the transpose, so the adjoint is the transpose made to work in every inner product space.
Let $V$ and $W$ be finite-dimensional [[inner product spaces|0QVNCJXRY3]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $T \colon V \to W$ be a [[linear map|0NRYHJPQG2]].
The *adjoint* of $T$ is the linear map $T^* \colon W \to V$ such that
$$\ip{Tv}{w} = \ip{v}{T^* w} \qquad \text{for all } v \in V \text{ and } w \in W.$$
The [[formal definition|0ST8QF9T3T]] states this, and the [[existence theorem|E0KFAXMTC2]] shows that exactly one such map exists.

## Motivation

Take a real $m \times n$ matrix $A$, with the dot products on $\mathbb{R}^n$ and on $\mathbb{R}^m$.
A $1 \times 1$ matrix is its own transpose, so
$$(Ax) \cdot y = y^{\mathsf{T}} A x = (A^{\mathsf{T}} y)^{\mathsf{T}} x = x \cdot (A^{\mathsf{T}} y).$$
So the transpose moves a matrix from one side of the dot product to the other.
Many arguments rest on this move: the normal equations of least squares, the relations between the four fundamental subspaces, and the symmetry of $A^{\mathsf{T}} A$.

The adjoint makes the same move for a linear map between any two inner product spaces.
It needs no basis, so it also works on spaces of polynomials or functions, where a transpose has no meaning until we choose coordinates.
The rest of the theory of operators on inner product spaces is built on the pair $T$, $T^*$.
The [[self-adjoint operators|0NEGN5CRSC]] have $T^* = T$, the [[normal operators|0C8BR8XRTR]] have $T T^* = T^* T$, and the [[unitary matrices|0AR68JTMDT]] have $T^* T = I$.
The spectral theorems describe these classes, and in quantum mechanics the measurable quantities are modeled by self-adjoint operators.

## Notation

We write $T^*$, and many physics books write $T^\dagger$.
The inner product is linear in the first slot and conjugate linear in the second slot.
With the opposite convention, which is common in physics, the defining identity and all the rules below stay the same.
For a matrix $A$, the symbol $A^*$ means the [[conjugate transpose|0DXKE10PHF]] $\overline{A}^{\mathsf{T}}$, and the [[matrix of the adjoint|0DBTE6HVBD]] shows that this agrees with the adjoint of $x \mapsto Ax$ for the standard inner products.
Some books also write $T^*$ for the [[dual map|0C2TQMW5A1]], which acts on spaces of linear forms, so check which map a book means.
In Mathlib the adjoint is `LinearMap.adjoint`.

## Remarks

### A first computation

Let $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$ act on $\mathbb{R}^2$ with the dot product, and take $x = (0, 1)$ and $y = (1, 0)$.
Then $Ax = (2, 3)$ and $A^{\mathsf{T}} y = (1, 2)$, so
$$Ax \cdot y = 2 \cdot 1 + 3 \cdot 0 = 2, \qquad x \cdot A^{\mathsf{T}} y = 0 \cdot 1 + 1 \cdot 2 = 2.$$
The two numbers agree, as the computation in the motivation says they must.

Over $\mathbb{C}$ the standard inner product is $\ip{x}{y} = y^* x$, and the same computation gives $\ip{Ax}{y} = y^* A x = (A^* y)^* x = \ip{x}{A^* y}$.
So the adjoint of a complex matrix is its conjugate transpose.
For the $1 \times 1$ matrix $(i)$ on $\mathbb{C}$, this means that the adjoint of multiplication by $i$ is multiplication by $-i$.
Check:
$$\ip{i \cdot 1}{1} = i, \qquad \ip{1}{-i \cdot 1} = 1 \cdot \overline{(-i)} = i.$$

### Finding an adjoint without a matrix

Fix $u \in V$ and $z \in W$, and let $T(v) = \ip{v}{u} z$, a map of rank one when $u$ and $z$ are not zero.
We guess $T^*(w) = \ip{w}{z} u$ and check the defining identity:
$$\ip{v}{\ip{w}{z} u} = \overline{\ip{w}{z}}\, \ip{v}{u} = \ip{z}{w} \ip{v}{u} = \ip{Tv}{w}.$$
The guess is correct, and by uniqueness it is the adjoint.

On the space of polynomials of degree at most $2$ with $\ip{p}{q} = \int_{-1}^{1} p q \, dx$, the [[adjoint of differentiation|CR3EXBJNPF]] sends $1$ to $3x$, $x$ to $\tfrac{5}{2}(3x^2 - 1)$ and $x^2$ to $x$.
It is found from an orthonormal basis of Legendre polynomials.
Check one case with $p = x$ and $q = 1$:
$$\ip{Dx}{1} = \int_{-1}^{1} 1 \, dx = 2, \qquad \ip{x}{D^*(1)} = \int_{-1}^{1} 3x^2 \, dx = 2.$$
So differentiation, which lowers the degree, has an adjoint that raises it.

### Why the basis and the inner product matter

The transpose rule is a rule about orthonormal coordinates.
On $\mathbb{R}^2$ with the dot product, let $T(x_1, x_2) = (x_2, 0)$, and use the basis $(1, 0)$, $(1, 1)$.
In that basis the matrix of $T$ is $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, but the [[matrix of $T^*$ in the same basis|2YX64QQ94Y]] is $\begin{pmatrix} -1 & -1 \\ 1 & 1 \end{pmatrix}$, not the transpose.

The inner product matters in the same way.
For the [[weighted inner product|CPQB5HABC6]] $\ip{x}{y} = 2x_1 y_1 + x_2 y_2$ on $\mathbb{R}^2$, the same map has $\ip{Tx}{y} = 2 x_2 y_1$, so its adjoint is $T^*(y_1, y_2) = (0, 2y_1)$.
The transpose gives $(0, y_1)$, which fails the defining identity.
So the adjoint belongs to the map together with the two inner products, and it changes when an inner product changes.

### What it is not

The plain transpose of a complex matrix is not its adjoint.
For $A = (i)$ the transpose is $(i)$, while the adjoint is $(-i)$, as the first computation shows.
The inverse is not the adjoint either.
On $\mathbb{R}$ with $\ip{a}{b} = ab$, the map $T = 2I$ has $T^* = 2I$, because $\ip{2a}{b} = \ip{a}{2b}$, but $T^{-1} = \tfrac{1}{2} I$.
The two maps agree exactly for the unitary maps, where $T^* T = I$.

### The rules you can use

The [[existence theorem|E0KFAXMTC2]] gives exactly one adjoint for each linear map, and the adjoint is linear.
Uniqueness gives a method: to show that $S = T^*$, check $\ip{Tv}{w} = \ip{v}{Sw}$ for all $v$ and $w$.
This method proves the [[algebraic rules|TPP76FP659]] $(S + T)^* = S^* + T^*$, $(aT)^* = \overline{a}\, T^*$, $(T^*)^* = T$ and $I^* = I$.
For the product rule, move one factor at a time:
$$\ip{STv}{w} = \ip{Tv}{S^* w} = \ip{v}{T^* S^* w}, \qquad \text{so } (ST)^* = T^* S^*.$$
So the map $T \mapsto T^*$ is linear over $\mathbb{R}$ and antilinear over $\mathbb{C}$.
In orthonormal bases the matrix of $T^*$ is the conjugate transpose of the matrix of $T$, by the [[matrix of the adjoint|0DBTE6HVBD]].
The [[kernel and image theorem|YPP8XT6B7Y]] gives $\ker T^* = (\im T)^\perp$, $\im T^* = (\ker T)^\perp$ and $\rank T^* = \rank T$.

### Watch out

The first error is to transpose the matrix of $T$ in any basis.
The basis $(1, 0)$, $(1, 1)$ above shows that the result is wrong unless the basis is orthonormal.
The second error is to drop the conjugate over $\mathbb{C}$ and write $(aT)^* = a T^*$.
For $a = i$ and $T = I$ on $\mathbb{C}$, the correct answer is $(iI)^* = -iI$.
The third error is to keep the order in a product.
For $S = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $T = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ on $\mathbb{R}^2$, the product $ST = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ is its own adjoint, but $S^* T^* = TS = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$.

### History

The adjoint is also called the Hermitian adjoint or the Hermitian conjugate, after Charles Hermite.
The definition for bounded operators on Hilbert spaces, the subject of the [[Hilbert space adjoint|6HSJBJ8TTQ]], uses the same identity.

### Try it

First, find the adjoint of $T(x_1, x_2) = (x_1 + i x_2, 2 x_2)$ on $\mathbb{C}^2$ with the standard inner product.
The matrix is $\begin{pmatrix} 1 & i \\ 0 & 2 \end{pmatrix}$, so $T^*$ has the matrix $\begin{pmatrix} 1 & 0 \\ -i & 2 \end{pmatrix}$ and $T^*(y_1, y_2) = (y_1, -i y_1 + 2 y_2)$.

Second, show that $T^* T$ is its own adjoint for every linear map $T$.
The product rule and the double adjoint give $(T^* T)^* = T^* (T^*)^* = T^* T$.

## Explanations

### L1 human

An inner product takes two vectors and gives one number, like the dot product.
A map $T$ can change the first vector before we take the number.
The adjoint $T^*$ is the map that changes the second vector instead and still gives the same number.
For the matrix with rows $(1, 2)$ and $(0, 3)$ and the dot product, the adjoint is the matrix with rows $(1, 0)$ and $(2, 3)$, the same table flipped along its diagonal.
With the vectors $(0, 1)$ and $(1, 0)$, both ways give the number $2$.

### L2 human

Here is a typical computation: the adjoint of a map between two different spaces.
Let $T \colon \mathbb{R}^2 \to \mathbb{R}^3$ be $T(x_1, x_2) = (x_1, x_1 + x_2, 2x_2)$, with the dot products.
The standard bases are orthonormal, so the matrix of $T^*$ is the transpose of the matrix of $T$:
$$A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 2 \end{pmatrix}, \qquad A^{\mathsf{T}} = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 2 \end{pmatrix}.$$
So $T^*(y_1, y_2, y_3) = (y_1 + y_2, y_2 + 2y_3)$, a map from $\mathbb{R}^3$ back to $\mathbb{R}^2$.
Check with $x = (1, 2)$ and $y = (1, 0, 1)$: $Tx = (1, 3, 4)$ and $T^* y = (1, 2)$, so
$$Tx \cdot y = 1 + 0 + 4 = 5, \qquad x \cdot T^* y = 1 + 4 = 5.$$
In proofs the adjoint is used to move a map across an inner product, as in $\norm{Tv}^2 = \ip{Tv}{Tv} = \ip{T^* T v}{v}$.
Watch out: the answer depends on the inner products, so a new inner product on $\mathbb{R}^2$ or $\mathbb{R}^3$ gives a new adjoint.

### L3 human

The [[Riesz representation theorem|04GYPXDXNH]] identifies each finite-dimensional inner product space with its [[dual space|0M856Q1AMZ]] by a map that is antilinear over $\mathbb{C}$.
Under these identifications $T^*$ is the [[dual map|0C2TQMW5A1]] of $T$, so the adjoint is the dual map brought back to the original spaces.
The rules $(ST)^* = T^* S^*$ and $T^{**} = T$ make the finite-dimensional inner product spaces a dagger category, and on the operators of one space $T \mapsto T^*$ is an involution.
The axioms of a $C^*$-algebra abstract this involution.
In infinite dimension the [[Hilbert space adjoint|6HSJBJ8TTQ]] of a bounded operator is defined by the same identity, while an unbounded operator has an adjoint only on a domain.
