---
tag: 0Q8BZXVT1Z
kind: definition
name: Orientation of a real vector space
msc: [15A04, 15A15]
topics: [DTBK11SR77]
audience: ug2
defines: 0QJJAQ6ZYZ
uses: [0VTQTPQGAV, 0KWXYZPJKN, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Orientation_(vector_space)
    locator: Definition
---

## Definition

An orientation of a real vector space is one of the two classes into which the sign of a determinant sorts its ordered bases.

Let $V$ be a real vector space of finite dimension $n \ge 1$.
Two ordered [[bases|0VTQTPQGAV]] $B$ and $B'$ of $V$ have the *same orientation* when the [[change of basis matrix|0KWXYZPJKN]] from $B$ to $B'$ has positive [[determinant|0C3CFHDN6R]].
This is an equivalence relation on the set of ordered bases of $V$, and it has exactly two classes.
An *orientation* of $V$ is a choice of one of these two classes.
The bases in the chosen class are *positively oriented*.

## Notation

We write $[B]$ for the class of $B$ and $-[B]$ for the other class.
An *oriented* vector space is a pair $(V, o)$ of a space $V$ and an orientation $o$ of $V$.
The *standard orientation* of $\mathbb{R}^n$ is $[(e_1, \dots, e_n)]$.

## Remarks

The definition asks for three things, and each one has a reason.
The field is $\mathbb{R}$ because a determinant must have a sign; over $\mathbb{C}$ the determinant $i$ is neither positive nor negative.
The dimension is finite because a change of basis needs a square matrix with a determinant.
The bases are ordered because a reordering changes the determinant by the sign of the permutation.

The relation is an equivalence relation because change of basis matrices compose by multiplication and the determinant is multiplicative.
For three bases, $\det P_{B \to B''} = \det P_{B \to B'} \cdot \det P_{B' \to B''}$, so two positive factors give a positive product, and $P_{B' \to B} = P_{B \to B'}^{-1}$ has determinant of the same sign as $P_{B \to B'}$.
There are exactly two classes, because exchanging the first two vectors of $B$ gives a basis with determinant $-1$ relative to $B$, and every other basis has a determinant of one sign or the other.

A small example: in $\mathbb{R}^2$ the basis $((0, 1), (-1, 0))$ is the standard basis turned by $90^\circ$.
Its change of basis matrix is $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, with determinant $0 \cdot 0 - (-1) \cdot 1 = 1 > 0$, so it has the standard orientation.
The basis $((0, 1), (1, 0))$ uses the vectors of the standard basis in the other order, and its matrix has determinant $-1$, so it has the opposite orientation.

For $V = 0$ the only basis is the empty one, and by convention an orientation is a choice of a sign $+1$ or $-1$.
The concept page on [[orientation|0QJJAQ6ZYZ]] gives more examples and the geometric meaning.

## Explanations

### L1 human

An orientation fixes what counts as turning to the left in the plane, or as a right-handed set of axes in space.
A counterclockwise pair of arrows and a clockwise pair of arrows have opposite orientations.
A mirror reflection changes the orientation, and a rotation keeps it.

### L2 human

Here is a typical check: do $B = ((2, 0), (1, 1))$ and $B' = ((1, 1), (2, 0))$ have the same orientation in $\mathbb{R}^2$?
Against the standard basis, the first has determinant $2 \cdot 1 - 1 \cdot 0 = 2$ and the second has determinant $1 \cdot 0 - 2 \cdot 1 = -2$.
The determinant from $B$ to $B'$ is the quotient $-2 / 2 = -1$, which is negative, so the two bases have opposite orientations.
Watch out: $B$ and $B'$ contain the same two vectors, and only the order differs.

### L3 human

The top exterior power $\Lambda^n V$ is a real line, and $\Lambda^n V \setminus \{0\}$ has two components.
A basis $B$ gives the nonzero element $b_1 \wedge \dots \wedge b_n$, and $B'$ gives $\det P_{B \to B'}$ times it.
So two bases have the same orientation exactly when their elements lie in the same component, and an orientation is a choice of one component.
