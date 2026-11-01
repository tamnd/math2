---
tag: VT3NYDTY95
kind: definition
name: Entourage
msc: ["54E15"]
defines: FVFFKNKEDF
uses: [A54T86KS63, 05AVARPXA2]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_space
---

## Definition

Let $(X, \mathcal{U})$ be a [[uniform space|A54T86KS63]].
An *entourage* of $X$ is a member of the uniformity $\mathcal{U}$, that is, a subset $U \subseteq X \times X$ with $U \in \mathcal{U}$.
For an entourage $U$ and a point $x \in X$, the set $U[x] = \set{y \in X : (x, y) \in U}$ is the $U$-neighbourhood of $x$.
An entourage $U$ is *symmetric* if $(x, y) \in U$ implies $(y, x) \in U$.

## Remarks

On $\R$ with the uniformity of the metric $\abs{x - y}$, the set $\set{(x, y) : \abs{x - y} < 1}$ is an entourage, and $U[x] = (x - 1, x + 1)$.
The set $\set{(x, y) : \abs{x - y} < 1 / (1 + x^2)}$ contains the diagonal, but it is not an entourage of that uniformity.
It contains no set $\set{(x, y) : \abs{x - y} < \varepsilon}$ with $\varepsilon > 0$, because its width tends to $0$ as $\abs{x}$ grows.
Every entourage contains a symmetric entourage, namely $U \cap U^{-1}$.
The sets $U[x]$, for $U$ an entourage, form a neighbourhood base at $x$ of the uniform topology.

## Explanations

### L1 human

An entourage is a set of pairs of points that a uniform space counts as close.
Picture the plane $X \times X$; an entourage is a region that contains the whole diagonal $y = x$.
For $\R$ with its usual distance, the region between the lines $y = x - 1$ and $y = x + 1$ is an entourage.
