---
tag: JKAPWAARTT
kind: definition
name: Stable map
msc: [58K25, 57R45]
defines: 1991WETZF9
uses: [F45VQ47GPV, 7PN9MD1PQB, 0KZZ70ZHXP]
sources:
  - url: https://en.wikipedia.org/wiki/Singularity_theory
---

## Definition

Let $M$ and $N$ be [[smooth manifolds|F45VQ47GPV]], and give the set $C^\infty(M, N)$ of smooth maps the [[Whitney $C^\infty$ topology|7PN9MD1PQB]].
Two smooth maps $f, g \colon M \to N$ are *equivalent* if there are [[diffeomorphisms|0KZZ70ZHXP]] $\varphi \colon M \to M$ and $\psi \colon N \to N$ with $g = \psi \circ f \circ \varphi^{-1}$.
A smooth map $f \colon M \to N$ is *stable* if there is a neighbourhood $U$ of $f$ in $C^\infty(M, N)$ such that every $g \in U$ is equivalent to $f$.

## Remarks

Example: the height function $f \colon S^1 \to \R$, $f(x, y) = y$, on the unit circle is stable.
Its critical points $(0, \pm 1)$ are nondegenerate with distinct values $\pm 1$.
Any $g$ close enough to $f$ in the $C^2$ sense also has exactly two nondegenerate critical points, a maximum and a minimum.
Their values are distinct, and such a $g$ is equivalent to $f$.
Non-example: a constant map $c \colon S^1 \to \R$ is not stable.
The maps $c + \varepsilon f$ come arbitrarily close to $c$ and have nonzero differential at some points, while every map equivalent to $c$ is constant.
For a compact manifold $M$, a function $f \colon M \to \R$ is stable if and only if all its critical points are nondegenerate and its critical values are pairwise distinct.
The equivalence used here is often called $\mathcal{A}$-equivalence, or left-right equivalence.
