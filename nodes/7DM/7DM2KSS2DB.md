---
tag: 7DM2KSS2DB
kind: statement
role: theorem
name: Freudenthal suspension theorem
msc: [55Q40, 55P40]
uses: [P976WYEFMB, Q7RFNJH76Q, 1A943BWBQT, 5W95QFHXPR, T9DG8DDE75]
about: [P976WYEFMB, Q7RFNJH76Q]
sources:
  - url: https://en.wikipedia.org/wiki/Freudenthal_suspension_theorem
same_as:
  wikidata: Q1455794
  wikipedia: Freudenthal suspension theorem
---

## Statement

Let $n \ge 1$, and let $X$ be a pointed [[CW complex|5W95QFHXPR]] that is [[$(n-1)$-connected|1A943BWBQT]].
Let $\Sigma X$ be the reduced [[suspension|Q7RFNJH76Q]] of $X$.
The suspension homomorphism $E \colon \pi_i(X) \to \pi_{i+1}(\Sigma X)$, $[f] \mapsto [\Sigma f]$, on [[homotopy groups|P976WYEFMB]] has the following properties:

1. it is an isomorphism for $i < 2n - 1$;
2. it is surjective for $i = 2n - 1$.

## Remarks

The usual proof applies the [[Blakers–Massey theorem|QF764XKBA3]] to the two cones that form $\Sigma X$, whose intersection is a copy of $X$.
For spheres, $S^n$ is $(n-1)$-connected and $\Sigma S^n = S^{n+1}$, so $\pi_i(S^n) \to \pi_{i+1}(S^{n+1})$ is an isomorphism for $i < 2n - 1$.
Hence $\pi_{n+k}(S^n)$ does not depend on $n$ once $n \ge k + 2$, which defines the [[stable homotopy groups of spheres|HGZAYPQBXW]].
The bound is sharp: for $n = 2$ and $i = 3$, the map $\pi_3(S^2) \cong \Z \to \pi_4(S^3) \cong \Z/2$ is onto but not injective.
The theorem also gives $\pi_n(S^n) \cong \Z$ for all $n \ge 1$ by induction from $\pi_1(S^1) \cong \Z$, using $\pi_2(S^2) \cong \Z$ from the Hopf fibration at the first step.

## Explanations

### L1 human

Suspending a space places it as the equator of a larger space made of two cones.
Every map of spheres into the space suspends to a map one dimension higher.
The theorem says that, in a range of dimensions, this loses no information and creates nothing new.

### L2 human

The theorem is the starting point of stable homotopy theory.
It shows that the suspension sequence $\pi_{n+k}(S^n) \to \pi_{n+k+1}(S^{n+1}) \to \cdots$ eventually becomes constant, so stable groups and spectra make sense.
In the stable range, homotopy groups behave like a homology theory, since excision holds there.
