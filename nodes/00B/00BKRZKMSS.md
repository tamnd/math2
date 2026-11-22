---
tag: 00BKRZKMSS
kind: concept
name: Composition of linear maps
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
uses: [0NRYHJPQG2, 0THBK9V825]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Definition and first consequences
  - book: isbn:9780134860244
    locator: Section 2.3
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Summary

Doing one linear map and then another is again a linear map, and in coordinates this "one after the other" is exactly matrix multiplication.
Let $U$, $V$ and $W$ be vector spaces over a field $F$, and let $S \colon U \to V$ and $T \colon V \to W$ be [[linear maps|0NRYHJPQG2]].
The *composition* of $T$ and $S$ is the map
$$T \circ S \colon U \to W, \qquad (T \circ S)(u) = T(S(u)),$$
which applies $S$ first and then $T$.
The [[formal definition|05YBKMRVAR]] states it, and the [[theorem on composites|FSXBBV9C76]] shows that $T \circ S$ is linear.
For matrix transformations, $T_A \circ T_B = T_{AB}$, so composition is the product of the matrices.

## Motivation

Many maps are built in stages: rotate the picture, then reflect it, then project it onto a screen.
To understand the result we want the whole process as one map, and composition gives it.
Because each stage is linear, the whole process is linear, so all the tools of the area apply to it.

Composition is also the reason behind the rule for multiplying matrices.
Cayley chose the product of matrices so that it describes two linear substitutions done one after the other.
That choice explains why the product is associative but not commutative, and it returns in every later sub-area: the [[algebra of endomorphisms|5JA4CYT1TB]] uses composition as its product, and the powers $T^k$ of one map are the subject of eigenvalue theory.

## Notation

The composite is written $T \circ S$, or $TS$ when the maps are linear.
In both notations the map on the right acts first, which matches the order of a matrix product $AB$ acting on a column $x$.
For a map $T \colon V \to V$, the powers are $T^0 = \id_V$, $T^1 = T$ and $T^{k+1} = T \circ T^k$.
In Mathlib the composite of `g` and `f` is written `g.comp f` or `g ∘ₗ f`.

## Remarks

### A first computation

Take $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, a shear, and $B = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$, a stretch, and follow $x = (1, 1)$ through $B$ and then $A$:
$$Bx = \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \qquad A(Bx) = \begin{pmatrix} 2 + 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}.$$
The product matrix is $AB = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}$, and $(AB)x = (3, 1)$, as before.
In the other order, $BA = \begin{pmatrix} 2 & 2 \\ 0 & 1 \end{pmatrix}$ gives $(BA)x = (4, 1)$, a different vector.

### More examples

A [[rotation and a reflection of the plane|W9GA3QFG24]] give two different reflections, one for each order.
On polynomials, [[differentiation and integration|25N6VYJ127]] satisfy $D \circ J = \id$, while $J \circ D$ removes the constant term.
In general the composite of the [[matrix transformations|W6KB0J3SZZ]] $x \mapsto Bx$ and $y \mapsto Ay$ is $x \mapsto (AB)x$.

### What it is not

The [[pointwise product of two linear maps|ZVW35WJ3YZ]] is not their composite: for $S(x) = 2x$ and $T(x) = 3x$ on $\R$, it gives $6x^2$, while $T \circ S$ gives $6x$.
The composite also needs matching spaces.
For $S \colon \R^2 \to \R^3$ and $T \colon \R^2 \to \R^2$, the outputs of $S$ are not inputs of $T$, so $T \circ S$ does not exist.

### The rules of composition

Composition is associative, $(R \circ T) \circ S = R \circ (T \circ S)$, because both sides send $u$ to $R(T(S(u)))$; this holds for all [[functions|0THBK9V825]].
The identity maps are neutral: $T \circ \id_V = T = \id_W \circ T$.
Composition is bilinear, so $T \circ (S_1 + S_2) = T \circ S_1 + T \circ S_2$ and $(T_1 + T_2) \circ S = T_1 \circ S + T_2 \circ S$, and scalars move out of each factor.
The first identity uses that $T$ is linear, and the second holds by the definition of the sum of maps.
In finite dimension with chosen bases, the [[matrix of a composite is the product of the matrices|05Q1B7MH0M]].

### Watch out

The order matters, and it is easy to read $T \circ S$ the wrong way.
The map on the right acts first, so $T \circ S$ means "first $S$, then $T$".
Composition is also not commutative, even for maps from a space to itself.
With $S(x, y) = (y, x)$ and $T(x, y) = (2x, y)$ on $\R^2$, we get $(T \circ S)(1, 0) = T(0, 1) = (0, 1)$ but $(S \circ T)(1, 0) = S(2, 0) = (0, 2)$.

### History

Cayley introduced matrices in his memoir of 1858 and defined their product as the composite of two linear substitutions of variables.

### Try it

First, let $R$ be the rotation of $\R^2$ by a right angle, with matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, and compute $R \circ R$.
The product is $\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$, so $R \circ R$ is the half turn $v \mapsto -v$.

Second, for $S \colon \R^3 \to \R^2$ and $T \colon \R^2 \to \R^4$, which composite exists, and what are its source and target?
Only $T \circ S$ exists, and it is a map $\R^3 \to \R^4$, given by a $4 \times 3$ matrix.

## Explanations

### L1 human

To compose two linear maps, apply one and then the other.
The result is again a linear map.
For example, rotating the plane by a right angle twice gives the half turn, which sends each point $(x, y)$ to $(-x, -y)$.
Doing two moves in the other order can give a different result, so the order counts.

### L2 human

Here is a typical problem: find one matrix for "reflect in the $x$-axis, then stretch the $x$-direction by $3$".
The reflection is $B = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ and the stretch is $A = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$.
The reflection acts first, so it goes on the right:
$$AB = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 3 & 0 \\ 0 & -1 \end{pmatrix}.$$
Check: $(2, 5)$ reflects to $(2, -5)$ and then stretches to $(6, -5)$, and $AB$ sends $(2, 5)$ to $(6, -5)$ as well.
In practice, a chain of many steps becomes one matrix that can be applied to many points at once.
Watch out: here $AB = BA$ because both matrices are diagonal, but for most pairs the order changes the product.

### L3 human

Vector spaces over $F$ and linear maps form a category, with composition as the operation on arrows.
Bilinearity of composition makes this category enriched over vector spaces: each $\Hom(U, V)$ is a vector space, and composition $\Hom(V, W) \times \Hom(U, V) \to \Hom(U, W)$ is bilinear.
For $U = V = W$, composition is the multiplication of the [[algebra of endomorphisms|5JA4CYT1TB]], and the sub-area on matrices of linear maps turns it into the matrix product for any choice of basis.
