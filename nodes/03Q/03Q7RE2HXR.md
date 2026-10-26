---
tag: 03Q7RE2HXR
kind: statement
role: theorem
name: A matrix is invertible iff its determinant is a unit
msc: [15A15]
uses: [0C3CFHDN6R, 0TWTS88TWN, 0GMPYM0NSR]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Invertible matrix theorem
---

## Statement

Let $K$ be a commutative ring and let $A$ be an $n \times n$ matrix over $K$.
Then $A$ is [[invertible|0EB9N0S33C]] if and only if its [[determinant|00KDZRW4C0]] $\det A$ is a unit of $K$.
In particular, over a field, $A$ is invertible if and only if $\det A \ne 0$.

## Remarks

If $\det A$ is a unit, then the [[adjugate|07W9H8QF38]] gives the inverse $A^{-1} = (\det A)^{-1} \operatorname{adj}(A)$.
Over $\Z$, the matrix $\begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ has determinant $2 \ne 0$, but it has no inverse with integer entries.
Over a field, this is one of many equivalent conditions for invertibility, with $\rank A = n$ and $\ker A = 0$.

## Explanations

### L1 human

A real square matrix has an inverse exactly when its determinant is not zero.
A zero determinant means that the matrix squeezes space into a lower dimension.
Such a squeeze cannot be undone.
