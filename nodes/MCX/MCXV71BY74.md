---
tag: MCXV71BY74
kind: statement
role: theorem
name: Eigenvalues of AB and BA
aliases: [characteristic-polynomials-of-ab-and-ba]
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
about: [0VSSPAFM2C, 0BQAA2BK3Q]
uses: [039HF58KQ5, 0ZND7NQ970, 0S7A0EMPF4, 06YSJVR356]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Characteristic polynomial of a product of two matrices
  - url: https://en.wikipedia.org/wiki/Sylvester%27s_determinant_theorem
    locator: lead section
---

## Statement

The two products $AB$ and $BA$ can be different matrices, even of different sizes, but they have the same nonzero eigenvalues with the same multiplicities.

Let $K$ be a commutative ring, let $A$ be an $m \times n$ matrix and let $B$ be an $n \times m$ matrix over $K$.

1. The [[characteristic polynomials|039HF58KQ5]] of the square matrices $AB$ (of size $m$) and $BA$ (of size $n$) satisfy
$$x^n \, p_{AB}(x) = x^m \, p_{BA}(x) \quad \text{in } K[x].$$
2. If $m = n$, then $p_{AB} = p_{BA}$.

Now let $K = F$ be a field.

3. $AB$ and $BA$ have the same nonzero [[eigenvalues|0BQAA2BK3Q]] in $F$, with the same [[algebraic multiplicities|0FY42N02DV]].
4. For each $\lambda \ne 0$, the eigenspaces $E_\lambda(AB) \subseteq F^m$ and $E_\lambda(BA) \subseteq F^n$ have the same dimension, and $v \mapsto Bv$ is an isomorphism from the first onto the second.

## Remarks

### A row times a column

Take $A = \begin{pmatrix} 1 & 2 \end{pmatrix}$, so $m = 1$, and $B = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$, so $n = 2$.
One product is a number and the other is a $2 \times 2$ matrix:
$$AB = \begin{pmatrix} 11 \end{pmatrix}, \qquad BA = \begin{pmatrix} 3 & 6 \\ 4 & 8 \end{pmatrix}.$$
The matrix $BA$ has trace $11$ and determinant $24 - 24 = 0$, so $p_{BA}(x) = x^2 - 11x = x(x - 11)$, while $p_{AB}(x) = x - 11$.
Part 1 reads $x^2 (x - 11) = x \cdot x(x - 11)$, which is true.
The nonzero eigenvalue $11$ is shared, and the larger product only gains the eigenvalue $0$.
The [[proof by two block products|2WW2DQYK7P]] handles the general case.

### Why the eigenvalue 0 is excluded

Parts 3 and 4 say nothing about $\lambda = 0$, and they would be false for it.
In the example above, $0$ is an eigenvalue of $BA$ but not of $AB$.
Even for square matrices the eigenspaces of $0$ can differ.
Take
$$A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \quad AB = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}, \quad BA = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}.$$
Both products have the characteristic polynomial $x^2$, as part 2 says, but $\dim E_0(AB) = 2$ and $\dim E_0(BA) = 1$.
The map $v \mapsto Bv$ fails here because it can send an eigenvector for $0$ to the zero vector.

### What it gives you

For square $A$ and $B$, part 2 gives $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ and $\det(AB) = \det(BA)$, because the trace and the determinant are coefficients of the characteristic polynomial, up to sign.
If $A$ is invertible, then $BA = A^{-1}(AB)A$ is similar to $AB$, and part 2 extends the equality of characteristic polynomials to every square $A$.
The second example above shows that $AB$ and $BA$ need not be [[similar|0E89HQATM8]], because the zero matrix is similar only to itself.

The identity also saves work.
To find the nonzero eigenvalues of a large product $BA$, compute the small product $AB$ instead.
For a column $u$ and a row $w$ of length $n$, the $n \times n$ matrix $uw$ has the single possible nonzero eigenvalue $wu$, the $1 \times 1$ product.

### Generalizations

Put $x = -1$ in part 1 and multiply out the signs.
The result is the [[Weinstein-Aronszajn identity|0G24VQ1088]], also called Sylvester's determinant theorem:
$$\det(I_m + AB) = \det(I_n + BA).$$
For bounded operators $S$ and $T$ on a Banach space the same idea gives $\sigma(ST) \cup \{0\} = \sigma(TS) \cup \{0\}$, a fact of [[spectral theory|XXXSST2DR5]].

## History

The determinant identity $\det(I_m + AB) = \det(I_n + BA)$ carries the name of James Joseph Sylvester, and in perturbation theory it carries the names of Weinstein and Aronszajn.

## Explanations

### L1 human

A row of numbers times a column of numbers gives one number.
The same column times the same row gives a whole square table.
The two results look very different, yet they share their nonzero eigenvalue.
For the row $(1, 2)$ and the column $(3, 4)$, the number is $11$, and the table has the eigenvalues $11$ and $0$.
In general, only the eigenvalue $0$ can appear more often in the larger product.

### L2 human

Here is a typical check of part 4, with the matrices of the first example.
The eigenspace of $AB = (11)$ for $11$ is all of $F^1$, spanned by $v = 1$.
The theorem says that $Bv$ is an eigenvector of $BA$ for $11$, and $Bv$ is the column $(3, 4)^{\mathsf{T}}$ itself.
Check:
$$BA \begin{pmatrix} 3 \\ 4 \end{pmatrix} = \begin{pmatrix} 3 \cdot 3 + 6 \cdot 4 \\ 4 \cdot 3 + 8 \cdot 4 \end{pmatrix} = \begin{pmatrix} 33 \\ 44 \end{pmatrix} = 11 \begin{pmatrix} 3 \\ 4 \end{pmatrix}.$$
The reason is one line: $(BA)(Bv) = B(AB)v = B(11 v) = 11\, Bv$.
Watch out: the theorem does not say that $AB$ and $BA$ are similar, or even that they have the same size.

### L3 human

The identity of part 1 holds over the polynomial ring $\mathbb{Z}[a_{ij}, b_{jk}]$ in independent variables, so it is a polynomial identity, and it then holds over every commutative ring by substitution.
For $m = n$, one proof uses density: for invertible $A$ the products are similar, and the invertible matrices are Zariski dense in the space of all matrices.
For a real $m \times n$ matrix $A$, the theorem applied to $A^{\mathsf{T}}$ and $A$ shows that $A^{\mathsf{T}} A$ and $A A^{\mathsf{T}}$ have the same nonzero eigenvalues.
These are the squares of the nonzero singular values of $A$, a theme of the later sub-area on positive operators and singular values.
