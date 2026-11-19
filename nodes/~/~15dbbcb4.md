---
tag: ~15dbbcb4
kind: statement
role: theorem
name: Volume and coplanarity by the scalar triple product
msc: ["15A72", "51N20"]
topics: [VKVAJ94SKZ]
audience: school
about: [~d7839aac]
uses: [~d7839aac, 0N5N15HWZ7, 0S52TNNTH9, 0SQV2VJTGY, 0CRMGPAH83, 4TWY53TBKK]
sources:
  - url: https://en.wikipedia.org/wiki/Triple_product
    locator: Scalar triple product
  - url: https://en.wikipedia.org/wiki/Coplanarity
    locator: lead section
---

## Statement

Let $a, b, c \in \mathbb{R}^3$, and let $[a, b, c] = a \cdot (b \times c)$ be their [[scalar triple product|~d7839aac]].

1. $|[a, b, c]|$ is the volume of the [[parallelepiped|0SQV2VJTGY]] with the edges $a$, $b$ and $c$ drawn from one point.
2. $[a, b, c] = 0$ if and only if $a$, $b$ and $c$ are [[linearly dependent|0CRMGPAH83]].

Three vectors in $\mathbb{R}^3$ are linearly dependent exactly when they lie in one plane through $0$, that is, when they are [[coplanar|4TWY53TBKK]].
So part 2 says: $[a, b, c] = 0$ if and only if $a$, $b$ and $c$ are coplanar.

## Remarks

### Why each hypothesis is needed

Part 1 uses the volume of solid geometry: area of the base times the height.
For a degenerate box, with $b$ parallel to $c$, the base has the area $0$ and both sides of part 1 are $0$.
Part 2 is about vectors from $0$.
For four points $P$, $A$, $B$, $C$, apply it to $A - P$, $B - P$ and $C - P$.

### Consequences

- Four points $P$, $A$, $B$, $C$ lie in one plane if and only if $[A - P, B - P, C - P] = 0$.
- The tetrahedron $PABC$ has the volume $\tfrac{1}{6} |[A - P, B - P, C - P]|$.
- Three vectors $a$, $b$, $c$ with $[a, b, c] \neq 0$ form a basis of $\mathbb{R}^3$.
- Two lines $p + t u$ and $q + s v$ with $u \times v \neq 0$ meet if and only if $[q - p, u, v] = 0$.

### Converse

Part 2 is an equivalence.
The converse of part 1 fails: equal volumes do not give equal boxes.
The boxes on $(2, 0, 0)$, $(0, 1, 0)$, $(0, 0, 1)$ and on $(1, 0, 0)$, $(0, 2, 0)$, $(0, 0, 1)$ both have volume $2$.

### Generalizations

For $n$ vectors in $\mathbb{R}^n$, $|\det(a_1, \ldots, a_n)|$ is the volume of the parallelotope, and $\det = 0$ exactly when the vectors are dependent.
The sub-area on [[determinants|DTBK11SR77]] proves this, and the [[signed volume|04X3PR72VJ]] node states it.

## Explanations

### L1 human

Three arrows from one corner make a slanted box.
The size of the scalar triple product is the volume of this box.
The box is flat exactly when the three arrows lie in one plane, and then the product is $0$.

### L2 human

To test whether $P = (0, 0, 0)$, $A = (1, 2, 3)$, $B = (4, 5, 6)$ and $C = (7, 8, 9)$ lie in one plane:

1. $B \times C = (5 \cdot 9 - 6 \cdot 8, \; 6 \cdot 7 - 4 \cdot 9, \; 4 \cdot 8 - 5 \cdot 7) = (-3, 6, -3)$.
2. $[A, B, C] = -3 + 12 - 9 = 0$.
3. So the four points lie in one plane. Indeed $C = 2B - A$.

A trap: $[a, b, c] = 0$ does not mean that two vectors are parallel.
It means only that one vector is a combination of the other two.

### L3 human

The proof of part 2 uses that three independent vectors in $\mathbb{R}^3$ form a basis.
The [[determinant formula|059Q2XWJDC]] gives a second proof: a $3 \times 3$ determinant is $0$ if and only if its rows are dependent.
