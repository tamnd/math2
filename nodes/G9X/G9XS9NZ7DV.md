---
tag: G9XS9NZ7DV
kind: example
name: The transpose of the inverse of a 2 × 2 matrix
msc: ["15A99", "15A09"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [09DXWYRD43]
uses: [0W809K6AW0, 09GK5PS824, 0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose
    locator: Properties
---

## Example

Let
$$A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}, \qquad C = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$$
over $\mathbb{R}$.
We check that $C$ is the inverse of $A$, and that $C^{\mathsf{T}}$ is the inverse of $A^{\mathsf{T}}$.

1. Multiply in both orders:
$$AC = \begin{pmatrix} 6 - 5 & -2 + 2 \\ 15 - 15 & -5 + 6 \end{pmatrix} = I, \qquad CA = \begin{pmatrix} 6 - 5 & 3 - 3 \\ -10 + 10 & -5 + 6 \end{pmatrix} = I.$$
So $A$ is [[invertible|0EB9N0S33C]] and $A^{-1} = C$.
2. By the [[definition|0W809K6AW0]], the transposes are
$$A^{\mathsf{T}} = \begin{pmatrix} 2 & 5 \\ 1 & 3 \end{pmatrix}, \qquad C^{\mathsf{T}} = \begin{pmatrix} 3 & -5 \\ -1 & 2 \end{pmatrix}.$$
3. Multiply them:
$$A^{\mathsf{T}} C^{\mathsf{T}} = \begin{pmatrix} 6 - 5 & -10 + 10 \\ 3 - 3 & -5 + 6 \end{pmatrix} = I.$$
For square matrices over a field a one-sided inverse is two-sided, and the product $C^{\mathsf{T}} A^{\mathsf{T}}$ is $(AC)^{\mathsf{T}} = I$ as well.
4. So $(A^{\mathsf{T}})^{-1} = C^{\mathsf{T}} = (A^{-1})^{\mathsf{T}}$.

## Remarks

The numbers follow a general argument.
By the [[transpose of a product|09GK5PS824]],
$$A^{\mathsf{T}} (A^{-1})^{\mathsf{T}} = (A^{-1} A)^{\mathsf{T}} = I^{\mathsf{T}} = I, \qquad (A^{-1})^{\mathsf{T}} A^{\mathsf{T}} = (A A^{-1})^{\mathsf{T}} = I.$$
So for every invertible matrix over a commutative ring, the inverse of the transpose is the transpose of the inverse, and some books write $A^{-\mathsf{T}}$ for both.

The example also fits the formula for $2 \times 2$ inverses.
Here $\det A = 2 \cdot 3 - 1 \cdot 5 = 1$, and $A^{\mathsf{T}}$ has the same determinant, as the [[determinant of the transpose|0ZZQ2E1MTE]] says.
If we change the entry $5$ to $6$, then $\det A = 0$, and neither $A$ nor $A^{\mathsf{T}}$ has an inverse.

## Explanations

### L1 human

To find the inverse of the transpose, you can transpose the inverse.
Here the inverse of $A$ is $C$, and flipping $C$ across its diagonal gives the inverse of the flipped $A$.
The product in step 3 is the identity, which confirms it.

### L2 human

The typical use is to save work: when you know $A^{-1}$, you know $(A^{\mathsf{T}})^{-1}$ without a new computation.
The reason is that the transpose reverses the order of a product, so the equations $A^{-1} A = I$ and $A A^{-1} = I$ turn into the two equations that define the inverse of $A^{\mathsf{T}}$.
Watch out: the reversal matters, and the formula $(AB)^{-1} = B^{-1} A^{-1}$ reverses the order in the same way.
