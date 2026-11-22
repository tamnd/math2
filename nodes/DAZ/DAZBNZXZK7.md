---
tag: DAZBNZXZK7
kind: example
name: A complex symmetric matrix that is not Hermitian
msc: ["15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
not_instance_of:
  - target: 0P17NGQQMQ
    note: "the matrix (1, i; i, 1) equals its transpose, but its conjugate transpose is (1, -i; -i, 1), and its eigenvalues 1 + i and 1 - i are not real"
uses: [0EKZCX4K3P, 0N28QN4CYA]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: Properties
---

## Example

Over the complex numbers, being symmetric and being Hermitian are different conditions.
Let
$$A = \begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}.$$

1. Transpose: the two entries off the diagonal are both $i$, so $A^{\mathsf{T}} = A$ and $A$ is [[symmetric|0N28QN4CYA]].
2. Conjugate transpose: conjugating turns each $i$ into $-i$, so
$$A^* = \begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix}.$$
The entry $(1, 2)$ of $A^*$ is $-i$, and that of $A$ is $i$, so $A^* \neq A$ and $A$ is not [[Hermitian|0EKZCX4K3P]].
3. The characteristic polynomial is
$$(t - 1)^2 - i \cdot i = (t - 1)^2 + 1,$$
so the eigenvalues are $1 + i$ and $1 - i$.
4. A Hermitian matrix has only real eigenvalues, so step 3 confirms in a second way that $A$ is not Hermitian.

## Remarks

The [[Cartesian decomposition|E2MNC3W2DM]] of $A$ is $A = I + iB$ with $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, so its Hermitian part is $H = I$ and $K = B$.
The non-real eigenvalues come from the nonzero part $K$.

If you replace the lower entry $i$ by $-i$, you get $\begin{pmatrix} 1 & i \\ -i & 1 \end{pmatrix}$, which is Hermitian and not symmetric.
Its characteristic polynomial is $(t - 1)^2 - 1$, with the real roots $0$ and $2$.
For a real matrix the two conditions agree, since conjugation does nothing.

## Explanations

### L1 human

For real matrices, a mirror image across the diagonal is enough to be Hermitian.
For complex matrices the mirror image must also flip the sign of each imaginary part.
Here both mirror entries are $i$, so the sign does not flip, and the test fails.

### L2 human

To test whether a complex matrix is Hermitian, compare each entry $a_{ij}$ with $\overline{a_{ji}}$, not with $a_{ji}$.
Watch out: many results about real symmetric matrices, such as real eigenvalues, do not hold for complex symmetric matrices.
Over $\mathbb{C}$, the Hermitian condition is the one that carries those results.
