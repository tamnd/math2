---
tag: 39XSQ9MTZ3
kind: example
name: Rayleigh quotient of a non-symmetric matrix exceeds its eigenvalues
msc: ["15A18", "15A42"]
topics: [3YM9EK6VMB]
audience: ug1
not_instance_of:
  - target: 0NEGN5CRSC
    note: the matrix with rows (1, 4) and (0, 1) is not symmetric, and its Rayleigh quotient takes the values 3 and -1, while its only eigenvalue is 1
illustrates: [T7MFPSY009]
uses: [06WHP8SE98, 0N28QN4CYA]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_quotient
    locator: Bounds for Hermitian M
---

## Example

Let $A = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$ act on $\mathbb{R}^2$ with the dot product.
We show that its Rayleigh quotient leaves the range of its eigenvalues, so the bounds for self-adjoint operators fail without symmetry.

1. The matrix is not [[symmetric|0N28QN4CYA]], since the entries $4$ and $0$ off the diagonal differ.
2. It is upper triangular, so its only eigenvalue is the diagonal entry $1$.
3. For $x = (x_1, x_2)$, the numerator of the quotient is
$$x^{\mathsf{T}} A x = x_1 (x_1 + 4 x_2) + x_2 \cdot x_2 = x_1^2 + 4 x_1 x_2 + x_2^2.$$
4. At $x = (1, 1)$, the numerator is $1 + 4 + 1 = 6$ and $x^{\mathsf{T}} x = 2$, so the [[Rayleigh quotient|06WHP8SE98]] is $R(1, 1) = 3$.
5. At $x = (1, -1)$, the numerator is $1 - 4 + 1 = -2$ and $x^{\mathsf{T}} x = 2$, so $R(1, -1) = -1$.
6. Both values differ from the only eigenvalue $1$, so part 1 of [[the extreme value theorem|T7MFPSY009]] fails for this matrix.

## Remarks

What does the quotient measure here?
A real number $x^{\mathsf{T}} A x$ equals its own transpose $x^{\mathsf{T}} A^{\mathsf{T}} x$, so it does not change when we replace $A$ by the symmetric part
$$S = \tfrac{1}{2}(A + A^{\mathsf{T}}) = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}.$$
The eigenvalues of $S$ are $3$ and $-1$, with the eigenvectors $(1, 1)$ and $(1, -1)$.
So the quotient of $A$ ranges over $[-1, 3]$, the range for $S$, and it tells us about $S$, not about the eigenvalues of $A$.

If we change the entry $4$ to $c$, the symmetric part has the eigenvalues $1 \pm \tfrac{c}{2}$, while $A$ keeps the single eigenvalue $1$.
So the gap grows with $c$, and it closes only for $c = 0$, where $A = I$ is symmetric.

## Explanations

### L1 human

This matrix has only one stretch factor, $1$, along its one special direction $(1, 0)$.
But along the direction $(1, 1)$ it pushes a vector forward by a factor of $3$, and along $(1, -1)$ it pushes a vector backward.
So for a matrix that is not symmetric, the Rayleigh quotient does not locate the eigenvalues.

### L2 human

To find the range of the Rayleigh quotient of any real matrix $A$, first replace $A$ by its symmetric part $S = \tfrac{1}{2}(A + A^{\mathsf{T}})$, which has the same quadratic form.
Then the largest and the smallest eigenvalue of $S$ are the maximum and the minimum of the quotient, by the theorem for symmetric matrices.
Here $\det(S - tI) = (1 - t)^2 - 4$, so the range is $[-1, 3]$.
Watch out: the eigenvalues of $A$ and of $S$ can be far apart, as $1$ for $A$ against $3$ and $-1$ for $S$ shows.
