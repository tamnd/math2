---
tag: ABYAPP6Q4C
kind: statement
role: theorem
name: Smith conjecture
msc: [57M60, 57K10]
uses: [QYEAZTYGPT, 1TQ06R4Q66]
about: [QYEAZTYGPT]
sources:
  - url: https://en.wikipedia.org/wiki/Smith_conjecture
same_as:
  wikidata: Q7545379
  wikipedia: Smith conjecture
---

## Statement

Let $f \colon S^3 \to S^3$ be an orientation-preserving diffeomorphism of finite order $n \ge 2$.
Suppose that the fixed point set $\set{x \in S^3 : f(x) = x}$ is homeomorphic to a circle.
Then this fixed circle is the [[unknot|1TQ06R4Q66]].

## Remarks

P. A. Smith showed that the fixed point set of such a map of prime order is empty or a circle, and asked whether the circle can be knotted.
The proof combined work of several authors, including Thurston on hyperbolic structures, Meeks and Yau on minimal surfaces, Bass on group theory, and Gordon and Litherland.
One case uses incompressible surfaces in the knot complement; the other uses a hyperbolic structure given by Thurston's work.
The orientation hypothesis matters: a reflection of $S^3$ has order $2$ and fixes a $2$-sphere.
The analogue in higher dimensions fails: in $S^4$, some knotted $2$-spheres are fixed sets of periodic diffeomorphisms.
Example: the rotation by angle $2\pi/n$ about the unknotted great circle $\set{(z, 0)} \subset S^3 \subset \C^2$, given by $(z, w) \mapsto (z, e^{2\pi i/n} w)$, fixes exactly that circle.

## Explanations

### L1 human

Imagine a rotation of three-dimensional space that, repeated a few times, comes back to where it started.
The points that do not move form an axis.
In ordinary space this axis is a straight line, and in the $3$-sphere it is an unknotted circle.
The theorem says that no smooth symmetry of finite order can have a knotted axis.
So a nontrivial [[knot|QYEAZTYGPT]] can never be the axis of such a rotation.

### L2 human

Equivalently, a nontrivial knot $K$ is never the branch set of a cyclic branched cover $S^3 \to S^3$.
The theorem was a test case for Thurston's geometrization program: the decisive input came from hyperbolic geometry and minimal surfaces.
It is a precursor of the orbifold theorem, which handles more general finite group actions on $3$-manifolds.
