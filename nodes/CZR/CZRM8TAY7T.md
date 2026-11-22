---
tag: CZRM8TAY7T
kind: example
name: Turning a matrix by a quarter turn is not the transpose
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
not_instance_of:
  - target: 09DXWYRD43
    note: turning (1, 2; 3, 4) clockwise by a quarter turn gives (3, 1; 4, 2), but the transpose is (1, 3; 2, 4)
uses: [0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose
    locator: lead section
---

## Example

Let
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}.$$
We compare its transpose with the array that we get by turning $A$ clockwise by a quarter turn, like a picture.

1. By the [[definition|0W809K6AW0]], $(A^{\mathsf{T}})_{ij} = a_{ji}$, so
$$A^{\mathsf{T}} = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}.$$
The diagonal entries $1$ and $4$ stay in place, and $2$ and $3$ change places.
2. Turning $A$ clockwise moves the first column $(1, 3)$, read from the bottom up, into the first row, and the second column into the second row:
$$\begin{pmatrix} 3 & 1 \\ 4 & 2 \end{pmatrix}.$$
3. The entry $(1, 1)$ is $3$ after the turn but $1$ in $A^{\mathsf{T}}$, so the two arrays differ, and the turn fails the rule $(A^{\mathsf{T}})_{11} = a_{11}$.

## Remarks

The transpose is a reflection of the array in its main diagonal, and a quarter turn is not a reflection.
The two are related: the turned array is $A^{\mathsf{T}}$ with its two columns swapped, that is, $A^{\mathsf{T}} P$ with $P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
Check: $A^{\mathsf{T}} P = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 3 & 1 \\ 4 & 2 \end{pmatrix}$.

For a symmetric array such as $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ the transpose changes nothing, but the turn still gives $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.
So the two operations differ even on matrices where the transpose does nothing.

## Explanations

### L1 human

The transpose flips the matrix across the line from the top left corner to the bottom right corner.
Turning the matrix like a picture on a wall is a different movement.
After a turn, the number in the top left corner is a new number; after a transpose, it is the same number.

### L2 human

The typical use of this example is a quick check of a computed transpose: the diagonal entries must not move.
In $\begin{pmatrix} 3 & 1 \\ 4 & 2 \end{pmatrix}$ the diagonal is $(3, 2)$, while the diagonal of $A$ is $(1, 4)$, so this array cannot be $A^{\mathsf{T}}$.
Watch out: for a non-square matrix, both the turn and the transpose change the size from $m \times n$ to $n \times m$, so the size alone does not catch the mistake.
