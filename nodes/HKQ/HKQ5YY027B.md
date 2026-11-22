---
tag: HKQ5YY027B
kind: concept
name: Cayley transform of matrices
aliases: [cayley-transform-of-matrices, matrix-cayley-transform, cayley-parametrization-of-rotations]
msc: ["15B10", "15A16"]
topics: [AZS5BPF5H3]
audience: grad
uses: [03RNVFDEAN, 0QRBVFJ50X, 0EB9N0S33C, 6WBVP2PB1Y]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley_transform
    locator: Matrix map
  - url: https://en.wikipedia.org/wiki/Cayley_transform
    locator: Other matrix forms
---

## Summary

The Cayley transform turns a skew-symmetric matrix, which is easy to write down, into a rotation, which is not.
It uses only sums, products and one inverse, so rational input gives rational rotations, and the same formula takes the rotation back.
Let $A$ be a real $n \times n$ [[skew-symmetric matrix|03RNVFDEAN]], so $A^{\mathsf{T}} = -A$.
The *Cayley transform* of $A$ is
$$C(A) = (I - A)(I + A)^{-1}.$$
The matrix $I + A$ is always [[invertible|0EB9N0S33C]], and $C(A)$ is an [[orthogonal matrix|0QRBVFJ50X]] with determinant $1$.
By [[the Cayley transform theorem|R9Z3W1CFPP]], $C$ is a bijection from the skew-symmetric matrices onto the elements of [[SO(n)|6WBVP2PB1Y]] that do not have the eigenvalue $-1$, and its inverse is given by the same formula, $A = (I - Q)(I + Q)^{-1}$.

## Motivation

The condition $Q^{\mathsf{T}}Q = I$ is a system of quadratic equations in the $n^2$ entries of $Q$, and it is hard to solve by hand.
The condition $A^{\mathsf{T}} = -A$ is linear: the $\frac{n(n - 1)}{2}$ entries above the diagonal are free, and they fix the rest.
The Cayley transform turns the easy condition into the hard one.
So it gives most rotations by $\frac{n(n - 1)}{2}$ free real numbers, with rational formulas in both directions.

For $n = 2$ this is the rational parametrization of the unit circle, the one that produces all [[Pythagorean triples|0M7ARED5Q7]].
In numerical work, the transform is used to build orthogonal matrices and to take steps on $SO(n)$ that stay exactly orthogonal, because no square roots or trigonometric functions are needed.
In Lie theory the skew-symmetric matrices are the Lie algebra of $SO(n)$, and the Cayley transform is a rational chart of the group near $I$.

## Notation

Some books use $(I + A)(I - A)^{-1}$ instead, which is $C(-A)$, so the two conventions give the same set of matrices with the sign of $A$ reversed.
The two factors commute, so $C(A) = (I + A)^{-1}(I - A)$ as well.
For a single number the same formula is $z \mapsto \frac{1 - z}{1 + z}$, and the [[Cayley transform of the upper half plane|0X45ZM731G]] in complex analysis is a related map.

## Remarks

### The plane: rational points of the circle

Take $A = \begin{pmatrix} 0 & -t \\ t & 0 \end{pmatrix}$ with $t \in \R$.
Then $I + A = \begin{pmatrix} 1 & -t \\ t & 1 \end{pmatrix}$ has determinant $1 + t^2 > 0$, and $I - A = \begin{pmatrix} 1 & t \\ -t & 1 \end{pmatrix}$ is $1 + t^2$ times $(I + A)^{-1}$.
So
$$C(A) = \frac{1}{1 + t^2}\begin{pmatrix} 1 & t \\ -t & 1 \end{pmatrix}^2 = \frac{1}{1 + t^2}\begin{pmatrix} 1 - t^2 & 2t \\ -2t & 1 - t^2 \end{pmatrix}.$$
With $t = \tan\frac{\theta}{2}$ this is the rotation $R(-\theta)$, by the half-angle formulas.
[[The case t = 1/2|QFJZBPVV00]] gives $\frac{1}{5}\begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix}$, built from the triple $3, 4, 5$.
Check: $9 + 16 = 25$, so each column has length $1$.

### A rotation of space

In $\R^3$, [[the transform of a 3 by 3 skew-symmetric matrix|TEZ3YS5VTB]] takes
$$A = \frac{1}{3}\begin{pmatrix} 0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0 \end{pmatrix} \quad \text{to} \quad C(A) = \frac{1}{3}\begin{pmatrix} 2 & -1 & 2 \\ 2 & 2 & -1 \\ -1 & 2 & 2 \end{pmatrix}.$$
The result is the rotation by $\frac{\pi}{3}$ about the line through $(1, 1, 1)$.
In general, if $A = -[w]_\times$ where $[w]_\times x = w \times x$, then $C(A)$ is the rotation about $w$ by the angle $\theta$ with $\tan\frac{\theta}{2} = \norm{w}$; here $w = \frac{1}{3}(1, 1, 1)$ and $\norm{w} = \frac{1}{\sqrt{3}}$.

### What it misses

The [[half turn -I_2|KFMTND2HXZ]] is in $SO(2)$ but is not $C(A)$ for any skew-symmetric $A$.
Its eigenvalue $-1$ makes $I + Q = 0$, so the inverse formula fails, and the entry $\frac{1 - t^2}{1 + t^2}$ is never $-1$.
A reflection such as $\operatorname{diag}(1, -1)$ is not $C(A)$ either, because every $C(A)$ has determinant $1$.
And the skew symmetry of $A$ matters: for $A = \operatorname{diag}(1, 0)$ the matrix $I + A$ is invertible, but $C(A) = \operatorname{diag}(0, 1)$ is singular, so not orthogonal.

### The rules you can use

The matrix $I + A$ is invertible because $(I + A)x = 0$ with $x$ real gives $x^{\mathsf{T}}x = -x^{\mathsf{T}}Ax = 0$, and $x^{\mathsf{T}}Ax = 0$ for every skew-symmetric $A$.
The transform is its own inverse, $C(C(M)) = M$, whenever $I + M$ is invertible.
It respects transposes and orthogonal changes of basis: $C(A^{\mathsf{T}}) = C(-A) = C(A)^{\mathsf{T}}$, and $C(PAP^{\mathsf{T}}) = PC(A)P^{\mathsf{T}}$ for every orthogonal $P$.
Near $A = 0$ it is close to $I - 2A$, so small skew-symmetric matrices give rotations close to the identity.

### Watch out

The image of $C$ is not all of $SO(n)$: it misses every rotation with the eigenvalue $-1$, such as the half turns.
The Cayley transform is also not the exponential map: $C(A)$ and $\exp(-2A)$ agree only up to second order near $0$.
For $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, $C(A) = R(-\frac{\pi}{2})$, while $\exp(-2A) = R(-2)$, a rotation by $-2$ radians.
Finally, keep track of the convention: the other sign gives $(I + A)(I - A)^{-1} = C(-A) = C(A)^{\mathsf{T}}$, the inverse rotation.

### History

Cayley introduced the transform in 1846.

### Try it

First, compute $C(A)$ for $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
With $t = 1$ the formula gives $\frac{1}{2}\begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, the quarter turn $R(-\frac{\pi}{2})$.

Second, which $t$ gives the rotation $\frac{1}{13}\begin{pmatrix} 5 & 12 \\ -12 & 5 \end{pmatrix}$?
We need $\frac{2t}{1 + t^2} = \frac{12}{13}$ and $\frac{1 - t^2}{1 + t^2} = \frac{5}{13}$; the second gives $t^2 = \frac{4}{9}$, and the first then forces $t = \frac{2}{3}$.

## Explanations

### L1 human

Rotations are hard to write down, because their numbers must satisfy many equations with squares at once.
A skew-symmetric table of numbers is easy to write down: choose the numbers above the diagonal freely, and put their negatives below it.
The Cayley transform is a recipe that turns each such table into a rotation.
For example, the single number $\frac{1}{2}$ turns into the rotation with entries $\frac{3}{5}$ and $\frac{4}{5}$.
The recipe also works backward, for almost every rotation.
Only the rotations that turn some direction completely around are missed.

### L2 human

Here is a typical use: find a rotation of $\R^3$ with rational entries about the $z$-axis.
Take $A = -[w]_\times$ with $w = (0, 0, \frac{1}{2})$, so $A = \begin{pmatrix} 0 & \frac{1}{2} & 0 \\ -\frac{1}{2} & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$.
The last coordinate is not touched, and on the first two coordinates $A$ is the $2 \times 2$ matrix with $t = -\frac{1}{2}$, so
$$C(A) = \begin{pmatrix} \frac{3}{5} & -\frac{4}{5} & 0 \\ \frac{4}{5} & \frac{3}{5} & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
Check: the first two columns have length $\sqrt{\frac{9}{25} + \frac{16}{25}} = 1$ and dot product $-\frac{12}{25} + \frac{12}{25} = 0$, and the determinant is $\frac{9}{25} + \frac{16}{25} = 1$.
The angle $\theta$ has $\cos\theta = \frac{3}{5}$ and $\tan\frac{\theta}{2} = \frac{1}{2} = \norm{w}$, as the general rule predicts.
This is how the transform is used: choose a few rational numbers and get an exact rotation, with no square roots at all.

### L3 human

The skew-symmetric matrices form the Lie algebra $\mathfrak{so}(n)$ of $SO(n)$.
The Cayley transform is a rational map from $\mathfrak{so}(n)$ onto a dense open subset of $SO(n)$, and its derivative at $0$ is $-2$ times the identity.
So it is a chart of $SO(n)$ near $I$, and it shows that $SO(n)$ is a rational variety.
The same formula sends skew-Hermitian matrices to unitary matrices without the eigenvalue $-1$, and the matrices $A$ with $A^{\mathsf{T}}J = -JA$ to the matrices $Q$ with $Q^{\mathsf{T}}JQ = J$ for an invertible symmetric $J$, whenever $I + A$ is invertible.
The Lie theory of this chart belongs to the area of Lie groups.
