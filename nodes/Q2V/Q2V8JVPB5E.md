---
tag: Q2V8JVPB5E
kind: definition
name: Homogeneous coordinates
msc: [51N15, 14N05]
defines: FS9FRJ17D2
uses: [ZT9A6JK8QF, 0W95W33CMP]
sources:
  - url: https://en.wikipedia.org/wiki/Homogeneous_coordinates
---

## Definition

Let $k$ be a field and let $n \ge 0$.
A point $p$ of the [[projective space|ZT9A6JK8QF]] $\mathbb{P}^n(k)$ is an [[equivalence class|0W95W33CMP]] of nonzero vectors of $k^{n+1}$.
Two vectors are equivalent when one is a nonzero scalar multiple of the other.
A tuple $(x_0, \dots, x_n) \in k^{n+1} \setminus \set{0}$ in this class is a tuple of *homogeneous coordinates* of $p$, and one writes $p = [x_0 : \dots : x_n]$.

## Remarks

Two tuples are homogeneous coordinates of the same point exactly when they differ by a nonzero factor $\lambda \in k$.

Example: in $\mathbb{P}^2(\R)$, $[1 : 2 : 3] = [-2 : -4 : -6]$.
Check: $(-2, -4, -6) = -2 \cdot (1, 2, 3)$.

Non-example: $(0, 0, 0)$ is not a tuple of homogeneous coordinates of any point, since the zero vector is excluded.

The affine point $(x_1, \dots, x_n)$ of $k^n$ corresponds to $[x_1 : \dots : x_n : 1]$; the points with last coordinate $0$ form the hyperplane at infinity.
For a homogeneous polynomial $F$, the condition $F(x_0, \dots, x_n) = 0$ does not depend on the chosen coordinates of a point, since $F(\lambda x) = \lambda^d F(x)$ for $F$ of degree $d$.
