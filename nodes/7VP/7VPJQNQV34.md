---
tag: 7VPJQNQV34
kind: definition
name: Face of a convex set
msc: [52A20, 52A05]
defines: KY7SB854VH
uses: [000AYPA9AJ, 02AS45T3H9, WD3RJZC5A7, CCZA91NE5X, 3MSGFJM2NX, K7N565NKCV]
sources:
  - url: https://en.wikipedia.org/wiki/Face_(geometry)
---

## Definition

Let $V$ be a real [[vector space|000AYPA9AJ]] and let $C \subseteq V$ be a [[convex set|02AS45T3H9]].
A *face* of $C$ is a subset $F \subseteq C$ such that:

1. $F$ is convex;
2. $F$ is an [[extreme set|WD3RJZC5A7]] of $C$: if $x_1, x_2 \in C$ and the [[open segment|CCZA91NE5X]] $(x_1, x_2)$ meets $F$, then $x_1, x_2 \in F$.

## Remarks

The empty set and $C$ are faces of $C$.
A one-point set $\set{x}$ is a face exactly when $x$ is an [[extreme point|3MSGFJM2NX]] of $C$.
A face of a face of $C$ is a face of $C$.

Example: for the square $C = [0, 1]^2$, the edge $F = [0, 1] \times \set{1}$ is a face.
It is convex.
If a point of $F$ lies strictly between $x_1, x_2 \in C$, the second coordinates of $x_1, x_2$ are at most $1$ and average to $1$ with positive weights.
So both equal $1$, and $x_1, x_2 \in F$.

Non-example: the lower half $F = [0, 1] \times [0, 1/2]$ of the same square is convex, but the point $(1/2, 1/2) \in F$ lies strictly between $(1/2, 0)$ and $(1/2, 1)$, and $(1/2, 1) \notin F$, so clause 2 fails.

If $H$ is a [[supporting hyperplane|K7N565NKCV]] of $C$, then $C \cap H$ is a face, called an exposed face.
Not every face is exposed: in the stadium, the convex hull of two unit discs centred at $(\pm 1, 0)$, the point $(1, 1)$ is a face but not an exposed face.
