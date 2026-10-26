---
tag: 0Q8HZTJC7G
kind: definition
name: Orthogonal projection
msc: [15A04, 46C05]
defines: 0B8KZRT28M
uses: [0SP7P0G7KQ, 0RH4E3CAV9]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
    locator: Orthogonal projections
---

## Definition

Let $V$ be an inner product space over $\R$ or $\C$, and let $W$ be a finite-dimensional subspace of $V$.
By the [[orthogonal decomposition|0SP7P0G7KQ]], each $v \in V$ is $v = w + w'$ with unique $w \in W$ and $w' \in W^\perp$.
The *orthogonal projection* onto $W$ is the map $P_W \colon V \to V$, $P_W(v) = w$.

## Remarks

$P_W$ is a linear [[projection|033DA1WE8Y]] with image $W$ and kernel $W^\perp$, and it is self-adjoint.
For an orthonormal basis $e_1, \dots, e_k$ of $W$, $P_W(v) = \sum_{i=1}^{k} \langle v, e_i \rangle e_i$.
For the line spanned by $u \ne 0$, $P(v) = \frac{\langle v, u \rangle}{\langle u, u \rangle} u$.
$P_W(v)$ is the point of $W$ [[closest to $v$|0MCDDSCB9Z]].

## Explanations

### L1 human

The orthogonal projection drops a perpendicular from a vector onto a subspace.
The foot of the perpendicular is the projection.
In $\R^3$, projecting onto the $xy$-plane sets the $z$-coordinate to zero.
