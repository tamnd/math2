---
tag: N2Q4RS43FD
kind: definition
name: Complete lattice
msc: [06B23]
defines: D7A0ZGZT5S
uses: [0QV2JS9RJ3, 0R3H5PANRQ, 0QF1MZ9FRG, WH4SFAACAS]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_lattice
---

## Definition

Let $(L, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
It is a *complete lattice* if every subset $S \subseteq L$ has a [[supremum|0R3H5PANRQ]] $\bigvee S$ and an [[infimum|0QF1MZ9FRG]] $\bigwedge S$ in $L$.

## Remarks

It is enough to ask that every subset has a supremum: then $\bigwedge S$ is the supremum of the set of lower bounds of $S$.
Taking $S = \varnothing$ shows that a complete lattice has a least element $\bigvee \varnothing$ and a greatest element $\bigwedge \varnothing$; in particular it is nonempty.
Every complete lattice is a [[lattice|WH4SFAACAS]], and every finite nonempty lattice is complete.
Example: for a set $X$, the power set of $X$ ordered by inclusion is complete, with $\bigvee S = \bigcup S$ and $\bigwedge S = \bigcap S$, where $\bigcap \varnothing = X$.
Non-example: $\Q$ with its usual order is a lattice but not complete, because $\set{q \in \Q : q^2 < 2}$ has no supremum in $\Q$.
