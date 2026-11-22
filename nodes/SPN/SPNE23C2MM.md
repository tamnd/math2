---
tag: SPNE23C2MM
kind: example
name: A polynomial in a symmetric 2 by 2 matrix
msc: ["15A18", "15A24"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [0E3MV6E6MG]
illustrates: [F2S8WGVARA, 0F765KFC2J]
uses: [0BNEXSKNRV, F2S8WGVARA, 0ZND7NQ970]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Additional properties
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Example

Let $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and $p(x) = x^2 - 4x$.
We compute the [[value p(A)|0BNEXSKNRV]] and compare its eigenvalues with the values of $p$ at the eigenvalues of $A$.

1. Square the matrix, row times column:
$$A^2 = \begin{pmatrix} 2 \cdot 2 + 1 \cdot 1 & 2 \cdot 1 + 1 \cdot 2 \\ 1 \cdot 2 + 2 \cdot 1 & 1 \cdot 1 + 2 \cdot 2 \end{pmatrix} = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}.$$
2. Subtract $4A$:
$$p(A) = A^2 - 4A = \begin{pmatrix} 5 - 8 & 4 - 4 \\ 4 - 4 & 5 - 8 \end{pmatrix} = \begin{pmatrix} -3 & 0 \\ 0 & -3 \end{pmatrix} = -3I.$$
3. The [[eigenvalues|0ZND7NQ970]] of $A$ are $1$ and $3$, with the eigenvectors $(1, -1)^{\mathsf{T}}$ and $(1, 1)^{\mathsf{T}}$.
   Check: $A(1, -1)^{\mathsf{T}} = (1, -1)^{\mathsf{T}}$ and $A(1, 1)^{\mathsf{T}} = (3, 3)^{\mathsf{T}}$.
4. The values of $p$ at these eigenvalues are $p(1) = 1 - 4 = -3$ and $p(3) = 9 - 12 = -3$.
5. On the eigenvectors, $p(A)(1, -1)^{\mathsf{T}} = (-3, 3)^{\mathsf{T}} = p(1)(1, -1)^{\mathsf{T}}$ and $p(A)(1, 1)^{\mathsf{T}} = (-3, -3)^{\mathsf{T}} = p(3)(1, 1)^{\mathsf{T}}$.
6. So the only eigenvalue of $p(A) = -3I$ is $-3 = p(1) = p(3)$, as the theorem on the [[eigenvalues of a polynomial in an endomorphism|F2S8WGVARA]] predicts.

## Remarks

Step 2 says $A^2 - 4A + 3I = 0$.
The [[characteristic polynomial|0VSSPAFM2C]] of $A$ is $t^2 - 4t + 3$, since $\operatorname{tr} A = 4$ and $\det A = 3$, so step 2 is the [[Cayley-Hamilton theorem|0F765KFC2J]] for $A$.
That is why $p$ takes the same value at both eigenvalues: $p(x) + 3$ is the characteristic polynomial, and it vanishes at $1$ and at $3$.

The example also shows that two different eigenvalues of $A$ can merge into one eigenvalue of $p(A)$, here $-3$ with multiplicity $2$.
Then $p(A)$ has more eigenvectors than $A$: every nonzero vector is an eigenvector of $-3I$, but $(1, 0)^{\mathsf{T}}$ is not an eigenvector of $A$.
Change $p$ to $q(x) = x^2$, and the values $q(1) = 1$ and $q(3) = 9$ stay apart.
Then $A^2 = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}$ has the same two eigenvectors as $A$ and no others, up to scaling.

## Explanations

### L1 human

If a matrix stretches a direction by $\lambda$, then its square stretches it by $\lambda^2$.
So a polynomial in the matrix stretches that direction by the same polynomial of $\lambda$.
Here the polynomial $x^2 - 4x$ gives $-3$ for both stretch factors $1$ and $3$.
So $p(A)$ multiplies every vector by $-3$.

### L2 human

The typical use is to find the eigenvalues of $p(A)$ from those of $A$, without computing $p(A)$: here $p(1)$ and $p(3)$ were enough.
Computing $p(A)$ directly, as in steps 1 and 2, is a good check on the arithmetic.
Watch out: do not expect $p(A)$ to have only the eigenvectors of $A$, because when $p(\lambda) = p(\mu)$ the two eigenspaces merge into one larger eigenspace.
