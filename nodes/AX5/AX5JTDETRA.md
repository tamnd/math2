---
tag: AX5JTDETRA
kind: counterexample
name: The transpose times a complex matrix can lose rank
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug2
uses: [0EWQEYRVA8, 0W809K6AW0, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Properties
---

## Counterexample

Over the real numbers $\rank(A^{\mathsf{T}} A) = \rank A$, but the claim "$\rank(A^{\mathsf{T}} A) = \rank A$ for every matrix over every field" is false.
A single complex column shows it.

1. Let $A = \begin{pmatrix} 1 \\ i \end{pmatrix}$, a $2 \times 1$ matrix over $\mathbb{C}$.
Its only column is nonzero, so its [[rank|0EWQEYRVA8]] is $1$.
2. The [[transpose|0W809K6AW0]] is $A^{\mathsf{T}} = \begin{pmatrix} 1 & i \end{pmatrix}$.
3. The [[matrix product|076JGP6R3T]] is the $1 \times 1$ matrix
$$A^{\mathsf{T}} A = (1 \cdot 1 + i \cdot i) = (1 + i^2) = (1 - 1) = (0).$$
4. So $\rank(A^{\mathsf{T}} A) = 0 \ne 1 = \rank A$.
5. The same thing happens over $\mathbb{F}_2$ with $B = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
Here $\rank B = 1$, but $B^{\mathsf{T}} B = (1 + 1) = (0)$ in $\mathbb{F}_2$, so $\rank(B^{\mathsf{T}} B) = 0$.
6. Over $\mathbb{C}$, the conjugate transpose repairs the claim.
With $A^* = \begin{pmatrix} 1 & -i \end{pmatrix}$, we get $A^* A = (1 + (-i)(i)) = (1 + 1) = (2)$, so $\rank(A^* A) = 1 = \rank A$.

## Remarks

In each case the column $y$ of the matrix is a nonzero vector with $y^{\mathsf{T}} y = 0$, an isotropic vector.
The [[theorem over the real numbers|FGPT52R1ZE]] works because a real vector with $y^{\mathsf{T}} y = 0$ is zero, and these two examples remove exactly that fact.
Step 6 shows the correct complex form: $\langle y, y \rangle = \overline{y}^{\mathsf{T}} y = \sum \lvert y_i \rvert^2$ is zero only for $y = 0$.

The failure is not tied to one column.
For the $2 \times 2$ matrix $M = \begin{pmatrix} 1 & 0 \\ i & 0 \end{pmatrix}$ of rank $1$, the product $M^{\mathsf{T}} M$ has entry $(1, 1)$ equal to $1 + i^2 = 0$ and all other entries $0$, so it is the zero matrix.
If we change the column to $(1, 2i)$, then $A^{\mathsf{T}} A = (1 - 4) = (-3)$, and the rank is kept; the loss needs exact cancellation.

## Explanations

### L1 human

Over the complex numbers, the vector $(1, i)$ has "squared length" $1 \cdot 1 + i \cdot i = 1 - 1 = 0$ when no conjugate is used.
So the product $A^{\mathsf{T}} A$ can be zero although $A$ is not.
With the conjugate, the squared length is $1 + 1 = 2$, as it should be.

### L2 human

The real proof uses that $x^{\mathsf{T}} A^{\mathsf{T}} A x = \lVert Ax \rVert^2$ is zero only when $Ax = 0$.
Over $\mathbb{C}$ without conjugation, and over $\mathbb{F}_2$, the expression $y^{\mathsf{T}} y$ is not a squared length, because it can vanish for $y \ne 0$.
Watch out: in complex linear algebra, replace every $A^{\mathsf{T}}$ that comes from a dot product by $A^*$, as in the normal equations $A^* A x = A^* b$.
