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

Let $V$ be a real vector space of finite dimension $n \ge 1$.
Two ordered [[bases|0VTQTPQGAV]] $B$ and $B'$ of $V$ have the *same orientation* when the [[change of basis matrix|0KWXYZPJKN]] from $B$ to $B'$ has positive [[determinant|0C3CFHDN6R]].
This is an equivalence relation with exactly two classes.
An *orientation* of $V$ is a choice of one of these two classes.

## Notation

- $[B]$ is the class of $B$, and $-[B]$ is the other class.
- An *oriented* vector space is a pair $(V, o)$ of a space $V$ and an orientation $o$.

## Remarks

The relation is an equivalence relation because change of basis matrices multiply and the determinant is multiplicative.
There are exactly two classes: exchanging the first two vectors of $B$ gives a basis of the other class.
The bases in the chosen class are *positively oriented*.
The standard orientation of $\mathbb{R}^n$ is the class of the standard basis.
An invertible linear map keeps the orientation if and only if its determinant is positive.
For $V = 0$, an orientation is by convention a choice of a sign $+1$ or $-1$.

## Explanations

### L1 human

An orientation fixes what counts as turning to the left, or as a right-handed system.
In the plane, a counterclockwise pair of basis vectors and a clockwise pair have opposite orientations.
A mirror reflection changes the orientation, and a rotation keeps it.

### L2 human

In $\mathbb{R}^2$, the basis $((0, 1), (-1, 0))$ is the standard basis rotated by $90^\circ$.

1. Its change of basis matrix from $(e_1, e_2)$ is $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, with determinant $1 > 0$.
2. So it has the standard orientation, as a rotation must.

The typical use is to say which bases count as positive before computing signed areas or volumes.
A trap: the basis $((0, 1), (1, 0))$ has determinant $-1$, so it has the opposite orientation, although it has the same vectors as the standard basis.

### L3 human

An orientation is equivalently a component of $\Lambda^n V \setminus \{0\}$, since $\Lambda^n V$ is a real line.
The basis $B$ gives the element $b_1 \wedge \dots \wedge b_n$, and $B, B'$ have the same orientation when these elements lie in the same component.
