---
tag: D8GA2R3QT5
kind: conjecture
name: Standard conjectures on algebraic cycles
msc: [14C25, 14F20, 14C15]
uses: [A4H4CZ2V35, 9VFWPZEVGN, E1DVHN06CR, 816AHR3DRT, JX47MS1R1H, 81TXP32VDM, K1AZ4YF2RE]
about: [9VFWPZEVGN, E1DVHN06CR]
sources:
  - url: https://en.wikipedia.org/wiki/Standard_conjectures_on_algebraic_cycles
history:
  posed_by: "Alexander Grothendieck"
  first_stated: "1969"
---

## Statement

Let $k$ be an algebraically closed field, and let $\ell$ be a prime different from the characteristic of $k$.
Let $X$ be a smooth irreducible [[projective variety|A4H4CZ2V35]] of dimension $n$ over $k$.
Write $H^i(X) = H^i(X, \Q_\ell)$ for [[ℓ-adic cohomology|E1DVHN06CR]], with the [[cup product|JX47MS1R1H]].
Let $\mathrm{cl} \colon Z^j(X) \to H^{2j}(X)$ be the cycle class map on [[algebraic cycles|9VFWPZEVGN]] of codimension $j$, and let $A^j(X) \subset H^{2j}(X)$ be the $\Q$-span of its image.
A class in $H^\bullet(X)$ is *algebraic* if it lies in the span of the $A^j(X)$.
Let $L \colon H^i(X) \to H^{i+2}(X)$ be the cup product with the class of a hyperplane section.
By the $\ell$-adic form of the [[hard Lefschetz theorem|816AHR3DRT]], due to Deligne, $L^{n-i} \colon H^i(X) \to H^{2n-i}(X)$ is an isomorphism for $i \le n$.
The standard conjectures are the following.

1. Lefschetz type (conjecture B): the operator $\Lambda$ on $H^\bullet(X)$ that inverts $L$ in the Lefschetz decomposition is induced by an algebraic class in $H^\bullet(X \times X)$.
2. Künneth type (conjecture C): the projectors $\pi_i$ of $H^\bullet(X)$ onto $H^i(X)$ are induced by algebraic classes in $H^{2n}(X \times X)$.
3. Conjecture D: for $Z \in Z^j(X) \otimes \Q$, one has $\mathrm{cl}(Z) = 0$ if and only if $\deg(Z \cdot W) = 0$ for every $W \in Z^{n-j}(X)$; that is, homological and numerical equivalence agree.
4. Hodge type (conjecture I): for $2j \le n$, the pairing $(x, y) \mapsto (-1)^j \deg\big(L^{n-2j} x \cdot y\big)$ is positive definite on the primitive part $\set{x \in A^j(X) : L^{n-2j+1} x = 0}$.

## Remarks

Grothendieck stated the conjectures in his 1968 lecture at the Bombay colloquium on algebraic geometry, published in 1969.
They remain open in general.
The standard conjectures imply the Riemann hypothesis part of the [[Weil conjectures|81TXP32VDM]], which Deligne later proved by other means.
In characteristic $0$, conjecture I follows from the Hodge–Riemann bilinear relations of Hodge theory.
Conjecture B is known for curves, surfaces and abelian varieties.
Conjecture D is known for cycles of codimension $1$.
If the conjectures hold, the category of [[motives|K1AZ4YF2RE]] for numerical equivalence has the properties Grothendieck wanted for a universal cohomology.

## Explanations

### L1 human

Many results about varieties concern the classes in cohomology that come from subvarieties, the algebraic classes.
The standard conjectures predict that some natural operations on cohomology, such as the projection onto one degree, are themselves given by subvarieties of $X \times X$.
They also predict that a class from subvarieties is zero in cohomology as soon as it meets every other such class with total multiplicity zero.
Grothendieck saw them as the key to a theory of motives and to a natural proof of the Weil conjectures.
