---
tag: 0Q8HZTJC7G
kind: definition
name: Orthogonal projection
msc: [15A04, 46C05]
topics: [8GQVME4SZZ]
audience: ug1
defines: 0B8KZRT28M
uses: [0SP7P0G7KQ, 0RH4E3CAV9, 079D68S3AW]
formal:
  - system: lean4
    library: mathlib
    decl: Submodule.orthogonalProjection
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
    locator: Orthogonal projections
  - book: isbn:9783031410253
    locator: Section 6C
---

## Definition

Let $V$ be an inner product space over $\R$ or $\C$, and let $U$ be a finite-dimensional subspace of $V$, with [[orthogonal complement|079D68S3AW]] $U^\perp$.
By the [[orthogonal decomposition|0SP7P0G7KQ]], each $v \in V$ is $v = u + u'$ with unique $u \in U$ and $u' \in U^\perp$.
The *orthogonal projection* onto $U$ is the map $P_U \colon V \to V$, $P_U(v) = u$.

## Notation

Other names are $\operatorname{proj}_U$ and $\pi_U$.
In Mathlib, `Submodule.orthogonalProjection U` has codomain `U`; it needs `U` to be complete, which holds for finite-dimensional `U`.

## Remarks

$P_U$ is the [[projection|0RH4E3CAV9]] onto $U$ along $U^\perp$.
The [[formulas for the orthogonal projection|~680b213e]] prove that it is linear and give it in an orthonormal basis and as a matrix.
For the line spanned by $a \ne 0$, $P(v) = \frac{\ip{v}{a}}{\ip{a}{a}} a$.
$P_U(v)$ is the point of $U$ [[closest to v|0MCDDSCB9Z]].

## Explanations

### L1 human

The orthogonal projection drops a perpendicular from a vector onto a subspace.
The foot of the perpendicular is the projection.
In $\R^3$, the projection onto the $xy$-plane sets the $z$-coordinate to zero.

### L2 human

For $U = \R(1, 0)$ in $\R^2$ and $v = (3, 4)$, the splitting is $(3, 4) = (3, 0) + (0, 4)$.
The first part lies in $U$ and the second part lies in $U^\perp = \R(0, 1)$, so $P_U(3, 4) = (3, 0)$.
The trap is to split along a line that is not orthogonal to $U$: $(3, 4) = (-1, 0) + (4, 4)$ is also a splitting, but $(4, 4) \notin U^\perp$.
