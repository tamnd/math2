---
tag: 0HZNE5QZDJ
kind: definition
name: Quadratic form
msc: ["15A63", "11E04"]
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

A quadratic form is a function on a vector space that scales like a square and whose failure to be additive is bilinear.
Let $F$ be a field and let $V$ be a finite-dimensional [[vector space|05EGHEQZAW]] over $F$.
A *quadratic form* on $V$ is a map $Q \colon V \to F$ such that:

1. $Q(av) = a^2 Q(v)$ for all $a \in F$ and $v \in V$;
2. the map $b_Q \colon V \times V \to F$, $b_Q(u, v) = Q(u + v) - Q(u) - Q(v)$, is a [[bilinear form|0P799D6AMN]] on $V$.

## Notation

The bilinear form $b_Q$ of condition 2 is the [[polar form|0HYFWKKY3C]] of $Q$.
Two quadratic forms $Q$ on $V$ and $Q'$ on $V'$ are *equivalent* when $Q' = Q \circ T$ for a linear bijection $T \colon V' \to V$.
In Mathlib, `QuadraticForm R M` is defined for a module $M$ over a commutative ring $R$, by the same two conditions.

## Remarks

Condition 1 makes $Q$ behave like a square under scaling, and it gives $Q(0) = 0$ and $Q(-v) = Q(v)$.
Condition 1 alone is too weak, because there are many functions with this scaling that are not polynomials.
For example, [[the function x⁴/(x² + y²)|AN5RQ78DD8]] on $\mathbb{R}^2$ satisfies condition 1 but fails condition 2.
Condition 2 is what forces $Q$ to be a homogeneous polynomial of degree $2$ in the coordinates of every basis, as [[the concept of a quadratic form|0RBQS1JJCR]] shows.

Here is a small example.
For $Q(x, y) = x^2 + 3xy + 2y^2$ on $\mathbb{R}^2$, condition 1 holds because every term picks up the factor $a^2$:
$$Q(ax, ay) = a^2 x^2 + 3a^2 xy + 2a^2 y^2 = a^2 Q(x, y).$$
For condition 2, expand with $u = (x, y)$ and $v = (x', y')$:
$$Q(u + v) - Q(u) - Q(v) = 2xx' + 3(xy' + x'y) + 4yy'.$$
Each term is a product of one coordinate of $u$ and one coordinate of $v$, so $b_Q$ is bilinear.

The definition does not mention a matrix and does not divide by $2$.
That is why it also works in characteristic $2$, where a quadratic form is more than a symmetric bilinear form.
When the characteristic of $F$ is not $2$, the form $Q$ is $x^{\mathsf{T}} A x$ for exactly one symmetric matrix $A$, with $a_{ii} = c_{ii}$ and $a_{ij} = a_{ji} = \tfrac{1}{2} c_{ij}$ for the coefficients $c_{ij}$ of $Q$.
For the example above, $A = \begin{pmatrix} 1 & 3/2 \\ 3/2 & 2 \end{pmatrix}$.

## Explanations

### L1 human

A quadratic form is a polynomial in which every term has degree two, such as $x^2 - 4xy + y^2$.
Double each variable and every term gets four times bigger, so the whole value gets four times bigger.
The squared length $x^2 + y^2$ of an arrow in the plane is the main example.

### L2 human

To test a candidate $Q$, check the two conditions in order.
For $Q(x, y) = x^2 - y^2$, the scaling gives $a^2 x^2 - a^2 y^2 = a^2 Q(x, y)$.
The polar form is
$$(x + x')^2 - (y + y')^2 - x^2 + y^2 - x'^2 + y'^2 = 2xx' - 2yy',$$
which is bilinear, so $Q$ is a quadratic form.
Watch out: a function that passes the first test can still fail the second one, so always compute the polar form.
