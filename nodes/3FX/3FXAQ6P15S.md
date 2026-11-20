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

Let $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$, a [[symmetric|0N28QN4CYA]] matrix with the eigenvalues $6$ and $1$.
For $x = (x_1, x_2) \neq 0$, its [[Rayleigh quotient|06WHP8SE98]] is
$$R(x) = \frac{x^T A x}{x^T x} = \frac{5 x_1^2 + 4 x_1 x_2 + 2 x_2^2}{x_1^2 + x_2^2}.$$

1. $R(1, 0) = \tfrac{5}{1} = 5$ and $R(0, 1) = \tfrac{2}{1} = 2$.
2. $R(1, 1) = \tfrac{5 + 4 + 2}{2} = \tfrac{11}{2}$ and $R(1, -1) = \tfrac{5 - 4 + 2}{2} = \tfrac{3}{2}$.
3. $R(3, 1) = \tfrac{45 + 12 + 2}{10} = \tfrac{59}{10}$.
4. $R(2, 1) = \tfrac{20 + 8 + 2}{5} = 6$. The vector $(2, 1)$ is an eigenvector for $6$.
5. $R(1, -2) = \tfrac{5 - 8 + 8}{5} = 1$. The vector $(1, -2)$ is an eigenvector for $1$.
6. All values lie in $[1, 6]$. The value $6$ is the maximum, and the value $1$ is the minimum.

## Remarks

- Step 6 is [[the extreme value statement|T7MFPSY009]]: the maximum and the minimum are the extreme eigenvalues, attained at the eigenvectors.
- $R(cx) = R(x)$ for $c \neq 0$. So it is enough to look at unit vectors, and on the unit circle $R$ is the quadratic form.
- The value $\tfrac{59}{10}$ at $(3, 1)$ is close to $6$, because $(3, 1)$ is close in direction to $(2, 1)$. [[The eigenvalue estimate example|S1XDFTT962]] makes this precise.

## Explanations

### L1 human

We test the matrix on several directions and record the stretch in each direction.
The stretch never exceeds $6$ and never drops below $1$.
The extreme values $6$ and $1$ occur along the eigenvectors.

### L2 human

To find the largest eigenvalue of a symmetric matrix approximately:

1. Pick a few test vectors.
2. Compute the Rayleigh quotient of each. Every value is a lower bound for the largest eigenvalue.
3. Keep the largest value. Here $(3, 1)$ already gives $5.9$.

A trap: the quotient must divide by $x^T x$.
Without the division, $(2, 2)$ would give $44$, which is not an eigenvalue bound.
