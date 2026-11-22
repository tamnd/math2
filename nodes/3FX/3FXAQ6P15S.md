---
tag: 3FXAQ6P15S
kind: example
name: Values of the Rayleigh quotient of a symmetric 2 × 2 matrix
msc: ["15A18", "15A42"]
topics: [3YM9EK6VMB]
audience: ug1
instance_of: [06WHP8SE98]
illustrates: [T7MFPSY009, 0C4NT4GT3X]
uses: [06WHP8SE98, 0N28QN4CYA]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_quotient
    locator: Bounds for Hermitian M
---

## Example

Let $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$, a [[symmetric|0N28QN4CYA]] matrix on $\mathbb{R}^2$ with the dot product.
For $x = (x_1, x_2) \neq 0$, its [[Rayleigh quotient|06WHP8SE98]] is
$$R(x) = \frac{x^{\mathsf{T}} A x}{x^{\mathsf{T}} x} = \frac{5 x_1^2 + 4 x_1 x_2 + 2 x_2^2}{x_1^2 + x_2^2}.$$
We find the eigenvalues, and then we compute the quotient at several vectors.

1. The characteristic polynomial is $(5 - t)(2 - t) - 4 = t^2 - 7t + 6 = (t - 6)(t - 1)$, so the eigenvalues are $6$ and $1$.
2. At the standard basis vectors, $R(1, 0) = \tfrac{5}{1} = 5$ and $R(0, 1) = \tfrac{2}{1} = 2$.
3. At the diagonals,
$$R(1, 1) = \frac{5 + 4 + 2}{2} = \frac{11}{2}, \qquad R(1, -1) = \frac{5 - 4 + 2}{2} = \frac{3}{2}.$$
4. At $(3, 1)$ we get $R(3, 1) = \tfrac{45 + 12 + 2}{10} = \tfrac{59}{10}$.
5. At $(2, 1)$ we get $R(2, 1) = \tfrac{20 + 8 + 2}{5} = 6$. This vector is an eigenvector for $6$, since $A(2, 1) = (12, 6)$.
6. At $(1, -2)$ we get $R(1, -2) = \tfrac{5 - 8 + 8}{5} = 1$. This vector is an eigenvector for $1$, since $A(1, -2) = (1, -2)$.
7. All values lie in $[1, 6]$, and the ends $6$ and $1$ are reached at the eigenvectors.

## Remarks

Step 7 is [[the extreme value theorem for the quotient|T7MFPSY009]] in action: the maximum and the minimum of $R$ are the extreme eigenvalues, reached at the eigenvectors.
Since $R(cx) = R(x)$ for $c \neq 0$, it is enough to look at unit vectors, and on the unit circle $R$ is just the quadratic form $x^{\mathsf{T}} A x$.
That is the setting of part 2 of [[the theorem on real eigenvalues|0C4NT4GT3X]], which finds the eigenvalue $6$ as the maximum of the form on the circle.

The value $\tfrac{59}{10}$ at $(3, 1)$ is close to $6$, because $(3, 1)$ points almost the same way as $(2, 1)$.
[[The quadratic accuracy example|S1XDFTT962]] explains why the error is so small.
If we change the off-diagonal entries from $2$ to $0$, the matrix becomes $\operatorname{diag}(5, 2)$, the eigenvectors become $(1, 0)$ and $(0, 1)$, and the range of $R$ shrinks to $[2, 5]$.

## Explanations

### L1 human

We test the matrix on several directions and record how much it stretches each direction along itself.
The stretch is $5$ for $(1, 0)$, $5.5$ for $(1, 1)$ and $5.9$ for $(3, 1)$.
It never goes above $6$ and never drops below $1$.
The extreme values $6$ and $1$ occur along the special directions $(2, 1)$ and $(1, -2)$, which are the eigenvectors.

### L2 human

To estimate the largest eigenvalue of a symmetric matrix, pick a few test vectors and compute the Rayleigh quotient of each.
Every value is a lower bound for the largest eigenvalue, so keep the largest one.
Here the vector $(3, 1)$ already gives $5.9$, and the true value is $6$.
Watch out: the quotient must divide by $x^{\mathsf{T}} x$.
Without the division, the vector $(2, 2)$ would give $20 + 16 + 8 = 44$, which says nothing about the eigenvalues.
