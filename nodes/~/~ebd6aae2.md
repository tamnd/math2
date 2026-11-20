---
tag: ~ebd6aae2
kind: example
name: The companion matrix of (x − 1)² is similar to a Jordan block
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
instance_of: [0ZCWPNZTQ3]
illustrates: [~dd227218, ~55322f5b]
uses: [0VH1TC1PWF, 0PBFS92AJP, 027KDW2K72, 03NDVCSHSB]
sources:
  - url: https://en.wikipedia.org/wiki/Companion_matrix
    locator: Diagonalizability
---

## Example

Let $p = (x - 1)^2 = x^2 - 2x + 1$, so $c_0 = 1$ and $c_1 = -2$.
Its companion matrix and the [[Jordan block|0PBFS92AJP]] $J_2(1)$ are
$$C = C(p) = \begin{pmatrix} 0 & -1 \\ 1 & 2 \end{pmatrix}, \qquad J_2(1) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.$$
We show that $C = P J_2(1) P^{-1}$ with $P = \begin{pmatrix} -1 & 1 \\ 1 & 0 \end{pmatrix}$.

1. $\operatorname{tr} C = 2$ and $\det C = 0 \cdot 2 - (-1) \cdot 1 = 1$, so $\chi_C = x^2 - 2x + 1 = p$.
2. $C - I = \begin{pmatrix} -1 & -1 \\ 1 & 1 \end{pmatrix} \ne 0$, so $m_C \ne x - 1$, and $m_C = p$ by the [[theorem on companion matrices|~dd227218]].
3. The kernel of $C - I$ is spanned by $p_1 = (-1, 1)$. So $1$ has geometric multiplicity $1$, and $C$ is not diagonalizable.
4. Solve $(C - I) p_2 = p_1$: $p_2 = (1, 0)$ works, since $(C - I)(1, 0) = (-1, 1)$.
5. Let $P$ have columns $p_1, p_2$. Then $\det P = 0 - 1 = -1 \ne 0$.
6. $CP = \begin{pmatrix} 0 \cdot (-1) + (-1) \cdot 1 & 0 \\ -1 + 2 & 1 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 1 & 1 \end{pmatrix}$.
7. $P J_2(1) = \begin{pmatrix} -1 & -1 + 1 \\ 1 & 1 + 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 1 & 1 \end{pmatrix}$.
8. So $CP = P J_2(1)$, and $C$ is [[similar|027KDW2K72]] to $J_2(1)$.

## Remarks

The example shows that a companion matrix with a repeated root is a single Jordan block, not a diagonal matrix.
For $p = (x - 1)(x - 2)$ instead, $C(p) = \begin{pmatrix} 0 & -2 \\ 1 & 3 \end{pmatrix}$ is similar to $\operatorname{diag}(1, 2)$.
For $p = (x - \lambda)^n$, the same method gives $C(p) \sim J_n(\lambda)$ for every $n$.

## Explanations

### L1 human

The polynomial $x$ minus one, squared, has the root one twice.
Its companion matrix has only one direction of eigenvectors, not two.
So it cannot be made diagonal, and the best we can do is a Jordan block with a single one above the diagonal.

### L2 human

1. Check $C p_1 = (-1, 1) = p_1$: $C(-1, 1) = (0 - 1, -1 + 2) = (-1, 1)$.
2. Check $C p_2 = p_1 + p_2$: $C(1, 0) = (0, 1) = (-1, 1) + (1, 0)$.
3. These are the two columns of $CP = P J_2(1)$.

The typical use is a check of the rule "a cyclic matrix with one eigenvalue is a single Jordan block".
The trap is the order of the chain: $p_1$ must be the eigenvector and come first, or the $1$ appears below the diagonal.
