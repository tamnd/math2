---
tag: G44NQXCWT9
kind: statement
role: theorem
name: Lefschetz fixed-point theorem
msc: [55M20, 37C25]
uses: [0TVJZYB6SH, V8GZ0W1ZZ5, 68PFSGP39B, 0VGFHTM75Y, ZSYCA4EGEZ, M0Q5CFJ7ZH, RNDDWDAFJ5]
about: [ZSYCA4EGEZ]
sources:
  - url: https://en.wikipedia.org/wiki/Lefschetz_fixed-point_theorem
same_as:
  wikidata: Q657469
  wikipedia: Lefschetz fixed-point theorem
---

## Statement

Let $X$ be a [[compact|0TVJZYB6SH]] space that is a [[retract|68PFSGP39B]] of a finite [[simplicial complex|V8GZ0W1ZZ5]].
Examples are compact triangulable spaces and compact smooth manifolds.
Let $f \colon X \to X$ be a [[continuous map|0VGFHTM75Y]] and let $L(f) = \sum_{k \ge 0} (-1)^k \tr\big(f_{\ast} \colon H_k(X; \Q) \to H_k(X; \Q)\big)$ be its [[Lefschetz number|ZSYCA4EGEZ]].
If $L(f) \neq 0$, then $f$ has a fixed point: there is $x \in X$ with $f(x) = x$.

## Remarks

The idea of the proof: suppose $f$ has no fixed point.
By compactness $d(x, f(x))$ is bounded below, so after fine subdivision $f$ has a simplicial approximation that moves every simplex off itself.
The chain map of this approximation then has zero trace in each degree.
The Hopf trace formula equates the alternating sum of traces on chains with that on [[homology|M0Q5CFJ7ZH]], so $L(f) = 0$.
Example: if $X$ is contractible and compact as above, then $H_0(X; \Q) = \Q$ and the other groups vanish, so $L(f) = 1$ for every $f$ and every continuous self-map has a fixed point.
For $f$ homotopic to the identity, $L(f) = \chi(X)$, the [[Euler characteristic|RNDDWDAFJ5]]; so if $\chi(X) \neq 0$, every map homotopic to the identity has a fixed point.
Compactness is necessary: $\R$ is contractible, so $L(f) = 1$, but the translation $x \mapsto x + 1$ has no fixed point.
The converse fails: $L(f) = 0$ does not prevent fixed points, as the identity of the circle shows.

## Explanations

### L1 human

The Lefschetz number is a whole number computed from how a map acts on the holes of a space, as detected by homology.
The theorem says that if this number is not zero, the map must leave some point where it is.
It turns the geometric question "is there a fixed point?" into an algebraic computation.

### L2 human

The Lefschetz number depends only on the homotopy class of $f$, so the theorem gives fixed points for all maps in a homotopy class at once.
It contains the Brouwer fixed-point theorem, since a closed ball is contractible.
A refined form counts fixed points with indices: for a map with isolated fixed points, the sum of their fixed-point indices equals $L(f)$.
In dynamics, applying it to the iterates $f^n$ gives periodic points, and the numbers $L(f^n)$ enter the Lefschetz zeta function.
