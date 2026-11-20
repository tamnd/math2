---
tag: TVW5BRK42N
kind: proof
name: Proof of the universal property of the direct product of vector spaces
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug2
proves: YT3GZ6YCAH
methods: [01XM7JEKHY, GQHHNV79PA]
uses: [0MM085RX00, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Product_(category_theory)
    locator: Examples
---

## Proof

1. Define $g(x) = (g_i(x))_{i \in I}$. This family has entry $g_i(x) \in V_i$ in place $i$, so it lies in the [[direct product|0MM085RX00]]. No finiteness condition is needed.
2. $g$ is additive: $g(x + y) = (g_i(x + y))_i = (g_i(x) + g_i(y))_i = g(x) + g(y)$, since each $g_i$ is [[linear|0RJF668P1T]] and the sum in the product is entrywise.
3. $g$ is homogeneous: $g(a x) = (a\, g_i(x))_i = a\, g(x)$, by the same reasons.
4. $\pi_j(g(x))$ is the entry of $g(x)$ in place $j$, which is $g_j(x)$. So $\pi_j \circ g = g_j$. This proves existence.
5. For uniqueness, let $h$ be linear with $\pi_i \circ h = g_i$ for all $i$.
6. For $x \in X$, the entry of $h(x)$ in place $i$ is $\pi_i(h(x)) = g_i(x)$, which is also the entry of $g(x)$ in place $i$.
7. Two families with the same entries are equal. So $h(x) = g(x)$ for all $x$, and $h = g$.

## Idea

A vector of the product is the list of its projections.
So a map into the product is the list of its compositions with the projections.

## Variants

- The same proof works for modules over any ring and for products of sets, groups or rings.
- For two factors, $g = (g_1, g_2)$ is the pairing of maps, written $\langle g_1, g_2 \rangle$ in category theory.
