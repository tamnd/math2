---
tag: 0Q8BZXVT1Z
kind: definition
name: Orientation of a real vector space
msc: [15A04, 15A15]
defines: 0QJJAQ6ZYZ
uses: [0VTQTPQGAV, 0KWXYZPJKN, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Orientation_(vector_space)
    locator: Definition
---

## Definition

Let $V$ be a real vector space of finite dimension $n \ge 1$.
Two ordered [[bases|0KCQ9Y3QKA]] $B$ and $B'$ of $V$ have the *same orientation* when the [[change of basis matrix|0MKRHZB3WS]] from $B$ to $B'$ has positive [[determinant|00KDZRW4C0]].
This is an equivalence relation with exactly two classes.
An *orientation* of $V$ is a choice of one of these two classes.

## Remarks

A vector space with a chosen orientation is *oriented*, and the bases in the chosen class are *positively oriented*.
The standard orientation of $\R^n$ is the class of the standard basis.
In $\R^2$, exchanging the two basis vectors reverses the orientation.
An invertible linear map keeps the orientation if and only if its determinant is positive.

## Explanations

### L1 human

An orientation fixes what counts as turning to the left, or as a right-handed system.
In the plane, a counterclockwise pair of basis vectors and a clockwise pair have opposite orientations.
A mirror reflection changes the orientation, and a rotation keeps it.
