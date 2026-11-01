---
tag: PE207P2DZD
kind: counterexample
name: Hedetniemi's conjecture
msc: [05C15, 05C76]
uses: [0JD5C82QMB, 0C5M7AM6FH, 06SCB3R6BN, 03WKB2H474]
sources:
  - url: https://en.wikipedia.org/wiki/Hedetniemi's_conjecture
---

## Counterexample

Let $G$ and $H$ be finite [[graphs|0JD5C82QMB]].
Their tensor product $G \times H$ has vertex set $V(G) \times V(H)$.
In it, $(g, h)$ is adjacent to $(g', h')$ when $gg'$ is an edge of $G$ and $hh'$ is an edge of $H$.
Hedetniemi's conjecture asserted that $\chi(G \times H) = \min(\chi(G), \chi(H))$ for all finite graphs $G$ and $H$, where $\chi$ is the [[chromatic number|0C5M7AM6FH]].
The conjecture is false: in 2019 Yaroslav Shitov constructed finite graphs $G$ and $H$ with
$$\chi(G \times H) < \min(\chi(G), \chi(H)).$$

## Remarks

The inequality $\chi(G \times H) \le \min(\chi(G), \chi(H))$ always holds.
Indeed, the projection $(g, h) \mapsto g$ is a [[graph homomorphism|06SCB3R6BN]] to $G$, so a proper colouring of $G$ pulls back to one of $G \times H$.
The same holds for $H$.
Shitov's counterexample uses an exponential graph.
For a graph $G$ and $c \ge 1$, the vertices of $K_c^G$ are all maps $f \colon V(G) \to \set{1, \dots, c}$.
Two maps $f$ and $f'$ are adjacent when $f(u) \ne f'(v)$ for every edge $uv$ of $G$, in both orders of $u$ and $v$.
The map $(v, f) \mapsto f(v)$ is a proper colouring of $G \times K_c^G$ with $c$ colours.
Indeed, if $(u, f)$ and $(v, f')$ are adjacent, then $uv$ is an edge and $f$ is adjacent to $f'$, so $f(u) \ne f'(v)$.
So any $G$ with $\chi(G) > c$ and $\chi(K_c^G) > c$ is a counterexample, and Shitov showed that such $G$ exist for large $c$.
The conjecture holds when $\min(\chi(G), \chi(H)) \le 4$; the case $4$ is a theorem of El-Zahar and Sauer.

## Explanations

### L1 human

In the tensor product of two graphs, two pairs are joined when both coordinates are joined.
Colouring either factor gives a colouring of the product, so the product never needs more colours than the easier factor.
For over fifty years people believed it never needs fewer, but Shitov found very large graphs where it does.
