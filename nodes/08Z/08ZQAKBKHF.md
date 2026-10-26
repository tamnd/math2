---
tag: 08ZQAKBKHF
kind: definition
name: Alternating bilinear form
msc: [15A63]
defines: 0DGDS5XY84
uses: [0P799D6AMN]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: "Symmetric, skew-symmetric, and alternating forms"
---

## Definition

Let $F$ be a field and let $V$ be a vector space over $F$.
A [[bilinear form|0SQZMXB6GP]] $B$ on $V$ is *alternating* when
$$B(v, v) = 0 \qquad \text{for all } v \in V.$$

## Remarks

An alternating form is *skew-symmetric*: $B(u, v) = -B(v, u)$ for all $u, v$.
If the characteristic of $F$ is not $2$, each skew-symmetric form is alternating.
On $F^2$, the form $B(x, y) = x_1 y_2 - x_2 y_1$ is alternating; it is the determinant of the matrix with the columns $x$ and $y$.
A nondegenerate alternating form is a *symplectic form*.

## Explanations

### L1 human

An alternating form gives zero when both vectors are equal.
Then swapping the two vectors changes the sign of the value.
The signed area of the parallelogram spanned by two plane vectors is an example.
