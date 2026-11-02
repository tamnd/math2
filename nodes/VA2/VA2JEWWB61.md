---
tag: VA2JEWWB61
kind: statement
role: theorem
name: Remmert's proper mapping theorem
msc: [32H35, 32C25]
uses: [HXSZA44J5J, 15XEBGNGHC, GB7M582M5Y, AN0BYRKNRA]
about: [15XEBGNGHC, GB7M582M5Y]
sources:
  - url: https://en.wikipedia.org/wiki/Proper_map
---

## Statement

Let $X$ and $Y$ be [[complex analytic spaces|HXSZA44J5J]] and let $f \colon X \to Y$ be a holomorphic map that is [[proper|15XEBGNGHC]].
Let $A \subseteq X$ be an [[analytic subset|GB7M582M5Y]].
Then $f(A)$ is an analytic subset of $Y$, and its [[dimension|AN0BYRKNRA]] is at most the dimension of $A$.

## Remarks

Properness is necessary.
The projection $f \colon \C^2 \to \C$, $(z_1, z_2) \mapsto z_1$, maps the analytic set $A = \set{z_1 z_2 = 1}$ onto $\C \setminus \set{0}$, which is not closed and so not analytic; here $f$ restricted to $A$ is not proper.

Example: the projection $\mathbb{P}^m \times Y \to Y$ is proper because $\mathbb{P}^m$ is compact, so the image of any analytic subset of $\mathbb{P}^m \times Y$ in $Y$ is analytic.
This is the analytic form of the main theorem of elimination theory.

One proof derives it from the coherence of direct images.
Give $A$ its reduced structure.
Then $f_* \mathcal{O}_A$ is a coherent sheaf on $Y$ by Grauert's direct image theorem, and its support is $f(A)$.
The support of a coherent sheaf is analytic.

## Explanations

### L1 human

If a holomorphic map does not let points escape to infinity, then it sends sets defined by holomorphic equations to sets of the same kind.
The image cannot be larger in dimension than the set itself.

### L2 human

The theorem is a basic tool for building analytic sets.
For example, the graph of a holomorphic map is analytic, and its image under a proper projection is analytic.
Remmert proved it before the direct image theorem was known, and it was an early milestone of the global theory of complex spaces.
