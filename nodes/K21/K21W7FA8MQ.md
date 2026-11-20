---
tag: K21W7FA8MQ
kind: example
name: The pivot columns of the reduced form do not span the column space
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
not_instance_of:
  - target: 03AJKXH1AV
    note: the span of the pivot column (1, 0) of the reduced form of the matrix with rows (1, 2) and (2, 4) is not its column space
uses: [0F0RPPJ2TT, 0NNR68BFRY, 0BCMGDHZGR]
sources:
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: Basis
---

## Example

Let $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ over $\R$.

1. Subtract $2$ times row 1 from row 2. The [[reduced row echelon form|0NNR68BFRY]] is $R = \begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix}$, with its [[pivot|0BCMGDHZGR]] in column 1.
2. The [[column space|0F0RPPJ2TT]] of $A$ is spanned by $a_1 = (1, 2)$ and $a_2 = (2, 4) = 2a_1$. So $\operatorname{Col}(A)$ is the line $\{(t, 2t) : t \in \R\}$.
3. The pivot column of $R$ is $(1, 0)$. It is not of the form $(t, 2t)$, since $t = 1$ would give second entry $2 \ne 0$.
4. So the span of the pivot column of $R$, the line $\{(t, 0)\}$, is not $\operatorname{Col}(A)$.
5. The correct basis is the pivot column of $A$ itself: $\{(1, 2)\}$.

The same trap appears for the [[$3 \times 4$ example|AGHYPF25CY]]: there the pivot columns of $R$ are $(1, 0, 0)$ and $(0, 1, 0)$, which are not in $\operatorname{Col}(A) = \{(u, v, w) : w = u + v\}$.

## Remarks

- Row operations change the column space. Here $\operatorname{Col}(R)$ is the line $\{(t, 0)\}$ and $\operatorname{Col}(A)$ is the line $\{(t, 2t)\}$.
- Row operations keep the dimension of the column space and the linear relations among the columns. So the positions of the pivot columns are correct; only the vectors must come from $A$.
- In contrast, the nonzero rows of $R$ do form a basis of the [[row space|069MCGX635]] of $A$.

## Explanations

### L1 human

After row reduction, go back to the original matrix to pick the columns.
The columns of the reduced matrix usually point in other directions.

### L2 human

Row operations multiply $A$ on the left by an invertible matrix $E$, so $\operatorname{Col}(R) = E \operatorname{Col}(A)$, a different subspace of the same dimension.
The pivot positions tell which columns of $A$ to keep.
This is a common error on examinations, because the reduced columns look simpler.
