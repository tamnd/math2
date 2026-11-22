---
tag: T1WN2DHS63
kind: statement
role: proposition
name: Change of basis rule for the determinant of a family of vectors
msc: [15A15, 15A75]
topics: [DTBK11SR77]
audience: ug2
uses: [0V94H674MB]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Determinant of n vectors
---

## Statement

When we change the basis that serves as the unit of volume, every determinant of a family changes by the same factor.
Let $F$ be a field, let $V$ be a vector space over $F$ of dimension $n \ge 1$, and let $B = (b_1, \dots, b_n)$ and $B' = (b'_1, \dots, b'_n)$ be two bases of $V$.
Then for all $v_1, \dots, v_n \in V$, the [[determinant in a basis|0V94H674MB]] satisfies
$$\det_B(v_1, \dots, v_n) = \det_B(B') \cdot \det_{B'}(v_1, \dots, v_n).$$
In particular, $\det_B(B') \cdot \det_{B'}(B) = 1$, and $\det_{B'} = \det_{B'}(B) \cdot \det_B$ as functions on $V^n$.

## Remarks

### A check in the plane

Let $E$ be the standard basis of $\mathbb{R}^2$ and $B = ((2, 0), (0, 1))$, so $\det_E(B) = 2 \cdot 1 - 0 \cdot 0 = 2$.
For $v_1 = (1, 2)$ and $v_2 = (3, 4)$ we have $\det_E(v_1, v_2) = 1 \cdot 4 - 3 \cdot 2 = -2$.
The rule with $E$ in the role of $B$ and $B$ in the role of $B'$ reads
$$-2 = 2 \cdot \det_B(v_1, v_2),$$
so $\det_B(v_1, v_2) = -1$.
[[The plane example|Q9N66CYVH4]] finds the same value from the coordinates in $B$.
Check of the second formula: the vectors of $E$ in $B$ have the coordinates $(\tfrac{1}{2}, 0)$ and $(0, 1)$, so $\det_B(E) = \tfrac{1}{2}$, and $\det_E(B) \det_B(E) = 2 \cdot \tfrac{1}{2} = 1$.

### Why each hypothesis is needed

Both $B$ and $B'$ must be bases, because $\det_B$ and $\det_{B'}$ are defined only with respect to a basis.
The families must have exactly $n = \dim V$ vectors, so that the coordinate matrices are square.
The field is a convenience rather than a need: the rule holds for free modules of rank $n$ over a commutative ring, with the same proof.

### What it gives you

The forms $\det_B$ for the different bases differ only by nonzero factors.
So the condition $\det_B(v_1, \dots, v_n) \ne 0$ does not depend on $B$, which is why the [[basis criterion|5D1CHPV9Z3]] makes sense without naming a basis.
Over $\mathbb{R}$ the sign of $\det_B(B')$ decides whether $B$ and $B'$ have the same [[orientation|0QJJAQ6ZYZ]].

### The converse

The factor is forced.
If $\det_B = c \cdot \det_{B'}$ for some scalar $c$, then evaluation at $B'$ gives $\det_B(B') = c \cdot \det_{B'}(B') = c$.

### Generalizations

For a linear map $T \colon V \to V$ the same idea gives $\det_B(T v_1, \dots, T v_n) = \det T \cdot \det_B(v_1, \dots, v_n)$, with the [[determinant of $T$|0X0HQYSZ0K]] as the factor.

## Explanations

### L1 human

A determinant of $n$ vectors depends on the basis that we use as the unit.
If we change the unit, every determinant changes by the same factor.
The factor is the determinant of the new basis measured in the old one, just as every length in centimeters is $100$ times the same length in meters.

### L2 human

The typical use is to move a volume computation to a convenient basis.
Suppose a basis $B'$ of $\mathbb{R}^2$ has $\det_E(B') = 3$, and some family has $\det_{B'}(v) = 4$.
Then $\det_E(v) = 3 \cdot 4 = 12$ without ever writing $v$ in standard coordinates.
Watch out: to go the other way, from $E$ to $B'$, divide by $\det_E(B')$, so a family with $\det_E(v) = 6$ has $\det_{B'}(v) = 2$.

### L3 human

The forms $\det_B$ are the nonzero elements of the line of alternating $n$-linear forms on $V$.
The rule says that two nonzero elements of a line differ by a nonzero scalar, and it names the scalar.
The [[proof|E4H8SGZWXW]] obtains it from the product rule for matrices.
