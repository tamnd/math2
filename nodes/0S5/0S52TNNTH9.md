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

The dot product takes two [[vectors|0QN3D80AWP]] and returns one number.
That number tells you how much the two vectors point the same way, and it is the tool that turns lengths and angles into arithmetic.
For $u = (u_1, \dots, u_n)$ and $v = (v_1, \dots, v_n)$ in $\mathbb{R}^n$, you multiply matching entries and add the results:
$$u \cdot v = u_1 v_1 + u_2 v_2 + \dots + u_n v_n.$$
This is the coordinate definition, and the [[formal definition|05HQYM0R4G]] states it.
In the plane and in space the same number also equals $\|u\| \, \|v\| \cos \theta$, where $\|u\|$ is the [[length|0XKBKGTCPC]] of $u$ and $\theta$ is the [[angle between the vectors|0ZEHZY85E6]].

## Motivation

Geometry keeps asking two kinds of question: how long is this, and what is this angle.
Coordinates answer the first kind well, because the Pythagorean theorem gives a length from the entries of a vector.
Angles are harder, since they seem to need trigonometry and a picture.
The dot product removes that difficulty.
It is one multiply-and-add over the entries, and the result already contains the cosine of the angle.

The same number turns up whenever a quantity is a weighted total.
A shopping bill is the dot product of the list of quantities with the list of prices.
In physics, the [[work that a constant force does|2ZK5YBNB59]] along a displacement $d$ is $F \cdot d$, because only the part of the force $F$ along the motion counts.
Later in linear algebra, every entry of a matrix product is a dot product of a row with a column.

## Notation

Most books write $u \cdot v$.
You will also see $\langle u, v \rangle$, $(u, v)$ and $\langle u \mid v \rangle$, and the names *scalar product* and *standard inner product*.
When $u$ and $v$ are columns, $u \cdot v = u^{\mathsf{T}} v$, a $1 \times 1$ matrix that we read as a number.
Some books also use a dot for the product $c \cdot v$ of a scalar and a vector, so read the types of the two factors before you compute.

## Remarks

### A first computation

Take $u = (3, 4)$ and $v = (4, 3)$.
Multiply the first entries, multiply the second entries, and add:
$$u \cdot v = 3 \cdot 4 + 4 \cdot 3 = 24.$$
Now take the dot product of $u$ with itself:
$$u \cdot u = 3^2 + 4^2 = 25.$$
That is the square of the length of $u$, so $\|u\| = 5$.
This is no accident: for every vector, $v \cdot v = v_1^2 + \dots + v_n^2 = \|v\|^2$, which is the Pythagorean theorem written with a dot.

### What the number means

Both vectors above have length 5, so the angle formula gives
$$\cos \theta = \frac{u \cdot v}{\|u\| \, \|v\|} = \frac{24}{25} = 0.96,$$
and $\theta$ is about $16.3$ degrees.
The two arrows point almost the same way, and the dot product is close to its largest possible value $\|u\| \, \|v\| = 25$.

The sign of the dot product is often all you need.
When $u \cdot v > 0$, the angle is less than a right angle and the vectors agree.
When $u \cdot v = 0$, the vectors are [[perpendicular|03NK6RSRQ1]].
When $u \cdot v < 0$, the angle is more than a right angle and the vectors disagree.
For example, $(1, 2) \cdot (-2, 1) = -2 + 2 = 0$, so these two vectors meet at a right angle.

Why do the two definitions give the same number?
Put $u$ and $v$ at the same starting point, so that the third side of the triangle is $v - u$.
The law of cosines gives $\|v - u\|^2 = \|u\|^2 + \|v\|^2 - 2 \|u\| \, \|v\| \cos \theta$.
If you expand $\|v - u\|^2 = (v - u) \cdot (v - u)$ with the rules below, you get $\|u\|^2 + \|v\|^2 - 2\, u \cdot v$.
The two right sides must agree, so $u \cdot v = \|u\| \, \|v\| \cos \theta$.
The [[geometric formula for the dot product|070TXS9AXM]] writes this out in full, and [[the case of (3, 0) and (2, 2)|9C7YQTW1ZM]] checks it with numbers.

### The rules you can use

The dot product behaves like ordinary multiplication in most ways, and each rule follows from the same rule for real numbers, entry by entry.
It is symmetric, $u \cdot v = v \cdot u$, because $u_i v_i = v_i u_i$.
It is linear in each factor, $(a u + b w) \cdot v = a (u \cdot v) + b (w \cdot v)$, because multiplication distributes over addition.
It is positive, $v \cdot v \ge 0$, and $v \cdot v = 0$ only for $v = 0$, because a sum of squares is zero only when each square is zero.
Together these give the expansion $\|u + v\|^2 = \|u\|^2 + 2\, u \cdot v + \|v\|^2$, which is the dot-product form of the law of cosines.
The size of the dot product is bounded by the [[Cauchy-Schwarz inequality|0RFWW56Y22]], $|u \cdot v| \le \|u\| \, \|v\|$, and that is why the cosine above is always between $-1$ and $1$.

### What it is not

Multiplying matching entries without adding them, $(1, 2, 3) \ast (4, 5, 6) = (4, 10, 18)$, gives a vector.
The dot product is the sum of those entries, $32$, and that sum is what carries the angle.
The product of the lengths, $\|u\| \, \|v\|$, is not the dot product either, because it stays the same when $v$ turns and the dot product changes.
The form $u_1 v_1 - u_2 v_2$ on $\mathbb{R}^2$ obeys symmetry and linearity but fails positivity, since it gives $0$ for $(1, 1)$; [[the Minkowski form|TFGECQ5C32]] studies it.

### Watch out

Three habits from ordinary multiplication fail here.
The dot product is a number, not a vector, so $(u \cdot v) \cdot w$ has no meaning as a dot product.
You cannot cancel: with $u = (1, 0)$, $v = (0, 1)$ and $w = (0, 2)$, both $u \cdot v$ and $u \cdot w$ are $0$, but $v \ne w$.
All that $u \cdot v = u \cdot w$ tells you is that $u$ is perpendicular to $v - w$.
You cannot regroup either: with $u = (1, 0)$, $v = (1, 1)$ and $w = (0, 1)$, the vector $(u \cdot v) w$ is $(0, 1)$ but $u (v \cdot w)$ is $(1, 0)$.

### History

Hamilton met the dot product inside his product of quaternions in the 1840s.
For two pure quaternions, the real part of the product is minus the dot product, and the vector part is the cross product.
Gibbs, in his lectures on vector analysis in the 1880s, made the dot product an operation of its own and gave it the notation $u \cdot v$.

### Try it

First, compute $(2, -1, 3) \cdot (1, 4, 2)$ and say whether the angle between the vectors is acute, right or obtuse.
The answer is $2 - 4 + 6 = 4$, which is positive, so the angle is acute.

Second, find a number $t$ that makes $(1, t)$ perpendicular to $(3, 6)$.
You need $3 + 6t = 0$, so $t = -\tfrac{1}{2}$.

## Explanations

### L1 human

Think of each vector as an arrow.
The dot product asks how much the two arrows agree about direction.
To compute it, multiply the first numbers, multiply the second numbers, and add.
For $(3, 4)$ and $(2, 1)$ this gives $3 \cdot 2 + 4 \cdot 1 = 10$.
A large positive answer means the arrows point nearly the same way.
Zero means they make a right angle, and a negative answer means they point nearly opposite ways.

### L2 human

Here is a typical use: is the triangle with corners $A = (1, 1)$, $B = (4, 5)$ and $C = (5, -2)$ right-angled at $A$?
The two sides that leave $A$ are $u = B - A = (3, 4)$ and $v = C - A = (4, -3)$.
Their dot product is $u \cdot v = 12 - 12 = 0$, so the angle at $A$ is a right angle by the [[criterion for perpendicular vectors|03NK6RSRQ1]].
You can check this a second way with lengths.
The sides have $\|u\| = 5$ and $\|v\| = 5$, and the third side is $C - B = (1, -7)$ with $\|C - B\| = \sqrt{50}$.
Since $25 + 25 = 50$, the Pythagorean theorem agrees.
Notice that the dot product needed one line of arithmetic and no square roots.
This is why it is the standard way to test for right angles, to find angles and to compute projections.

### L3 human

The dot product is the standard example of an [[inner product|0NB0AWGJBW]]: a form that is symmetric, bilinear and positive definite.
The sub-area on [[inner product spaces|1D4JTZ9VS3]] takes these three properties as axioms, and Euclidean geometry follows from them alone.
Fixing $v$ gives a linear form $u \mapsto u \cdot v$, and every linear form on $\mathbb{R}^n$ arises this way from exactly one $v$; the sub-area on [[duality|9K7FFF26QR]] builds on this.
In matrix language $u \cdot v = u^{\mathsf{T}} v$, and the entry $(i, j)$ of a product $AB$ is the dot product of row $i$ of $A$ with column $j$ of $B$.
If you drop positivity you reach the [[bilinear forms|DYAK7YMK7B]] of signature $(p, q)$, such as the Minkowski form of special relativity.
