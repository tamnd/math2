---
tag: CRFGFCNG3Q
kind: definition
name: Group scheme
msc: [14L15]
defines: TJ04VQP4NB
uses: [5A35TYZD02, JXRKH6P1Z4, 1DZMT4S9FB, SWWW9X4A3N, G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Group_scheme
---

## Definition

Let $S$ be a [[scheme|5A35TYZD02]], and let $\pi \colon G \to S$ be a scheme over $S$.
Products below are [[fiber products|1DZMT4S9FB]] over $S$, and all maps are [[morphisms|JXRKH6P1Z4]] over $S$.
A *group scheme* over $S$ is such a $G$ with morphisms $m \colon G \times_S G \to G$, $e \colon S \to G$ and $i \colon G \to G$ such that:

1. $m \circ (m \times \id_G) = m \circ (\id_G \times m)$ as morphisms $G \times_S G \times_S G \to G$.
2. $m \circ (e \circ \pi, \id_G) = \id_G = m \circ (\id_G, e \circ \pi)$.
3. $m \circ (i, \id_G) = e \circ \pi = m \circ (\id_G, i)$.

## Remarks

Equivalently, for every $S$-scheme $T$, the set $G(T)$ of $S$-morphisms $T \to G$ carries a [[group|G5S1M9]] structure, and the maps $G(T') \to G(T)$ induced by $S$-morphisms $T \to T'$ are group homomorphisms.
This is the [[functor of points|SWWW9X4A3N]] form of the definition.
For example, the multiplicative group $\mathbb{G}_{m,S} = \operatorname{Spec} \Z[t, t^{-1}] \times_{\operatorname{Spec} \Z} S$ is a group scheme over $S$.
For an affine $S$-scheme $T = \operatorname{Spec} R$, its points are $\mathbb{G}_m(T) = R^\times$, the units of $R$ under multiplication.
The affine line $\mathbb{A}^1_S$ with multiplication $(a, b) \mapsto ab$ is not a group scheme.
Clause 3 fails, since the point $0 \in R$ has no multiplicative inverse in a nonzero ring $R$.
