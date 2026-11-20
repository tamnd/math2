---
tag: YPP8XT6B7Y
kind: statement
role: theorem
name: Kernel and image of the adjoint
msc: ["15A04", "47A05"]
topics: [3YM9EK6VMB]
audience: ug1
about: [0R9NMSM1ZP, 0XJXTBCB2T]
uses: [0ST8QF9T3T, TPP76FP659, 079D68S3AW, 0PXN9G4MX1, 0E2NYPVSP9, 0W4FSW1TVB, 0JGB7A6GTS]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_adjoint
    locator: Properties
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780134860244
    locator: Section 6.3
---

## Statement

Let $V$ and $W$ be finite-dimensional inner product spaces over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$.
Let $T \colon V \to W$ be a linear map with [[adjoint|0ST8QF9T3T]] $T^* \colon W \to V$.
Write $U^\perp$ for the [[orthogonal complement|079D68S3AW]] of a subspace $U$.

1. $\ker T^* = (\im T)^\perp$, as subspaces of $W$.
2. $\im T^* = (\ker T)^\perp$, as subspaces of $V$.
3. $\ker T = (\im T^*)^\perp$ and $\im T = (\ker T^*)^\perp$.
4. $\rank T^* = \rank T$, where the [[rank|0JGB7A6GTS]] is the dimension of the image.
5. $T$ is injective if and only if $T^*$ is surjective, and $T$ is surjective if and only if $T^*$ is injective.

## Remarks

### Why each hypothesis is needed

- Part 1 holds in every inner product space, with the same proof, when the adjoint exists.
- Part 2 needs finite dimension. On the Hilbert space $\ell^2$ of square-summable sequences, let $T(x_1, x_2, x_3, \dots) = (x_1, x_2/2, x_3/3, \dots)$. Then $T^* = T$, and $\ker T = 0$, so $(\ker T)^\perp = \ell^2$.
- But the sequence $(1, 1/2, 1/3, \dots)$ lies in $\ell^2$ and not in $\im T$, because its only preimage would be $(1, 1, 1, \dots) \notin \ell^2$. So $\im T^* \neq (\ker T)^\perp$ there. In a Hilbert space only $\overline{\im T^*} = (\ker T)^\perp$ holds, with the closure.

### Consequences

- For an $m \times n$ real matrix $A$ and the dot products, part 1 says that the null space of $A^T$ is the orthogonal complement of the column space of $A$. This is [[the column space and the left null space|J4SZVFBHS5]], one of the relations between the [[four fundamental subspaces|73DVECPAT6]].
- Part 4 for real matrices says that the row rank equals the column rank, since the row space of $A$ is the column space of $A^T$.
- Solvability. The equation $Tv = w$ has a solution if and only if $w \perp \ker T^*$, by part 3. This is the finite-dimensional Fredholm alternative.
- For a [[self-adjoint|0MB8HQW495]] operator $T$, parts 1 and 2 give $V = \ker T \oplus \im T$ with $\ker T \perp \im T$.
- $\ker (T^* T) = \ker T$, so $\rank (T^* T) = \rank T$. The reason: if $T^* T v = 0$, then $\norm{Tv}^2 = \ip{T^* T v}{v} = 0$.

### Converse

The four equalities in parts 1 to 3 hold for the adjoint, but they do not characterize it.
For example, the map $2T^*$ has the same kernel and image as $T^*$, but it is not the adjoint of $T$ when $T \neq 0$.

### Generalizations

- For a bounded operator $T$ between Hilbert spaces, $\ker T^* = (\im T)^\perp$ and $(\ker T)^\perp = \overline{\im T^*}$.
- For a linear map $T \colon V \to W$ between any vector spaces, the [[dual map|0C2TQMW5A1]] $T'$ has the kernel equal to the annihilator of $\im T$. This is part 1 without an inner product.

## Explanations

### L1 human

A map $T$ sends some vectors to zero, and it reaches some vectors as outputs.
The adjoint swaps these two kinds of sets, with a right angle in between.
For the projection of the plane onto the $x$-axis, the outputs form the $x$-axis.
The adjoint is the same projection, and it sends exactly the $y$-axis to zero.
The $y$-axis is the set of vectors at a right angle to the $x$-axis.

### L2 human

Worked example: a $2 \times 3$ matrix.

1. Let $A = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 4 & 0 \end{pmatrix}$, as a map from $\mathbb{R}^3$ to $\mathbb{R}^2$ with the dot products.
2. The columns of $A$ are $(1, 2)$, $(2, 4)$ and $(0, 0)$. So the image of $A$ is the line spanned by $(1, 2)$.
3. Then $(\im A)^\perp$ is the line spanned by $(2, -1)$.
4. The adjoint is $A^T = \begin{pmatrix} 1 & 2 \\ 2 & 4 \\ 0 & 0 \end{pmatrix}$, and $A^T (2, -1) = (0, 0, 0)$. So $\ker A^T$ is the line spanned by $(2, -1)$, as part 1 says.
5. Both $A$ and $A^T$ have rank $1$, as part 4 says.

The typical use is to decide whether a linear system has a solution: check that the right side is orthogonal to the kernel of the adjoint.
A trap: $\ker T^*$ lives in $W$, while $\ker T$ lives in $V$, so the two parts of a statement can live in different spaces.

### L3 human

Parts 1 and 2 are the inner product form of the duality between kernels and cokernels.
For the dual map $T'$, the kernel is the annihilator of the image, and the Riesz isomorphisms turn annihilators into orthogonal complements.
In functional analysis, the closed range theorem says when $\im T$ is closed, and then $\im T = (\ker T^*)^\perp$ holds without closure.
Index theory starts here: for a Fredholm operator, $\dim \ker T - \dim \ker T^*$ is the index.
