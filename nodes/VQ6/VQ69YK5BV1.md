---
tag: VQ69YK5BV1
kind: statement
role: theorem
name: Periodic table of topological insulators
msc: [82D20, 19L64, 81V70]
uses: [X66S7EJ1R7, 6XCFW7YGX8, A38B1QFK20]
about: [X66S7EJ1R7]
sources:
  - url: https://en.wikipedia.org/wiki/Periodic_table_of_topological_insulators_and_topological_superconductors
same_as:
  wikidata: Q55629489
  wikipedia: Periodic table of topological insulators and topological superconductors
---

## Statement

Consider gapped, translation-invariant, non-interacting fermion Hamiltonians in dimension $d \ge 0$.
They are taken up to deformation without closing the gap and up to adding trivial bands, as in the definition of a [[topological insulator|X66S7EJ1R7]].
The ten Altland–Zirnbauer symmetry classes record which symmetries are present and their squares.
The symmetries are a time-reversal symmetry $\Theta$, a particle-hole symmetry $\Xi$ and a chiral symmetry.
The classes A and AIII have neither $\Theta$ nor $\Xi$, and only AIII has a chiral symmetry.
The other eight classes, listed with $(\Theta^2, \Xi^2)$, are AI $(+1, \text{none})$, BDI $(+1, +1)$, D $(\text{none}, +1)$ and DIII $(-1, +1)$.
They continue with AII $(-1, \text{none})$, CII $(-1, -1)$, C $(\text{none}, -1)$ and CI $(+1, -1)$.
Then the group of strong topological phases in each class and dimension $d$ is given by the table below.
In the table, $0$ means only the trivial phase, and $2\Z$ means a copy of $\Z$ whose invariant takes only even values.

| class | $d=0$ | $d=1$ | $d=2$ | $d=3$ | $d=4$ | $d=5$ | $d=6$ | $d=7$ |
|---|---|---|---|---|---|---|---|---|
| A | $\Z$ | $0$ | $\Z$ | $0$ | $\Z$ | $0$ | $\Z$ | $0$ |
| AIII | $0$ | $\Z$ | $0$ | $\Z$ | $0$ | $\Z$ | $0$ | $\Z$ |
| AI | $\Z$ | $0$ | $0$ | $0$ | $2\Z$ | $0$ | $\Z_2$ | $\Z_2$ |
| BDI | $\Z_2$ | $\Z$ | $0$ | $0$ | $0$ | $2\Z$ | $0$ | $\Z_2$ |
| D | $\Z_2$ | $\Z_2$ | $\Z$ | $0$ | $0$ | $0$ | $2\Z$ | $0$ |
| DIII | $0$ | $\Z_2$ | $\Z_2$ | $\Z$ | $0$ | $0$ | $0$ | $2\Z$ |
| AII | $2\Z$ | $0$ | $\Z_2$ | $\Z_2$ | $\Z$ | $0$ | $0$ | $0$ |
| CII | $0$ | $2\Z$ | $0$ | $\Z_2$ | $\Z_2$ | $\Z$ | $0$ | $0$ |
| C | $0$ | $0$ | $2\Z$ | $0$ | $\Z_2$ | $\Z_2$ | $\Z$ | $0$ |
| CI | $0$ | $0$ | $0$ | $2\Z$ | $0$ | $\Z_2$ | $\Z_2$ | $\Z$ |

The table repeats with period $2$ in $d$ for the classes A and AIII and with period $8$ for the other eight classes.

## Remarks

The table was found by Andreas Schnyder, Shinsei Ryu, Akira Furusaki and Andreas Ludwig in 2008 and by Alexei Kitaev in 2009.
Kitaev's derivation identifies the phases with [[topological K-theory|6XCFW7YGX8]] groups of a point, using the representation theory of [[Clifford algebras|A38B1QFK20]].
Read from AI to CI, the column $d = 0$ of the real classes is $\Z, \Z_2, \Z_2, 0, 2\Z, 0, 0, 0$, the real K-theory groups $KO^{-q}$ of a point for $q = 0, \dots, 7$.
Moving one row down shifts a row one step to the right.
The periods $2$ and $8$ are complex and real Bott periodicity.
The table classifies strong invariants only; weak invariants, which depend on lower-dimensional sub-tori of the Brillouin zone, come on top.

Example: class AII in $d = 2$ and $d = 3$ gives $\Z_2$, the time-reversal-invariant topological insulators.
Class A in $d = 2$ gives $\Z$, the Chern number of the integer quantum Hall effect.
Class D in $d = 1$ gives $\Z_2$, realised by the [[Kitaev chain|3S0K7QZCAA]].

## Explanations

### L1 human

Insulators and superconductors can be "twisted" in ways that cannot be undone, and the possible twists depend on the dimension and on which symmetries are present.
The periodic table lists, for ten symmetry types and each dimension, which twists exist: none ($0$), an integer's worth ($\Z$), or just one ($\Z_2$).
Its rows repeat in a regular pattern, as in the chemical periodic table, which explains its name.

### L2 human

The entries come from Bott periodicity, the same phenomenon that makes homotopy groups of orthogonal and unitary groups repeat with periods $8$ and $2$.
Each symmetry class corresponds to a Clifford algebra extension problem, and the dimension $d$ shifts the Clifford index.
The table predicts which models can carry protected boundary states: for example, the [[Su–Schrieffer–Heeger model|TKZQG3Z3YZ]] in class BDI, $d = 1$, has a $\Z$ invariant, a winding number.
It assumes no interactions; with interactions some of the $\Z$ entries reduce, as shown by Fidkowski and Kitaev for class BDI in $d = 1$, where $\Z$ becomes $\Z_8$.
