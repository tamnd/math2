---
tag: BF9MKKHH4Z
kind: example
name: The shear matrix is not normal
msc: ["15A04", "47B15"]
topics: [3YM9EK6VMB]
audience: ug1
not_instance_of:
  - target: 0C8BR8XRTR
    note: for A with rows (1, 1) and (0, 1), the products A A^T and A^T A differ, and the norms of A e_1 and A^T e_1 are 1 and the square root of 2
  - target: 07SQCNV233
    note: the only eigenvalue is 1, and its eigenspace is the line spanned by e_1, so A has no basis of eigenvectors
illustrates: [EMW3QTE3H9, 04CW1P44VD]
uses: [0ENZN5G4CV, 0XYKE8BE7X]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_matrix
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Example

Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ act on $\mathbb{R}^2$ or on $\mathbb{C}^2$ with the standard inner product.
The adjoint has the matrix $A^* = A^T = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, since $A$ is real.

1. We compute $A A^T = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$.
2. We compute $A^T A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$.
3. The two products differ, so $A$ is not [[normal|0ENZN5G4CV]].
4. The norm test gives the same answer: $A e_1 = (1, 0)$ has norm $1$, and $A^T e_1 = (1, 1)$ has norm $\sqrt{2}$.
5. The characteristic polynomial is $(1 - t)^2$, so $1$ is the only eigenvalue. The kernel of $A - I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ is the line spanned by $e_1$.
6. So $A$ has no basis of eigenvectors, and in particular no orthonormal basis of eigenvectors, over $\mathbb{R}$ or over $\mathbb{C}$.

## Remarks

- The example shows the direction "orthonormal eigenbasis implies normal" of [[the complex spectral theorem|04CW1P44VD]] in contrapositive form: $A$ is not normal, and it has no orthonormal eigenbasis.
- The vector $e_1$ is an eigenvector of $A$ but not of $A^T$. This shows that part 3 of [[the norm criterion|EMW3QTE3H9]] needs normality.
- For $A_c = \begin{pmatrix} 1 & c \\ 0 & 1 \end{pmatrix}$, we get $A_c A_c^T - A_c^T A_c = \begin{pmatrix} c^2 & 0 \\ 0 & -c^2 \end{pmatrix}$. So $A_c$ is normal only for $c = 0$.
- The matrix $A$ is already upper triangular. It is its own Schur form, and the entry $1$ above the diagonal measures the failure of normality.

## Explanations

### L1 human

This matrix shears the plane: it slides each point to the right by its height.
Its transpose slides points upwards instead.
Doing the shear and then the transposed shear differs from the opposite order.
So the shear is not normal, and it has only one special direction, the horizontal one.

### L2 human

The test for normality:

1. Write down $A$ and $A^*$.
2. Compute both products $A A^*$ and $A^* A$, and compare them entry by entry.
3. If one entry differs, the matrix is not normal. Here the top left entries are $2$ and $1$.

A trap: the matrix has real eigenvalues and is triangular, but these facts do not make it normal.
