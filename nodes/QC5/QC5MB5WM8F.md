---
tag: QC5MB5WM8F
kind: statement
role: theorem
name: Banach–Mazur theorem
msc: [46B04, 46B25]
uses: [AH45GS6RCR, 07SJXTWVQW, 0PARCKE8WP]
about: [AH45GS6RCR]
sources:
  - url: https://en.wikipedia.org/wiki/Banach%E2%80%93Mazur_theorem
same_as:
  wikidata: Q2226610
  wikipedia: Banach–Mazur theorem
---

## Statement

Let $X$ be a [[separable Banach space|AH45GS6RCR]] over $\R$.
Let $C([0,1])$ be the Banach space of continuous real functions on $[0,1]$ with the [[supremum norm|0PARCKE8WP]].
Then there is a [[linear isometry|07SJXTWVQW]] $T \colon X \to C([0,1])$.
In particular, $X$ is isometrically isomorphic to the closed subspace $T(X)$ of $C([0,1])$.

## Remarks

The idea of the proof: let $B$ be the closed unit ball of the dual space $X^*$ with the weak-* topology.
Since $X$ is separable, $B$ is a compact metrizable space, so it is a continuous image of the Cantor set $\Delta$ under some map $\varphi$.
The map $x \mapsto (t \mapsto \varphi(t)(x))$ is a linear isometry of $X$ into $C(\Delta)$, by the Hahn–Banach theorem.
Each function in $C(\Delta)$ extends to $[0,1]$ by linear interpolation on the open intervals removed from $[0,1]$, and this extension is a linear isometry from $C(\Delta)$ into $C([0,1])$.

For example, the Hilbert space $\ell^2$ and every space $L^p([0,1])$ with $1 \le p < \infty$ are isometric to subspaces of $C([0,1])$.
Separability is necessary: $C([0,1])$ is separable, so each of its subspaces is separable, and the non-separable space $\ell^\infty$ does not embed in it.

## Explanations

### L1 human

The space of continuous functions on an interval is big enough to hold a copy of every separable Banach space.
The copy keeps all distances exactly.
So questions about separable Banach spaces can be asked inside one single space.

### L2 human

The theorem says that $C([0,1])$ is universal for the class of separable Banach spaces.
It is the linear analogue of the fact that every compact metric space is a continuous image of the Cantor set, and the proof uses exactly that fact.
The weak-* compactness of the dual ball comes from the Banach–Alaoglu theorem.
Universality makes $C([0,1])$ itself very complicated: every property that fails in some separable space fails in some subspace of $C([0,1])$.
