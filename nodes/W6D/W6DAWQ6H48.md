---
tag: W6DAWQ6H48
kind: statement
role: theorem
name: G-signature theorem
msc: [58J20, 57S15, 57R20]
uses: [TEG1ZX1AGJ, WK8GKRKAVD, 07EZA80NEH, T866256Y1W, 4NCYA7GME1]
about: [TEG1ZX1AGJ]
sources:
  - url: https://en.wikipedia.org/wiki/Genus_of_a_multiplicative_sequence
---

## Statement

Let $M$ be a closed oriented smooth manifold of dimension $4k$.
Let a compact Lie group $G$ act smoothly on $M$, and let $g \in G$ act by an orientation-preserving diffeomorphism.
The [[intersection form|WK8GKRKAVD]] on $H^{2k}(M; \R)$ is $g$-invariant, so $H^{2k}(M; \R) = H^+ \oplus H^-$ with $g$-invariant subspaces on which the form is positive and negative definite.
The $g$-signature is $\operatorname{sign}(g, M) = \operatorname{tr}(g \mid H^+) - \operatorname{tr}(g \mid H^-)$.
Let $M^g$ be the fixed point set of $g$, a disjoint union of closed submanifolds $F$.
Then
$$\operatorname{sign}(g, M) = \sum_{F} \langle L(g, F), [F] \rangle.$$
Here each $L(g, F) \in H^*(F; \C)$ is a characteristic class.
It is determined by the tangent bundle of $F$, the normal bundle of $F$ in $M$ and the action of $g$ on that normal bundle.
In particular:

1. If $g$ has no fixed points, then $\operatorname{sign}(g, M) = 0$.
2. If $g$ is the identity, the formula is the [[Hirzebruch signature theorem|TEG1ZX1AGJ]].

## Remarks

The theorem is the [[equivariant index theorem|T866256Y1W]] for the [[signature operator|4NCYA7GME1]], whose equivariant index evaluated at $g$ is $\operatorname{sign}(g, M)$; the topological side localizes to the fixed point set.
For an isolated fixed point the contribution is an explicit product of cotangents of half the rotation angles of $g$ on the tangent space, up to a power of $i$.
Example: let a finite group $\Gamma$ act freely and preserving orientation on $M$.
Then every $g \ne 1$ has $\operatorname{sign}(g, M) = 0$, and averaging the characters gives $\sigma(M) = \abs{\Gamma} \, \sigma(M / \Gamma)$, where $\sigma$ is the [[signature|07EZA80NEH]] of the intersection form.

## Explanations

### L1 human

A symmetry of a manifold acts on its middle cohomology and preserves the intersection form.
The $g$-signature measures this action by a trace.
The theorem says that this trace can be computed only by looking near the points that the symmetry fixes.

### L2 human

The $G$-signature theorem of Atiyah and Singer is a basic tool in the study of group actions on manifolds.
It gives obstructions to actions with prescribed fixed point data, through the cotangent expressions that appear at isolated fixed points.
It is a model for later fixed point formulas from the equivariant index theorem.
