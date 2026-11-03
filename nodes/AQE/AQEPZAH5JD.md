---
tag: AQEPZAH5JD
kind: definition
name: Complex K-theory KU
msc: [55N15, 55R50]
defines: 9E4JE4902G
uses: [P4DZM975BV, 5FDMY7PDYY, A4393CW9G4, RASZAXBHX0, Q7RFNJH76Q, 0TVJZYB6SH, 0S1FJ8VEX9]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_K-theory
    locator: Definitions
---

## Definition

Let $X$ be a [[compact|0TVJZYB6SH]] [[Hausdorff space|0S1FJ8VEX9]].
Consider the commutative monoid of isomorphism classes of complex [[vector bundles|P4DZM975BV]] over $X$ under direct sum.
The group $K^0(X)$ is its [[Grothendieck group|5FDMY7PDYY]]; see [[Grothendieck group of vector bundles|A4393CW9G4]].
The tensor product of bundles makes $K^0(X)$ a commutative ring.
For $n \ge 1$, set
$$K^{-n}(X) = \tilde{K}^0(\Sigma^n (X_+)),$$
where $X_+$ is $X$ with a disjoint base point added, $\Sigma$ is the reduced [[suspension|Q7RFNJH76Q]], and $\tilde{K}^0$ is [[reduced K-theory|RASZAXBHX0]].
*Complex K-theory* $KU$ is the family of functors $X \mapsto K^{-n}(X)$, $n \ge 0$, on compact Hausdorff spaces, with the maps induced by pulling back bundles.

## Remarks

Example: for $X$ a point, a complex vector bundle is a finite-dimensional complex vector space, determined up to isomorphism by its dimension.
The monoid is $\N$, so $K^0(\text{point}) = \Z$.
Also $K^{-1}(\text{point}) = \tilde{K}^0(S^1) = 0$, since every complex vector bundle over $S^1$ is trivial.

Non-example: the monoid of bundles itself is not $K^0(X)$, because it is not a group.
Over a point, no vector space $V$ satisfies $V \oplus \C \cong 0$, so the trivial line bundle has no inverse before passing to the Grothendieck group.

For compact $X$, $K^0(X)$ is the set of homotopy classes of maps $X \to \Z \times BU$, where $BU$ is the classifying space of the infinite unitary group.
So $KU$ is represented by a spectrum with $\Z \times BU$ in even degrees and $U$ in odd degrees.
