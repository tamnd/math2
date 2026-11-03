---
tag: X2RF2WKWV9
kind: statement
role: theorem
name: Kochen–Specker theorem
msc: [81P13, 81P10]
uses: [HM2HHE3J51, 0S9GGTR0EX, 0B8KZRT28M, 21Q9PMSKC4]
about: [21Q9PMSKC4]
sources:
  - url: https://en.wikipedia.org/wiki/Kochen%E2%80%93Specker_theorem
same_as:
  wikidata: Q528955
  wikipedia: Kochen–Specker theorem
---

## Statement

Let $\mathcal{H}$ be a real or complex [[Hilbert space|HM2HHE3J51]] with $3 \le \dim \mathcal{H} < \infty$.
Then there is a finite set $S$ of unit vectors in $\mathcal{H}$ with the following property.
There is no map $v \colon S \to \set{0, 1}$ such that $\sum_{x \in B} v(x) = 1$ for every [[orthonormal basis|0S9GGTR0EX]] $B$ of $\mathcal{H}$ with $B \subseteq S$.

## Remarks

A map $v$ as in the statement is a noncontextual assignment of definite answers to the yes-no questions given by the [[projections|0B8KZRT28M]] onto the vectors of $S$.
In each measurement context, an orthonormal basis, exactly one answer would be "yes", and the answer to a question would not depend on the basis in which it is asked.
The proof is a finite combinatorial check: one exhibits a set $S$ whose orthogonality graph admits no such colouring.
Kochen and Specker used $117$ vectors in $\R^3$, and a set of $18$ vectors in $\R^4$ found by Cabello, Estebaranz and García-Alcaine gives a short parity proof.
In that proof the $18$ vectors form $9$ bases, and each vector lies in exactly $2$ of them.
So the sum of $v$ over all $9$ bases is even, while it should equal $9$.
A set for dimension $3$ yields a set for every larger finite dimension, so dimension $3$ is the key case.
The hypothesis $\dim \mathcal{H} \ge 3$ is necessary.
In dimension $2$ each ray is orthogonal to exactly one other ray.
So one can give the value $1$ to one ray of each orthogonal pair and $0$ to the other.

## Explanations

### L1 human

Imagine that every possible yes-no measurement on a quantum system had a hidden, fixed answer before it is made.
In each complete set of compatible measurements, exactly one answer would be "yes".
The theorem says that in dimension three or more such a table of answers cannot exist, even for a finite list of measurements.
So the outcomes of quantum measurements cannot be fixed in advance independently of which other measurements are made with them.

### L2 human

The theorem is the main no-go result for noncontextual [[hidden-variable theories|QRW6NE1VY7]], and it is the origin of the notion of [[contextuality|21Q9PMSKC4]].
Unlike Bell's theorem, it needs no spatial separation and no entanglement, only the structure of orthogonality in a single Hilbert space.
It also follows from Gleason's theorem by a continuity argument, but the finite sets make the obstruction explicit and testable.
Hidden-variable models that are contextual, such as [[de Broglie–Bohm theory|KN403Z7F1R]], are not ruled out.
