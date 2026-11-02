---
tag: CZ6ABG86WY
kind: definition
name: Join-irreducible element
msc: [06B05]
defines: ZHRQ0AT8PM
uses: [WH4SFAACAS, J2T75ATRV5, 0AANKKNHS4]
sources:
  - url: https://en.wikipedia.org/wiki/Join_and_meet
---

## Definition

Let $(L, \vee, \wedge)$ be a [[lattice|WH4SFAACAS]].
An element $a \in L$ is *join-irreducible* if:

1. $a$ is not a [[least element|0AANKKNHS4]] of $L$;
2. for all $b, c \in L$, if $a = b \vee c$, then $a = b$ or $a = c$.

An element is *meet-irreducible* if it satisfies the dual conditions, with the greatest element and the [[meet|J2T75ATRV5]].

## Remarks

Clause 2 says that $a$ is not the join of two elements strictly below it.
Example: in the power set of a set $X$, each singleton $\set{x}$ is join-irreducible.
It is not $\emptyset$, and if $\set{x} = B \cup C$ then $B$ or $C$ contains $x$, so it equals $\set{x}$.
Non-example: $\set{1, 2} = \set{1} \cup \set{2}$ with $\set{1} \ne \set{1, 2}$ and $\set{2} \ne \set{1, 2}$, so clause 2 fails.
In a chain, every element other than the least element is join-irreducible, since $b \vee c = \max(b, c)$.
In a finite lattice, every element is the join of the join-irreducible elements below it.
