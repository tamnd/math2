---
tag: 13RPZZFD43
kind: example
name: Testing row equivalence with the reduced row echelon form
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
instance_of: [006BHFWMAP]
uses: [095DDGZF16, 0NNR68BFRY, BF9SMZMJZE]
sources:
  - url: https://en.wikipedia.org/wiki/Row_equivalence
    locator: lead section
---

## Example

To decide whether two matrices are row equivalent, reduce both and compare.
Let
$$A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 7 \end{bmatrix}, \qquad B = \begin{bmatrix} 1 & 2 & 0 \\ 1 & 2 & 1 \end{bmatrix}, \qquad C = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}$$
over $\mathbb{R}$.

1. For $A$, the step $R_2 \leftarrow R_2 - 2R_1$ makes row 2 equal to $(0, 0, 1)$. Then $R_1 \leftarrow R_1 - 3R_2$ makes row 1 equal to $(1, 2, 0)$.
2. So the [[RREF|0NNR68BFRY]] of $A$ is $\begin{bmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix}$.
3. For $B$, the step $R_2 \leftarrow R_2 - R_1$ makes row 2 equal to $(0, 0, 1)$, and the result $\begin{bmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ is already in RREF.
4. The RREFs agree, so $A$ and $B$ are [[row equivalent|095DDGZF16]].
5. For $C$, the step $R_2 \leftarrow R_2 - 2R_1$ gives $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \end{bmatrix}$, which is in RREF.
6. This RREF differs from that of $A$. By the [[uniqueness of the RREF|BF9SMZMJZE]], $C$ is not row equivalent to $A$.
7. An explicit sequence from $A$ to $B$: the two steps of step 1, then the inverse of step 3, $R_2 \leftarrow R_2 + R_1$, which turns $(0, 0, 1)$ into $(1, 2, 1)$.

## Remarks

Step 6 needs the uniqueness theorem.
Without it, two different RREFs might still be row equivalent, and comparing them would prove nothing.

The rank gives a quicker proof that $A$ and $C$ differ, since $\rank A = 2$ and $\rank C = 1$.
But equal ranks would not prove row equivalence: $B$ and $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$ both have rank $2$, and their RREFs differ.

## Explanations

### L1 human

To check whether two tables can be turned into each other by row moves, simplify both as far as possible.
If the simplest forms agree, the answer is yes.
If they do not agree, the answer is no.

### L2 human

1. Reduce each matrix to its RREF.
2. Compare the RREFs entry by entry.
3. For a sequence from the first matrix to the second, reduce the first, then undo the steps of the second in reverse order.

Watch out: comparing echelon forms that are not reduced can give the wrong answer, since a matrix has many echelon forms.
