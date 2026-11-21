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

Two cross products in a row can always be replaced by dot products, and that is the main tool for simplifying vector expressions.
Let $a$, $b$ and $c$ be vectors in $\mathbb{R}^3$.
Let $\times$ be the [[cross product|0N5N15HWZ7]] and $\cdot$ the [[dot product|0S52TNNTH9]].
Then
$$a \times (b \times c) = (a \cdot c) \, b - (a \cdot b) \, c.$$

## Remarks

### Why each hypothesis is needed

The identity holds for all $a, b, c \in \mathbb{R}^3$, with no further hypothesis.
It fails for the seven-dimensional cross product mentioned on the [[cross product|0N5N15HWZ7]] page, so the space really must be $\mathbb{R}^3$.

### Why the answer lies in a plane

The shape of the formula has a geometric reason.
The vector $b \times c$ is perpendicular to the plane of $b$ and $c$.
Crossing it with $a$ gives a vector perpendicular to $b \times c$, so the result falls back into the plane of $b$ and $c$.
The identity says exactly which combination of $b$ and $c$ it is.
When $b$ and $c$ are not parallel, those coefficients are unique.

### What it gives you

The other bracketing follows by anticommutativity:
$$(a \times b) \times c = -\,c \times (a \times b) = (a \cdot c) \, b - (b \cdot c) \, a.$$
Comparing the two shows that the cross product is not associative.
For $a = b = \mathbf{i}$ and $c = \mathbf{j}$, the first bracketing gives $\mathbf{i} \times \mathbf{k} = -\mathbf{j}$, while $(\mathbf{i} \times \mathbf{i}) \times \mathbf{j} = 0$.
Applying the identity to the three cyclic shifts and adding gives the [[Jacobi identity|NDDB9EDN84]].

The identity also splits a vector along a unit vector $n$:
$$v = (v \cdot n) \, n + n \times (v \times n),$$
where the first part runs along $n$ and the second lies across it.
Together with the exchange of dot and cross, it gives the Binet-Cauchy identity $(a \times b) \cdot (c \times d) = (a \cdot c)(b \cdot d) - (a \cdot d)(b \cdot c)$.

### Beyond three dimensions

In geometric algebra the identity reads $a \cdot (b \wedge c) = (a \cdot b) \, c - (a \cdot c) \, b$, and in that form it holds in every dimension.
In $\mathbb{R}^3$ the map $v \mapsto a \times v$ is the infinitesimal rotation about $a$, and the identity describes the square of this map.

## Explanations

### L1 human

The vector $b \times c$ is perpendicular to the plane of $b$ and $c$.
A second cross product with $a$ gives a vector perpendicular to $b \times c$, so the result lies back in the plane of $b$ and $c$.
The formula says which combination of $b$ and $c$ it is.
A memory aid is "BAC minus CAB": $a \times (b \times c) = b (a \cdot c) - c (a \cdot b)$.

### L2 human

Here is a check with $a = (1, 2, 3)$, $b = (4, 5, 6)$ and $c = (7, 8, 10)$, which the [[worked example|V2CJH2RJ93]] carries out in full.
Directly, $b \times c = (2, 2, -3)$ and $a \times (b \times c) = (-12, 9, -2)$.
By the formula, with $a \cdot c = 53$ and $a \cdot b = 32$,
$$53 \, (4, 5, 6) - 32 \, (7, 8, 10) = (-12, 9, -2).$$
The typical use is to turn an expression with two cross products into one with dot products only.
Watch out: the middle vector of the bracket, here $b$, gets the plus sign, and the outer one, $c$, gets the minus sign.

### L3 human

Let $[a]_\times$ be the antisymmetric matrix of the map $v \mapsto a \times v$.
The identity shows that $[a \times b]_\times = [a]_\times [b]_\times - [b]_\times [a]_\times$, so $a \mapsto [a]_\times$ is an isomorphism from the Lie algebra $(\mathbb{R}^3, \times)$ onto $\mathfrak{so}(3)$, the [[Lie algebra|5JJYBJ6A8K]] of antisymmetric $3 \times 3$ matrices.
It also gives $[a]_\times^2 = a a^{\mathsf{T}} - \|a\|^2 I$.
