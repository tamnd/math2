---
tag: 361GJ6QWAR
kind: statement
role: theorem
name: Albert–Brauer–Hasse–Noether theorem
msc: [11R37, 16K50, 11R52]
uses: [634XKY8RZ0, J85FZEQG38, 5HRKJBAY2V, NVD7R0T835, BEW48TA9WZ]
about: [5HRKJBAY2V, BEW48TA9WZ]
sources:
  - url: https://en.wikipedia.org/wiki/Albert%E2%80%93Brauer%E2%80%93Hasse%E2%80%93Noether_theorem
same_as:
  wikidata: Q4712316
  wikipedia: Albert–Brauer–Hasse–Noether theorem
---

## Statement

Let $K$ be a [[global field|634XKY8RZ0]] and let $A$ be a [[central simple algebra|5HRKJBAY2V]] over $K$.
For each place $v$ of $K$, let $K_v$ be the completion of $K$ at $v$, a [[local field|J85FZEQG38]] or $\R$ or $\C$.
If $K_v$ [[splits|NVD7R0T835]] $A$, that is, $A \otimes_K K_v$ is a matrix algebra over $K_v$, for every place $v$, then $A$ is a matrix algebra over $K$.
Equivalently, the natural map of [[Brauer groups|BEW48TA9WZ]] $\mathrm{Br}(K) \to \bigoplus_v \mathrm{Br}(K_v)$ is injective.

## Remarks

The proof uses class field theory: one reduces to cyclic algebras and then uses the Hasse norm theorem.
That theorem says that in a cyclic extension of global fields, an element that is a local norm everywhere is a global norm.
Example: the quaternion algebra $\left(\frac{-1, -1}{\Q}\right)$ splits over $\Q_p$ for every odd prime $p$, but not over $\Q_2$ or over $\R$.
So it is not split over $\Q$, in agreement with the theorem.
Class field theory gives more: the sequence $0 \to \mathrm{Br}(K) \to \bigoplus_v \mathrm{Br}(K_v) \to \Q/\Z \to 0$, with the sum of local invariants as the last map, is exact.
Because of this sum rule it is enough to check all places but one, and a quaternion algebra over $K$ is ramified at an even number of places.

## Explanations

### L1 human

Is a given central simple algebra over the rational numbers just a matrix algebra?
To decide, it is enough to check it over the real numbers and over each field of $p$-adic numbers.
These local questions are much easier.
The theorem is a local-global principle, like the Hasse–Minkowski theorem for quadratic forms.

### L2 human

The theorem is a cornerstone of the arithmetic of central simple algebras over number fields.
With the exact sequence above it gives the classification of central simple algebras over a global field by their local invariants.
Consequences are that every central simple algebra over a global field is cyclic and that its period equals its index.
For quaternion algebras it reduces to the Hasse–Minkowski theorem for the ternary quadratic form $a x^2 + b y^2 - a b z^2$.
