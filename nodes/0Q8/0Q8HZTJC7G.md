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

The orthogonal projection onto a subspace keeps the part of each vector that lies in the subspace and drops the part that is orthogonal to it.

Let $V$ be an inner product space over $\R$ or $\C$, and let $U$ be a finite-dimensional subspace of $V$, with [[orthogonal complement|079D68S3AW]] $U^\perp$.
By the [[orthogonal decomposition|0SP7P0G7KQ]], each $v \in V$ can be written as $v = u + u'$ with $u \in U$ and $u' \in U^\perp$, and the pair $(u, u')$ is unique.
The *orthogonal projection* onto $U$ is the map
$$P_U \colon V \to V, \qquad P_U(v) = u.$$

## Notation

Books also write $\operatorname{proj}_U$ or $\pi_U$.
In Mathlib, `Submodule.orthogonalProjection U` has codomain `U` rather than `V`, and it needs `U` to be complete, which every finite-dimensional `U` is.

## Remarks

The definition rests on the splitting $v = u + u'$, and each condition is there to make that splitting exist and be unique.
Uniqueness comes from $U \cap U^\perp = \{0\}$, which holds in every inner product space because a vector orthogonal to itself is zero.
Existence is where finite dimension of $U$ enters: the proof of the orthogonal decomposition builds $u$ from an orthonormal basis of $U$.
Without it the splitting can fail, as in [[the counterexample in l2|DNZF0R4VMZ]], where the finitely supported sequences have orthogonal complement $\{0\}$.

A small case shows how the splitting works.
For $U = \R(1, 0)$ in $\R^2$ and $v = (3, 4)$, we have $(3, 4) = (3, 0) + (0, 4)$, with $(3, 0) \in U$ and $(0, 4) \in U^\perp = \R(0, 1)$.
So $P_U(3, 4) = (3, 0)$.
The splitting $(3, 4) = (-1, 0) + (4, 4)$ also has its first part in $U$, but $(4, 4)$ is not orthogonal to $(1, 0)$, so it is not the splitting of the definition.
Any other complement of $U$ gives a [[projection|0RH4E3CAV9]] too, but an oblique one; the orthogonal projection is the one whose kernel is $U^\perp$.

The [[concept page|0B8KZRT28M]] develops the idea, the [[formulas for the orthogonal projection|AK3JJ5HHG2]] prove that $P_U$ is linear and give its matrix, and the [[best approximation theorem|0MCDDSCB9Z]] shows that $P_U(v)$ is the point of $U$ closest to $v$.

## Explanations

### L1 human

The orthogonal projection drops a perpendicular from a vector onto a subspace, and the foot of the perpendicular is the answer.
In space, the projection onto the floor keeps the two horizontal coordinates and sets the height to zero.
So the point $(2, 5, 7)$ goes to $(2, 5, 0)$.

### L2 human

For a line $U = \R a$ with $a \ne 0$, the definition gives a formula at once.
Try $u = c a$ and ask that $v - c a$ be orthogonal to $a$:
$$\ip{v - c a}{a} = \ip{v}{a} - c \ip{a}{a} = 0, \qquad \text{so} \qquad c = \frac{\ip{v}{a}}{\ip{a}{a}}.$$
For $a = (1, 1)$ and $v = (3, 1)$ this gives $c = 2$ and $P_U v = (2, 2)$.
Check: $v - P_U v = (1, -1)$, and $(1, -1) \cdot (1, 1) = 0$.
Watch out: the splitting must use $U^\perp$, and a splitting along another line gives a different vector.
