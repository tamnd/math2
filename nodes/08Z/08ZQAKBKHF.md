---
tag: 08ZQAKBKHF
kind: definition
name: Alternating bilinear form
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
defines: 0DGDS5XY84
uses: [0P799D6AMN]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Symmetric, skew-symmetric, and alternating forms
inventory: [JEX1WKZNKA]
---

## Definition

Let $F$ be a field and let $V$ be a vector space over $F$.
A [[bilinear form|0SQZMXB6GP]] $B$ on $V$ is *alternating* when
$$B(v, v) = 0 \qquad \text{for all } v \in V.$$
It is *skew-symmetric* when $B(u, v) = -B(v, u)$ for all $u, v \in V$.

## Notation

An alternating form is often written $\omega$.
Some books say "antisymmetric" for skew-symmetric.

## Remarks

An alternating form is skew-symmetric, and if the characteristic of $F$ is not $2$, each skew-symmetric form is alternating, by [[this statement|SX9CD5NEPD]].
In characteristic $2$ the two notions differ: the form $x_1 y_1$ on $\mathbb{F}_2$ is skew-symmetric but not alternating.
On $F^2$, the form $B(x, y) = x_1 y_2 - x_2 y_1$ is alternating; it is the determinant of the matrix with the columns $x$ and $y$.
A nondegenerate alternating form is a *symplectic form*.

## Explanations

### L1 human

An alternating form gives zero when both vectors are equal.
Then swapping the two vectors changes the sign of the value.
The signed area of the parallelogram spanned by two plane vectors is an example.

### L2 human

To test the definition with a matrix $A$, check that $A^T = -A$ and that every diagonal entry of $A$ is $0$.
For $A = \begin{pmatrix} 0 & 5 \\ -5 & 0 \end{pmatrix}$ both conditions hold, so $5(x_1 y_2 - x_2 y_1)$ is alternating.
A trap: in characteristic $2$ the first condition alone is not enough.
