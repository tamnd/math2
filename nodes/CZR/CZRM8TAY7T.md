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

Let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.

1. By the [[definition|0W809K6AW0]], $A^{\mathsf{T}} = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$: the diagonal $1, 4$ stays, and $2$ and $3$ change places.
2. Turning the array clockwise by a quarter turn puts the first column $(1, 3)$, read upwards, in the first row: $\begin{pmatrix} 3 & 1 \\ 4 & 2 \end{pmatrix}$.
3. The entry $(1, 1)$ is $3$ after the turn and $1$ in $A^{\mathsf{T}}$, so the two results differ.
4. The transpose is a reflection of the array in the main diagonal, and a turn is not a reflection.

## Remarks

The quarter turn of the array is $A^{\mathsf{T}}$ with its columns in reverse order, that is, $A^{\mathsf{T}} P$ with $P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
Image software sometimes calls a reflection in the antidiagonal a "transpose"; in linear algebra the word means the reflection in the main diagonal.

## Explanations

### L1 human

The transpose flips the matrix across the line from the top left to the bottom right.
Turning the matrix like a picture is a different movement.

### L2 human

A turn moves the diagonal entries, and the transpose never moves them.
This is a quick check of a computed transpose.
