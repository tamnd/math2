---
tag: M4DP72HFE5
kind: definition
name: Rees matrix semigroup
msc: [20M10, 20M17]
defines: X54RV6SENQ
uses: [G5S1M9, 0XMEM406JM, 0SJ3RX9TXA]
sources:
  - url: https://en.wikipedia.org/wiki/Rees_matrix_semigroup
---

## Definition

Let $G$ be a [[group|G5S1M9]], let $I$ and $\Lambda$ be nonempty [[sets|0SJ3RX9TXA]], and let $P = (p_{\lambda i})_{\lambda \in \Lambda, i \in I}$ be a $\Lambda \times I$ matrix with entries in $G$.
The *Rees matrix semigroup* $\mathcal{M}(G; I, \Lambda; P)$ is the set $I \times G \times \Lambda$ with the product
$$(i, g, \lambda)(j, h, \mu) = (i, \, g \, p_{\lambda j} \, h, \, \mu).$$
The matrix $P$ is called the sandwich matrix.

## Remarks

The product is associative: both ways of bracketing $(i, g, \lambda)(j, h, \mu)(k, f, \nu)$ give $(i, \, g p_{\lambda j} h p_{\mu k} f, \, \nu)$.
So $\mathcal{M}(G; I, \Lambda; P)$ is a [[semigroup|0XMEM406JM]].
It is simple: given $x = (i, g, \lambda)$ and $y = (j, h, \mu)$, one can solve $(j, a, \lambda) \, x \, (i, b, \mu) = y$ for $a, b \in G$.
Rees's theorem: a semigroup is completely simple if and only if it is isomorphic to some $\mathcal{M}(G; I, \Lambda; P)$.

Example: if $I = \Lambda = \set{1}$ and $P = (e)$, then $(1, g, 1) \mapsto g$ is an isomorphism onto $G$.
Example: if $G$ is trivial, $I = \set{1, 2}$ and $\Lambda = \set{1}$, the product is $(i, \lambda)(j, \mu) = (i, \mu) = (i, 1)$, so $xy = x$ for all $x, y$: a left zero semigroup.

Non-example: the monoid $(\N, +)$ is not isomorphic to any Rees matrix semigroup over a group.
It has the proper ideal $\set{1, 2, 3, \dots}$, while a Rees matrix semigroup has no proper two-sided ideal.
