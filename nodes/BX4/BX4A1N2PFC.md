---
tag: BX4A1N2PFC
kind: example
name: Counting diagonal entries gives the algebraic multiplicity
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
not_instance_of:
  - target: 099TWVJ909
    note: The number of times 1 appears on the diagonal of the shear is 2, which is its algebraic multiplicity, while its geometric multiplicity is 1
uses: [06YSJVR356, 0S7A0EMPF4, 0W4FSW1TVB]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenspaces, geometric multiplicities, and eigenbasis for a matrix
---

## Example

Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ be the [[shear|HTAWRAC3QE]] of the plane.
We count the entries $1$ on its diagonal and compare that count with the dimension of the eigenspace for $1$.

1. The matrix is upper triangular, so $tI - A$ is upper triangular with diagonal $t - 1, t - 1$, and
$$p_A(t) = (t - 1)^2.$$
   The [[algebraic multiplicity|0S7A0EMPF4]] of $1$ is $2$, which is the number of diagonal entries equal to $1$.
2. Subtract the identity:
$$A - I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix},$$
   a matrix of rank $1$, since its one nonzero row is $(0, 1)$.
3. By the [[rank-nullity theorem|0W4FSW1TVB]], $\dim \ker(A - I) = 2 - 1 = 1$.
   So the [[geometric multiplicity|06YSJVR356]] of $1$ is $1$, and the kernel is the line spanned by $(1, 0)$.
4. Check: $A(1, 0) = (1, 0)$, while $A(0, 1) = (1, 1)$, which is not a multiple of $(0, 1)$.
5. So the diagonal count $2$ is not the geometric multiplicity $1$.

## Remarks

For a triangular matrix, counting the diagonal entries equal to $\lambda$ always gives the algebraic multiplicity, because $\det(tI - A)$ is the product of the diagonal entries of $tI - A$.
The geometric multiplicity needs a rank computation, $n - \operatorname{rank}(A - \lambda I)$, and it can be smaller.

Change the corner entry from $1$ to $0$, and $A$ becomes $I$.
Then $A - I = 0$ has rank $0$, the eigenspace is the whole plane, and the two counts agree at $2$.
For every diagonal matrix the two counts agree, since each standard basis vector with diagonal entry $\lambda$ is an eigenvector for $\lambda$.
The corner entry of the shear is what breaks the second eigenvector.

## Explanations

### L1 human

The diagonal of the shear shows the number $1$ twice, so the eigenvalue $1$ is a double root.
But the shear slides every point sideways, and only the arrows along the horizontal axis keep their direction.
So there is only one line of eigenvectors.
The diagonal count gives the algebraic multiplicity, not the number of independent eigenvectors.

### L2 human

The lesson is to compute the geometric multiplicity from the rank of $A - \lambda I$ and never from the diagonal.
For $\begin{pmatrix} 3 & 2 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{pmatrix}$, the diagonal gives $a(3) = 3$.
The matrix $A - 3I$ has the single nonzero row $(0, 2, 0)$, so its rank is $1$ and $g(3) = 3 - 1 = 2$.
Watch out: a triangular matrix shows its eigenvalues, but it need not be diagonalizable, and this one is not, since $2 < 3$.
