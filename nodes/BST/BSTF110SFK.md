---
tag: BSTF110SFK
kind: example
name: A polynomial in a matrix commutes with the matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [8G3X8MPG7E]
uses: [MX26N71ZD3, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Commuting_matrices
    locator: Examples
---

## Example

Let
$$A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$$
over $\mathbb{R}$, and let $p(x) = x^2 + 1$, so that $p(A) = A^2 + I$.
We compute $p(A)$ and check that it commutes with $A$.

1. Square the matrix:
$$A^2 = \begin{pmatrix} 1 \cdot 1 + 1 \cdot 0 & 1 \cdot 1 + 1 \cdot 2 \\ 0 \cdot 1 + 2 \cdot 0 & 0 \cdot 1 + 2 \cdot 2 \end{pmatrix} = \begin{pmatrix} 1 & 3 \\ 0 & 4 \end{pmatrix}.$$
2. Add the identity: $p(A) = A^2 + I = \begin{pmatrix} 2 & 3 \\ 0 & 5 \end{pmatrix}$.
3. Multiply in the first order:
$$A \, p(A) = \begin{pmatrix} 1 \cdot 2 + 1 \cdot 0 & 1 \cdot 3 + 1 \cdot 5 \\ 0 \cdot 2 + 2 \cdot 0 & 0 \cdot 3 + 2 \cdot 5 \end{pmatrix} = \begin{pmatrix} 2 & 8 \\ 0 & 10 \end{pmatrix}.$$
4. Multiply in the other order:
$$p(A) \, A = \begin{pmatrix} 2 \cdot 1 + 3 \cdot 0 & 2 \cdot 1 + 3 \cdot 2 \\ 0 \cdot 1 + 5 \cdot 0 & 0 \cdot 1 + 5 \cdot 2 \end{pmatrix} = \begin{pmatrix} 2 & 8 \\ 0 & 10 \end{pmatrix}.$$
5. The two products agree in all four entries, so $A$ and $p(A)$ [[commute|MX26N71ZD3]].

## Remarks

The same holds for every polynomial $p$ and every square matrix $A$.
The reason is $A \cdot A^j = A^{j + 1} = A^j \cdot A$ for each $j$, and the distributive law extends this to sums of multiples of powers.
So the polynomials in $A$ form a commutative subring of the matrix ring, and any two of them commute with each other as well.

Here $p(A)$ is not a multiple of $I$, so the example is not the case of a scalar matrix in disguise.
Since $A$ has the two different eigenvalues $1$ and $2$, the converse also holds for this $A$: every matrix that commutes with $A$ is a polynomial in $A$, in fact of the form $aI + bA$.
For instance, $p(A) = 3A - I$, since $3A - I = \begin{pmatrix} 2 & 3 \\ 0 & 5 \end{pmatrix}$.

## Explanations

### L1 human

A matrix and its own powers can be multiplied in either order, because both orders give a higher power of the same matrix.
So a matrix commutes with every sum of its powers, such as $A^2 + I$.

### L2 human

The identity $p(A) = 3A - I$ from the Remarks comes from the $2 \times 2$ rule $A^2 = (\operatorname{tr} A) A - (\det A) I$.
Here $\operatorname{tr} A = 3$ and $\det A = 2$, so $A^2 = 3A - 2I$ and $A^2 + I = 3A - I$.
Watch out: a matrix that commutes with $A$ need not be a polynomial in $A$ in general; for $A = I$ every matrix commutes with $A$, but only the scalar matrices are polynomials in $I$.
