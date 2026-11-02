---
tag: HH2EM3DPNK
kind: statement
role: theorem
name: Gabrielov's theorem of the complement
msc: [32B20, 14P15, 03C64]
uses: [K1HTQF26MA, E1V22QQHYJ, DTWHAW1N0V, 3W5JGDZAN0]
about: [K1HTQF26MA]
sources:
  - url: https://en.wikipedia.org/wiki/Subanalytic_set
---

## Statement

Let $X \subseteq \R^n$ be a [[subanalytic set|K1HTQF26MA]].
Then the complement $\R^n \setminus X$ is subanalytic.

## Remarks

For [[semianalytic sets|E1V22QQHYJ]] the analogous fact is immediate, since the complement of a set defined by equations and inequalities is again so defined.
A subanalytic set is locally a projection, and the complement of a projection is not visibly a projection.
Overcoming this is the content of the theorem; Gabrielov's proof studies the fibres of projections of semianalytic sets.
For example, if $A \subseteq \R^{n+m}$ is bounded and semianalytic and $\pi$ forgets the last $m$ coordinates, then $\R^n \setminus \pi(A)$ is subanalytic.
With the theorem, the subanalytic subsets of $\R^n$ form a Boolean algebra, and the closure, interior and boundary of a subanalytic set are subanalytic.

## Explanations

### L1 human

Subanalytic sets are built by taking shadows of sets cut out by analytic equations and inequalities.
The theorem says that the region outside such a shadow is again a set of the same kind.
So one can take complements freely and never leave the class.

### L2 human

In semialgebraic geometry, closure under projection is the [[Tarski–Seidenberg theorem|3W5JGDZAN0]], and closure under complement is trivial.
For subanalytic sets the roles are reversed: projections are built in, and complements are the hard part.
Gabrielov's theorem is the starting point of the result that the real field with restricted analytic functions is an [[o-minimal|DTWHAW1N0V]] structure.
