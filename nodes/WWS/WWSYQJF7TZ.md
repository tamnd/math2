---
tag: WWSYQJF7TZ
kind: conjecture
name: Eremenko's conjecture
msc: [37F10, 30D05]
uses: [0G4F0XB9X2, 5M4S7P04GR, 0JG9W3KA6B]
about: [0G4F0XB9X2]
sources:
  - url: https://en.wikipedia.org/wiki/Escaping_set
history:
  posed_by: "Alexandre Eremenko"
  first_stated: "1989"
---

## Statement

Let $f \colon \C \to \C$ be a transcendental [[entire function|0G4F0XB9X2]].
Let $I(f) = \set{z \in \C : f^n(z) \to \infty \text{ as } n \to \infty}$ be its escaping set.
Then every [[connected component|0JG9W3KA6B]] of $I(f)$ is unbounded.

## Remarks

Eremenko proved that $I(f)$ is nonempty and that the [[Julia set|5M4S7P04GR]] of $f$ is the boundary of $I(f)$.
He also proved that every component of the closure of $I(f)$ is unbounded.
Rippon and Stallard proved in 2005 that $I(f)$ always has at least one unbounded component.
A stronger form, that every escaping point can be joined to $\infty$ by a curve in $I(f)$, is false.
Rottenfußer, Rückert, Rempe and Schleicher gave entire functions whose escaping sets contain no curves at all.
In 2021 Martí-Pete, Rempe and Waterman constructed a counterexample to the conjecture itself.
For a polynomial of degree at least $2$ the analogous statement holds.
There the escaping set is the complement of the filled Julia set $K$, which is compact and has connected complement.
So the escaping set is connected and unbounded.

## Explanations

### L1 human

For a transcendental entire function such as $e^z$, some points run off to infinity under iteration; together they form the escaping set.
Eremenko guessed that this set has no bounded pieces: every piece should reach out to infinity.
For many families, such as the exponential maps, the escaping set is indeed made of curves that go to infinity.
In general the guess turned out to be false, but the question shaped much of the study of transcendental dynamics.
