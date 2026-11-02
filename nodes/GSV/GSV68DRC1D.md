---
tag: GSV68DRC1D
kind: definition
name: Lusternik–Schnirelmann theory of critical points
msc: ["58E05", 55M30]
defines: QARH15D2PN
uses: [F45VQ47GPV, W5BHHXCYXA, 0YTCMFB4HC, 9ZQC7ARWTT]
sources:
  - url: https://en.wikipedia.org/wiki/Lusternik–Schnirelmann_category
---

## Definition

Let $M$ be a compact connected [[smooth manifold|F45VQ47GPV]] without boundary and let $f \colon M \to \R$ be a $C^1$ function.
For a closed subset $A \subseteq M$, let $\operatorname{cat}_M(A)$ be the least $m \ge 0$ such that $m + 1$ open subsets of $M$, each contractible in $M$, cover $A$.
Then $\operatorname{cat}_M(M) = \operatorname{cat}(M)$, the normalized [[Lusternik–Schnirelmann category|W5BHHXCYXA]].
For $k = 0, 1, \dots, \operatorname{cat}(M)$, the *Lusternik–Schnirelmann minimax values* of $f$ are
$$c_k = \inf \set{ \max_{x \in A} f(x) : A \subseteq M \text{ closed}, \ A \ne \emptyset, \ \operatorname{cat}_M(A) \ge k }.$$
*Lusternik–Schnirelmann theory* is the [[critical point theory|9ZQC7ARWTT]] built on these values.
Its basic theorem states:

1. each $c_k$ is a critical value of $f$, and $c_0 \le c_1 \le \cdots \le c_{\operatorname{cat}(M)}$;
2. if $c_k = c_{k+1}$ for some $k$, then $f$ has infinitely many [[critical points|0YTCMFB4HC]] at that level;
3. hence $f$ has at least $\operatorname{cat}(M) + 1$ critical points.

## Remarks

The proof uses a deformation along a pseudo-gradient flow.
If $c$ is not a critical value, the sublevel set $\set{f \le c + \varepsilon}$ can be pushed into $\set{f \le c - \varepsilon}$, and such deformations do not increase category.
If the critical set at level $c_k = c_{k+1}$ were finite, it would have a neighbourhood of category $0$, and subadditivity of category would give a contradiction.
Since one-point sets are allowed for $k = 0$, the first value is $c_0 = \min f$.

Example: for $M = T^2$, $\operatorname{cat}(T^2) = 2$, so every $C^1$ function on the torus has at least three critical points.
This bound is attained by suitable functions, while a Morse function on $T^2$ has at least four.

Non-example: the theory does not apply as stated to $f(x) = \arctan x$ on the non-compact manifold $\R$.
There $\operatorname{cat}(\R) = 0$ would predict one critical point, but $f$ has none, since the infimum defining $c_0$ is not attained.
In infinite dimensions compactness of $M$ is replaced by the [[Palais–Smale condition|4724KRNHAT]] together with completeness and a lower bound on $f$.
