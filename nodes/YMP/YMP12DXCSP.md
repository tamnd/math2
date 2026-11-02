---
tag: YMP12DXCSP
kind: statement
role: theorem
name: Bochner's tube theorem
msc: [32D10, 32Q02, 32A10]
uses: [507C34W0ZT, 0FQSDC2EQ2, 0SPE8WNWFV, 02BH3MCBQB]
about: [507C34W0ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Bochner%27s_tube_theorem
same_as:
  wikidata: Q107535899
  wikipedia: Bochner's tube theorem
---

## Statement

Let $B \subseteq \R^n$ be a nonempty [[connected|0SPE8WNWFV]] [[open set|02BH3MCBQB]], and let $\operatorname{ch}(B)$ be its [[convex hull|0FQSDC2EQ2]].
For a set $S \subseteq \R^n$ let $T_S = \set{x + iy \in \C^n : x \in S, \ y \in \R^n}$ be the tube over $S$.
Then every [[holomorphic function|507C34W0ZT]] on $T_B$ is the restriction of a unique holomorphic function on $T_{\operatorname{ch}(B)}$.

## Remarks

Uniqueness holds because $T_{\operatorname{ch}(B)}$ is connected and contains the nonempty open set $T_B$.
Classical proofs push the function across the convex hull with Cauchy integrals over families of analytic discs, in the spirit of the continuity principle.
Another route uses that a tube which is a domain of holomorphy has a convex base.
On such a tube, $-\log$ of the distance to the boundary is plurisubharmonic.
It does not depend on $y$, so it is a convex function of $x$.

Example: let $B = \set{x \in \R^2 : 1 < \abs{x} < 2}$, an annulus.
Its convex hull is the disc $\abs{x} < 2$, so every holomorphic function on $T_B$ extends to the tube over the disc.

Consequently, a tube $T_B$ with connected open base is a domain of holomorphy exactly when $B$ is convex.
For $n = 1$ the theorem is empty, since connected open subsets of $\R$ are intervals and already convex.

## Explanations

### L1 human

A tube domain is determined by its real part: the imaginary part may be anything.
The theorem says that holomorphic functions on a tube automatically extend to the tube over the convex hull of the base.
So, for tubes, being a natural domain of holomorphic functions is the same as ordinary convexity of the base.

### L2 human

Tube domains appear in Fourier and Laplace analysis: the Laplace transform $z \mapsto \int e^{z_1 t_1 + \cdots + z_n t_n} \, d\mu(t)$ of a measure $\mu$ on $\R^n$ is holomorphic on a tube whose base is convex.
The theorem explains why convex bases are the natural ones.
It is a basic example of the computation of an envelope of holomorphy: the envelope of $T_B$ is $T_{\operatorname{ch}(B)}$.
