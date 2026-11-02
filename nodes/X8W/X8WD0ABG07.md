---
tag: X8WD0ABG07
kind: definition
name: Lattice
msc: [06B05]
defines: WH4SFAACAS
uses: [0QV2JS9RJ3, J2T75ATRV5]
sources:
  - url: https://en.wikipedia.org/wiki/Lattice_(order)
---

## Definition

A *lattice* is a [[partially ordered set|0QV2JS9RJ3]] $(L, \le)$ in which every two elements $x, y \in L$ have a [[join|J2T75ATRV5]] $x \vee y$ and a meet $x \wedge y$.

Algebraic form: a *lattice* is a set $L$ with two binary operations $\vee$ and $\wedge$ such that, for all $x, y, z \in L$:

1. $x \vee y = y \vee x$ and $x \wedge y = y \wedge x$;
2. $(x \vee y) \vee z = x \vee (y \vee z)$ and $(x \wedge y) \wedge z = x \wedge (y \wedge z)$;
3. $x \vee (x \wedge y) = x$ and $x \wedge (x \vee y) = x$.

## Remarks

The two forms are equivalent.
From a lattice order, the join and meet satisfy clauses 1 to 3.
From the operations, the order is recovered by $x \le y \iff x \vee y = y$, which holds exactly when $x \wedge y = x$.
The idempotent laws $x \vee x = x$ and $x \wedge x = x$ follow from the absorption laws in clause 3.
Example: $\N_{>0}$ ordered by divisibility is a lattice with $a \vee b = \lcm(a, b)$ and $a \wedge b = \gcd(a, b)$.
Indeed $\lcm(a, b)$ is a common multiple of $a$ and $b$ and divides every common multiple.
Non-example: the poset $\set{a, b, c, d}$ with $a, b < c$ and $a, b < d$ and no other strict relations is not a lattice.
The elements $a$ and $b$ have the two upper bounds $c$ and $d$, which are incomparable, so $a \vee b$ does not exist.
