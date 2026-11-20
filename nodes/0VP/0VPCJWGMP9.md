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

Let $F$ be a field and let $V$ and $W$ be [[vector spaces|05EGHEQZAW]] over $F$.
The *space of linear maps* $\Hom_F(V, W)$ is the set of all [[linear maps|0RJF668P1T]] $V \to W$, with the operations
$$(S + T)(v) = S(v) + T(v), \qquad (aT)(v) = a\, T(v)$$
for $S, T \in \Hom_F(V, W)$, $a \in F$ and $v \in V$.

## Notation

Other notations are $\Hom(V, W)$, $L(V, W)$ and $\mathcal L(V, W)$.
For $W = V$, the space is written $\End(V)$.
For $W = F$, it is the dual space $V^*$.

## Remarks

- The operations are pointwise: each one acts on the values $S(v)$ and $T(v)$ in $W$.
- The sum $S + T$ and the multiple $aT$ are again linear, and the vector space axioms hold. A separate statement proves this.
- The zero vector is the zero map $v \mapsto 0$.
- The definition does not use composition. Composition is a second operation, defined only when the spaces match.

## Explanations

### L1 human

The space of linear maps collects all linear maps from $V$ to $W$.
Two such maps are added by adding their values, and a map is scaled by scaling its values.

### L2 human

For $S(x, y) = (2x, y)$ and $T(x, y) = (y, 0)$ on $\R^2$, the definition gives $(S + T)(x, y) = (2x + y,\ y)$.
Also $(3T)(x, y) = (3y, 0)$.
The trap is to read $S + T$ as "apply $S$, then $T$"; that is the composite $T \circ S$.
