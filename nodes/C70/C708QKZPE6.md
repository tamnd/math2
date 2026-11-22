---
tag: C708QKZPE6
kind: statement
role: theorem
name: A matrix is similar to its transpose
aliases: [matrix-similar-to-its-transpose, similarity-of-a-matrix-and-its-transpose]
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: grad
about: [0E89HQATM8, 09DXWYRD43]
uses: [027KDW2K72, 0W809K6AW0, 0N28QN4CYA]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose
    locator: Properties
  - book: isbn:9780521839402
    locator: Chapter 3
---

## Statement

Flipping a square matrix over its diagonal gives the same linear map in another basis, and the change of basis can even be chosen symmetric.

Let $F$ be a field and $A \in M_n(F)$.
Then $A$ is [[similar|027KDW2K72]] over $F$ to its [[transpose|0W809K6AW0]] $A^{\mathsf T}$.
More precisely, there is an invertible [[symmetric matrix|0N28QN4CYA]] $T \in M_n(F)$ with $A^{\mathsf T} = T A T^{-1}$.

## Remarks

### A symmetric similarity for a companion matrix

The proof reduces everything to companion matrices, so here is one.
Take $p = x^3 - 2x^2 + 3x - 4$, with the column version
$$C = C(p) = \begin{pmatrix} 0 & 0 & 4 \\ 1 & 0 & -3 \\ 0 & 1 & 2 \end{pmatrix}.$$
The symmetric matrix that works is the Hankel matrix $S$ with entries $S_{ij} = \lambda(x^{i+j-2})$, where $\lambda$ reads off the coefficient of $x^2$ after reduction modulo $p$.
Reduction gives $x^3 \equiv 2x^2 - 3x + 4$ and $x^4 \equiv x^2 - 2x + 8$, so the values of $\lambda$ on $1, x, x^2, x^3, x^4$ are $0, 0, 1, 2, 1$, and
$$S = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 2 \\ 1 & 2 & 1 \end{pmatrix}, \qquad C^{\mathsf T} S = S C = \begin{pmatrix} 0 & 1 & 2 \\ 1 & 2 & 1 \\ 2 & 1 & 0 \end{pmatrix}.$$
Since $\det S = -1$, the matrix $S$ is invertible, and $C^{\mathsf T} = S C S^{-1}$ with $S$ symmetric.

### Why each hypothesis is needed

The only hypothesis is that the entries lie in a field, and the result holds over every field.
The statement fails for the conjugate transpose.
The $1 \times 1$ complex matrix $(i)$ is not similar to its conjugate transpose $(-i)$, because similar matrices have the same eigenvalues.

### What it gives you

The matrices $A$ and $A^{\mathsf T}$ have the same Jordan form, when it exists, and the same invariant factors.
For each eigenvalue $\lambda$ and each $k$, the kernels of $(A - \lambda I)^k$ and $(A^{\mathsf T} - \lambda I)^k$ have the same dimension.
A linear map $V \to V$ and its dual map $V^* \to V^*$ are similar, because their matrices in dual bases are transposes of each other.

The symmetric choice gives more.
From $TA = A^{\mathsf T} T$ and $T^{\mathsf T} = T$ we get $(TA)^{\mathsf T} = A^{\mathsf T} T = TA$, so $TA$ is symmetric.
So $A = T^{-1} (TA)$ is a product of two symmetric matrices, and the first factor is invertible.
In the example above, $C = S^{-1} (SC)$ with both $S^{-1}$ and $SC$ symmetric.

### Generalizations

For a cyclic matrix $A$ the symmetric matrix $T$ is unique up to a polynomial factor.
If $X A = A^{\mathsf T} X$, then $T^{-1} X$ commutes with $A$, so $T^{-1} X = f(A)$ for a polynomial $f$, by the [[theorem on centralizers|GXZGWZSJ2J]].
So every such $X$ is $T f(A)$, and every such $X$ is symmetric, since
$$(T f(A))^{\mathsf T} = f(A^{\mathsf T}) T = f(T A T^{-1}) T = T f(A).$$

### Watch out

The reversal matrix alone does not do the job for every matrix.
It turns each Jordan block into its transpose, but for the companion matrix $C$ above the reversal matrix $J$ gives
$$J C J = \begin{pmatrix} 2 & 1 & 0 \\ -3 & 0 & 1 \\ 4 & 0 & 0 \end{pmatrix} \ne C^{\mathsf T} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 4 & -3 & 2 \end{pmatrix}.$$
The correct symmetric matrix depends on the coefficients of $p$, as $S$ does.

## Explanations

### L1 human

Write a square matrix and flip it over its main diagonal, so that rows become columns.
The new matrix looks different, but it describes the same linear map seen in another basis.
For the $2 \times 2$ matrix with rows $(1, 1)$ and $(0, 1)$, the flipped matrix has rows $(1, 0)$ and $(1, 1)$.
Swapping the two basis vectors turns one into the other.

### L2 human

Here is a typical problem: find a symmetric $T$ with $A^{\mathsf T} = T A T^{-1}$ for $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
The transpose is $A^{\mathsf T} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$.
Try the swap $T = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, which is symmetric and satisfies $T^{-1} = T$.
Multiply both ways:
$$T A = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}, \qquad A^{\mathsf T} T = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}.$$
So $T A = A^{\mathsf T} T$, that is, $A^{\mathsf T} = T A T^{-1}$.
In the same way the reversal permutation matrix turns every Jordan block $J_k(\lambda)$ into its transpose.
The trap is the "Watch out" above: for a matrix that is not a single Jordan block, the reversal matrix is usually not enough.

### L3 human

The quickest proof of similarity uses the [[characteristic matrix|92VZF0QRM8]].
The matrix $xI - A^{\mathsf T}$ is $(xI - A)^{\mathsf T}$, and transposition keeps the set of minors, so the determinantal divisors agree.
The symmetric similarity comes from the companion matrix $C(p)$, which is the matrix of multiplication by $x$ on $F[x]/(p)$.
That map is self-adjoint for the symmetric bilinear form $(f, g) \mapsto \lambda(fg)$, where $\lambda$ takes the coefficient of $x^{n-1}$.
The Gram matrix of this form is a [[Hankel matrix|PQ1D8FQB3E]] with ones on the antidiagonal and zeros above it, as in the example.
