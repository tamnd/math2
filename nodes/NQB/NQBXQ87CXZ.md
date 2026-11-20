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

Let $A = \begin{pmatrix} 1 & 2 \\ 0 & i \end{pmatrix}$, so $A^* = \begin{pmatrix} 1 & 0 \\ 2 & -i \end{pmatrix}$.

1. $A + A^* = \begin{pmatrix} 2 & 2 \\ 2 & 0 \end{pmatrix}$, so $H = \tfrac12 (A + A^*) = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.
2. $A - A^* = \begin{pmatrix} 0 & 2 \\ -2 & 2i \end{pmatrix}$, so $K = \tfrac{1}{2i} (A - A^*) = \begin{pmatrix} 0 & -i \\ i & 1 \end{pmatrix}$, using $1/i = -i$.
3. $H$ is real symmetric, so it is [[Hermitian|0EKZCX4K3P]].
4. $K^* = \begin{pmatrix} 0 & \overline{i} \\ \overline{-i} & 1 \end{pmatrix} = \begin{pmatrix} 0 & -i \\ i & 1 \end{pmatrix} = K$, so $K$ is Hermitian.
5. $iK = \begin{pmatrix} 0 & 1 \\ -1 & i \end{pmatrix}$, and $H + iK = \begin{pmatrix} 1 + 0 & 1 + 1 \\ 1 - 1 & 0 + i \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & i \end{pmatrix} = A$.

## Remarks

The matrix $iK$ is skew-Hermitian, so $A = H + iK$ is also the split into Hermitian and skew-Hermitian parts.
$HK = \begin{pmatrix} i & -i + 1 \\ 0 & -i \end{pmatrix}$ and $KH = \begin{pmatrix} -i & 0 \\ i + 1 & i \end{pmatrix}$ are different.
So $A$ is not [[normal|0MR0BYF0K2]], in line with the [[theorem|E2MNC3W2DM]].

## Explanations

### L1 human

The matrix $H$ is the "real part" of $A$ and $K$ is the "imaginary part".
Both are Hermitian, and $H + iK$ gives back $A$.

### L2 human

The Hermitian part averages each entry with the conjugate of its mirror entry.
Here the upper triangular $A$ has a full $H$ and a full $K$, because the mirror entries of $A$ differ.
