---
tag: CPQB5HABC6
kind: example
name: The transpose is not the adjoint for a weighted inner product
msc: ["15A04", "47A05"]
topics: [3YM9EK6VMB]
audience: ug1
not_instance_of:
  - target: 0R9NMSM1ZP
    note: the map y -> A^T y is not the adjoint of x -> Ax for the inner product 2 x_1 y_1 + x_2 y_2, because the defining identity fails at x = (0, 1), y = (1, 0)
uses: [0ST8QF9T3T, 0VGSYBWHV2, E0KFAXMTC2]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_adjoint
    locator: Definition for bounded operators between Hilbert spaces
---

## Example

On $\mathbb{R}^2$, take the inner product $\ip{x}{y} = 2x_1 y_1 + x_2 y_2$.
Let $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $T(x) = Ax = (x_2, 0)$.
We show that the map $y \mapsto A^{\mathsf{T}} y$ is not the [[adjoint|0ST8QF9T3T]] of $T$ for this inner product, and we find the adjoint.

1. The form is an [[inner product|0VGSYBWHV2]]. It is bilinear and symmetric, and $\ip{x}{x} = 2x_1^2 + x_2^2 > 0$ for $x \neq 0$.
2. We test the identity at $x = (0, 1)$ and $y = (1, 0)$. Then $Tx = (1, 0)$ and $A^{\mathsf{T}} y = (0, 1)$, so
$$\ip{Tx}{y} = 2 \cdot 1 \cdot 1 + 0 \cdot 0 = 2, \qquad \ip{x}{A^{\mathsf{T}} y} = 2 \cdot 0 \cdot 0 + 1 \cdot 1 = 1.$$
3. Since $2 \neq 1$, the defining identity fails, and $y \mapsto A^{\mathsf{T}} y$ is not the adjoint of $T$.
4. We find the adjoint. For all $x$ and $y$, $\ip{Tx}{y} = 2 x_2 y_1$. We need $S(y) = (s_1, s_2)$ with $2 x_1 s_1 + x_2 s_2 = 2 x_2 y_1$ for all $x$.
5. Comparing the coefficients of $x_1$ and $x_2$ gives $s_1 = 0$ and $s_2 = 2y_1$. So $T^*(y_1, y_2) = (0, 2y_1)$, with the matrix $\begin{pmatrix} 0 & 0 \\ 2 & 0 \end{pmatrix}$.
6. Check at the same pair: $T^* y = (0, 2)$, and $\ip{x}{T^* y} = 1 \cdot 2 = 2$, which matches $\ip{Tx}{y} = 2$. By the [[uniqueness of the adjoint|E0KFAXMTC2]], this map is the adjoint.

## Remarks

The example shows that the adjoint depends on the inner product, not only on the map.
Write the inner product as $\ip{x}{y} = y^{\mathsf{T}} M x$ with $M = \operatorname{diag}(2, 1)$.
Then $\ip{Ax}{y} = y^{\mathsf{T}} M A x$ and $\ip{x}{Sy} = y^{\mathsf{T}} S^{\mathsf{T}} M x$, and these agree for all $x$ and $y$ exactly when $S^{\mathsf{T}} M = M A$, that is, $S = M^{-1} A^{\mathsf{T}} M$.
Check:
$$M^{-1} \left(A^{\mathsf{T}} M\right) = \begin{pmatrix} 1/2 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & 0 \\ 2 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 2 & 0 \end{pmatrix}.$$

If the weight $2$ changes to $1$, the inner product becomes the dot product, $M = I$, and the adjoint becomes $A^{\mathsf{T}}$ again.
A symmetric matrix need not give a self-adjoint map for a weighted inner product.
For $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ the same formula gives the adjoint $\begin{pmatrix} 0 & 1/2 \\ 2 & 0 \end{pmatrix}$, which is not the matrix itself.

## Explanations

### L1 human

The rule "adjoint equals transpose" is true for the usual dot product.
Here we count the first coordinate twice in the inner product.
With this new rule, the transpose no longer gives the same numbers on both sides.
For the vectors $(0, 1)$ and $(1, 0)$, one side gives $2$ and the other gives $1$.

### L2 human

Every inner product on $\mathbb{R}^n$ has the form $\ip{x}{y} = y^{\mathsf{T}} M x$ for a symmetric positive definite matrix $M$, and the computation in the remarks gives the adjoint $M^{-1} A^{\mathsf{T}} M$ of $x \mapsto Ax$.
Weighted inner products of this kind are common in statistics, where weights come from variances, and in mechanics, where the mass matrix gives the inner product of kinetic energy.
Watch out: "symmetric" and "self-adjoint" mean the same thing only for the dot product, or more generally only in an orthonormal basis.
