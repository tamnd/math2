---
tag: PR7Q3QMEHZ
kind: statement
role: fact
name: Playfair's axiom
msc: [51M05, 51F05]
uses: [0MP9BCF6DP, 0V3XAMF3C1, VKFPCSRNDH]
about: [KRZD96GSVC]
sources:
  - url: https://en.wikipedia.org/wiki/Playfair%27s_axiom
same_as:
  wikidata: Q3915714
  wikipedia: Playfair's axiom
---

## Statement

Let $\ell$ be a [[line|0MP9BCF6DP]] in a [[plane|0V3XAMF3C1]] and let $P$ be a point of the plane not on $\ell$.
Then there is at most one line in the plane through $P$ that does not meet $\ell$.

## Remarks

In [[absolute geometry|VKFPCSRNDH]], at least one such line always exists: drop the perpendicular from $P$ to $\ell$ and take the perpendicular to it at $P$.
So, over those axioms, Playfair's axiom says that the parallel through $P$ exists and is unique.
It is the parallel axiom in Hilbert's system, and it is equivalent to Euclid's fifth postulate over the other axioms.
In the hyperbolic plane it fails: through $P$ there are infinitely many lines that do not meet $\ell$.
In the real plane $\R^2$ with $\ell = \set{(x, 0) : x \in \R}$ and $P = (0, 1)$, the only line through $P$ missing $\ell$ is $y = 1$.

## Explanations

### L1 human

Through a point off a line, you can draw exactly one line that never meets it.
This is the parallel axiom in its most common form.
It is named after John Playfair, who used it in his edition of Euclid.

### L2 human

Playfair's axiom is the form of the parallel postulate that one uses in practice.
It speaks only of incidence, and not of angles, so it also makes sense in an affine plane, where it is one of the defining axioms.
