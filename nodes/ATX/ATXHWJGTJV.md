---
tag: ATXHWJGTJV
kind: example
name: Similar matrices are conjugate in GL2(R)
msc: ["20E45"]
topics: [E1506A5A55]
audience: ug1
instance_of: [0DXD4QSZ8A]
illustrates: [0E89HQATM8]
uses: [0FCHE902D7, 0NRYHJPQG2, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_similarity
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Conjugacy_class
    locator: Examples
---

## Example

Let $G = \mathrm{GL}_2(\mathbb{R})$ be the [[general linear group|0FCHE902D7]] of invertible real $2 \times 2$ matrices.
Let
$$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}, \qquad P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.$$
We show that $A$ and $B$ are [[conjugate|0DXD4QSZ8A]] in $G$, and that the conjugation is a change of basis.

1. $\det A = 1$, $\det B = 1$ and $\det P = -1$. So the three matrices are invertible, and they are elements of $G$.
2. $P^2 = I$, so $P^{-1} = P$.
3. $PA = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$, because $P$ swaps the two rows of $A$.
4. $(PA)P = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = B$, because $P$ on the right swaps the two columns.
5. So $PAP^{-1} = B$, and $A$ and $B$ are conjugate in $G$.

Now we read the same computation as a change of basis.

6. Let $T \colon \mathbb{R}^2 \to \mathbb{R}^2$ be the [[linear map|0NRYHJPQG2]] $T(x, y) = (x + y, y)$. Let $e_1 = (1, 0)$ and $e_2 = (0, 1)$.
7. $T(e_1) = e_1$ and $T(e_2) = e_1 + e_2$. So the matrix of $T$ in the basis $(e_1, e_2)$ is $A$.
8. Take the new basis $(f_1, f_2) = (e_2, e_1)$. Then $T(f_1) = f_1 + f_2$ and $T(f_2) = f_2$.
9. So the matrix of $T$ in the basis $(f_1, f_2)$ is $B$.
10. The columns of $P$ are the new basis vectors $f_1$ and $f_2$. The general rule gives the new matrix $P^{-1}AP$, and here $P^{-1}AP = PAP^{-1} = B$.

## Remarks

The general rule is as follows.
Let $Q$ be the invertible matrix whose columns are the vectors of a new basis.
If $A$ is the matrix of a linear map in the standard basis, then $Q^{-1}AQ$ is its matrix in the new basis.
With $g = Q^{-1}$ this is $gAg^{-1}$, so a change of basis is a conjugation in $\mathrm{GL}_n$.
Conversely, each conjugate $gAg^{-1}$ is the matrix of the same map in the basis given by the columns of $g^{-1}$.
Thus two matrices in $\mathrm{GL}_n(F)$ are conjugate exactly when they are [[similar|0E89HQATM8]].
Conjugate matrices have the same [[determinant|00KDZRW4C0]], the same trace and the same eigenvalues, because these numbers depend only on the linear map.
Here both $A$ and $B$ have determinant $1$, trace $2$ and the single eigenvalue $1$.

## Explanations

### L1 human

A matrix is a way to write down a linear map with numbers.
The numbers depend on the coordinate axes that we choose.
Here the map $T$ pushes each point to the right by its height.
If we swap the names of the two axes, the same map gets a different matrix.
The two matrices are conjugate because they describe the same map.

### L2 human

The left and right conventions for a change of basis are a common source of errors.
The formula $Q^{-1}AQ$ uses a matrix $Q$ whose columns are the new basis vectors.
Some books write the formula as $PAP^{-1}$ with $P = Q^{-1}$.
Both formulas describe conjugation, so the set of matrices similar to $A$ is the same.
In this example $P = P^{-1}$, so the two conventions give the same matrix $B$.
To test a claim that two matrices are not conjugate, compare the determinant, the trace or the eigenvalues.
If one of them differs, the matrices are not conjugate.
If all of them agree, the matrices can still fail to be conjugate: $I$ and $A$ are an example, because $gIg^{-1} = I$ for each $g$.
