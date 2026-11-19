---
tag: 03FTB26QYD
kind: statement
role: proposition
name: Vector triple product
aliases: [triple-product-expansion, bac-cab-identity]
msc: ["15A72"]
topics: [VKVAJ94SKZ]
audience: ug1
about: [0N5N15HWZ7]
uses: [0N5N15HWZ7, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Triple_product
    locator: Vector triple product
inventory: [TPQYVR234A]
---

## Statement

Let $a$, $b$ and $c$ be vectors in $\mathbb{R}^3$.
Let $\times$ be the [[cross product|0N5N15HWZ7]] and let $\cdot$ be the [[dot product|0S52TNNTH9]].
Then
$$a \times (b \times c) = (a \cdot c) \, b - (a \cdot b) \, c.$$

## Remarks

### Why each hypothesis is needed

The identity holds for all $a, b, c \in \mathbb{R}^3$, with no further hypothesis.
It fails for the seven-dimensional cross product, which is mentioned in the [[cross product|0N5N15HWZ7]] node.
So the space must be $\mathbb{R}^3$.

### Consequences

- The other bracketing: $(a \times b) \times c = -c \times (a \times b) = (a \cdot c) \, b - (b \cdot c) \, a$.
- The cross product is not associative. For $a = b = \mathbf{i}$ and $c = \mathbf{j}$: $\mathbf{i} \times (\mathbf{i} \times \mathbf{j}) = \mathbf{i} \times \mathbf{k} = -\mathbf{j}$, but $(\mathbf{i} \times \mathbf{i}) \times \mathbf{j} = 0$.
- The [[Jacobi identity|~d54cd1fb]] $a \times (b \times c) + b \times (c \times a) + c \times (a \times b) = 0$.
- For a unit vector $n$, $v = (v \cdot n) \, n + n \times (v \times n)$. This splits $v$ into its parts along and across $n$.
- The Binet-Cauchy identity $(a \times b) \cdot (c \times d) = (a \cdot c)(b \cdot d) - (a \cdot d)(b \cdot c)$, by the exchange of dot and cross.

### Converse

The result $a \times (b \times c)$ lies in the plane of $b$ and $c$, and the identity gives its coefficients.
The coefficients are unique when $b$ and $c$ are not parallel.

### Generalizations

In geometric algebra the identity reads $a \cdot (b \wedge c) = (a \cdot b) \, c - (a \cdot c) \, b$, and it holds in every dimension.
In $\mathbb{R}^3$, $\operatorname{ad}_a(v) = a \times v$ is the infinitesimal rotation about $a$, and the identity describes the square of this map.

## Explanations

### L1 human

The vector $b \times c$ is perpendicular to the plane of $b$ and $c$.
A second cross product with $a$ gives a vector perpendicular to $b \times c$, so the result lies back in the plane of $b$ and $c$.
The formula says which combination of $b$ and $c$ it is.
A memory aid is "BAC minus CAB": $a \times (b \times c) = b (a \cdot c) - c (a \cdot b)$.

### L2 human

Worked check with $a = (1, 2, 3)$, $b = (4, 5, 6)$ and $c = (7, 8, 10)$; the [[worked example|~ef2efaab]] gives all details.

1. $b \times c = (2, 2, -3)$ and $a \times (b \times c) = (-12, 9, -2)$.
2. $a \cdot c = 53$ and $a \cdot b = 32$, and $53 \, (4, 5, 6) - 32 \, (7, 8, 10) = (-12, 9, -2)$.

The typical use is to simplify an expression with two cross products into dot products.
A trap: the middle vector of the bracket, here $b$, gets the plus sign; the outer one, $c$, gets the minus sign.

### L3 human

The identity says that the Lie algebra $(\mathbb{R}^3, \times)$ is isomorphic to $\mathfrak{so}(3)$, the [[Lie algebra|5JJYBJ6A8K]] of antisymmetric $3 \times 3$ matrices.
The map $a \mapsto [a]_\times$ sends $a$ to the matrix of $v \mapsto a \times v$, and $[a]_\times^2 = a a^{\mathsf{T}} - \|a\|^2 I$.
