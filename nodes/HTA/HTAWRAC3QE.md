---
tag: HTAWRAC3QE
kind: example
name: The shear of the plane
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [0FY42N02DV, 099TWVJ909, 03NDVCSHSB]
illustrates: [FWY8A9M5HK]
uses: [039HF58KQ5, 0S7A0EMPF4, 06YSJVR356, 0AYEPBQMAW, 0V58FPM3EQ, 0K1KKMFHYH]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Matrix with repeated eigenvalues example
  - book: isbn:9780134860244
---

## Example

Let
$$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$
over a field $F$.
It sends $(x, y)$ to $(x + y, y)$, so it slides each horizontal line sideways by its height.
We find its eigenvalue, the two multiplicities and the minimal polynomial.

1. The matrix $tI - A = \begin{pmatrix} t - 1 & -1 \\ 0 & t - 1 \end{pmatrix}$ is upper triangular, so the [[determinant of a triangular matrix|0K1KKMFHYH]] gives
$$p_A(t) = (t - 1)^2.$$
   Check: $\operatorname{tr} A = 2$ and $\det A = 1$, so $p_A(t) = t^2 - 2t + 1$, the same polynomial.
2. So $1$ is the only eigenvalue, and its [[algebraic multiplicity|0S7A0EMPF4]] is $2$.
3. The matrix $A - I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ sends $(x, y)$ to $(y, 0)$, so its kernel is $\{ (x, 0) : x \in F \}$.
4. Check: $A(1, 0) = (1, 0)$, while $A(0, 1) = (1, 1)$ is not a multiple of $(0, 1)$.
5. So the [[eigenspace|0AYEPBQMAW]] $E_1$ is the line spanned by $(1, 0)$, and the [[geometric multiplicity|06YSJVR356]] of $1$ is $1$.
6. The matrix $A - I$ squares to zero:
$$(A - I)^2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}.$$
7. The monic divisors of $(t - 1)^2$ of smaller degree are $1$ and $t - 1$, and neither annihilates $A$, since $I \ne 0$ and $A - I \ne 0$.
8. So the [[minimal polynomial|0V58FPM3EQ]] is $m_A(t) = (t - 1)^2$, equal to $p_A$.

## Remarks

The geometric multiplicity $1$ is strictly less than the algebraic multiplicity $2$, so the eigenvalue is defective and $A$ is not [[diagonalizable|07SQCNV233]].
The repeated root of $m_A$ gives the same conclusion by a different route.
The shear is the smallest matrix with this behavior, since a $1 \times 1$ matrix is always diagonal.

Replace the corner entry $1$ by any $c \ne 0$.
Nothing changes: $p = (t - 1)^2$, $A - I$ still has rank $1$, and $m = (t - 1)^2$.
Replace it by $0$, and $A$ becomes $I$, with $g(1) = 2$ and $m = t - 1$.
Replace a diagonal entry instead, as in $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$, and the two eigenvalues become distinct, so the matrix becomes diagonalizable, with eigenvectors $(1, 0)$ and $(1, 1)$.

## Explanations

### L1 human

Think of a deck of cards pushed sideways, with each card moved by its height.
The bottom card stays where it is, and the cards on the bottom line keep their direction.
Every other arrow is tilted.
So the shear has just one line of eigenvectors, the horizontal axis, although its eigenvalue $1$ is a double root of the characteristic polynomial.

### L2 human

The shear is the standard example of a defective matrix.
The characteristic polynomial counts the root $1$ twice, but the eigenspace is only a line.
So a basis of eigenvectors would need two independent eigenvectors and there is only one direction available.
Watch out: you cannot count eigenvectors by counting roots with multiplicity; you must compute the rank of $A - \lambda I$.
