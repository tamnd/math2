---
tag: KPCM3KY0MR
kind: definition
name: Character table
msc: [20C15]
defines: P16AFZT3K0
uses: [G5S1M9, RMWMYBY8TC, FX3NEFYFFN, 0DEBXAJ5SA]
sources:
  - url: https://en.wikipedia.org/wiki/Character_table
---

## Definition

Let $G$ be a finite [[group|G5S1M9]].
Let $\chi_1, \ldots, \chi_r$ be the distinct irreducible complex [[characters|RMWMYBY8TC]] of $G$, and let $C_1, \ldots, C_s$ be the [[conjugacy classes|0DEBXAJ5SA]] of $G$, with $g_j \in C_j$.
The *character table* of $G$ is the $r \times s$ matrix with entries $\chi_i(g_j)$.
By convention $\chi_1$ is the trivial character and $C_1 = \set{1}$.

## Remarks

The table is square: $r = s$.
Example: the symmetric group $S_3$ has three classes, of the identity, the transpositions and the $3$-cycles.
Its three irreducible characters are the trivial one, the sign, and a character of degree $2$.
The last one is the permutation character on three points minus the trivial character.
Its table is
$$\begin{array}{c|ccc} & 1 & (1\,2) & (1\,2\,3) \\ \hline \chi_1 & 1 & 1 & 1 \\ \chi_2 & 1 & -1 & 1 \\ \chi_3 & 2 & 0 & -1 \end{array}$$
The check: $1^2 + 1^2 + 2^2 = 6 = \abs{S_3}$, and the rows are orthogonal for the weighted inner product of the [[Schur orthogonality relations|AY0B20QC04]].
Non-example: the $2 \times 3$ matrix with rows $\chi_1, \chi_2$ only is not the character table of $S_3$, because it omits the irreducible character $\chi_3$.
Non-isomorphic groups can have the same character table: the dihedral group of order $8$ and the quaternion group do.
