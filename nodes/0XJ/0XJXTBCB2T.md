---
tag: 0XJXTBCB2T
kind: concept
name: Orthogonal complement
msc: [15A63, 46C05]
topics: [8GQVME4SZZ]
audience: ug1
specializes: [00YC1D652K]
uses: [0NB0AWGJBW, 0Y2X7P2WB7, 00YC1D652K]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: Inner product spaces
  - book: isbn:9783031410253
    locator: Section 6C
  - book: isbn:9780134860244
    locator: Section 6.2
  - book: isbn:9780321982384
    locator: Section 6.1
same_as:
  wikidata: Q1780921
  wikipedia: Orthogonal complement
inventory: [G20Z36F7VP]
---

## Summary

The orthogonal complement of a set of vectors collects every vector that stands at a right angle to all of them.
It turns "perpendicular to this plane" or "perpendicular to these rows" into a subspace that we can compute and measure.
Let $V$ be an [[inner product space|0QVNCJXRY3]] over $\R$ or $\C$, and let $S$ be a subset of $V$.
The *orthogonal complement* of $S$ is
$$S^\perp = \{ v \in V : \ip{v}{s} = 0 \text{ for every } s \in S \}.$$
So $S^\perp$ holds exactly the vectors that are [[orthogonal|0Y2X7P2WB7]] to each vector of $S$.
It is always a [[linear subspace|00YC1D652K]], even when $S$ is not, and the [[formal definition|079D68S3AW]] states it for a subspace $U$.

## Motivation

A plane through the origin in $\R^3$ is fixed by one normal vector $n$: the plane is the set of $x$ with $n \cdot x = 0$.
In the other direction, the normal line is the set of vectors at a right angle to every vector of the plane.
So a plane and its normal line determine each other, and the orthogonal complement makes this relation exact for subspaces of every dimension in every inner product space.

The same idea explains a fact about matrices.
Entry $i$ of $Ax$ is the dot product of row $i$ of $A$ with $x$, so the solutions of $Ax = 0$ are the vectors orthogonal to every row.
In data fitting, the error of a best fit is orthogonal to the space of allowed fits, so it lies in an orthogonal complement.
That is why the whole sub-area rests on this splitting: the [[orthogonal projection|0B8KZRT28M]], the [[best approximation theorem|0MCDDSCB9Z]] and [[least squares|0BYTQ4X1HC]] all start from a subspace and its complement.

## Notation

We write $U^\perp$ and read it "$U$ perp".
For one vector we write $v^\perp$ for $\{v\}^\perp$, the set of vectors orthogonal to $v$.
Some books write $U^\circ$ or $U^0$ for the complement, but here $U^0$ is kept for the [[annihilator|0ASHNYF7AG]], which lives in the dual space $V^*$.
In Mathlib the orthogonal complement of `U : Submodule 𝕜 E` is `Uᗮ`, defined as `Submodule.orthogonal`.

## Remarks

### A first computation

Take the plane $U$ in $\R^3$ spanned by $u_1 = (1, 1, 0)$ and $u_2 = (0, 1, 1)$.
A vector $x$ is orthogonal to all of $U$ exactly when it is orthogonal to $u_1$ and to $u_2$, since every vector of $U$ is a combination of the two.
That gives two equations:
$$x_1 + x_2 = 0, \qquad x_2 + x_3 = 0.$$
Put $x_3 = t$; then $x_2 = -t$ and $x_1 = t$, so $U^\perp = \R(1, -1, 1)$.
Check: $(1, -1, 1) \cdot (1, 1, 0) = 0$ and $(1, -1, 1) \cdot (0, 1, 1) = 0$.
The equations say that $U^\perp$ is the null space of the matrix with rows $u_1$ and $u_2$, and [[the plane example|38S0WYCSA3]] works this out step by step.

### More examples

In $\R^n$ with the [[dot product|0S52TNNTH9]], the complement of the span of $e_1, \dots, e_k$ is the span of $e_{k+1}, \dots, e_n$, because $x \cdot e_i = x_i$ and so $x \perp e_1, \dots, e_k$ means that the first $k$ entries of $x$ are zero.
For a real $m \times n$ matrix $A$, the [[null space|0PHDYNR24D]] is the complement of the [[row space|069MCGX635]], by the computation in the motivation.
Complements also live in spaces of functions.
On the polynomials of degree at most $2$ with $\ip{f}{g} = \int_{-1}^{1} f g \, dx$, a polynomial $p$ is orthogonal to the constants exactly when $\int_{-1}^{1} p \, dx = 0$.
So $x$ and $3x^2 - 1$ lie in the complement of the constants, since $\int_{-1}^{1} x \, dx = 0$ and $\int_{-1}^{1} (3x^2 - 1) \, dx = 2 - 2 = 0$.

### What it is not

A subspace has many complements in the sense of direct sums, and only one of them is orthogonal.
In $\R^2$ the line $\R(1, 1)$ is a [[complement of the x-axis that is not orthogonal|NFHJSAH156]]: it meets the axis only in $0$ and the two lines span the plane, but $(1, 1) \cdot (1, 0) = 1 \ne 0$.
The set difference $\R^3 \setminus U$ of a plane $U$ is not $U^\perp$ either, because it does not contain $0$ and so is not a subspace.
The annihilator $U^0$ needs no inner product and consists of linear forms, not vectors of $V$, and [[the example in the duality sub-area|ENNMQ30X9F]] compares the two.

### The rules you can use

The [[basic properties of the orthogonal complement|T5Q51M5BAK]] hold in every inner product space.
The set $S^\perp$ is a subspace, because each condition $\ip{v}{s} = 0$ is linear in $v$.
It only depends on the span, $S^\perp = (\operatorname{span} S)^\perp$, so testing a spanning set is enough.
A larger set has a smaller complement, and the sum rule $(U + W)^\perp = U^\perp \cap W^\perp$ holds, as [[the two lines in R3|1JKAGB6W4Z]] check with numbers.
Positivity gives $U \cap U^\perp = \{0\}$, since a vector orthogonal to itself has $\ip{v}{v} = 0$.

When $U$ is finite-dimensional, the [[orthogonal decomposition|0SP7P0G7KQ]] gives $V = U \oplus U^\perp$.
When $V$ is finite-dimensional, it also gives $\dim U^\perp = \dim V - \dim U$, and the [[double orthogonal complement|0PXN9G4MX1]] gives $(U^\perp)^\perp = U$.
For matrices, the [[orthogonality of the fundamental subspaces|GQF2KG1R1N]] gives $\operatorname{Row}(A) = \operatorname{Nul}(A)^\perp$ and $\operatorname{Col}(A) = \operatorname{Nul}(A^{\mathsf{T}})^\perp$.

### Watch out

The most common mistake is to test $v$ against a few vectors of $U$ that do not span $U$.
Let $U$ be the plane in $\R^3$ spanned by $(1, 0, 0)$ and $(0, 1, 1)$.
The vector $v = (0, 1, 0)$ is orthogonal to $(1, 0, 0)$, but $v \cdot (0, 1, 1) = 1$, so $v$ is not in $U^\perp$.
Test a full spanning set, and then one test per spanning vector is enough.

A second mistake is to put the spanning vectors into the columns of the matrix.
Then $Ax = 0$ asks which combinations of the vectors vanish, and that is a different question.

A third mistake is to expect $(U^\perp)^\perp = U$ in every space.
It fails for [[a subspace of l2 that is not closed|DNZF0R4VMZ]], whose complement is $\{0\}$.

### History

The idea grew with the theory of Hilbert spaces in the early twentieth century, where the complement of a closed subspace gives the projection theorem.

### Try it

First, find the orthogonal complement of the line $\R(1, 2)$ in $\R^2$.
The condition is $x_1 + 2x_2 = 0$, so the complement is the line $\R(2, -1)$.

Second, find the dimension of the complement of the line $\R(1, 1, 1, 1)$ in $\R^4$.
The complement is the solution set of one nonzero equation $x_1 + x_2 + x_3 + x_4 = 0$, so its dimension is $4 - 1 = 3$.

## Explanations

### L1 human

Hold a flat sheet of paper and stand a pencil straight up on it.
Every direction in the sheet makes a right angle with the pencil.
The orthogonal complement of the sheet is the line of the pencil, and the complement of the pencil line is the whole sheet.
For the floor of a room, the complement is the vertical direction.

### L2 human

Here is the typical computation: find the complement of $U = \operatorname{span}\{(1, 0, 2, 0), (0, 1, -1, 1)\}$ in $\R^4$.
A vector $x$ lies in $U^\perp$ exactly when it is orthogonal to both spanning vectors, so we solve
$$x_1 + 2x_3 = 0, \qquad x_2 - x_3 + x_4 = 0.$$
Take $x_3 = s$ and $x_4 = t$ as free variables.
Then $x_1 = -2s$ and $x_2 = s - t$, so
$$U^\perp = \operatorname{span}\{(-2, 1, 1, 0), (0, -1, 0, 1)\}.$$
Check: $(-2, 1, 1, 0) \cdot (1, 0, 2, 0) = -2 + 2 = 0$ and $(-2, 1, 1, 0) \cdot (0, 1, -1, 1) = 1 - 1 = 0$, and in the same way $(0, -1, 0, 1)$ passes both tests.
The dimensions add up, $2 + 2 = 4$, as the orthogonal decomposition predicts.
In general, put a spanning set of $U$ into the rows of a matrix and solve $Ax = 0$.

### L3 human

Over any field, the pairing $x^{\mathsf{T}} y$ on $F^n$ defines a set $\{ x : x^{\mathsf{T}} u = 0 \text{ for all } u \in U \}$, and it is the image of the annihilator $U^0$ when we identify $F^n$ with its dual.
An inner product is what makes this set a true complement, because positivity gives $U \cap U^\perp = \{0\}$.
For an indefinite form, such as the Minkowski form, a nonzero vector can be orthogonal to itself, and $U \cap U^\perp$ can be nonzero; the theory of [[bilinear forms|0SQZMXB6GP]] studies this.
In a Hilbert space $U^\perp$ is always closed, and $(U^\perp)^\perp$ is the closure of $U$.
The sub-area on operators uses the complement for the kernel and image of the [[adjoint|0R9NMSM1ZP]], $\ker T^* = (\im T)^\perp$, and for the invariant subspaces in the spectral theorem.
