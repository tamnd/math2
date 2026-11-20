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

Let $A$ be a real $n \times n$ [[skew-symmetric matrix|03RNVFDEAN]], so $A^T = -A$.
The *Cayley transform* of $A$ is the matrix
$$C(A) = (I - A)(I + A)^{-1}.$$
The matrix $I + A$ is [[invertible|0EB9N0S33C]], and $C(A)$ is an [[orthogonal matrix|0QRBVFJ50X]] with determinant $1$.
By [[the Cayley transform theorem|R9Z3W1CFPP]], $C$ is a bijection from the skew-symmetric matrices onto the matrices of [[$SO(n)$|6WBVP2PB1Y]] without the eigenvalue $-1$.
Its inverse is given by the same formula, $A = (I - Q)(I + Q)^{-1}$.
So the Cayley transform describes most rotations by $\frac{n(n - 1)}{2}$ free real numbers, with rational formulas in both directions.

## Motivation

The condition $Q^TQ = I$ is a system of quadratic equations in the entries of $Q$.
The condition $A^T = -A$ is linear: the entries above the diagonal are free, and they determine the rest.
So it is easy to write down skew-symmetric matrices, and harder to write down orthogonal ones.
The Cayley transform turns each skew-symmetric matrix into an orthogonal one with only additions, multiplications and one inverse.
For $n = 2$, it is the rational parametrization of the unit circle, which produces the Pythagorean triples.

## Notation

- Some books use $(I + A)(I - A)^{-1}$ instead. This is $C(-A)$, so it gives the same set of matrices.
- The factors commute, so $C(A) = (I + A)^{-1}(I - A)$ as well.
- The same formula with a complex number $z$ is $\frac{1 - z}{1 + z}$. The [[Cayley transform of the upper half plane|0X45ZM731G]] is a related map of complex numbers.

## Remarks

### Examples

- $C(0) = I_n$.
- For $n = 2$ and $A = \begin{pmatrix} 0 & -t \\ t & 0 \end{pmatrix}$, $C(A) = \frac{1}{1 + t^2}\begin{pmatrix} 1 - t^2 & 2t \\ -2t & 1 - t^2 \end{pmatrix}$. This is the rotation $R(-\theta)$ with $t = \tan\frac{\theta}{2}$.
- [[With $t = \frac{1}{2}$|QFJZBPVV00]], $C(A) = \frac{1}{5}\begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix}$. Its entries come from the Pythagorean triple $3, 4, 5$.
- [[A $3 \times 3$ example|TEZ3YS5VTB]]: $A = \frac{1}{3}\begin{pmatrix} 0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0 \end{pmatrix}$ gives the rotation by $\frac{\pi}{3}$ about the line through $(1, 1, 1)$.

### Non-examples

- [[The half turn $-I_2$|KFMTND2HXZ]] is in $SO(2)$, but it is not $C(A)$ for any skew-symmetric $A$. Its eigenvalue $-1$ makes $I + Q$ singular.
- A reflection, such as $\operatorname{diag}(1, -1)$, is not $C(A)$, because $\det C(A) = 1$.
- For a matrix $A$ that is not skew-symmetric, $C(A)$ is in general not orthogonal. For $A = \operatorname{diag}(1, 0)$, $C(A) = \operatorname{diag}(0, 1)$, which is singular.

### Basic properties

- $I + A$ is invertible: if $(I + A)x = 0$ with $x$ real, then $x^Tx = -x^TAx = 0$, because $x^TAx = 0$ for a skew-symmetric $A$.
- $C(A)$ is orthogonal, $\det C(A) = 1$, and $C(A)$ does not have the eigenvalue $-1$.
- $C(C(M)) = M$ for each matrix $M$ with $I + M$ invertible. So $C$ is its own inverse.
- The entries of $C(A)$ are rational functions of the entries of $A$. So a skew-symmetric matrix with rational entries gives an orthogonal matrix with rational entries.
- $C(A^T) = C(A)^T = C(A)^{-1}$, and $C(PAP^T) = PC(A)P^T$ for each orthogonal $P$.

### History

Cayley introduced the transform in 1846.

### Common errors

- The image of $C$ is not all of $SO(n)$. It misses each rotation with the eigenvalue $-1$, for example the half turns.
- $C(A)$ is not $\exp(-2A)$ or $\exp(A)$. Both maps send skew-symmetric matrices into $SO(n)$, but they are different maps.
- Putting the inverse on the other factor changes the result. $(I + A)(I - A)^{-1} = C(-A)$, and this is $C(A)^{-1} = C(A)^T$.

## Explanations

### L1 human

Rotations are hard to write down, because their numbers must satisfy many square equations at once.
A skew-symmetric table of numbers is easy to write down: choose the numbers above the diagonal freely.
The Cayley transform is a recipe that turns each such table into a rotation.
It works backwards too, for nearly all rotations.
Only the rotations that turn some direction completely around are missed.

### L2 human

Worked example: the $2 \times 2$ case with $t = \frac{1}{2}$.

1. $A = \begin{pmatrix} 0 & -\frac{1}{2} \\ \frac{1}{2} & 0 \end{pmatrix}$, so $I + A = \begin{pmatrix} 1 & -\frac{1}{2} \\ \frac{1}{2} & 1 \end{pmatrix}$ with determinant $\frac{5}{4}$.
2. $(I + A)^{-1} = \frac{4}{5}\begin{pmatrix} 1 & \frac{1}{2} \\ -\frac{1}{2} & 1 \end{pmatrix}$.
3. $(I - A)(I + A)^{-1} = \frac{4}{5}\begin{pmatrix} 1 & \frac{1}{2} \\ -\frac{1}{2} & 1 \end{pmatrix}^2 = \frac{4}{5}\begin{pmatrix} \frac{3}{4} & 1 \\ -1 & \frac{3}{4} \end{pmatrix} = \frac{1}{5}\begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix}$.
4. Check: $3^2 + 4^2 = 5^2$, so the columns have length $1$, and they are orthogonal.

The typical use: produce orthogonal matrices with rational entries, or describe the rotations near $I$ by free parameters.
A trap: some books put the minus sign in the other factor, so the sign of $A$ depends on the book.

### L3 human

The skew-symmetric matrices form the Lie algebra $\mathfrak{so}(n)$ of $SO(n)$.
The Cayley transform is a rational map from $\mathfrak{so}(n)$ onto a dense open subset of $SO(n)$, and its derivative at $0$ is $-2$ times the identity.
So it gives a chart of $SO(n)$ near $I$, and it shows that $SO(n)$ is a rational variety.
The same formula sends skew-Hermitian matrices to unitary matrices without the eigenvalue $-1$.
The Lie theory of this chart belongs to the area of Lie groups.
