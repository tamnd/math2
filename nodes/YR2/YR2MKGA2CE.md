---
tag: YR2MKGA2CE
kind: definition
name: Diagonally dominant matrix
msc: [15B99, 65F05]
defines: 89P5GTKW87
uses: [0JXZKX526R]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonally_dominant_matrix
---

## Definition

Let $A = (a_{ij})$ be an $n \times n$ complex [[square matrix|0JXZKX526R]].
The matrix $A$ is *diagonally dominant* (by rows) when
$$\abs{a_{ii}} \ge \sum_{j \ne i} \abs{a_{ij}} \qquad \text{for all } i = 1, \dots, n.$$
It is *strictly diagonally dominant* when this inequality is strict for all $i$.

## Remarks

Example: $\begin{pmatrix} 3 & -1 \\ 1 & 2 \end{pmatrix}$ is strictly diagonally dominant, because $3 > 1$ and $2 > 1$.
Non-example: $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$ is not diagonally dominant, because in the first row $\abs{1} < \abs{2}$.
Diagonal dominance by columns is the same condition for the transpose $A^T$.
A strictly diagonally dominant matrix is invertible, by the [[Levy–Desplanques theorem|PWKN6ANA0G]].
A diagonally dominant matrix that is not strictly so can be singular, for example $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.
