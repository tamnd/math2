---
tag: YHCD6MTSV8
kind: example
name: A nilpotent 2 × 2 matrix with no zero entries
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [07BSPZPSMF, 063D5Z2C70]
illustrates: [N40XPYS89W]
uses: [0419GJC84P, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: Examples
---

## Example

Let
$$N = \begin{pmatrix} 2 & 4 \\ -1 & -2 \end{pmatrix}$$
over the real numbers.
No entry of $N$ is zero, and yet $N$ is nilpotent.

1. Multiply row by column to get the square:
$$N^2 = \begin{pmatrix} 2 \cdot 2 + 4 \cdot (-1) & 2 \cdot 4 + 4 \cdot (-2) \\ (-1) \cdot 2 + (-2)(-1) & (-1) \cdot 4 + (-2)(-2) \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}.$$
2. Since $N \ne 0$, the matrix $N$ is [[nilpotent|0419GJC84P]] of index $2$.
3. The trace is $2 + (-2) = 0$ and the determinant is $2 \cdot (-2) - 4 \cdot (-1) = 0$, as they must be for a nilpotent matrix.
4. By the [[geometric series for a nilpotent matrix|N40XPYS89W]], the inverse of $I - N$ is $I + N$:
$$(I - N)^{-1} = I + N = \begin{pmatrix} 3 & 4 \\ -1 & -1 \end{pmatrix}.$$
5. Check: $I - N = \begin{pmatrix} -1 & -4 \\ 1 & 3 \end{pmatrix}$, and
$$\begin{pmatrix} -1 & -4 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 3 & 4 \\ -1 & -1 \end{pmatrix} = \begin{pmatrix} -3 + 4 & -4 + 4 \\ 3 - 3 & 4 - 3 \end{pmatrix} = I.$$

## Remarks

The zero entries of a matrix say nothing about nilpotency, and the reason here is a hidden structure.
The matrix is a column times a row:
$$N = \begin{pmatrix} 2 \\ -1 \end{pmatrix} \begin{pmatrix} 1 & 2 \end{pmatrix}, \qquad \begin{pmatrix} 1 & 2 \end{pmatrix} \begin{pmatrix} 2 \\ -1 \end{pmatrix} = 2 - 2 = 0.$$
With $x = (2, -1)$ and $y = (1, 2)$ this reads $N = x y^{\mathsf{T}}$, so $N^2 = x (y^{\mathsf{T}} x) y^{\mathsf{T}} = 0$.
As a map, $N$ sends the plane onto the line spanned by $(2, -1)$, and it sends that line to $0$.

Every nonzero nilpotent $2 \times 2$ matrix has this shape.
Its image lies in its kernel, both are lines, so the matrix has rank one and equals $x y^{\mathsf{T}}$ with $y^{\mathsf{T}} x = 0$.
If we change one entry, say $n_{11} = 3$, the trace becomes $1$, and the matrix is no longer nilpotent.

## Explanations

### L1 human

None of the four entries of this matrix is $0$, but its square is the zero matrix.
The positive and negative products cancel in every entry of the square.
So we cannot spot a nilpotent matrix by looking for zeros; we have to multiply.

### L2 human

The quickest test for a $2 \times 2$ matrix uses the trace and the determinant.
A $2 \times 2$ matrix $A$ satisfies $A^2 = (\operatorname{tr} A) A - (\det A) I$, so when both numbers are $0$ we get $A^2 = 0$.
Here both are $0$, which confirms step 1 without a second multiplication.
Watch out: this shortcut is special to size $2$; in general we need the whole characteristic polynomial to be $x^n$.
