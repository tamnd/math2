---
tag: 0SEDGXG9S3
kind: definition
name: Cross product
msc: ["15A72"]
topics: [VKVAJ94SKZ]
audience: school
defines: 0N5N15HWZ7
uses: [0QN3D80AWP]
formal:
  - system: lean4
    library: mathlib
    decl: crossProduct
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Cross_product
    locator: Coordinate notation
---

## Definition

Let $a = (a_1, a_2, a_3)$ and $b = (b_1, b_2, b_3)$ be [[vectors|0QN3D80AWP]] in $\mathbb{R}^3$.
The cross product of $a$ and $b$ is the vector
$$a \times b = (a_2 b_3 - a_3 b_2, \; a_3 b_1 - a_1 b_3, \; a_1 b_2 - a_2 b_1).$$

## Notation

Another name is the vector product.
Some books write $a \wedge b$ or $[a, b]$.
In Mathlib the cross product of two vectors $a, b : \text{Fin } 3 \to R$ is `crossProduct a b`, written `a ×₃ b`, for any commutative ring $R$.

## Remarks

For the standard basis vectors $e_1$, $e_2$, $e_3$ of $\mathbb{R}^3$: $e_1 \times e_2 = e_3$, $e_2 \times e_3 = e_1$ and $e_3 \times e_1 = e_2$.
If $\theta$ is the angle between nonzero vectors $a$ and $b$, then $\|a \times b\| = \|a\| \, \|b\| \sin \theta$, the area of the parallelogram with the sides $a$ and $b$, by the [[length formula|~bafd22bd]].
The cross product is [[perpendicular to its factors|0T4QHJXSD4]] and [[anticommutative|07ZS685JJC]], and it is bilinear but not associative.
In the usual right-handed coordinates, $a$, $b$ and $a \times b$ follow the right-hand rule.

## Explanations

### L1 human

The cross product of two arrows in space gives a third arrow that stands at right angles to both.
For example, $(1, 0, 0) \times (0, 1, 0) = (0, 0, 1)$.
The longer the two arrows, and the closer they are to a right angle, the longer their cross product.

### L2 human

To compute a component, cover the column of that component and take the cross difference of the other two columns, with the sign $+$, $-$, $+$.
For $a = (2, 0, 1)$ and $b = (1, 3, 0)$: $a \times b = (0 \cdot 0 - 1 \cdot 3, \; 1 \cdot 1 - 2 \cdot 0, \; 2 \cdot 3 - 0 \cdot 1) = (-3, 1, 6)$.
A trap: the sign of the middle component is the one most often wrong.
