---
tag: PT9FSNP9T5
kind: definition
name: Killing vector field
msc: [53B20, 53C20]
defines: 5AKNNW3W4Z
uses: [GH6CXWFNDJ, PJWK0PKN6Q, CAZYGE1T4E, WY6K3P4YCG]
sources:
  - url: https://en.wikipedia.org/wiki/Killing_vector_field
---

## Definition

Let $(M, g)$ be a [[pseudo-Riemannian manifold|GH6CXWFNDJ]].
Let $X$ be a smooth vector field on $M$, that is, a smooth section of the [[tangent bundle|WY6K3P4YCG]].
It is a *Killing vector field* if the [[Lie derivative|PJWK0PKN6Q]] of $g$ along $X$ vanishes:
$$\mathcal{L}_X g = 0.$$

## Remarks

Equivalently, with the [[Levi-Civita connection|CAZYGE1T4E]] $\nabla$, the field $X$ is Killing if and only if $g(\nabla_Y X, Z) + g(Y, \nabla_Z X) = 0$ for all vector fields $Y, Z$.
In coordinates this is Killing's equation $\nabla_i X_j + \nabla_j X_i = 0$.
Another equivalent form: the local flow of $X$ consists of isometries.

Example: on $\R^2$ with the Euclidean metric, the rotation field $X = -y \, \partial_x + x \, \partial_y$ has $\nabla X$ given by the constant matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, which is antisymmetric, so Killing's equation holds.

Non-example: on $\R^2$, the field $X = x \, \partial_x + y \, \partial_y$ has $\nabla X$ equal to the identity matrix, which is not antisymmetric; indeed $\mathcal{L}_X g = 2g \ne 0$.

The Killing fields of $(M, g)$ form a Lie algebra under the Lie bracket, of dimension at most $n(n + 1)/2$ on a connected manifold of dimension $n$.
