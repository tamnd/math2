---
tag: C6GH4VHAMQ
kind: statement
role: theorem
name: M3–N5 characterization of distributivity
msc: [06D05, 06C05]
uses: [WH4SFAACAS, 0HM0HQCK6N, PV90EW00XK, JQ6FJH2TP8, DHC8TZXGYS]
about: [0HM0HQCK6N]
sources:
  - url: https://en.wikipedia.org/wiki/Distributive_lattice
---

## Statement

Let $L$ be a [[lattice|WH4SFAACAS]].
Let $M_3$ be the [[diamond lattice|JQ6FJH2TP8]] and $N_5$ the [[pentagon lattice|DHC8TZXGYS]].
Then $L$ is a [[distributive lattice|0HM0HQCK6N]] if and only if $L$ has no [[sublattice|PV90EW00XK]] isomorphic to $M_3$ and no sublattice isomorphic to $N_5$.

## Remarks

If $L$ is distributive, so is every sublattice, and $M_3$ and $N_5$ are not distributive.
Conversely, if $L$ has no copy of $N_5$, then $L$ is [[modular|QX7WZ92QAK]] by [[Dedekind's characterization|ANRXAG227H]].
In a modular lattice in which $a \wedge (b \vee c) \ne (a \wedge b) \vee (a \wedge c)$, put $d = (a \wedge b) \vee (b \wedge c) \vee (c \wedge a)$ and $e = (a \vee b) \wedge (b \vee c) \wedge (c \vee a)$.
Then $d < e$, and the elements $d$, $e$, $(a \wedge e) \vee d$, $(b \wedge e) \vee d$, $(c \wedge e) \vee d$ form a sublattice isomorphic to $M_3$.

Example: the lattice of subspaces of $\R^2$ is not distributive, because the zero subspace, three distinct lines and $\R^2$ form a copy of $M_3$.
The lattice of divisors of $12$ under divisibility, with $\gcd$ as meet and $\lcm$ as join, is distributive, so it contains neither shape.

## Explanations

### L1 human

The distributive law is the familiar rule that "and" distributes over "or".
The theorem says that a lattice breaks this rule only if one of two small five-element lattices, the diamond or the pentagon, sits inside it.
So one can test distributivity by looking for these two shapes.

### L2 human

This theorem is the standard way to show that a lattice is not distributive: one exhibits a diamond or a pentagon.
It refines [[Dedekind's characterization|ANRXAG227H]] of modular lattices, which forbids only the pentagon.
For a finite distributive lattice, the structure is then described completely by [[Birkhoff's representation theorem|6RDM3069KC]].
The proof constructs the forbidden sublattice explicitly from any triple that violates distributivity.
