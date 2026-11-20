---
tag: 059THXBRBB
kind: statement
role: proposition
name: Isomorphism with the coordinate space
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [04CYQHN6MC]
uses: [0BMVBHTWV2, 0XSJ25Z9M4]
proofs: [C5282SWAEV]
sources:
  - url: https://en.wikipedia.org/wiki/Coordinate_vector
    locator: The standard representation
  - book: isbn:9780134860244
    locator: Section 2.4
---

## Statement

Let $F$ be a field, let $V$ be a vector space over $F$, and let $B = (b_1, \dots, b_n)$ be a basis of $V$.
Then the map
$$V \to F^n, \qquad v \mapsto [v]_B,$$
that sends each vector to its [[coordinate vector|0BMVBHTWV2]] in $B$, is a [[linear isomorphism|0B8T10CE7N]].
Its inverse sends $(a_1, \dots, a_n)$ to $a_1 b_1 + \cdots + a_n b_n$.

## Remarks

### Why each hypothesis is needed

$B$ must be a basis: for the spanning family $(1, 0), (0, 1), (1, 1)$ of $\R^2$, coordinates are not unique, so $v \mapsto [v]_B$ is not even a map.
For an independent family that does not span, the map is defined only on the span.
$B$ must be ordered: the coordinates of $v$ in $(b_2, b_1)$ are those in $(b_1, b_2)$ in reverse order.

### Consequences

The isomorphism depends on the choice of the basis.
It sends $b_i$ to the standard basis vector $e_i$.
Through this map, each statement about $F^n$ gives a statement about $V$.
Two spaces of the same finite dimension are isomorphic; see [[isomorphic iff equal dimension|0VJBSK15SN]].

### Converse

Conversely, each linear isomorphism $\varphi \colon V \to F^n$ is the coordinate map of exactly one basis, namely $b_i = \varphi^{-1}(e_i)$.

### Generalizations

For a basis $(b_i)_{i \in I}$ of any space, $v \mapsto (a_i)_{i \in I}$ is an isomorphism $V \to F^{(I)}$ onto the finitely supported families.
In Mathlib, this map is `Module.Basis.repr`.

## Explanations

### L1 human

Choosing a basis turns every vector into a list of $n$ numbers.
This translation respects addition and scaling, and it loses no information.
So each $n$-dimensional space is a copy of $F^n$.

### L2 human

Example: $V = P_2(\R)$ with $B = (1, x - 1, (x - 1)^2)$.
Then $[x^2]_B = (1, 2, 1)$ and $[x]_B = (1, 1, 0)$, because $x^2 = 1 + 2(x - 1) + (x - 1)^2$ and $x = 1 + (x - 1)$.
Linearity predicts $[x^2 + 3x]_B = (1, 2, 1) + 3(1, 1, 0) = (4, 5, 1)$.
Check: $4 + 5(x - 1) + (x - 1)^2 = 4 + 5x - 5 + x^2 - 2x + 1 = x^2 + 3x$.
