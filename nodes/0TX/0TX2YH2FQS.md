---
tag: 0TX2YH2FQS
kind: definition
name: Symmetric bilinear form associated with a quadratic form
msc: ["15A63", "11E04"]
defines: 0KRVRV5V80
topics: [6TSCEW8QMK]
audience: ug1
uses: [0HZNE5QZDJ, 02STTYFBVY, 0744CN4MDA]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Definitions
---

## Definition

When $2$ can be inverted, each quadratic form comes from exactly one symmetric bilinear form, and this definition names it.
Let $F$ be a field of characteristic not $2$, let $V$ be a finite-dimensional vector space over $F$, and let $Q$ be a [[quadratic form|0HZNE5QZDJ]] on $V$.
The *symmetric bilinear form associated with* $Q$ is
$$B(u, v) = \tfrac{1}{2} \bigl( Q(u + v) - Q(u) - Q(v) \bigr) \qquad (u, v \in V).$$

## Remarks

The form $B$ is half of the [[polar form|02STTYFBVY]] $b_Q$, so it is a [[symmetric bilinear form|0744CN4MDA]].
The factor $\tfrac{1}{2}$ is chosen so that $B(v, v) = \tfrac{1}{2} \cdot 2Q(v) = Q(v)$, and the hypothesis on the characteristic is exactly what makes $\tfrac{1}{2}$ exist.
By [[the correspondence theorem|VN9AG8JKYT]], $B$ is the only symmetric bilinear form with $B(v, v) = Q(v)$, and every symmetric bilinear form arises this way from $v \mapsto B(v, v)$.

For example, take $Q(x, y) = x^2 + 4xy$ on $\mathbb{R}^2$.
Its polar form is $2xx' + 4(xy' + x'y)$, so $B(u, v) = xx' + 2xy' + 2x'y$, with matrix $\begin{pmatrix} 1 & 2 \\ 2 & 0 \end{pmatrix}$.
In general, for $Q(x) = x^{\mathsf{T}} A x$ with $A$ symmetric, $B(x, y) = x^{\mathsf{T}} A y$.

The definition fails in characteristic $2$, and not only because $\tfrac{1}{2}$ is missing.
Over $\mathbb{F}_2$ the form $xy$ is $B(v, v)$ for no symmetric bilinear form $B$ at all, as [[the example over F₂|ZEGSCCVGZF]] shows.

## Explanations

### L1 human

Outside characteristic $2$, a quadratic form and its symmetric bilinear form are the same information written in two ways.
From $B$ you get $Q$ by putting the same vector in both places.
From $Q$ you get $B$ by the formula above.
For $Q(x, y) = x^2 + y^2$ the formula gives the dot product $xx' + yy'$.
