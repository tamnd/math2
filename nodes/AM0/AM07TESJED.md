---
tag: AM07TESJED
kind: definition
name: Quaternion algebra
msc: [16K20, 11R52]
defines: ZWXW0T3EAC
uses: [04C5ZBG1WT, 0F6ES3BRYP, 3CTW1P4HBP, 5HRKJBAY2V]
sources:
  - url: https://en.wikipedia.org/wiki/Quaternion_algebra
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]].
A *quaternion algebra* over $F$ is a [[central simple algebra|5HRKJBAY2V]] over $F$ of dimension $4$.

Let the [[characteristic|0F6ES3BRYP]] of $F$ be different from $2$, and let $a, b \in F$ be nonzero.
The quaternion algebra $\left(\frac{a, b}{F}\right)$ is the [[associative algebra|3CTW1P4HBP]] over $F$ with basis $1, i, j, k$ and multiplication determined by
$$i^2 = a, \qquad j^2 = b, \qquad ij = -ji = k.$$

## Remarks

When the characteristic of $F$ is not $2$, every quaternion algebra over $F$ is isomorphic to $\left(\frac{a, b}{F}\right)$ for some nonzero $a, b$.
In this algebra $k^2 = -ab$.

Example: $\left(\frac{-1, -1}{\R}\right)$ is Hamilton's algebra $\mathbb{H}$ of quaternions.
The element $q = x + yi + zj + wk$ has $q \bar{q} = x^2 + y^2 + z^2 + w^2$ for $\bar{q} = x - yi - zj - wk$, so every $q \ne 0$ is invertible, and $\mathbb{H}$ is a division algebra.

Example: $\left(\frac{1, 1}{F}\right) \cong M_2(F)$, through $i \mapsto \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ and $j \mapsto \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

Non-example: the algebra $F[x, y]/(x^2 - a, y^2 - b, xy - yx)$ also has dimension $4$, but it is commutative, so its center is not $F$ and it is not a quaternion algebra.

Every quaternion algebra is either a division algebra or isomorphic to $M_2(F)$.
The algebra $\left(\frac{a, b}{F}\right)$ is isomorphic to $M_2(F)$ if and only if the equation $a x^2 + b y^2 = 1$ has a solution with $x, y \in F$.
