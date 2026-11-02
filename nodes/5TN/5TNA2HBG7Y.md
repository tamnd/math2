---
tag: 5TNA2HBG7Y
kind: statement
role: theorem
name: Whitman's condition
msc: [06B25]
uses: [WP20S9NZ15, J2T75ATRV5, PV90EW00XK]
about: [WP20S9NZ15]
sources:
  - url: https://en.wikipedia.org/wiki/Free_lattice
---

## Statement

Let $X$ be a set and let $\mathrm{FL}(X)$ be the [[free lattice|WP20S9NZ15]] on $X$, with [[join and meet|J2T75ATRV5]] $\vee$ and $\wedge$.
Then $\mathrm{FL}(X)$ satisfies *Whitman's condition* (W): for all $a, b, c, d \in \mathrm{FL}(X)$, if
$$a \wedge b \le c \vee d,$$
then $a \le c \vee d$, or $b \le c \vee d$, or $a \wedge b \le c$, or $a \wedge b \le d$.

## Remarks

The converse implication is automatic in any lattice, since $a \wedge b \le a$, $a \wedge b \le b$, $c \le c \vee d$ and $d \le c \vee d$.
So (W) says that an inequality between a meet and a join holds in $\mathrm{FL}(X)$ only for one of these four trivial reasons.
Proof idea: Whitman described the order of $\mathrm{FL}(X)$ on lattice terms by recursive rules, the solution of the [[word problem for free lattices|Z86VGP5RMG]].
He showed that these rules define a lattice with the universal property.
The rule for comparing a meet with a join is exactly (W).
Every [[sublattice|PV90EW00XK]] of a lattice satisfying (W) satisfies (W), since joins and meets in a sublattice are computed in the big lattice.
Example of failure: in the lattice of subsets of $\set{1, 2, 3, 4}$, take $a = \set{1, 2, 3}$, $b = \set{1, 2, 4}$, $c = \set{1}$ and $d = \set{2}$.
Then $a \cap b = \set{1, 2} = c \cup d$, but $a \not\subseteq \set{1, 2}$, $b \not\subseteq \set{1, 2}$, $\set{1, 2} \not\subseteq c$ and $\set{1, 2} \not\subseteq d$.
So this lattice is not a sublattice of any free lattice.

## Explanations

### L1 human

In a free lattice nothing holds by accident.
If a meet $a \wedge b$ lies below a join $c \vee d$, then there is an obvious reason.
Either one of $a$ or $b$ lies below $c \vee d$, or $a \wedge b$ lies below one of $c$ or $d$.
Lattices of sets do not behave this way, since two sets can overlap in exactly the union of two smaller sets.

### L2 human

Whitman's condition is the key structural property of free lattices.
Together with the rules for generators, it gives an algorithm that decides the order of $\mathrm{FL}(X)$.
It is also the main test for deciding which finite lattices embed in free lattices, because it passes to sublattices.
Since the subsets of a four-element set fail (W), a free lattice cannot contain this Boolean lattice as a sublattice.
