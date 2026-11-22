---
tag: RNZ6YSRZWP
kind: example
name: A rank one update of a 3 × 3 inverse by the Sherman-Morrison formula
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: ug2
instance_of: [0EB9N0S33C]
uses: [MDZDEFE53C, 032Q9FB8MT, 0Q9PGXD9E4]
sources:
  - url: https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula
---

## Example

Adding a rank one matrix to a diagonal matrix gives a matrix whose inverse the Sherman-Morrison formula finds with one division and no elimination.
Let $A = \operatorname{diag}(2, 1, 1)$ over $\mathbb{Q}$, $u = (1, 1, 0)^{\mathsf{T}}$ and $v = (1, 0, 1)^{\mathsf{T}}$.
Then
$$B = A + uv^{\mathsf{T}} = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} + \begin{pmatrix} 1 & 0 & 1 \\ 1 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 3 & 0 & 1 \\ 1 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}.$$

1. $A$ is [[diagonal|0Q9PGXD9E4]], so $A^{-1} = \operatorname{diag}(1/2, 1, 1)$.
2. $A^{-1}u = (1/2, 1, 0)^{\mathsf{T}}$ and $v^{\mathsf{T}}A^{-1} = (1/2, 0, 1)$.
3. $1 + v^{\mathsf{T}}A^{-1}u = 1 + (1 \cdot \tfrac12 + 0 \cdot 1 + 1 \cdot 0) = 3/2$. This is nonzero, so $B$ is invertible, by the [[Sherman-Morrison formula|MDZDEFE53C]].
4. The correction is the outer product divided by $3/2$:
$$\frac{2}{3} \begin{pmatrix} 1/2 \\ 1 \\ 0 \end{pmatrix}(1/2, 0, 1) = \frac{2}{3} \begin{pmatrix} 1/4 & 0 & 1/2 \\ 1/2 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 1/6 & 0 & 1/3 \\ 1/3 & 0 & 2/3 \\ 0 & 0 & 0 \end{pmatrix}.$$
5. Subtract it from $A^{-1}$:
$$B^{-1} = \begin{pmatrix} 1/3 & 0 & -1/3 \\ -1/3 & 1 & -2/3 \\ 0 & 0 & 1 \end{pmatrix}.$$

Check: row 1 of $B$ times $B^{-1}$ is $(3 \cdot \tfrac13,\ 0,\ -1 + 1) = (1, 0, 0)$, row 2 gives $(\tfrac13 - \tfrac13,\ 1,\ -\tfrac13 - \tfrac23 + 1) = (0, 1, 0)$, and row 3 gives $(0, 0, 1)$.

Now update a solution, with $b = (4, 3, 1)^{\mathsf{T}}$.
Here $y = A^{-1}b = (2, 3, 1)^{\mathsf{T}}$ and $z = A^{-1}u = (1/2, 1, 0)^{\mathsf{T}}$, so $v^{\mathsf{T}}y = 2 + 1 = 3$ and $1 + v^{\mathsf{T}}z = 3/2$.
Then
$$x = y - \frac{3}{3/2}\, z = y - 2z = (1, 1, 1)^{\mathsf{T}}.$$
Check: $Bx$ is the vector of row sums of $B$, which is $(4, 3, 1)^{\mathsf{T}} = b$.

## Remarks

### What the update saved

The update used only products with $A^{-1}$ and one division, and no new elimination.
For a large $n$, with $A^{-1}$ known, this costs about $n^2$ operations, while a new inversion costs about $n^3$.
The [[matrix determinant lemma|0BC3Q6K92H]] gives $\det B = \tfrac32 \det A = \tfrac32 \cdot 2 = 3$.
Check: expansion along row 3 gives $\det B = 1 \cdot \det \begin{pmatrix} 3 & 0 \\ 1 & 1 \end{pmatrix} = 3$.

### Watch out

The denominator $1 + v^{\mathsf{T}}A^{-1}u$ is the test for invertibility.
If $v$ were $(-2, 0, 0)^{\mathsf{T}}$, the denominator would be $1 - 2 \cdot \tfrac12 = 0$.
Then
$$B = A + uv^{\mathsf{T}} = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} + \begin{pmatrix} -2 & 0 & 0 \\ -2 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 \\ -2 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix},$$
whose first row is zero, so $B$ is singular, as the test predicts.

### Try it

Use the formula to invert $I_2 + uv^{\mathsf{T}}$ for $u = (1, 1)^{\mathsf{T}}$ and $v = (1, 0)^{\mathsf{T}}$.
Answer: the denominator is $1 + v^{\mathsf{T}}u = 2$, and
$$(I_2 + uv^{\mathsf{T}})^{-1} = I_2 - \tfrac12 \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1/2 & 0 \\ -1/2 & 1 \end{pmatrix}.$$
Check: $I_2 + uv^{\mathsf{T}} = \begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix}$, and $\begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1/2 & 0 \\ -1/2 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 1/2 - 1/2 & 1 \end{pmatrix} = I_2$.

## Explanations

### L1 human

We change a simple diagonal matrix by adding a rank one matrix.
Instead of inverting the new matrix from scratch, we correct the old inverse.
The correction is one outer product divided by the number $3/2$.

### L2 human

Compute in the order $A^{-1}u$, then $v^{\mathsf{T}}A^{-1}$, then the denominator, then the outer product.
Each step is a product with the diagonal matrix $A^{-1}$, so each costs a few multiplications.
