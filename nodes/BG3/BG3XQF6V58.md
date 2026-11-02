---
tag: BG3XQF6V58
kind: statement
role: theorem
name: Bellows conjecture
msc: [52C25, 51M25, 52B10]
uses: [ZGD3TQX0K6, 0325SGSJAR]
about: [ZGD3TQX0K6]
sources:
  - url: https://en.wikipedia.org/wiki/Flexible_polyhedron
---

## Statement

Let $P_t$, for $t \in [0, 1]$, be a continuous flex of a closed orientable polyhedral surface in $\R^3$.
That is, each face of $P_t$ stays congruent to the same face of $P_0$, and the combinatorics stay the same.
Then the oriented volume enclosed by $P_t$ does not depend on $t$.

## Remarks

The statement was proved in 1997 by Connelly, Sabitov and Walz, so it is now a theorem.
The proof rests on a result of Sabitov: the volume of a polyhedron is a root of a monic polynomial whose coefficients are polynomials in the squared edge lengths.
Along a flex the edge lengths are fixed, so the volume takes only finitely many values.
Since it varies continuously in $t$, it is constant.

Example: every [[flexible polyhedron|ZGD3TQX0K6]], such as Steffen's polyhedron, keeps its volume while it moves.
So such a polyhedron cannot work as a bellows that pumps air by changing its volume.

## Explanations

### L1 human

Some polyhedra made of rigid faces with hinged edges can still wobble.
One might hope to use such a shape as a bellows, squeezing air in and out.
The theorem says this is impossible: the volume inside stays the same during the whole motion.

### L2 human

The result complements [[Cauchy's rigidity theorem|CJ7KCDDF31]].
Cauchy rules out any flex of a convex polyhedron, while the bellows theorem allows flexes of nonconvex surfaces but fixes their volume.
Its algebraic proof treats the volume as an algebraic function of the edge lengths, a three-dimensional relative of [[Heron's formula|0FRBZ2X4HJ]].
