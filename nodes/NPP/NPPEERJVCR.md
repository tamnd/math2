---
tag: NPPEERJVCR
kind: definition
name: Pullback
msc: [18A30]
defines: Q05K04QJ71
uses: [A2DE66937D, 859F0TFVA3, CHS5AFJGWE, S5744QZV4N, CTJ5AD8ST5, 01AHG4G9RT]
sources:
  - url: https://en.wikipedia.org/wiki/Pullback_(category_theory)
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] and let $f \colon X \to Z$ and $g \colon Y \to Z$ be [[morphisms|859F0TFVA3]] of $\mathcal{C}$.
A *pullback* of $f$ and $g$ is an object $P$ with morphisms $p_1 \colon P \to X$ and $p_2 \colon P \to Y$ such that:

1. $f \circ p_1 = g \circ p_2$;
2. for every object $W$ and all morphisms $q_1 \colon W \to X$ and $q_2 \colon W \to Y$ with $f \circ q_1 = g \circ q_2$, there is exactly one morphism $u \colon W \to P$ with $p_1 \circ u = q_1$ and $p_2 \circ u = q_2$.

The object $P$ is written $X \times_Z Y$ and called the *fibre product* of $X$ and $Y$ over $Z$.

## Remarks

A pullback is the [[limit|CHS5AFJGWE]] of the diagram $X \xrightarrow{f} Z \xleftarrow{g} Y$, so it is unique up to unique isomorphism.
If the [[product|S5744QZV4N]] $X \times Y$ exists, the pullback is the [[equalizer|CTJ5AD8ST5]] of $f \circ \pi_1$ and $g \circ \pi_2 \colon X \times Y \to Z$.

Example: in the category of sets, let $P = \set{(x, y) \in X \times Y : f(x) = g(y)}$ with the two coordinate maps.
Clause 1 holds by the choice of $P$.
Given $q_1, q_2$ with $f \circ q_1 = g \circ q_2$, the map $u(w) = (q_1(w), q_2(w))$ lands in $P$ and is the only map with the required coordinates.
When $g$ is the inclusion of a subset $Y \subseteq Z$, the pullback is the [[preimage|01AHG4G9RT]] $f^{-1}(Y)$ with its inclusion into $X$.

Non-example: in the category of sets, let $X = Y = \{0, 1\}$, $Z = \{*\}$ and let $f, g$ be the constant maps.
The set $\{0, 1\}$ with $p_1 = p_2 = \id$ satisfies clause 1, but the pair $q_1 = \id$, $q_2 = (0 \mapsto 1, 1 \mapsto 0)$ on $W = \{0, 1\}$ admits no $u$ with $p_1 \circ u = q_1$ and $p_2 \circ u = q_2$, so clause 2 fails.
