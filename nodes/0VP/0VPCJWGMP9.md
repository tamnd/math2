---
tag: 0VPCJWGMP9
kind: definition
name: Space of linear maps
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
defines: 0X9MBPP2Z3
uses: [0RJF668P1T, 05EGHEQZAW]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Vector space of linear maps
  - book: isbn:9783031410253
    locator: Chapter 3
  - book: isbn:9780135367971
    locator: Section 3.2
---

## Definition

The space of linear maps collects all linear maps from one space to another, and adds and scales them value by value.

Let $F$ be a field and let $V$ and $W$ be [[vector spaces|05EGHEQZAW]] over $F$.
The *space of linear maps* $\Hom_F(V, W)$ is the set of all [[linear maps|0RJF668P1T]] $V \to W$, with the operations
$$(S + T)(v) = S(v) + T(v), \qquad (aT)(v) = a\, T(v)$$
for $S, T \in \Hom_F(V, W)$, $a \in F$ and $v \in V$.

## Notation

Other notations are $\Hom(V, W)$, $L(V, W)$ and $\mathcal L(V, W)$.
For $W = V$ the space is written $\End(V)$, and for $W = F$ it is the dual space $V^*$.

## Remarks

The operations are pointwise: each one acts on the values $S(v)$ and $T(v)$ in $W$.
That the sum $S + T$ and the multiple $aT$ are again linear, and that the vector space axioms hold, is a [[separate theorem|PB7N4R8C6X]].
The zero vector is the zero map $v \mapsto 0$.

For example, for $S(x, y) = (2x, y)$ and $T(x, y) = (y, 0)$ on $\R^2$, the definition gives $(S + T)(x, y) = (2x + y, \; y)$ and $(3T)(x, y) = (3y, 0)$.
A failing case is a map that is not linear, such as $v \mapsto v + (1, 0)$ on $\R^2$, which does not belong to $\Hom(\R^2, \R^2)$ at all.

The definition does not use composition, which is a second operation, defined only when the spaces match.
The [[concept page|0X9MBPP2Z3]] has more examples and the main properties.

## Explanations

### L1 human

The space of linear maps collects all linear maps from $V$ to $W$.
Two such maps are added by adding their values, and a map is scaled by scaling its values.

### L2 human

For $S(x, y) = (x, 0)$ and $T(x, y) = (0, y)$ on $\R^2$, the definition gives $(S + T)(x, y) = (x, y)$, so $S + T = \id$.
Watch out: $S + T$ does not mean "apply $S$, then $T$", which is the composite $T \circ S$, here the zero map.
