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
The matrix is real, so its adjoint has the matrix $A^* = A^{\mathsf{T}} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$.
We show that $A$ is not [[normal|0ENZN5G4CV]] and that it has no basis of eigenvectors.

1. Multiply in the first order. The entries of $A A^{\mathsf{T}}$ are the dot products of the rows $(1, 1)$ and $(0, 1)$, so $A A^{\mathsf{T}} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$.
2. Multiply in the other order. The entries of $A^{\mathsf{T}} A$ are the dot products of the columns $(1, 0)$ and $(1, 1)$, so $A^{\mathsf{T}} A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$.
3. The two products differ in the top left entry, $2$ against $1$, so $A$ is not normal.
4. The norm test gives the same answer: $A e_1 = (1, 0)$ has norm $1$, while $A^{\mathsf{T}} e_1 = (1, 1)$ has norm $\sqrt{2}$.
5. The characteristic polynomial is $(1 - t)^2$, so $1$ is the only eigenvalue, over $\mathbb{R}$ and over $\mathbb{C}$.
6. The kernel of $A - I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ is the line spanned by $e_1$. So all eigenvectors lie on one line, and $A$ has no basis of eigenvectors, orthonormal or not.

## Remarks

The shear shows the easy direction of [[the complex spectral theorem|04CW1P44VD]] in contrapositive form.
A matrix with an orthonormal eigenbasis must be normal, and $A$ is not normal, so it cannot have one.
Here the failure is even stronger, since $A$ has no eigenbasis at all.

The vector $e_1$ is an eigenvector of $A$ but not of $A^{\mathsf{T}}$, since $A^{\mathsf{T}} e_1 = (1, 1)$.
So part 3 of [[the norm criterion|EMW3QTE3H9]] really needs normality.

What happens when the shear gets weaker?
For $A_c = \begin{pmatrix} 1 & c \\ 0 & 1 \end{pmatrix}$ the same two products give
$$A_c A_c^{\mathsf{T}} - A_c^{\mathsf{T}} A_c = \begin{pmatrix} 1 + c^2 & c \\ c & 1 \end{pmatrix} - \begin{pmatrix} 1 & c \\ c & 1 + c^2 \end{pmatrix} = \begin{pmatrix} c^2 & 0 \\ 0 & -c^2 \end{pmatrix}.$$
So $A_c$ is normal only for $c = 0$, when it is the identity.
The matrix $A$ is already upper triangular, so it is its own Schur form, and the entry $1$ above the diagonal is exactly what stops it from being normal.

## Explanations

### L1 human

This matrix shears the plane: it slides each point to the right by its height.
Its transpose slides each point upwards by its distance to the right instead.
Doing the shear and then the transposed shear gives a different result from the opposite order.
So the shear is not normal, and it has only one special direction, the horizontal one.

### L2 human

The test for normality has three steps.
Write down $A$ and $A^*$, compute both products $A A^*$ and $A^* A$, and compare them entry by entry.
One entry that differs is enough, and here the top left entries are $2$ and $1$.
A quicker route is often the norm test of the norm criterion, which needs only one vector: $\norm{A e_1} = 1$ but $\norm{A^{\mathsf{T}} e_1} = \sqrt{2}$.
Watch out: $A$ is real, triangular and has a real eigenvalue, and none of these facts makes it normal.
