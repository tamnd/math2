---
tag: XAEEDWV3PM
kind: conjecture
name: Hodge conjecture
msc: [14C30, 14C25]
uses: [A4H4CZ2V35, EXKGG9X6J0, 6N7BC70CX0, HABCJ4Y0SR, ZSM083M97C, 9VFWPZEVGN]
about: [9VFWPZEVGN, ZSM083M97C]
sources:
  - url: https://en.wikipedia.org/wiki/Hodge_conjecture
same_as:
  wikidata: Q1143138
  wikipedia: Hodge conjecture
history:
  posed_by: "W. V. D. Hodge"
  first_stated: "1950"
---

## Statement

Let $X$ be a [[smooth|EXKGG9X6J0]] [[projective variety|A4H4CZ2V35]] over $\C$, and let $p \ge 0$.
Let $H^{p,p}(X)$ be the $(p, p)$ part of the [[Hodge decomposition|HABCJ4Y0SR]] of $H^{2p}(X, \C)$.
Here $H^{2p}(X, \Q)$ is [[singular cohomology|6N7BC70CX0]], viewed inside $H^{2p}(X, \C)$.
Let $\mathrm{Hdg}^p(X) = H^{2p}(X, \Q) \cap H^{p,p}(X)$ be the group of rational Hodge classes.
Then every class in $\mathrm{Hdg}^p(X)$ is a $\Q$-linear combination of classes of closed subvarieties of $X$ of codimension $p$.
In other words, it is the class of an [[algebraic cycle|9VFWPZEVGN]] with rational coefficients.

## Remarks

The conjecture is open.
It is one of the Millennium Prize Problems of the Clay Mathematics Institute.
The class of a subvariety of codimension $p$ always lies in $\mathrm{Hdg}^p(X)$, so the conjecture asks for the converse.

The case $p = 1$ is true: it is the Lefschetz theorem on $(1,1)$-classes, which follows from the exponential sequence.
It shows that every class in $H^{2}(X, \Z)$ whose image lies in $H^{1,1}$ is the first Chern class of a line bundle.
By the hard Lefschetz theorem, the case $p = 1$ implies the case $p = n - 1$, where $n = \dim X$.
So the conjecture holds for varieties of dimension at most $3$.

The version with integer coefficients is false: Atiyah and Hirzebruch found torsion classes that are not algebraic, and Kollár found non-torsion counterexamples.
The analogous statement for compact Kähler manifolds, with analytic cycles or Chern classes of coherent sheaves, is false by an example of Voisin.

## Explanations

### L1 human

The Hodge conjecture asks which cohomology classes of a complex projective variety come from geometry, namely from subvarieties.
Hodge theory singles out a natural candidate set, the rational classes of type $(p, p)$, and every subvariety gives such a class.
The conjecture says that there are no others: every class that looks algebraic from the point of view of Hodge theory is algebraic.
