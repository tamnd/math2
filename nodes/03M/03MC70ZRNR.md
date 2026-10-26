---
tag: 03MC70ZRNR
kind: statement
role: theorem
name: Equivalence of norms in finite dimension
msc: [46B20]
uses: [0J3578562S, 07PFYV65MB, 0V4DET59NW, 0KNJWEVSMG]
sources:
  - url: https://en.wikipedia.org/wiki/Norm_(mathematics)
    locator: Equivalence
---

## Statement

Let $V$ be a finite-dimensional vector space over $\mathbb{R}$ or $\mathbb{C}$.
Then any two norms on $V$ are [[equivalent|0J3578562S]].

## Remarks

Proof idea: fix a basis and compare a norm $\|\cdot\|$ with the [[sup norm|0KNJWEVSMG]] $\|\cdot\|_\infty$ of the coordinates. The triangle inequality gives $\|x\| \le C \|x\|_\infty$, so $\|\cdot\|$ is continuous for $\|\cdot\|_\infty$. The unit sphere of $\|\cdot\|_\infty$ is compact by the [[Heine–Borel theorem|07PFYV65MB]], so $\|\cdot\|$ has a positive minimum $c$ on it, by the [[extreme value theorem|0V4DET59NW]].
Thus there is only one norm topology on $\mathbb{R}^n$, the Euclidean topology.
The statement fails in infinite dimensions: each infinite-dimensional normed space has norms that are not equivalent.

## Explanations

### L1 human

In finite dimensions, it does not matter which norm you choose: all norms give the same convergent sequences and the same open sets.
