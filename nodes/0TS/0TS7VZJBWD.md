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

Two vectors are orthogonal when their inner product is zero, and a family is orthogonal when any two different members are.
Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{R}$ or $\mathbb{C}$, with inner product $\ip{\cdot}{\cdot}$.

1. Two vectors $x, y \in V$ are *orthogonal*, written $x \perp y$, when $\ip{x}{y} = 0$.
2. A family $(v_1, \dots, v_k)$ of vectors of $V$ is an *orthogonal family* when $v_j \perp v_l$ for all $j \neq l$.
3. A set of vectors is an *orthogonal set* when any two distinct elements are orthogonal.
4. A vector $x$ is orthogonal to a subset $S \subseteq V$, written $x \perp S$, when $x \perp s$ for every $s \in S$.

## Notation

The symbol $\perp$ is read "is orthogonal to".
When two inner products are present, we say "orthogonal for $\ip{\cdot}{\cdot}_1$" to name the one we use.

## Remarks

Condition 1 asks for $\ip{x}{y} = 0$ and says nothing about $\ip{y}{x}$, but the two conditions agree.
Conjugate symmetry gives $\ip{y}{x} = \overline{\ip{x}{y}}$, and the conjugate of $0$ is $0$, so the relation is symmetric.
The zero vector is orthogonal to every vector, and it is the only vector orthogonal to itself, by positive definiteness.

Condition 2 speaks of a family, so a vector may appear twice.
A family with a repeated nonzero vector is not orthogonal, because $\ip{v}{v} > 0$.
Condition 3 speaks of a set, where repetition cannot happen.

For example, $(1, 2)$ and $(-2, 1)$ are orthogonal in $\mathbb{R}^2$ with the dot product, since $-2 + 2 = 0$.
The notion depends on the inner product.
For $\ip{x}{y} = 2x_1y_1 + x_2y_2$ on $\mathbb{R}^2$, the same vectors give
$$2 \cdot 1 \cdot (-2) + 2 \cdot 1 = -4 + 2 = -2,$$
so they are not orthogonal for that inner product, as the [[weighted example|H8ZMNX035D]] explains.
The concept page on [[orthogonal vectors|0Y2X7P2WB7]] gives the uses of the notion.

## Explanations

### L1 human

Orthogonal is the general word for perpendicular.
Two vectors are orthogonal when their inner product is zero.
In the plane, $(3, 1)$ and $(-1, 3)$ give $-3 + 3 = 0$, so they meet at a right angle.

### L2 human

Take $v_1 = (1, 1, 0)$, $v_2 = (1, -1, 0)$ and $v_3 = (0, 0, 2)$ in $\mathbb{R}^3$.
The three dot products are
$$v_1 \cdot v_2 = 1 - 1 = 0, \qquad v_1 \cdot v_3 = 0, \qquad v_2 \cdot v_3 = 0,$$
so $(v_1, v_2, v_3)$ is an orthogonal family.
Its vectors have lengths $\sqrt{2}$, $\sqrt{2}$ and $2$, so it is not orthonormal until we divide each vector by its length.
Watch out: an orthogonal family may contain the zero vector, and then it is not linearly independent.
