---
tag: DMWEBMB1RS
kind: definition
name: Pointed cone
msc: [52A20, 46A55]
defines: J9HA54ACME
uses: [000AYPA9AJ, 6VE4KA12VD]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_cone
---

## Definition

Let $V$ be a real [[vector space|000AYPA9AJ]].
A *pointed cone* in $V$ is a [[convex cone|6VE4KA12VD]] $C \subseteq V$ with $0 \in C$.

## Remarks

Equivalently, $C$ is nonempty and $\alpha x + \beta y \in C$ for all $x, y \in C$ and all real $\alpha, \beta \ge 0$.
In this form a pointed cone is a submodule of $V$ over the semiring of nonnegative reals.

Example: the closed upper half-plane $H = \set{(x, y) \in \R^2 : y \ge 0}$.
It is closed under sums and positive multiples, and it contains $(0, 0)$.
It contains the whole $x$-axis, so it is pointed in this sense but not salient.

Non-example: the open quadrant $\set{(x, y) : x > 0, y > 0}$ is a convex cone, but it does not contain $(0, 0)$.

Warning on terminology: many texts on convex analysis say pointed for a convex cone $C$ with $C \cap (-C) \subseteq \set{0}$, that is, a cone that contains no line.
That property is called salient here.
