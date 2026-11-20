---
tag: 0HZNE5QZDJ
kind: definition
name: Quadratic form
msc: [15A63, "11E04"]
topics: [6TSCEW8QMK]
audience: ug1
defines: 0RBQS1JJCR
uses: [05EGHEQZAW, 0P799D6AMN]
formal:
  - system: lean4
    library: mathlib
    decl: QuadraticForm
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Definitions
  - book: isbn:9780387728285
---

## Definition

Let $F$ be a field and let $V$ be a finite-dimensional vector space over $F$.
A *quadratic form* on $V$ is a map $Q \colon V \to F$ such that:

1. $Q(av) = a^2 Q(v)$ for all $a \in F$ and $v \in V$.
2. The map $(u, v) \mapsto Q(u + v) - Q(u) - Q(v)$ is a [[bilinear form|0SQZMXB6GP]] on $V$.

## Notation

The bilinear form of condition 2 is the [[polar form|0HYFWKKY3C]] $b_Q$ of $Q$.
Two quadratic forms $Q$ on $V$ and $Q'$ on $V'$ are *equivalent* when $Q' = Q \circ T$ for a linear bijection $T \colon V' \to V$.

## Remarks

On $F^n$, the quadratic forms are the maps $Q(x) = \sum_{i \le j} c_{ij} x_i x_j$, that is, the homogeneous polynomials of degree $2$.
In matrix notation, $Q(x) = x^T A x$ for an $n \times n$ matrix $A$.
If the characteristic of $F$ is not $2$, the matrix $A$ can be chosen symmetric, and then it is unique: $a_{ii} = c_{ii}$ and $a_{ij} = a_{ji} = \frac12 c_{ij}$ for $i < j$.
For example, $Q(x, y) = x^2 + 3xy + 2y^2$ is a quadratic form on $\R^2$, with the symmetric matrix $\begin{pmatrix} 1 & 3/2 \\ 3/2 & 2 \end{pmatrix}$.
In Mathlib, `QuadraticForm R M` is defined for a module $M$ over a commutative ring $R$, with the same two conditions.

## Explanations

### L1 human

A quadratic form is a polynomial in which every term has degree two, such as $x^2 - 4xy + y^2$.
It is the simplest kind of function after linear functions.
The squared length $x_1^2 + \cdots + x_n^2$ is the main example.

### L2 human

To check that $Q(x, y) = x^2 + 3xy + 2y^2$ satisfies the definition, we test the two conditions.

1. $Q(ax, ay) = a^2 x^2 + 3a^2 xy + 2a^2 y^2 = a^2 Q(x, y)$.
2. $Q(x + x', y + y') - Q(x, y) - Q(x', y') = 2xx' + 3(xy' + x'y) + 4yy'$, which is bilinear in $(x, y)$ and $(x', y')$.

A trap: condition 1 alone does not make $Q$ a quadratic form, as [[the function $x^4 / (x^2 + y^2)$|AN5RQ78DD8]] shows.
