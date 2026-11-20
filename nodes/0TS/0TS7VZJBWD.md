---
tag: 0TS7VZJBWD
kind: definition
name: Orthogonal vectors
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
defines: 0Y2X7P2WB7
uses: [01EK923SKP]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonality_(mathematics)
    locator: Euclidean vector spaces
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Orthogonality
---

## Definition

Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{R}$ or $\mathbb{C}$, with inner product $\ip{\cdot}{\cdot}$.

1. Two vectors $x, y \in V$ are *orthogonal*, written $x \perp y$, when $\ip{x}{y} = 0$.
2. A family $(v_1, \dots, v_k)$ of vectors of $V$ is an *orthogonal family* when $v_j \perp v_l$ for all $j \neq l$. A set of vectors is an *orthogonal set* when any two distinct elements are orthogonal.
3. A vector $x$ is orthogonal to a subset $S \subseteq V$, written $x \perp S$, when $x \perp s$ for every $s \in S$.

## Notation

- The symbol $\perp$ is read "is orthogonal to".
- When two inner products are present, we say "orthogonal for $\ip{\cdot}{\cdot}_1$" to name the inner product.

## Remarks

- The relation is symmetric, because $\ip{y}{x} = \overline{\ip{x}{y}}$, and the conjugate of $0$ is $0$.
- The zero vector is orthogonal to every vector, and it is the only vector orthogonal to itself.
- In $\mathbb{R}^2$ with the dot product, $(1, 2)$ and $(-2, 1)$ are orthogonal.
- The notion depends on the inner product. For $\ip{x}{y} = 2x_1 y_1 + x_2 y_2$ on $\mathbb{R}^2$, the vectors $(1, 2)$ and $(-2, 1)$ give $-4 + 2 = -2$, so they are not orthogonal.

## Explanations

### L1 human

Orthogonal is the general word for perpendicular.
Two vectors are orthogonal when their inner product is zero.
In the plane, $(3, 1)$ and $(-1, 3)$ give $-3 + 3 = 0$, so they meet at a right angle.

### L2 human

Worked example: an orthogonal family in $\mathbb{R}^3$.

1. Let $v_1 = (1, 1, 0)$, $v_2 = (1, -1, 0)$ and $v_3 = (0, 0, 2)$.
2. The dot products are $v_1 \cdot v_2 = 1 - 1 = 0$, $v_1 \cdot v_3 = 0$ and $v_2 \cdot v_3 = 0$.
3. So $(v_1, v_2, v_3)$ is an orthogonal family. Its vectors are not unit vectors, so it is not orthonormal.

The typical use is to check that a candidate basis is orthogonal before we normalize it.
A trap: an orthogonal family may contain the zero vector, and then it is not linearly independent.
