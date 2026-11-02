---
tag: 759KSC8XQD
kind: definition
name: Geometric lattice
msc: [06C10, 05B35]
defines: VDF7CGPC0P
uses: [WH4SFAACAS, TTVCTW6TNC, 99DVVV7BH2, C1NET23GG0]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_lattice
---

## Definition

Let $L$ be a finite [[lattice|WH4SFAACAS]].
The lattice $L$ is *geometric* if:

1. $L$ is [[atomistic|99DVVV7BH2]]: every element of $L$ is the join of a set of [[atoms|TTVCTW6TNC]];
2. $L$ is [[semimodular|C1NET23GG0]] (upper semimodular).

## Remarks

Example: the Boolean lattice of all subsets of a finite set $S$.
The atoms are the singletons, and every subset is the union of its singletons.
If $A$ covers $A \cap B$, then $A = (A \cap B) \cup \set{s}$ with $s \notin B$, so $A \cup B = B \cup \set{s}$ covers $B$.

Non-example: the chain $0 < a < 1$ with three elements.
It is semimodular, but its only atom is $a$, and $1$ is not a join of atoms.

The lattice of flats of a finite [[matroid|PX31ZNYS3Z]] is geometric, and every geometric lattice is isomorphic to the lattice of flats of a simple matroid, unique up to isomorphism.
Some authors allow infinite geometric lattices, replacing finiteness by finite length or by compactness conditions.
