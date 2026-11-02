---
tag: T7B1WJVT9Z
kind: definition
name: Projective transformation
msc: [51N15, 51A10]
defines: P1MKTF7MWQ
uses: [ZT9A6JK8QF, 0EB9N0S33C, 0FCHE902D7]
sources:
  - url: https://en.wikipedia.org/wiki/Homography
---

## Definition

Let $V$ and $W$ be vector spaces of the same finite dimension over a field $k$.
Let $\mathbb{P}(V)$ and $\mathbb{P}(W)$ be their [[projective spaces|ZT9A6JK8QF]].
For a nonzero vector $v$, write $[v]$ for the point spanned by $v$.
A *projective transformation* (or *homography*) from $\mathbb{P}(V)$ to $\mathbb{P}(W)$ is a map of the form
$$[v] \mapsto [T v],$$
where $T \colon V \to W$ is an invertible linear map.

## Remarks

The map is well defined, since $T(\lambda v) = \lambda T v$, and it is a bijection.
In coordinates, a projective transformation of $\mathbb{P}^n(k)$ is $[x] \mapsto [A x]$ for an [[invertible matrix|0EB9N0S33C]] $A$ of size $n + 1$.
Two matrices give the same map exactly when they differ by a nonzero scalar factor.
So the projective transformations of $\mathbb{P}^n(k)$ form the group $\mathrm{PGL}(n + 1, k) = \mathrm{GL}(n + 1, k) / k^{\times}$, a quotient of the [[general linear group|0FCHE902D7]].

Example: on $\mathbb{P}^1(\C)$, with $z = x_0 / x_1$, the matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $ad - bc \ne 0$ gives $z \mapsto (az + b)/(cz + d)$.
Check: $[x_0 : x_1] \mapsto [a x_0 + b x_1 : c x_0 + d x_1]$, and dividing gives $(az + b)/(cz + d)$.

Non-example: on $\mathbb{P}^2(\C)$ the map $[x_0 : x_1 : x_2] \mapsto [\bar x_0 : \bar x_1 : \bar x_2]$ is a bijection that maps lines to lines, but it is not a projective transformation.
It fixes the four points $[1:0:0]$, $[0:1:0]$, $[0:0:1]$, $[1:1:1]$ without being the identity.
A projective transformation of the plane that fixes four points in general position is the identity, so this map is not one.

Every projective transformation maps projective subspaces to projective subspaces of the same dimension and preserves the [[cross-ratio|09ASMRMD67]].
