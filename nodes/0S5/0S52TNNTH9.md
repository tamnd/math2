---
tag: 0S52TNNTH9
kind: concept
name: Dot product
aliases: [scalar-product]
msc: ["15A63", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
specializes: [0NB0AWGJBW]
uses: [0QN3D80AWP, 0XKBKGTCPC]
sources:
  - url: https://en.wikipedia.org/wiki/Dot_product
    locator: Coordinate definition
  - url: https://en.wikipedia.org/wiki/Dot_product
    locator: Equivalence of the definitions
  - book: isbn:9781733146678
    locator: Section 1.2
  - url: https://understandinglinearalgebra.org/
    locator: Section 6.1
same_as:
  wikidata: Q181365
  wikipedia: Dot product
---

## Summary

The dot product of two [[vectors|0QN3D80AWP]] $u = (u_1, \dots, u_n)$ and $v = (v_1, \dots, v_n)$ of $\mathbb{R}^n$ is the real number
$$u \cdot v = u_1 v_1 + u_2 v_2 + \dots + u_n v_n.$$
This is the coordinate definition, and the [[formal definition|05HQYM0R4G]] states it.
In the plane and in space there is also a geometric definition: $u \cdot v = \|u\| \, \|v\| \cos \theta$, where $\|\cdot\|$ is the [[length|0XKBKGTCPC]] and $\theta$ is the [[angle between the vectors|0ZEHZY85E6]].
The [[geometric formula for the dot product|070TXS9AXM]] shows by the law of cosines that the two definitions agree.
The dot product matters because it turns lengths, angles and perpendicularity into calculations with numbers.

## Motivation

Many questions of geometry ask for an angle or for a length: is this corner a right angle, or how far is this point from that line.
With coordinates, lengths come from the Pythagorean theorem, but angles need trigonometry.
The law of cosines links the two: for the triangle with the sides $u$, $v$ and $v - u$, it gives $\|v - u\|^2 = \|u\|^2 + \|v\|^2 - 2\|u\| \, \|v\| \cos \theta$.
If we expand $\|v - u\|^2$ in coordinates, the term $-2(u_1 v_1 + \dots + u_n v_n)$ appears.
So the number $u_1 v_1 + \dots + u_n v_n$ is exactly $\|u\| \, \|v\| \cos \theta$.
This number is easy to compute, and it carries the angle.
Physics found the same number independently: the work of a constant force $F$ along a displacement $d$ is $F \cdot d$.

## Notation

- Books write $u \cdot v$, $\langle u, v \rangle$, $(u, v)$ or $\langle u \mid v \rangle$.
- When vectors are columns, $u \cdot v = u^{\mathsf{T}} v$, a $1 \times 1$ matrix that we identify with a number.
- Other names are the scalar product and, for $\mathbb{R}^n$, the standard inner product.
- Do not confuse the dot product with the product $c \cdot v$ of a scalar and a vector, which some books also write with a dot.

## Remarks

### Examples

- $(1, 2, 3) \cdot (4, 5, 6) = 4 + 10 + 18 = 32$.
- $(1, 2) \cdot (-2, 1) = -2 + 2 = 0$, so the two vectors are perpendicular.
- For the standard unit vectors, $\mathbf{i} \cdot \mathbf{i} = 1$ and $\mathbf{i} \cdot \mathbf{j} = 0$.
- For $u = (3, 0)$ and $v = (2, 2)$ both definitions give $6$. The [[worked comparison|~98714500]] shows the steps.
- A force $(2, 3, 1)$ newtons along the displacement $(4, -1, 2)$ metres does the work $7$ joules. The [[work example|~d27715bf]] gives the details.

### Non-examples

- The product component by component, $(1, 2, 3) \ast (4, 5, 6) = (4, 10, 18)$, is a vector, not the dot product. The dot product adds these numbers.
- The form $u_1 v_1 - u_2 v_2$ on $\mathbb{R}^2$ is symmetric and bilinear, but it is not positive. The [[non-example of the Minkowski form|~22f8dc4f]] shows that the vector $(1, 1)$ gives $0$.
- The product $\|u\| \, \|v\|$ of the lengths is not the dot product: it does not change when $v$ turns, and the dot product does.

### Basic properties

For all $u, v, w \in \mathbb{R}^n$ and all real $a$ and $b$:

- Symmetry: $u \cdot v = v \cdot u$, because $u_i v_i = v_i u_i$ for each $i$.
- Linearity in each factor: $(au + bw) \cdot v = a(u \cdot v) + b(w \cdot v)$, because real multiplication distributes over addition.
- Positivity: $v \cdot v = v_1^2 + \dots + v_n^2 \geq 0$, with equality only for $v = 0$.
- Length: $v \cdot v = \|v\|^2$, by the definition of the length.
- Expansion of a square: $\|u + v\|^2 = \|u\|^2 + 2\, u \cdot v + \|v\|^2$, by linearity and symmetry.
- [[Perpendicularity|03NK6RSRQ1]]: $u$ and $v$ are perpendicular exactly when $u \cdot v = 0$.
- The [[Cauchy-Schwarz inequality|0RFWW56Y22]]: $|u \cdot v| \leq \|u\| \, \|v\|$.

### History

Hamilton found the dot product inside the product of quaternions in the 1840s.
For two pure quaternions, the real part of the product is minus the dot product, and the vector part is the cross product.
Gibbs, in his lectures on vector analysis of the 1880s, made the dot product a separate operation and introduced the notation $u \cdot v$.

### Common errors

- Students treat $u \cdot v$ as a vector. It is a number, so an expression like $(u \cdot v) \cdot w$ has no meaning as a dot product.
- Students cancel a factor: from $u \cdot v = u \cdot w$ they conclude $v = w$. For $u = (1, 0)$, $v = (0, 1)$ and $w = (0, 2)$ both products are $0$, but $v \neq w$.
- Students regroup factors: $(u \cdot v) w$ and $u (v \cdot w)$ are in general different vectors. For $u = (1, 0)$, $v = (1, 1)$ and $w = (0, 1)$ they are $(0, 1)$ and $(1, 0)$.

## Explanations

### L1 human

The dot product takes two vectors and gives one number.
Multiply the first components, multiply the second components, and add the results.
For $(3, 4)$ and $(2, 1)$ this gives $3 \cdot 2 + 4 \cdot 1 = 10$.
The number is large and positive when the two arrows point in almost the same direction.
It is zero when the arrows make a right angle, and negative when they point in almost opposite directions.

### L2 human

Worked example: the angle at the vertex $A$ of the triangle with $A = (1, 1)$, $B = (4, 5)$ and $C = (5, -2)$.

1. The sides from $A$ are $u = B - A = (3, 4)$ and $v = C - A = (4, -3)$.
2. The dot product is $u \cdot v = 12 - 12 = 0$.
3. So the angle at $A$ is a right angle, by the [[criterion for perpendicular vectors|03NK6RSRQ1]].
4. Check by lengths: $\|u\| = 5$, $\|v\| = 5$ and $\|C - B\| = \|(1, -7)\| = \sqrt{50}$. Then $25 + 25 = 50$, as the Pythagorean theorem requires.

The typical use is to test perpendicularity, to compute angles, and to compute projections.
A trap: the dot product has no cancellation law, so $u \cdot v = u \cdot w$ only says that $u$ is perpendicular to $v - w$.

### L3 human

The dot product is the standard example of an [[inner product|0NB0AWGJBW]]: a symmetric, bilinear and positive definite form.
The sub-area on [[inner product spaces|1D4JTZ9VS3]] takes these three properties as axioms, and all of Euclidean geometry follows from them.
For a fixed $v$, the map $u \mapsto u \cdot v$ is a linear form, and each linear form on $\mathbb{R}^n$ has this shape for exactly one $v$; the sub-area on [[duality|9K7FFF26QR]] studies this.
In matrix language $u \cdot v = u^{\mathsf{T}} v$, and the entry $(i, j)$ of a matrix product $AB$ is the dot product of row $i$ of $A$ with column $j$ of $B$.
Dropping positivity leads to the [[bilinear forms|DYAK7YMK7B]] of signature $(p, q)$, such as the Minkowski form of special relativity.
