---
tag: W8V1S8TFWF
kind: statement
role: theorem
name: Lagrange's identity for the cross product
msc: ["15A72"]
topics: [VKVAJ94SKZ]
audience: ug1
about: [0N5N15HWZ7, 0S52TNNTH9]
uses: [0N5N15HWZ7, 0S52TNNTH9, 0XKBKGTCPC]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange%27s_identity
    locator: Lagrange's identity and vector calculus
  - url: https://en.wikipedia.org/wiki/Cross_product
    locator: Lagrange's identity
---

## Statement

The dot product and the cross product of two vectors together carry all the information in their lengths.
Let $a, b \in \mathbb{R}^3$, let $a \times b$ be the [[cross product|0N5N15HWZ7]], let $a \cdot b$ be the [[dot product|0S52TNNTH9]], and let $\|\cdot\|$ be the [[length|0XKBKGTCPC]].
Then
$$\|a \times b\|^2 = \|a\|^2 \, \|b\|^2 - (a \cdot b)^2.$$

## Remarks

### Why each hypothesis is needed

The identity holds for all $a, b \in \mathbb{R}^3$, with no further hypothesis.
The restriction to $\mathbb{R}^3$ is there only because the cross product is defined there; the right side makes sense in every $\mathbb{R}^n$.

### What it gives you

Moving $(a \cdot b)^2$ to the left gives a balance of two squares,
$$\|a \times b\|^2 + (a \cdot b)^2 = \|a\|^2 \, \|b\|^2.$$
For unit vectors this is $\sin^2 \theta + \cos^2 \theta = 1$, and that is the source of the [[length formula|SAZ353S8W0]] $\|a \times b\| = \|a\| \, \|b\| \sin \theta$.

The identity also proves the [[Cauchy-Schwarz inequality|0RFWW56Y22]] in $\mathbb{R}^3$ in one line.
The left side is a square, so it is $\geq 0$, and hence $(a \cdot b)^2 \leq \|a\|^2 \|b\|^2$.
Equality holds exactly when $a \times b = 0$, that is, when $a$ and $b$ are parallel.

### The converse

The identity fixes the length of $a \times b$, but not its direction.
The vectors $a \times b$ and $-(a \times b)$ both satisfy it, and only perpendicularity together with the right-hand rule singles out $a \times b$.

### Beyond three dimensions

In $\mathbb{R}^n$, Lagrange's identity reads
$$\Big(\sum_i a_i^2\Big)\Big(\sum_i b_i^2\Big) - \Big(\sum_i a_i b_i\Big)^2 = \sum_{i < j} (a_i b_j - a_j b_i)^2.$$
The right side is a sum of squares, so this proves the Cauchy-Schwarz inequality for $\mathbb{R}^n$ at once.
It is the squared area of the parallelogram spanned by $a$ and $b$, and it equals the Gram determinant $\det \begin{pmatrix} a \cdot a & a \cdot b \\ b \cdot a & b \cdot b \end{pmatrix}$.
The case $n = 2$ is the Brahmagupta-Fibonacci identity
$$(a_1^2 + a_2^2)(b_1^2 + b_2^2) = (a_1 b_1 + a_2 b_2)^2 + (a_1 b_2 - a_2 b_1)^2.$$

## History

The identity is named after Joseph-Louis Lagrange.
Its two-dimensional case is much older: Brahmagupta knew it in the seventh century, and Fibonacci used it in his *Liber quadratorum* of 1225.

## Explanations

### L1 human

The dot product measures how much two arrows agree in direction, and the cross product measures how much they disagree.
Lagrange's identity says that together they account for everything.
For $(1, 0, 0)$ and $(1, 1, 0)$ the dot product is $1$, the cross product is $(0, 0, 1)$ with length $1$, and the lengths are $1$ and $\sqrt{2}$.
Then $1^2 = 1 \cdot 2 - 1^2$, as the identity says.

### L2 human

Here is a check with $a = (1, 2, 3)$ and $b = (4, 5, 6)$.
The cross product is $(-3, 6, -3)$, so the left side is $9 + 36 + 9 = 54$.
For the right side, $\|a\|^2 = 14$, $\|b\|^2 = 77$ and $a \cdot b = 32$, so
$$14 \cdot 77 - 32^2 = 1078 - 1024 = 54.$$
The typical use is the area of a parallelogram from dot products alone, without computing the cross product.
Watch out: the identity is about squares, and $\|a \times b\| = \|a\| \, \|b\| - |a \cdot b|$ is false.

### L3 human

The identity says that the map $(a, b) \mapsto (a \cdot b, a \times b)$ from $\mathbb{R}^3 \times \mathbb{R}^3$ to $\mathbb{R} \times \mathbb{R}^3 = \mathbb{R}^4$ multiplies lengths.
This is the multiplicativity of the norm of quaternions: for pure quaternions $a$ and $b$, $ab = -a \cdot b + a \times b$, and $\|ab\| = \|a\| \, \|b\|$.
A bilinear product on $\mathbb{R}^n$ with perpendicularity and this identity exists only for $n = 3$ and $n = 7$, which is the content of the [[Hurwitz theorem on composition algebras|WZ81H3S4KK]] in this setting.
