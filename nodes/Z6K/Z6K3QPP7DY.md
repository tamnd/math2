---
tag: Z6K3QPP7DY
kind: example
name: The symmetric matrix with rows (2, 1) and (1, 2)
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [0BQAA2BK3Q, 0N6960W0BV, 0XPX5NC67E, 7JJE96MZQY]
illustrates: [053QVHF6N7, 0NMXDCNNKR, 0C2F40MEBC]
uses: [0ZND7NQ970, 0B5H4208Z9, 039HF58KQ5, 04EHB7YDQS, 053QVHF6N7]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Two-dimensional matrix example
  - book: isbn:9780134860244
---

## Example

Let $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ over $\mathbb{R}$.
We find its [[eigenvalues|0ZND7NQ970]] and [[eigenvectors|0B5H4208Z9]] by the method for [[computing eigenvalues by hand|7JJE96MZQY]].

1. The [[characteristic polynomial|039HF58KQ5]] is
$$p_A(t) = \det(tI - A) = \det \begin{pmatrix} t - 2 & -1 \\ -1 & t - 2 \end{pmatrix} = (t - 2)^2 - 1 = t^2 - 4t + 3.$$
2. Check with the $2 \times 2$ shortcut $p_A(t) = t^2 - (\tr A)t + \det A$.
   Here $\tr A = 4$ and $\det A = 4 - 1 = 3$, so we get the same polynomial.
3. It factors as $t^2 - 4t + 3 = (t - 1)(t - 3)$.
   Since the [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]], the eigenvalues are $1$ and $3$.
4. For $\lambda = 1$, the matrix $A - I$ has the two rows $(1, 1)$, so its kernel is the line $v_1 + v_2 = 0$, spanned by $v_1 = (1, -1)$.
   Check: $A v_1 = (2 - 1, 1 - 2) = (1, -1) = 1 \cdot v_1$.
5. For $\lambda = 3$, the matrix $A - 3I$ has the rows $(-1, 1)$ and $(1, -1)$, so its kernel is the line $v_1 = v_2$, spanned by $v_2 = (1, 1)$.
   Check: $A v_2 = (2 + 1, 1 + 2) = (3, 3) = 3 \cdot v_2$.
6. So the [[spectrum|04EHB7YDQS]] of $A$ is $\{1, 3\}$, and each eigenvalue has a line of eigenvectors.

## Remarks

The two eigenvalues give the trace and the determinant: $1 + 3 = 4 = \tr A$ and $1 \cdot 3 = 3 = \det A$.
The two eigenvectors $(1, -1)$ and $(1, 1)$ are perpendicular, since their dot product is $1 - 1 = 0$.
This happens for every real symmetric matrix with distinct eigenvalues, a fact that the spectral theorem explains.
Put the eigenvectors into the columns of $S = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$.
Then $AS = \begin{pmatrix} 1 & 3 \\ -1 & 3 \end{pmatrix} = S \operatorname{diag}(1, 3)$, so $S^{-1} A S = \operatorname{diag}(1, 3)$.
The [[minimal polynomial|03NDVCSHSB]] is $p_A$ itself, because no polynomial of degree $1$ kills $A$, as $A$ is not a multiple of $I$.

Now change the off-diagonal entries from $1$ to a real number $b$.
The same two vectors still work, because $\begin{pmatrix} 2 & b \\ b & 2 \end{pmatrix}$ sends $(1, 1)$ to $(2 + b)(1, 1)$ and $(1, -1)$ to $(2 - b)(1, -1)$.
So the eigenvalues become $2 + b$ and $2 - b$, and they merge into the single eigenvalue $2$ when $b = 0$, where every nonzero vector is an eigenvector.

## Explanations

### L1 human

The matrix stretches the line through $(1, 1)$ by the factor $3$.
It leaves each vector on the line through $(1, -1)$ where it is.
These two lines are the eigenvector directions, and they cross at a right angle.
Every other vector gets turned toward the line through $(1, 1)$.

### L2 human

The two-stage method is the standard one: factor $p_A$, then solve $(A - \lambda I)v = 0$ for each root.
Always check $Av = \lambda v$ at the end, because it costs one line.
Watch out: the diagonal entries are $2$ and $2$, but $2$ is not an eigenvalue, since $\det(A - 2I) = 0 \cdot 0 - 1 \cdot 1 = -1 \ne 0$.
Reading eigenvalues from the diagonal works only for triangular matrices.
