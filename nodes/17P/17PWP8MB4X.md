---
tag: 17PWP8MB4X
kind: definition
name: Vector measure
msc: [28B05, 46G10]
defines: PS28BSAJKJ
uses: [PFMGZ7988V, 06GZ956657]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_measure
---

## Definition

Let $\mathcal{F}$ be an [[algebra of sets|PFMGZ7988V]] on a set $\Omega$, and let $B$ be a [[Banach space|06GZ956657]].
A *vector measure* is a map $F \colon \mathcal{F} \to B$ that is finitely additive: $F(E_1 \cup E_2) = F(E_1) + F(E_2)$ for all disjoint $E_1, E_2 \in \mathcal{F}$.
A vector measure $F$ is *countably additive* if, for every sequence $(E_n)$ of pairwise disjoint sets in $\mathcal{F}$ whose union $E$ lies in $\mathcal{F}$,
$$\lim_{N \to \infty} \Big\| F(E) - \sum_{n=1}^{N} F(E_n) \Big\| = 0.$$

## Remarks

Example: let $\mathcal{F}$ be the Lebesgue measurable subsets of $[0, 1]$, let $1 \le p < \infty$, and let $F(E) = \mathbf{1}_E \in L^p([0, 1])$.
Then $F$ is a countably additive vector measure.
Finite additivity holds because $\mathbf{1}_{E_1 \cup E_2} = \mathbf{1}_{E_1} + \mathbf{1}_{E_2}$ for disjoint sets.
For a disjoint sequence, $\norm{F(E) - \sum_{n \le N} F(E_n)}_p = \lambda\big( \bigcup_{n > N} E_n \big)^{1/p} \to 0$.

The same map with values in $L^\infty([0, 1])$ is a vector measure that is not countably additive.
For $E_n = [2^{-n}, 2^{-n+1})$, the remainder $\mathbf{1}_{(0, 2^{-N})}$ has $L^\infty$ norm $1$ for every $N$.

Non-example: $G(E) = \lambda(E)^2 \in \R$ is not a vector measure, since $G([0, 1]) = 1$ but $G([0, \tfrac12)) + G([\tfrac12, 1]) = \tfrac12$.

A real or complex measure that is finite is a countably additive vector measure with $B = \R$ or $B = \C$.
