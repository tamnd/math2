---
tag: NHR1K0GPS1
kind: example
name: A triangular matrix
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [0BQAA2BK3Q, 7JJE96MZQY, 0FY42N02DV]
illustrates: [053QVHF6N7, FWY8A9M5HK, 0NMXDCNNKR, 0C2F40MEBC]
uses: [039HF58KQ5, 0K1KKMFHYH, 0ZND7NQ970, 0S7A0EMPF4, 06YSJVR356, 0FRYPZ6D0X, 0W4FSW1TVB]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Triangular matrix example
  - book: isbn:9780321982384
---

## Example

Let
$$A = \begin{pmatrix} 2 & 5 & 7 \\ 0 & -1 & 3 \\ 0 & 0 & 2 \end{pmatrix}$$
over $\mathbb{R}$, an upper triangular matrix.
We find its eigenvalues, their multiplicities and its eigenvectors.

1. The matrix $tI - A$ is upper triangular with diagonal entries $t - 2$, $t + 1$ and $t - 2$.
   By the [[determinant of a triangular matrix|0K1KKMFHYH]],
$$p_A(t) = (t - 2)(t + 1)(t - 2) = (t - 2)^2 (t + 1) = t^3 - 3t^2 + 4.$$
2. Check by the [[coefficients of the characteristic polynomial|0FRYPZ6D0X]].
   The trace is $2 - 1 + 2 = 3$.
   The three $2 \times 2$ principal minors are $2 \cdot (-1) = -2$, $2 \cdot 2 = 4$ and $(-1) \cdot 2 = -2$, with sum $0$.
   The determinant is $2 \cdot (-1) \cdot 2 = -4$.
   So $p_A(t) = t^3 - 3t^2 + 0 \cdot t - (-4)$, as in step 1.
3. So the [[eigenvalues|0ZND7NQ970]] are the diagonal entries $2$ and $-1$.
   The [[algebraic multiplicity|0S7A0EMPF4]] of $2$ is $2$, and that of $-1$ is $1$.
4. For the eigenvalue $2$, the first column gives $A(1, 0, 0) = (2, 0, 0) = 2(1, 0, 0)$.
5. For the eigenvalue $-1$, solve $(A + I)x = 0$: the third row gives $x_3 = 0$, and the first row gives $3x_1 + 5x_2 = 0$, so $x = (5, -3, 0)$.
   Check: $A(5, -3, 0) = (10 - 15, 3, 0) = (-5, 3, 0) = -(5, -3, 0)$.
6. The matrix
$$A - 2I = \begin{pmatrix} 0 & 5 & 7 \\ 0 & -3 & 3 \\ 0 & 0 & 0 \end{pmatrix}$$
   has rank $2$, because its first two rows are independent.
   By the [[rank-nullity theorem|0W4FSW1TVB]], its kernel has dimension $3 - 2 = 1$, so the [[geometric multiplicity|06YSJVR356]] of $2$ is $1$.

## Remarks

For a triangular matrix the eigenvalues are the diagonal entries, each counted as often as it appears, and no determinant needs to be expanded.
The diagonal does not tell you the eigenvectors or the geometric multiplicity.
Here $2$ appears twice, but its eigenspace is only the line through $(1, 0, 0)$, so $A$ has no basis of eigenvectors.
The trace and determinant rules hold as they should: $2 + 2 - 1 = 3 = \operatorname{tr} A$ and $2 \cdot 2 \cdot (-1) = -4 = \det A$.

Change the entry $5$ in place $(1, 2)$ and $7$ in place $(1, 3)$ to $0$, and keep the $3$.
Then the rows of $A - 2I$ are $(0, 0, 0)$, $(0, -3, 3)$ and $(0, 0, 0)$, of rank $1$, so the eigenspace of $2$ becomes a plane.
The eigenvalues stay the same, because the diagonal did not change, but the geometric multiplicity grows to match the algebraic one.

## Explanations

### L1 human

For a triangular matrix, the eigenvalues can be read from the diagonal.
Here they are $2$, $-1$ and $2$, with $2$ counted twice.
The eigenvectors still have to be found by solving equations, and the repeated $2$ gives only one direction.

### L2 human

The typical use is to read the spectrum of a triangular matrix at once, and then to solve one linear system for each eigenvalue.
The same shortcut works for lower triangular matrices, since $tI - A$ is then lower triangular.
Watch out: the shortcut needs a triangular matrix.
It fails for a general matrix, and it fails after row reduction, because row operations change the eigenvalues.
