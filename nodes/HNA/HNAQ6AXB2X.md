---
tag: HNAQ6AXB2X
kind: example
name: A thin QR factorization of a 3 by 2 matrix and its least-squares use
msc: [15A23, 65F20]
topics: [8GQVME4SZZ]
audience: ug1
instance_of: [0VT6P0GNQR]
illustrates: [0ERWG4NXQ9, 4D7MRG4D91]
uses: [0W809K6AW0, 0MKABWDRNC, 0B8KZRT28M]
sources:
  - book: isbn:9780321982384
    locator: Section 6.4
  - url: https://en.wikipedia.org/wiki/QR_decomposition
    locator: Using the Gram–Schmidt process
---

## Example

Let
$$A = \begin{pmatrix} 1 & 3 \\ 2 & 0 \\ 2 & 3 \end{pmatrix}, \quad a_1 = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}, \quad a_2 = \begin{pmatrix} 3 \\ 0 \\ 3 \end{pmatrix}, \quad b = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}.$$
The columns are independent, because $a_2$ is not a multiple of $a_1$.
We find the thin [[QR decomposition|0ERWG4NXQ9]] by the [[Gram-Schmidt process|0VT6P0GNQR]], and then we use it to solve $Ax = b$ in the least-squares sense.

1. The length of $a_1$ is $r_{11} = \sqrt{1 + 4 + 4} = 3$, so $q_1 = \tfrac{1}{3}(1, 2, 2)$.
2. The component of $a_2$ along $q_1$ has size $r_{12} = a_2 \cdot q_1 = (3 + 0 + 6)/3 = 3$.
3. Removing that component leaves $v_2 = a_2 - r_{12} q_1 = (3, 0, 3) - (1, 2, 2) = (2, -2, 1)$.
4. The length of $v_2$ is $r_{22} = \sqrt{4 + 4 + 1} = 3$, so $q_2 = \tfrac{1}{3}(2, -2, 1)$.
5. The factors are
$$Q = \frac{1}{3} \begin{pmatrix} 1 & 2 \\ 2 & -2 \\ 2 & 1 \end{pmatrix}, \qquad R = \begin{pmatrix} 3 & 3 \\ 0 & 3 \end{pmatrix}.$$
6. Check $Q^{\mathsf{T}} Q = I_2$: $q_1 \cdot q_1 = 9/9 = 1$, $q_2 \cdot q_2 = 9/9 = 1$ and $q_1 \cdot q_2 = (2 - 4 + 2)/9 = 0$.
7. Check $QR = A$: column 1 of $QR$ is $3 q_1 = (1, 2, 2) = a_1$, and column 2 is $3 q_1 + 3 q_2 = (1, 2, 2) + (2, -2, 1) = (3, 0, 3) = a_2$.
8. For least squares we need
$$Q^{\mathsf{T}} b = \left( \frac{1 + 2 + 2}{3}, \frac{2 - 2 + 1}{3} \right) = \left( \frac{5}{3}, \frac{1}{3} \right).$$
9. Back substitution in $R \hat x = Q^{\mathsf{T}} b$ starts with the second row, $3 \hat x_2 = 1/3$, so $\hat x_2 = 1/9$.
10. The first row is $3 \hat x_1 + 3/9 = 5/3$, so $3 \hat x_1 = 4/3$ and $\hat x_1 = 4/9$.
11. Check with the [[normal equations|4D7MRG4D91]]: $A^{\mathsf{T}} A = \begin{pmatrix} 9 & 9 \\ 9 & 18 \end{pmatrix}$ and $A^{\mathsf{T}} b = (5, 6)$, and indeed $9 \cdot \tfrac{4}{9} + 9 \cdot \tfrac{1}{9} = 5$ and $9 \cdot \tfrac{4}{9} + 18 \cdot \tfrac{1}{9} = 6$.
12. The fitted vector is $A \hat x = (7/9, 8/9, 11/9)$, so the residual is $r = b - A \hat x = (2/9, 1/9, -2/9)$.
13. The residual is orthogonal to both columns, since $r \cdot a_1 = (2 + 2 - 4)/9 = 0$ and $r \cdot a_2 = (6 + 0 - 6)/9 = 0$.

## Remarks

The vector $A \hat x = Q Q^{\mathsf{T}} b = \tfrac{5}{3} q_1 + \tfrac{1}{3} q_2$ is the [[orthogonal projection|0B8KZRT28M]] of $b$ onto the column space of $A$.
So the entries of $Q^{\mathsf{T}} b$ are the coordinates of the projection in the orthonormal basis $q_1, q_2$.

The $3 \times 2$ matrix $Q$ has orthonormal columns, but it is not an orthogonal matrix.
Its product $Q Q^{\mathsf{T}}$ is a projection of rank $2$ with trace $2$, so it is not $I_3$.
The unit vector $q_3 = \tfrac{1}{3}(2, 1, -2)$ is orthogonal to $q_1$ and $q_2$, since $(2 + 2 - 4)/9 = 0$ and $(4 - 2 - 2)/9 = 0$, and adding it as a third column gives an orthogonal $3 \times 3$ matrix.
The residual is the part of $b$ along $q_3$: $b \cdot q_3 = 1/3$, so $r = \tfrac{1}{3} q_3 = \tfrac{1}{9}(2, 1, -2)$ and $\norm{r}^2 = 1/9$, which agrees with step 12.

If $b$ is changed to a vector of the column space, such as $b = a_1 + a_2 = (4, 2, 5)$, the same steps give $\hat x = (1, 1)$ and residual $0$.

## Explanations

### L1 human

Gram-Schmidt turns the two columns of $A$ into two perpendicular unit vectors $q_1$ and $q_2$.
The triangular matrix $R$ stores the lengths and the overlap that we removed: $3$, $3$ and $3$ here.
With $Q$ and $R$ in hand, the least-squares problem becomes a small triangular system that we solve from the bottom up.

### L2 human

The method has two stages.
First compute $q_1$, subtract from $a_2$ its component along $q_1$, normalize, and record the coefficients in $R$.
Then solve $R \hat x = Q^{\mathsf{T}} b$ from the bottom row up.
The typical use is a least-squares fit in which we want to avoid forming $A^{\mathsf{T}} A$.
The trap is to write $Q Q^{\mathsf{T}} = I$ and conclude $A \hat x = b$, but here $A \hat x \ne b$, because $b$ is not in the column space.
