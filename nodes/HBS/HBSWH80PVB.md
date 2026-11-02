---
tag: HBSWH80PVB
kind: definition
name: Bounded lattice
msc: [06B05]
defines: 72V1Z82M5F
uses: [WH4SFAACAS, 0XR2QK49V6, 0AANKKNHS4]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_lattice
---

## Definition

A *bounded lattice* is a [[lattice|WH4SFAACAS]] $(L, \le)$ that has a [[greatest element|0XR2QK49V6]] and a [[least element|0AANKKNHS4]].
The greatest element is written $1$ or $\top$, and the least element is written $0$ or $\bot$.

Algebraic form: a bounded lattice is a lattice $(L, \vee, \wedge)$ with two elements $0, 1 \in L$ such that $x \vee 0 = x$ and $x \wedge 1 = x$ for all $x \in L$.

## Remarks

The two forms agree: $x \vee 0 = x$ for all $x$ says $0 \le x$ for all $x$, and $x \wedge 1 = x$ says $x \le 1$.
Then also $x \wedge 0 = 0$ and $x \vee 1 = 1$.
Example: the power set of a set $X$, ordered by $\subseteq$, is a bounded lattice with $0 = \emptyset$ and $1 = X$.
Every subset $A$ satisfies $\emptyset \subseteq A \subseteq X$.
Non-example: $(\Z, \le)$ is a lattice with $x \vee y = \max(x, y)$ and $x \wedge y = \min(x, y)$, but it has no greatest element.
Every finite nonempty lattice $L$ is bounded, with $1 = \bigvee L$ and $0 = \bigwedge L$, the join and the meet of all its elements.
