---
tag: RRK8P6TXG2
kind: concept
name: Ample line bundle
msc: [14C20]
sources:
  - url: https://en.wikipedia.org/wiki/Ample_line_bundle
same_as:
  wikidata: Q4748472
  wikipedia: Ample line bundle
---

## Summary

A line bundle is ample when its high tensor powers have enough global sections to embed the scheme into projective space.
Let $X$ be a scheme of finite type over a Noetherian ring.
A line bundle $L$ on $X$ is ample exactly when some power $L^{\otimes m}$ is very ample.
Very ample means that it is the pullback of $\mathcal{O}(1)$ under an immersion into projective space.
Ampleness is the algebraic form of positivity: it plays the role of positive curvature in complex geometry.
Many vanishing, finiteness and embedding theorems assume an ample line bundle.

## Explanations

### L1 human

A line bundle attaches a line to each point of a space, and its sections are like functions with values in these lines.
A line bundle is ample if, after taking a high enough power, its sections can tell all points apart and all tangent directions apart.
Then the sections give coordinates that place the space inside a projective space without folding it.
On the projective line, the bundle $\mathcal{O}(1)$, whose sections are the linear forms, is ample.
Its dual $\mathcal{O}(-1)$ has no nonzero sections in any positive power, so it is not ample.
