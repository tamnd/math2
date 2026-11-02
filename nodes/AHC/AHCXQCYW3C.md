---
tag: AHCXQCYW3C
kind: definition
name: Quadric
msc: ["51N15", "51A50", "14J70"]
defines: Q3Q4FF23VG
uses: [04C5ZBG1WT, 000AYPA9AJ, ZT9A6JK8QF, 0RBQS1JJCR]
sources:
  - url: https://en.wikipedia.org/wiki/Quadric
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]], let $V$ be a [[vector space|000AYPA9AJ]] over $F$ of finite dimension $n + 1 \ge 2$, and let $\mathbb{P}(V)$ be its [[projective space|ZT9A6JK8QF]].
Let $Q$ be a nonzero [[quadratic form|0RBQS1JJCR]] on $V$.
For a nonzero vector $v$, write $\langle v \rangle$ for the point of $\mathbb{P}(V)$ that it spans.
The *(projective) quadric* of $Q$ is the set
$$\set{\langle v \rangle \in \mathbb{P}(V) : Q(v) = 0}.$$
It is well defined because $Q(\lambda v) = \lambda^2 Q(v)$.
An *affine quadric* in $F^n$ is the set of zeros of a polynomial of degree exactly $2$ in $n$ variables with coefficients in $F$.

## Remarks

Example: in $\mathbb{P}^3(F)$, the form $Q(x) = x_0 x_1 + x_2 x_3$ defines a quadric that contains the line of points $[s : 0 : t : 0]$, since $Q(s, 0, t, 0) = 0$ for all $s, t$.
Example: the sphere $x^2 + y^2 + z^2 = 1$ in $\R^3$ is an affine quadric, and $x^2 + y^2 + z^2 - w^2 = 0$ is its projective closure.

Non-example: the zero set of $y - x^3$ in $F^2$ is not an affine quadric, because the polynomial has degree $3$.

For $n = 2$ the projective quadrics are the [[projective conics|R3TMVHTP3A]].
Different forms can define the same point set.
For example, over $\R$ every positive definite form defines the empty quadric.
For this reason the quadric is often taken together with its form, up to a nonzero scalar.
