---
tag: 34VJYG6GVD
kind: concept
name: Scalar triple product
msc: ["15A72", "51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
uses: [0N5N15HWZ7, 0S52TNNTH9, 0SQV2VJTGY]
sources:
  - url: https://en.wikipedia.org/wiki/Triple_product
    locator: Scalar triple product
  - url: https://en.wikipedia.org/wiki/Cross_product
    locator: History
---

## Summary

The scalar triple product is one number that tells you how much space three vectors span, and whether they span space at all.
For $a, b, c \in \mathbb{R}^3$ it is
$$[a, b, c] = a \cdot (b \times c),$$
the [[dot product|0S52TNNTH9]] of $a$ with the [[cross product|0N5N15HWZ7]] $b \times c$.
Its absolute value is the volume of the [[parallelepiped|0SQV2VJTGY]] with edges $a$, $b$ and $c$, and it is $0$ exactly when the three vectors lie in one plane through $0$, by the [[volume and coplanarity test|7RMCRQ9ERC]].
In coordinates it is the $3 \times 3$ determinant with rows $a$, $b$ and $c$, by the [[determinant formula|059Q2XWJDC]].
That makes it the first place where determinants appear as volumes, a theme that runs through the rest of linear algebra.

## Motivation

Three edges $a$, $b$, $c$ from one corner span a slanted box, a parallelepiped, and we want its volume.
As for any prism, the volume is the area of the base times the height.

Take the base to be the parallelogram on $b$ and $c$.
Its area is $\|b \times c\|$, and the vector $b \times c$ stands perpendicular to it.
The height is the part of $a$ along that perpendicular, which is $|a \cdot (b \times c)| / \|b \times c\|$.
Multiplying area by height, the factor $\|b \times c\|$ cancels and leaves $|a \cdot (b \times c)|$.

A box of volume $0$ is flat, so the same number also tests whether three vectors lie in a plane.

## Notation

Books write $a \cdot (b \times c)$, $[a, b, c]$, $[a\,b\,c]$ or $(a, b, c)$, and some call it the box product or the mixed product.
The parentheses in $a \cdot (b \times c)$ are often dropped, because $a \cdot b \times c$ can only mean $a \cdot (b \times c)$; the other reading $(a \cdot b) \times c$ is undefined.
In coordinates,
$$[a, b, c] = \det \begin{pmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{pmatrix}.$$

## Remarks

### A first computation

The unit vectors give the unit cube: $[\mathbf{i}, \mathbf{j}, \mathbf{k}] = \mathbf{i} \cdot (\mathbf{j} \times \mathbf{k}) = \mathbf{i} \cdot \mathbf{i} = 1$.
A cuboid with edges $(2, 0, 0)$, $(0, 3, 0)$ and $(0, 0, 4)$ gives $[a, b, c] = 24 = 2 \cdot 3 \cdot 4$, as it should.

For a slanted box take $a = (1, 2, 3)$, $b = (0, 1, 4)$ and $c = (5, 6, 0)$.
Then
$$b \times c = (-24, 20, -5), \qquad [a, b, c] = -24 + 40 - 15 = 1.$$
The edges are long, yet the box holds exactly one unit of volume, as the [[worked example|HCYSHZ50K8]] explains.

### Flat boxes

For $a = (1, 2, 3)$, $b = (4, 5, 6)$ and $c = (7, 8, 9)$ the triple product is $0$, because $c = 2b - a$ lies in the plane of $a$ and $b$.
The [[coplanar example|3VX46SFKZB]] finds this dependence.
The simplest flat case is a repeated vector: $[a, a, c] = 0$ for all $a$ and $c$, since $a \times c$ is perpendicular to $a$.

### The rules you can use

Cyclic shifts do not change the value: $[a, b, c] = [b, c, a] = [c, a, b]$.
A swap of two vectors changes the sign, for example $[b, a, c] = -[a, b, c]$.
Together with the symmetry of the dot product, this lets you exchange dot and cross: $a \cdot (b \times c) = (a \times b) \cdot c$.
The product is linear in each slot, so $[a + a', b, c] = [a, b, c] + [a', b, c]$ and $[ta, b, c] = t[a, b, c]$.
A tetrahedron with the same three edges is one sixth of the box, so its volume is $\tfrac{1}{6} |[a, b, c]|$.

### What the sign means

The sign records orientation.
The value $[a, b, c]$ is positive exactly when $(a, b, c)$ is a right-handed triple, with the same [[orientation|0QJJAQ6ZYZ]] as $(\mathbf{i}, \mathbf{j}, \mathbf{k})$.
Swapping two edges reverses the orientation and the sign, but leaves the volume alone.

### Watch out

The product of the edge lengths, $\|a\| \, \|b\| \, \|c\|$, is not the volume unless the edges are perpendicular.
The [[non-example|31NZ20EWKC]] gets $\sqrt{2}$ that way for a box of volume $1$.

A zero triple product does not mean that two of the vectors are parallel.
The vectors $(1, 0, 0)$, $(0, 1, 0)$ and $(1, 1, 0)$ give $0$ and contain no parallel pair; they only lie in one plane.
Keep the sign until the end, and keep the factor $\tfrac{1}{6}$ for a tetrahedron, not $\tfrac{1}{3}$ or $\tfrac{1}{2}$.
Finally, $(a \cdot b)\, c$ and $a \times (b \times c)$ are vectors, not triple products; the second is the [[vector triple product|03FTB26QYD]].

### History

In 1773 Lagrange used the dot and cross products in coordinates to study the tetrahedron.
The vector form $a \cdot (b \times c)$ and its name come from the vector analysis of Gibbs and Heaviside in the 1880s.

### Try it

Find the volume of the tetrahedron with vertices $0$, $(1, 0, 0)$, $(0, 2, 0)$ and $(0, 0, 3)$.
The triple product of the three edges is $1 \cdot 2 \cdot 3 = 6$, so the volume is $\tfrac{6}{6} = 1$.

Do $(1, 1, 0)$, $(0, 1, 1)$ and $(1, 0, -1)$ lie in one plane through $0$?
The cross product of the last two is $(-1, 1, -1)$, and its dot product with $(1, 1, 0)$ is $0$, so they do.

## Explanations

### L1 human

Three arrows from one corner make a slanted box.
The scalar triple product is a single number whose size is the volume of this box.
For the three unit arrows along the axes, the box is a cube with volume $1$.
If the three arrows lie flat in one plane, the box is flat, and the number is $0$.

### L2 human

Here is a typical problem: find the volume of the tetrahedron with vertices $P = (0, 0, 0)$, $A = (1, 2, 3)$, $B = (0, 1, 4)$ and $C = (5, 6, 0)$.
The edges from $P$ are $a = (1, 2, 3)$, $b = (0, 1, 4)$ and $c = (5, 6, 0)$.
The cross product of the last two is
$$b \times c = (1 \cdot 0 - 4 \cdot 6, \; 4 \cdot 5 - 0 \cdot 0, \; 0 \cdot 6 - 1 \cdot 5) = (-24, 20, -5),$$
so $[a, b, c] = -24 + 40 - 15 = 1$.
The box has volume $1$, and the tetrahedron has volume $\tfrac{1}{6}$.
The same computation tests whether four points lie in one plane and finds the orientation of three vectors.
Watch out: for four points that do not include the origin, use the three edges from one vertex, such as $A - P$, $B - P$ and $C - P$.

### L3 human

The map $(a, b, c) \mapsto [a, b, c]$ is the unique alternating trilinear form on $\mathbb{R}^3$ with $[\mathbf{i}, \mathbf{j}, \mathbf{k}] = 1$, so it is the determinant.
The sub-area on [[determinants|DTBK11SR77]] proves that $|\det A|$ is the volume of the image of the unit cube, the [[signed volume|04X3PR72VJ]] view in every dimension.
In the [[exterior algebra|0MDMZ965VE]], $a \wedge b \wedge c = [a, b, c] \, e_1 \wedge e_2 \wedge e_3$.
The relation can also be read backward: $b \times c$ is the only vector $w$ with $a \cdot w = [a, b, c]$ for all $a$.
