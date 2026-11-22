---
tag: FBFW5FE62Y
kind: example
name: Solving a 2 × 2 system with the inverse matrix
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: school
instance_of: [FBQCE3HVMP]
uses: [FBQCE3HVMP, 3RQX3T70NX, 8XWC7RKNN1]
sources:
  - book: isbn:9780321982384
    locator: Section 2.2
---

## Example

The system $2x + y = 5$, $5x + 3y = 13$ has the unique solution $(x, y) = (2, 1)$, and the inverse matrix finds it in one product.
In matrix form the system reads
$$\begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 5 \\ 13 \end{pmatrix}.$$
The coefficient matrix $A$ has $ad - bc = 2 \cdot 3 - 1 \cdot 5 = 1$, so the [[2 × 2 formula|8XWC7RKNN1]] gives
$$A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}.$$
Check: $AA^{-1} = \begin{pmatrix} 6 - 5 & -2 + 2 \\ 15 - 15 & -5 + 6 \end{pmatrix} = I_2$.
Now multiply:
$$\begin{pmatrix} x \\ y \end{pmatrix} = A^{-1} \begin{pmatrix} 5 \\ 13 \end{pmatrix} = \begin{pmatrix} 15 - 13 \\ -25 + 26 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}.$$
Check in the equations: $2 \cdot 2 + 1 = 5$ and $5 \cdot 2 + 3 \cdot 1 = 13$.

## Remarks

By the [[solution theorem|3RQX3T70NX]], $(2, 1)$ is the only solution.
The inverse keeps working when the right side changes.
For the right side $(1, 0)$, the solution is column 1 of $A^{-1}$, namely $(3, -5)$, and indeed $2 \cdot 3 - 5 = 1$ and $15 - 15 = 0$.
For a general right side $(p, q)$, the solution is $(3p - q, \, -5p + 2q)$, a formula that no single elimination gives you.

## Explanations

### L1 human

We write the two equations as one matrix equation, find the inverse matrix, and multiply.
The answer is $x = 2$ and $y = 1$.

### L2 human

The method has three steps: write the matrix, invert it, multiply.
Because $ad - bc = 1$ here, the inverse has whole-number entries, and so does every solution with whole-number right sides.
A trap: the vector $(5, 13)$ must stand to the right of $A^{-1}$.
