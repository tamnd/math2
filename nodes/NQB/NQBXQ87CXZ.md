---
tag: NQBXQ87CXZ
kind: example
name: The Cartesian decomposition of a 2 × 2 complex matrix
msc: ["15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [0P17NGQQMQ]
illustrates: [E2MNC3W2DM]
uses: [0EKZCX4K3P, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: Properties
---

## Example

We split a matrix that is neither Hermitian nor skew-Hermitian into a "real part" and an "imaginary part".
Let
$$A = \begin{pmatrix} 1 & 2 \\ 0 & i \end{pmatrix}, \qquad A^* = \begin{pmatrix} 1 & 0 \\ 2 & -i \end{pmatrix}.$$

1. Add the two matrices and halve:
$$H = \tfrac12 (A + A^*) = \tfrac12 \begin{pmatrix} 2 & 2 \\ 2 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}.$$
2. Subtract and divide by $2i$, using $1/(2i) = -i/2$:
$$K = \tfrac{1}{2i} (A - A^*) = -\tfrac{i}{2} \begin{pmatrix} 0 & 2 \\ -2 & 2i \end{pmatrix} = \begin{pmatrix} 0 & -i \\ i & 1 \end{pmatrix}.$$
3. The matrix $H$ is real and symmetric, so $H^* = H$ and $H$ is [[Hermitian|0EKZCX4K3P]].
4. Conjugate and transpose $K$: the entry $-i$ in position $(1, 2)$ becomes $i$ in position $(2, 1)$, and the entry $i$ becomes $-i$ in position $(1, 2)$. So $K^* = K$, and $K$ is Hermitian.
5. Recombine: $iK = \begin{pmatrix} 0 & 1 \\ -1 & i \end{pmatrix}$, so
$$H + iK = \begin{pmatrix} 1 + 0 & 1 + 1 \\ 1 - 1 & 0 + i \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & i \end{pmatrix} = A.$$

## Remarks

The matrix $iK$ is skew-Hermitian, so $A = H + iK$ is also the split of $A$ into a Hermitian part and a skew-Hermitian part.
By the [[Cartesian decomposition theorem|E2MNC3W2DM]], no other pair of Hermitian matrices gives $A$.

The two parts do not commute:
$$HK = \begin{pmatrix} i & 1 - i \\ 0 & -i \end{pmatrix}, \qquad KH = \begin{pmatrix} -i & 0 \\ 1 + i & i \end{pmatrix}.$$
So $A$ is not [[normal|0MR0BYF0K2]].
Check: $A^* A = \begin{pmatrix} 1 & 2 \\ 2 & 5 \end{pmatrix}$ and $A A^* = \begin{pmatrix} 5 & -2i \\ 2i & 1 \end{pmatrix}$ differ.

If we change the entry $2$ of $A$ to $0$, then $A = \operatorname{diag}(1, i)$, the parts become $H = \operatorname{diag}(1, 0)$ and $K = \operatorname{diag}(0, 1)$, and these commute, as they must for a normal matrix.

## Explanations

### L1 human

Every complex number is a real part plus $i$ times an imaginary part.
Here the matrix $A$ is written the same way, with Hermitian matrices in the role of real numbers.
The real part $H$ is the average of $A$ and $A^*$, and the imaginary part $K$ comes from their difference.

### L2 human

The recipe has two steps: compute $A^*$, then form $(A + A^*)/2$ and $(A - A^*)/(2i)$.
Watch out for the factor $1/(2i)$, which equals $-i/2$ and not $i/2$.
With $i/2$ you would get $-K$, and then $H + i(-K) = A^*$, not $A$.
