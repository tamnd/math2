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

The span of the pivot columns of the reduced row echelon form is a subspace of the right dimension, but in general it is not the column space.
Let $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ over $\mathbb{R}$.

1. Subtract $2$ times row 1 from row 2; the [[reduced row echelon form|0NNR68BFRY]] is $R = \begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix}$, with its [[pivot|0BCMGDHZGR]] in column 1.
2. The columns of $A$ are $a_1 = (1, 2)$ and $a_2 = (2, 4) = 2a_1$, so the [[column space|0F0RPPJ2TT]] of $A$ is the line $\{(t, 2t) : t \in \mathbb{R}\}$.
3. The pivot column of $R$ is $(1, 0)$, and it is not of the form $(t, 2t)$, since its first entry forces $t = 1$ and then the second entry would be $2$, not $0$.
4. So the span of the pivot column of $R$ is the line $\{(t, 0) : t \in \mathbb{R}\}$, which is not $\operatorname{Col}(A)$.
5. The correct basis takes the pivot position from $R$ and the vector from $A$, which gives $\{(1, 2)\}$.

The same failure appears in the [[3 by 4 example|AGHYPF25CY]].
There the pivot columns of $R$ are $(1, 0, 0)$ and $(0, 1, 0)$, and neither lies in $\operatorname{Col}(A) = \{(u, v, w) : w = u + v\}$.

## Remarks

The example shows exactly what row operations keep and what they change.
They change the column space: here $\operatorname{Col}(R)$ is the line $\{(t, 0)\}$, while $\operatorname{Col}(A)$ is the line $\{(t, 2t)\}$.
They keep the dimension of the column space and every linear relation among the columns, such as $a_2 = 2a_1$, which reads $r_2 = 2r_1$ in $R$.
So the positions of the pivot columns are correct, and only the vectors must come from $A$.

The row space behaves the other way.
The nonzero rows of $R$ do form a basis of the [[row space|069MCGX635]] of $A$, since row operations keep the row space; here $(1, 2)$ spans the rows of both matrices.
If $A$ already has its pivot columns equal to unit vectors, as for $A = R$, the trap disappears, which is why it is easy to miss on small examples.

## Explanations

### L1 human

After row reduction, go back to the original matrix to pick the columns.
The columns of the reduced matrix usually point in other directions.
Here the reduced matrix suggests the direction $(1, 0)$, but every output of $A$ points along $(1, 2)$.

### L2 human

Row operations multiply $A$ on the left by an invertible matrix $E$, so that $R = EA$.
Then $\operatorname{Col}(R) = E \operatorname{Col}(A)$, a subspace of the same dimension that is in general different.
In this example, $E = \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix}$ sends $(1, 2)$ to $(1, 0)$.
Watch out: the reduced columns look simpler, and that is exactly why they are a common wrong answer on examinations.
