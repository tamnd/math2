---
tag: YBAPZPEDWQ
kind: definition
name: Thurston norm
msc: [57K30, 57K31]
defines: 9B4A2WHAPQ
uses: [R20TB2KEQQ, 702SNFQG0W, RNDDWDAFJ5, M0Q5CFJ7ZH, FP5GVCN8GV]
sources:
  - url: https://en.wikipedia.org/wiki/Thurston_norm
---

## Definition

Let $M$ be a compact [[orientable|702SNFQG0W]] [[3-manifold|R20TB2KEQQ]].
For a compact surface $S$ with connected components $S_1, \ldots, S_k$, set
$$\chi_-(S) = \sum_{i=1}^{k} \max(0, -\chi(S_i)),$$
where $\chi$ is the [[Euler characteristic|RNDDWDAFJ5]].
For a class $a \in H_2(M, \partial M; \Z)$ in [[homology|M0Q5CFJ7ZH]], the *Thurston norm* of $a$ is
$$x(a) = \min \set{\chi_-(S) : S \text{ a properly embedded oriented surface in } M \text{ with } [S] = a}.$$
The function $x$ satisfies $x(n a) = n\, x(a)$ for integers $n \ge 0$ and $x(a + b) \le x(a) + x(b)$, and it extends uniquely to a continuous [[seminorm|FP5GVCN8GV]] on $H_2(M, \partial M; \R)$, also called the Thurston norm.

## Remarks

Example: let $F$ be a closed orientable surface of genus $g \ge 2$ and $M = F \times S^1$.
The fiber $F \times \set{1}$ represents a class $a$ with $\chi_-(F) = 2g - 2$, and Thurston showed that fibers of a fibration over the circle minimise $\chi_-$ in their class, so $x(a) = 2g - 2$.

Non-example of definiteness: in $M = S^2 \times S^1$ the class $a$ of $S^2 \times \set{1}$ is nonzero, but $\chi_-(S^2) = 0$, so $x(a) = 0$.
So $x$ is in general only a seminorm, not a norm.
It is a norm when no nonzero class is represented by spheres, disks, tori and annuli, for example when $M$ is hyperbolic.
