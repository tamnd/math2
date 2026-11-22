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

We define $g$ by listing the values of the $g_i$, check that it is linear with the right projections, and then show that a map into the product is determined by its projections.

1. For $x \in X$, define $g(x) = (g_i(x))_{i \in I}$.
   This family has the entry $g_i(x) \in V_i$ in place $i$, so it lies in the [[direct product|0MM085RX00]].
   No finiteness condition has to be checked, because the product allows all families.
2. The map $g$ is additive, since each $g_i$ is [[linear|0RJF668P1T]] and the addition of the product is entrywise:
$$g(x + y) = \big(g_i(x + y)\big)_i = \big(g_i(x) + g_i(y)\big)_i = g(x) + g(y).$$
3. The map $g$ is homogeneous, for the same two reasons:
$$g(a x) = \big(g_i(a x)\big)_i = \big(a\, g_i(x)\big)_i = a\, g(x).$$
4. For $j \in I$, the vector $\pi_j(g(x))$ is the entry of $g(x)$ in place $j$, which is $g_j(x)$.
   So $\pi_j \circ g = g_j$, and a map with the required property exists.
5. For uniqueness, let $h \colon X \to \prod_i V_i$ be a linear map with $\pi_i \circ h = g_i$ for all $i$.
6. For $x \in X$ and $i \in I$, the entry of $h(x)$ in place $i$ is $\pi_i(h(x)) = g_i(x)$, which is also the entry of $g(x)$ in place $i$.
7. Two families with the same entry in every place are equal.
   So $h(x) = g(x)$ for every $x$, and $h = g$.

## Idea

A vector of the product is nothing more than the list of its projections.
So a map into the product is nothing more than the list of its compositions with the projections, and the only possible map is the one that lists the values $g_i(x)$.
Unlike the proof for the direct sum, no finiteness enters, which is why the product, and not the direct sum, receives the combined map of an infinite family.

## Variants

The same proof works for modules over any ring and for products of sets, groups or rings, since it uses only that the operations are entrywise.
For two factors, the map $g$ is the pairing of $g_1$ and $g_2$, written $(g_1, g_2)$ or $\langle g_1, g_2 \rangle$ in category theory, and in matrix form it stacks the matrix of $g_1$ above the matrix of $g_2$.
