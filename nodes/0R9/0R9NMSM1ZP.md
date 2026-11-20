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

Let $V$ and $W$ be finite-dimensional [[inner product spaces|0QVNCJXRY3]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $T \colon V \to W$ be a [[linear map|0NRYHJPQG2]].
The adjoint of $T$ is the linear map $T^* \colon W \to V$ with $\ip{Tv}{w} = \ip{v}{T^* w}$ for all $v \in V$ and $w \in W$.
The [[formal definition|0ST8QF9T3T]] states this, and [[the existence theorem|E0KFAXMTC2]] shows that exactly one such map exists.
The adjoint matters because it turns questions about $T$ into questions about the pair $T$, $T^*$, and the spectral theorems are statements about this pair.

## Motivation

For a real $m \times n$ matrix $A$ and the dot product, $(Ax) \cdot y = x \cdot (A^T y)$ for all $x$ and $y$.
So the transpose moves a matrix from one side of the dot product to the other.
Many arguments use this move: least squares, the four fundamental subspaces, and the symmetry of $A^T A$.
The adjoint is the same move for a linear map between any two inner product spaces.
It needs no basis, so it also works for spaces of polynomials or functions.

## Notation

- We write $T^*$. Many physics books write $T^\dagger$.
- The inner product is linear in the first slot, as everywhere in this topic. With the other convention, the defining identity and all the rules below stay the same.
- In Mathlib, `LinearMap.adjoint` is the adjoint of a linear map between finite-dimensional inner product spaces.
- For a matrix $A$, the notation $A^*$ means the [[conjugate transpose|0DXKE10PHF]]. By [[the matrix of the adjoint|0DBTE6HVBD]], this agrees with the adjoint of $x \mapsto Ax$ for the standard inner products.

## Remarks

### Examples

- For a real $m \times n$ matrix $A$, the adjoint of $x \mapsto Ax$ from $\mathbb{R}^n$ to $\mathbb{R}^m$ with the dot products is $y \mapsto A^T y$. The reason is $(Ax) \cdot y = y^T A x = (A^T y)^T x$.
- For a complex matrix $A$ and the standard inner products, the adjoint of $x \mapsto Ax$ is $y \mapsto A^* y$, by the same computation with conjugates.
- [[Differentiation on the polynomials of degree at most 2|CR3EXBJNPF]] with the inner product $\int_{-1}^{1} pq$ has the adjoint $D^*(1) = 3x$, $D^*(x) = \tfrac{5}{2}(3x^2 - 1)$, $D^*(x^2) = x$.
- For fixed $u \in V$ and $z \in W$, the rank-one map $T(v) = \ip{v}{u} z$ has the adjoint $T^*(w) = \ip{w}{z} u$. Indeed $\ip{Tv}{w} = \ip{v}{u} \ip{z}{w}$ and $\ip{v}{\ip{w}{z} u} = \overline{\ip{w}{z}} \ip{v}{u} = \ip{z}{w} \ip{v}{u}$.
- [[An operator in a basis that is not orthonormal|2YX64QQ94Y]]: the matrix of the adjoint there is not the transpose of the matrix of the map.

### Non-examples

- [[The transpose for a weighted inner product|CPQB5HABC6]]: on $\mathbb{R}^2$ with $\ip{x}{y} = 2x_1 y_1 + x_2 y_2$, the map $y \mapsto A^T y$ is not the adjoint of $x \mapsto Ax$ for $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$. The defining identity fails.
- For a complex matrix $A$ with a non-real entry, the plain transpose $A^T$ is not the adjoint of $x \mapsto Ax$ on $\mathbb{C}^n$. For $A = (i)$ on $\mathbb{C}$, we have $\ip{i \cdot 1}{1} = i$, but $\ip{1}{i \cdot 1} = -i$.

### Basic properties

- [[Existence and uniqueness of the adjoint|E0KFAXMTC2]]: each linear map $T \colon V \to W$ has exactly one adjoint, and it is linear.
- [[Algebraic properties of the adjoint|TPP76FP659]]: $(S + T)^* = S^* + T^*$, $(aT)^* = \overline{a} T^*$, $(ST)^* = T^* S^*$, $(T^*)^* = T$, $I^* = I$, and $(T^{-1})^* = (T^*)^{-1}$ for invertible $T$. So the map $T \mapsto T^*$ is antilinear over $\mathbb{C}$.
- [[The matrix of the adjoint|0DBTE6HVBD]] in orthonormal bases is the conjugate transpose of the matrix of $T$.
- [[Kernel and image of the adjoint|YPP8XT6B7Y]]: $\ker T^* = (\im T)^\perp$, $\im T^* = (\ker T)^\perp$, and $\rank T^* = \rank T$.

### History

The adjoint is also called the Hermitian adjoint or the Hermitian conjugate, after Hermite, as the Wikipedia article on the Hermitian adjoint states.
The same article defines the adjoint for bounded operators between Hilbert spaces, which is the subject of [[the adjoint in Hilbert spaces|6HSJBJ8TTQ]].

### Common errors

- Students use the transpose of the matrix of $T$ in any basis. This is correct only in orthonormal bases, as [[the basis example|2YX64QQ94Y]] shows.
- Students forget the conjugation over $\mathbb{C}$ and write $(aT)^* = aT^*$. The correct rule is $(aT)^* = \overline{a} T^*$.
- Students reverse the order in a product and write $(ST)^* = S^* T^*$. The correct order is $(ST)^* = T^* S^*$, as for the transpose of a product of matrices.

## Explanations

### L1 human

An inner product takes two vectors and gives a number, like the dot product.
A linear map $T$ acts on the first vector.
The adjoint $T^*$ is the map that gives the same number when it acts on the second vector instead.
For the matrix $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$ with the dot product, the adjoint is the transpose $\begin{pmatrix} 1 & 0 \\ 2 & 3 \end{pmatrix}$.
For $x = (0, 1)$ and $y = (1, 0)$, both sides give the number $2$.

### L2 human

Worked example: the adjoint of a map between two different spaces.

1. Let $T \colon \mathbb{R}^2 \to \mathbb{R}^3$ be $T(x_1, x_2) = (x_1, x_1 + x_2, 2x_2)$, with the dot products.
2. The matrix of $T$ in the standard bases is $A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 2 \end{pmatrix}$.
3. The standard bases are orthonormal, so $T^*$ has the matrix $A^T = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 2 \end{pmatrix}$. Hence $T^*(y_1, y_2, y_3) = (y_1 + y_2, y_2 + 2y_3)$.
4. Check with $x = (1, 2)$ and $y = (1, 0, 1)$. Then $Tx = (1, 3, 4)$ and $Tx \cdot y = 1 + 0 + 4 = 5$.
5. Also $T^* y = (1, 2)$ and $x \cdot T^* y = 1 + 4 = 5$. The two numbers agree.

The typical use is to move a map across an inner product inside a proof.
For example, $\norm{Tv}^2 = \ip{Tv}{Tv} = \ip{T^* T v}{v}$.
A trap: the adjoint depends on the inner products, not only on the map.

### L3 human

The adjoint is the finite-dimensional case of the Hilbert space adjoint.
In categorical terms, the [[Riesz representation theorem|04GYPXDXNH]] identifies each space with its [[dual space|0M856Q1AMZ]] by an antilinear map, and under this identification $T^*$ is the [[dual map|0C2TQMW5A1]] of $T$.
So the adjoint is the dual map made into a map between the original spaces.
The rules $(ST)^* = T^* S^*$ and $T^{**} = T$ make the finite-dimensional inner product spaces a dagger category.
In an algebra of operators, $T \mapsto T^*$ is an involution, and the axioms of a $C^*$-algebra abstract its properties.
The [[self-adjoint operators|0NEGN5CRSC]], the [[normal operators|0C8BR8XRTR]] and the [[unitary matrices|0AR68JTMDT]] are defined by relations between $T$ and $T^*$.
In infinite dimension, an unbounded operator has an adjoint only on a domain, and [[the adjoint in Hilbert spaces|6HSJBJ8TTQ]] treats the bounded case.
