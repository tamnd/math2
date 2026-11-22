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

An alternating bilinear form is a bilinear form that vanishes on every pair of equal vectors, and a skew-symmetric form is one that changes sign when its arguments swap.
Let $F$ be a field and let $V$ be a vector space over $F$.
A [[bilinear form|0SQZMXB6GP]] $B$ on $V$ is *alternating* when
$$B(v, v) = 0 \qquad \text{for all } v \in V.$$
It is *skew-symmetric* when $B(u, v) = -B(v, u)$ for all $u, v \in V$.

## Notation

An alternating form is often written $\omega$.
Some books say "antisymmetric" for skew-symmetric, and a few say "skew-symmetric" for alternating.
A nondegenerate alternating form is called a *symplectic form*.

## Remarks

The alternating condition is about one vector at a time, while the skew-symmetric condition is about pairs.
The first gives the second in every field: expand $0 = B(u + v, u + v)$ by bilinearity and drop the two terms $B(u, u)$ and $B(v, v)$, which leaves $B(u, v) + B(v, u) = 0$.
The second gives the first only when $1 + 1 \ne 0$ in $F$, by the [[relation of the two notions|SX9CD5NEPD]].

For example, $B(x, y) = x_1 y_2 - x_2 y_1$ on $F^2$ is alternating, since $B(x, x) = x_1 x_2 - x_2 x_1 = 0$; it is the determinant of the matrix with columns $x$ and $y$.
The form $B(x, y) = xy$ on the one-dimensional space $\mathbb{F}_2$ fails the alternating condition, since $B(1, 1) = 1$.
It is still skew-symmetric, because $-1 = 1$ in $\mathbb{F}_2$, so in characteristic $2$ the two words name different classes.
The concept page [[alternating bilinear form|0DGDS5XY84]] gives the matrix test, more examples and the classification.

## Explanations

### L1 human

An alternating form gives zero when both vectors are the same.
The signed area of the parallelogram spanned by two arrows in the plane is an example: an arrow with itself spans no area.
Swapping the two arrows then changes the sign of the area.

### L2 human

To test the definition with a matrix $A$, check that $A^{\mathsf{T}} = -A$ and that every diagonal entry of $A$ is $0$.
For $A = \begin{pmatrix} 0 & 5 \\ -5 & 0 \end{pmatrix}$ over $\mathbb{Q}$ both conditions hold, so $B(x, y) = 5(x_1 y_2 - x_2 y_1)$ is alternating.
Check: $B(x, x) = 5(x_1 x_2 - x_2 x_1) = 0$.
Watch out: in characteristic $2$ the first condition alone says only that $A$ is symmetric, so the diagonal test is the one that matters.
