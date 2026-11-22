---
tag: YX1ZQ6TXD4
kind: proof
name: Proof of the universal property of the external direct sum
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug2
proves: N04WS31KXB
methods: [01XM7JEKHY, GQHHNV79PA]
uses: [02WZB422CE, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_sum_of_modules
    locator: Universal property
---

## Proof

We define $f$ by the formula of the statement, check that it is linear and restricts to each $f_j$, and then show that every such map agrees with it.

1. Let $v = (v_i)_{i \in I}$ lie in the [[external direct sum|02WZB422CE]].
   Only finitely many $v_i$ are nonzero, and $f_i(0) = 0$ because $f_i$ is [[linear|0RJF668P1T]].
   So $\sum_{i \in I} f_i(v_i)$ has only finitely many nonzero terms, and we define $f(v)$ as this finite sum.
2. The map $f$ is additive, by the additivity of each $f_i$ and by regrouping a finite sum:
$$f(v + w) = \sum_i f_i(v_i + w_i) = \sum_i f_i(v_i) + \sum_i f_i(w_i) = f(v) + f(w).$$
3. The map $f$ is homogeneous, by the homogeneity of each $f_i$:
$$f(a v) = \sum_i f_i(a v_i) = a \sum_i f_i(v_i) = a f(v).$$
4. Let $j \in I$ and $x \in V_j$.
   The family $\iota_j(x)$ has $x$ in place $j$ and $0$ in the other places, so $f(\iota_j(x)) = f_j(x) + \sum_{i \ne j} f_i(0) = f_j(x)$.
   This proves that $f \circ \iota_j = f_j$, so a map with the required property exists.
5. For uniqueness, let $g$ be a linear map with $g \circ \iota_i = f_i$ for all $i$.
6. Let $v = (v_i)_i$, and let $S$ be the finite set of indices $i$ with $v_i \ne 0$.
   Then $v = \sum_{i \in S} \iota_i(v_i)$, because both sides have the entry $v_i$ in each place $i \in S$ and the entry $0$ elsewhere.
7. Since $g$ is linear,
$$g(v) = \sum_{i \in S} g(\iota_i(v_i)) = \sum_{i \in S} f_i(v_i) = f(v).$$
8. This holds for every $v$, so $g = f$, and the linear map $f$ with $f \circ \iota_i = f_i$ for all $i$ is unique.

## Idea

Every vector of the direct sum is a finite sum of vectors that each live in one summand.
A linear map is therefore forced on the whole sum by its values on the summands, and the forced formula turns out to be linear.
The finite support is used twice: once so that the formula is a finite sum, and once to write $v$ as a finite combination of the injected pieces.

## Variants

The same proof works for modules over any ring, since it uses only addition, scalar multiplication and finite sums.
For a finite family, we can instead write $f$ as the block row $\begin{pmatrix} f_1 & \cdots & f_k \end{pmatrix}$ acting on the column $(v_1, \dots, v_k)$, and the matrix product gives $f_1(v_1) + \cdots + f_k(v_k)$ directly.
