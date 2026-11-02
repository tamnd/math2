---
tag: Z6JR1GN2RE
kind: statement
role: theorem
name: No-retraction theorem
msc: [55M20, 54C15]
uses: [0Q0H13G8ZB, T62369RFH6, 0VGFHTM75Y, NJQMWVK3QK]
about: [0Q0H13G8ZB, T62369RFH6]
sources:
  - url: https://en.wikipedia.org/wiki/Brouwer_fixed-point_theorem
---

## Statement

Let $n \ge 1$, let $D^n = \set{x \in \R^n : \norm{x} \le 1}$ be the [[closed unit ball|0Q0H13G8ZB]], and let $S^{n-1} = \set{x \in \R^n : \norm{x} = 1}$ be its boundary [[sphere|T62369RFH6]].
There is no [[continuous map|0VGFHTM75Y]] $r \colon D^n \to S^{n-1}$ with $r(x) = x$ for all $x \in S^{n-1}$.

## Remarks

Suppose such a retraction $r$ exists, and let $i \colon S^{n-1} \to D^n$ be the inclusion, so that $r \circ i = \id_{S^{n-1}}$.
Apply [[reduced homology|NJQMWVK3QK]] in degree $n - 1$: the identity of $\tilde{H}_{n-1}(S^{n-1}; \Z) \cong \Z$ factors through $\tilde{H}_{n-1}(D^n; \Z) = 0$, which is impossible.
For $n = 1$ the argument is simply that $D^1 = [-1, 1]$ is connected and $S^0 = \set{-1, 1}$ is not.
For smooth retractions there is also a proof by Sard's theorem: the preimage of a regular value would be a compact $1$-manifold with only one boundary point.

Example of use: the theorem gives the [[Brouwer fixed-point theorem|N7AAJ2MW5T]].
If $f \colon D^n \to D^n$ had no fixed point, the ray from $f(x)$ through $x$ would meet $S^{n-1}$ in a point $r(x)$, and $r$ would be a retraction of $D^n$ onto $S^{n-1}$.

The ball cannot be replaced by any space: the cylinder $S^{n-1} \times [0, 1]$ retracts onto its end $S^{n-1} \times \set{0}$ by $(x, t) \mapsto (x, 0)$.

## Explanations

### L1 human

You cannot push a drum skin onto its rim continuously while holding the rim fixed.
Somewhere the skin would have to tear.

### L2 human

The no-retraction theorem is equivalent to the Brouwer fixed-point theorem, and each implies the other with a short argument.
In homotopy terms, it says that the identity map of $S^{n-1}$ is not null-homotopic, and so it is a statement about the degree of the identity.
Similar retraction arguments, with homology or cohomology, show that the boundary of a compact manifold is never a retract of the manifold.
