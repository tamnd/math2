---
tag: KSPDXANYC0
kind: definition
name: Extreme set
msc: [52A05, 46A55]
defines: WD3RJZC5A7
uses: [000AYPA9AJ, CCZA91NE5X, 3MSGFJM2NX]
sources:
  - url: https://en.wikipedia.org/wiki/Extreme_point
---

## Definition

Let $V$ be a real [[vector space|000AYPA9AJ]] and let $B \subseteq A \subseteq V$.
The set $B$ is an *extreme set* of $A$ if the following holds.
For all $x_1, x_2 \in A$ and $x \in B$ with $x \in (x_1, x_2)$, both $x_1$ and $x_2$ lie in $B$.
Here $(x_1, x_2)$ is the [[open segment|CCZA91NE5X]] between $x_1$ and $x_2$.

## Remarks

A point $x \in A$ is an [[extreme point|3MSGFJM2NX]] of $A$ exactly when $\set{x}$ is an extreme set of $A$.
The sets $\emptyset$ and $A$ are always extreme sets of $A$, and an extreme set of an extreme set of $A$ is an extreme set of $A$.

Example: for $A = [0, 1]^2$, the bottom edge $B = [0, 1] \times \set{0}$ is an extreme set.
Let $x \in B$ lie in $(x_1, x_2)$ with $x_1, x_2 \in A$.
The second coordinates of $x_1, x_2$ are $\ge 0$, and an average of them with positive weights is $0$.
So both are $0$, and $x_1, x_2 \in B$.

Non-example: the diagonal $D = \set{(s, s) : 0 \le s \le 1}$ of the same square.
The point $(1/2, 1/2) \in D$ lies in the open segment between $(1, 0)$ and $(0, 1)$, which are in $A$ but not in $D$.
