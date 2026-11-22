---
tag: STX4PZKC69
kind: example
name: Determinant of the transpose map on 2 × 2 matrices
msc: [15A04, 15A15]
topics: [DTBK11SR77]
audience: ug2
instance_of: [0X0HQYSZ0K]
uses: [03F5KP94K0, 0KMN32XGPF, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Determinant of an endomorphism
---

## Example

Let $V = M_2(\mathbb{R})$ be the space of real $2 \times 2$ matrices, and let $T(X) = X^{\mathsf{T}}$ be the [[transpose|0W809K6AW0]].
Let $E_{ij}$ be the matrix with entry $1$ at position $(i, j)$ and $0$ elsewhere.
We show that $\det T = -1$ in two bases.

1. The transpose is linear, since $(X + Y)^{\mathsf{T}} = X^{\mathsf{T}} + Y^{\mathsf{T}}$ and $(cX)^{\mathsf{T}} = c X^{\mathsf{T}}$.
   The space $V$ has dimension $4$, so the matrix of $T$ is $4 \times 4$.
2. In the basis $E_{11}, E_{12}, E_{21}, E_{22}$, the map fixes $E_{11}$ and $E_{22}$ and exchanges $E_{12}$ and $E_{21}$.
   So the matrix is the identity with its second and third columns swapped:
$$[T] = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.$$
3. Swapping two columns of $I_4$ changes the determinant from $1$ to $-1$, so the [[definition|03F5KP94K0]] gives $\det T = -1$.
4. For a check, use the basis $E_{11}$, $E_{22}$, $E_{12} + E_{21}$, $E_{12} - E_{21}$.
   The first three are symmetric, so $T$ fixes them.
5. The last one is skew-symmetric: $T(E_{12} - E_{21}) = E_{21} - E_{12} = -(E_{12} - E_{21})$.
6. So the matrix in this basis is $\operatorname{diag}(1, 1, 1, -1)$, with determinant $-1$, as the [[invariance theorem|0KMN32XGPF]] predicts.

## Remarks

The second basis splits $V$ into the symmetric matrices, a space of dimension $3$, and the skew-symmetric matrices, a space of dimension $1$.
The transpose is the identity on the first part and minus the identity on the second, and that is why its determinant is $(-1)^1$.

The size of the matrices changes the answer.
On $M_n(\mathbb{R})$ the transpose fixes the symmetric matrices and negates the skew-symmetric ones, which form a space of dimension $n(n-1)/2$.
So its determinant is $(-1)^{n(n-1)/2}$.
For $n = 3$ this is $(-1)^3 = -1$, and for $n = 4$ it is $(-1)^6 = 1$.
In every size $T \circ T = \operatorname{id}$, which agrees with $(\det T)^2 = 1$.

## Explanations

### L1 human

Transposing a $2 \times 2$ matrix keeps the two diagonal entries and swaps the two other entries.
Swapping two coordinates is a reflection, and a reflection turns space over, so its determinant is $-1$.

### L2 human

The space here has dimension $4$, so the matrix of $T$ is $4 \times 4$, not $2 \times 2$.
The basis of symmetric and skew-symmetric matrices makes the matrix diagonal, and that is the fastest way to the answer.
Watch out: $\det T$ is the determinant of the map $X \mapsto X^{\mathsf{T}}$.
It is not $\det(X^{\mathsf{T}})$ for one matrix $X$, which always equals $\det X$.
