---
tag: WJ0D8QAMW0
kind: problem
name: Congruence lattice problem
msc: [06B15, 08A30, 06B10]
uses: [REE07CSXHR, 3J0BTXSCVN, 0HM0HQCK6N, WH4SFAACAS, T782PJYVEZ]
about: [REE07CSXHR]
sources:
  - url: https://en.wikipedia.org/wiki/Congruence_lattice_problem
same_as:
  wikidata: Q5160997
  wikipedia: Congruence lattice problem
history:
  posed_by: "Robert P. Dilworth"
  first_stated: "1940s"
---

## Problem

Is every [[distributive|0HM0HQCK6N]] [[algebraic lattice|3J0BTXSCVN]] isomorphic to the [[congruence lattice|REE07CSXHR]] of some [[lattice|WH4SFAACAS]]?

## Remarks

The question is natural because the congruence lattice of every lattice is distributive and algebraic.
An equivalent form asks whether every distributive join-semilattice with a least element is isomorphic to the semilattice of compact [[lattice congruences|T782PJYVEZ]] of some lattice.

The answer is positive for finite lattices: every finite distributive lattice is isomorphic to the congruence lattice of a finite lattice.
It is also positive when the semilattice of compact elements has at most $\aleph_1$ elements.

The problem was solved in the negative by Friedrich Wehrung, in a paper published in 2007.
He built a counterexample whose semilattice of compact elements has $\aleph_{\omega+1}$ elements.
Pavel Růžička later lowered the size of a counterexample to $\aleph_2$, which is optimal by the positive result above.

## Explanations

### L1 human

Every lattice has a lattice of congruences, and this lattice always has two special properties: it is distributive and algebraic.
Dilworth asked whether these two properties are the whole story, that is, whether every lattice with them arises from some lattice.
For finite and for not too large lattices the answer is yes.
For very large ones it is no, which was proved after about sixty years.
