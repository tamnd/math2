---
tag: ANRXAG227H
kind: statement
role: theorem
name: Dedekind's characterization of modular lattices
msc: [06C05, 06B05]
uses: [WH4SFAACAS, QX7WZ92QAK, PV90EW00XK, DHC8TZXGYS]
about: [QX7WZ92QAK]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_lattice
---

## Statement

Let $L$ be a [[lattice|WH4SFAACAS]].
Let $N_5$ be the [[pentagon lattice|DHC8TZXGYS]], with elements $0 < a < c < 1$ and an element $b$ that is incomparable to $a$ and $c$, with $b \wedge c = 0$ and $a \vee b = 1$.
Then $L$ is a [[modular lattice|QX7WZ92QAK]] if and only if $L$ has no [[sublattice|PV90EW00XK]] isomorphic to $N_5$.

## Remarks

One direction is easy: $N_5$ is not modular, and the modular law holds in every sublattice of a modular lattice.
For the other direction, suppose $a \le b$ and $x$ violate the law, and put $u = a \vee (x \wedge b)$ and $v = (a \vee x) \wedge b$, so $u < v$.
A direct computation gives $x \wedge u = x \wedge v = x \wedge b$ and $x \vee u = x \vee v = a \vee x$.
So the five elements $x \wedge b$, $u$, $v$, $x$ and $a \vee x$ form a sublattice isomorphic to $N_5$.

Example: the lattice of subspaces of a vector space is modular, so it contains no copy of $N_5$.
Together with the [[M3–N5 characterization of distributivity|C6GH4VHAMQ]], it shows that the pentagon and the diamond are the only obstructions to distributivity.

## Explanations

### L1 human

The modular law is an equation that must hold in all of a lattice.
The theorem says that it fails only when a five-element picture, the pentagon, appears inside the lattice.
So to test modularity, one looks for a pentagon.

### L2 human

The theorem turns an equational condition into a forbidden-substructure condition.
It is used to show that a given lattice is not modular by exhibiting a pentagon, and to prove modularity of lattices built from modular pieces.
The same style of result, with the diamond $M_3$ added, characterizes [[distributive lattices|0HM0HQCK6N]].
The proof is short and gives the pentagon explicitly from any failure of the modular law.
