---
tag: NDDB9EDN84
kind: statement
role: proposition
name: Jacobi identity for the cross product
msc: ["15A72", "17B05"]
topics: [VKVAJ94SKZ]
audience: ug1
about: [0N5N15HWZ7]
uses: [0N5N15HWZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Cross_product
    locator: Algebraic properties
  - url: https://en.wikipedia.org/wiki/Jacobi_identity
    locator: Examples
---

## Statement

For all $a, b, c \in \mathbb{R}^3$, the [[cross product|0N5N15HWZ7]] satisfies
$$a \times (b \times c) + b \times (c \times a) + c \times (a \times b) = 0.$$

## Remarks

### Why each hypothesis is needed

The identity holds for all $a, b, c \in \mathbb{R}^3$.
The three terms are the cyclic shifts of $a \times (b \times c)$; a single term is not $0$ in general.
For $a = (1, 2, 3)$, $b = (4, 5, 6)$, $c = (7, 8, 10)$ the terms are $(-12, 9, -2)$, $(96, 0, -64)$ and $(-84, -9, 66)$, by the [[worked example|V2CJH2RJ93]].

### Consequences

- The failure of associativity is one term: $a \times (b \times c) - (a \times b) \times c = -\,b \times (c \times a)$, since $(a \times b) \times c = -\,c \times (a \times b)$.
- $(\mathbb{R}^3, \times)$ is a [[Lie algebra|5JJYBJ6A8K]]: the product is bilinear, $a \times a = 0$, and the Jacobi identity holds.
- The map $\operatorname{ad}_a(v) = a \times v$ satisfies $\operatorname{ad}_a(b \times c) = \operatorname{ad}_a(b) \times c + b \times \operatorname{ad}_a(c)$, a product rule.

### Converse

The Jacobi identity and anticommutativity do not determine the cross product.
The zero product $a \ast b = 0$ also satisfies both.

### Generalizations

The general [[Jacobi identity|ZKFN197MBR]] for the commutator $[x, y] = xy - yx$ of an associative ring is the same identity.
The seven-dimensional cross product does not satisfy it, so it gives no Lie algebra.

## Explanations

### L1 human

The cross product does not let us move brackets: $a \times (b \times c)$ and $(a \times b) \times c$ are in general different.
The Jacobi identity is a rule that replaces the missing rule for brackets.
It says that the three cyclic shifts of $a \times (b \times c)$ add up to the zero vector.

### L2 human

The proof uses the [[vector triple product|03FTB26QYD]] three times; the six dot product terms cancel in pairs.
For $a = \mathbf{i}$, $b = \mathbf{i}$, $c = \mathbf{j}$: the terms are $\mathbf{i} \times \mathbf{k} = -\mathbf{j}$, then $\mathbf{i} \times (\mathbf{j} \times \mathbf{i}) = \mathbf{i} \times (-\mathbf{k}) = \mathbf{j}$, then $\mathbf{j} \times 0 = 0$.
The sum is $0$.
A trap: the identity uses cyclic shifts $(a, b, c) \to (b, c, a) \to (c, a, b)$, not all six orders.

### L3 human

In $\mathbb{R}^3$ with $\times$, the map $a \mapsto [a]_\times$ to antisymmetric matrices turns $\times$ into the commutator $[A, B] = AB - BA$.
So the Jacobi identity for $\times$ follows from the Jacobi identity in the matrix ring, and $(\mathbb{R}^3, \times) \cong \mathfrak{so}(3)$.
