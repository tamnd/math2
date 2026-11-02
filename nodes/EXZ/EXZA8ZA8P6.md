---
tag: EXZA8ZA8P6
kind: statement
role: theorem
name: Lyusternik–Fet theorem
msc: ["58E10", 53C22]
uses: [7CBT4SM83Y, 4MCCP8GG4J, SGGXZ3TBSA]
about: [4MCCP8GG4J]
sources:
  - url: https://en.wikipedia.org/wiki/Lyusternik–Fet_theorem
same_as:
  wikidata: Q61761423
  wikipedia: Lyusternik–Fet theorem
---

## Statement

Let $(M, g)$ be a compact [[Riemannian manifold|7CBT4SM83Y]] without boundary, of dimension at least $1$.
Then $M$ has a [[closed geodesic|4MCCP8GG4J]].

## Remarks

If the fundamental group of $M$ is nontrivial, a loop of least length in a nontrivial free homotopy class exists by compactness, and it is a closed geodesic.
If $M$ is simply connected, then $M$ is not contractible, because a closed $n$-manifold has nonzero homology in degree $n$ with coefficients in $\Z/2$.
By the Hurewicz theorem, some homotopy group $\pi_k(M)$ with $k \ge 2$ is nonzero.
Then a minimax over $(k-1)$-parameter families of loops in the [[free loop space|SGGXZ3TBSA]] gives a critical value of the energy.
The Palais–Smale condition for the energy makes the minimax work.
The nontriviality of the class makes the critical value positive, so the critical point is not a constant loop.

Example: on a round sphere every great circle is a closed geodesic.
On an ellipsoid in $\R^3$ the theorem gives at least one, and the intersections with the three coordinate planes are in fact closed geodesics.
Compactness is needed: in $\R^n$ with the Euclidean metric no geodesic is closed.

## Explanations

### L1 human

On any closed curved space, there is a loop that runs straight ahead and closes up on itself.
If the space has a hole that a loop can wind around, one can tighten such a loop as much as possible.
If not, the space still has a higher-dimensional hole.
One sweeps it by a family of loops and looks for the loop at the highest point of the best sweep.

### L2 human

The theorem was the first general existence result for closed geodesics, and its proof is the model for minimax methods on loop spaces.
It extends Birkhoff's earlier result for spheres, which uses the [[Birkhoff min-max method|1R5X9HW6D3]].
Questions about the number of geometrically distinct closed geodesics are much harder; see the [[Gromoll–Meyer theorem|XC8BRYJN93]] and the [[theorem of Bangert and Franks|X93AEE88PX]].
