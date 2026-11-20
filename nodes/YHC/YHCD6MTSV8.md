---
tag: YHCD6MTSV8
kind: example
name: A nilpotent 2 × 2 matrix with no zero entries
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [07BSPZPSMF]
illustrates: [N40XPYS89W]
uses: [0419GJC84P, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: Examples
---

## Example

Let $N = \begin{pmatrix} 2 & 4 \\ -1 & -2 \end{pmatrix}$.

1. $N^2 = \begin{pmatrix} 2 \cdot 2 + 4 \cdot (-1) & 2 \cdot 4 + 4 \cdot (-2) \\ -1 \cdot 2 + (-2)(-1) & -1 \cdot 4 + (-2)(-2) \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$.
2. $N \neq 0$, so $N$ is [[nilpotent|0419GJC84P]] of index $2$.
3. $\operatorname{tr} N = 2 - 2 = 0$ and $\det N = -4 + 4 = 0$.
4. By the [[geometric series|N40XPYS89W]], $(I - N)^{-1} = I + N = \begin{pmatrix} 3 & 4 \\ -1 & -1 \end{pmatrix}$.
5. Check: $I - N = \begin{pmatrix} -1 & -4 \\ 1 & 3 \end{pmatrix}$, and $(I - N)(I + N) = \begin{pmatrix} -3 + 4 & -4 + 4 \\ 3 - 3 & 4 - 3 \end{pmatrix} = I$.

## Remarks

$N = \begin{pmatrix} 2 \\ -1 \end{pmatrix} \begin{pmatrix} 1 & 2 \end{pmatrix}$, a column times a row, and $\begin{pmatrix} 1 & 2 \end{pmatrix} \begin{pmatrix} 2 \\ -1 \end{pmatrix} = 0$.
So $N^2 = x (y^{\mathsf{T}} x) y^{\mathsf{T}} = 0$.
As a map, $N$ sends $\mathbb{R}^2$ onto the line spanned by $(2, -1)$, and it sends that line to $0$.

## Explanations

### L1 human

None of the entries of $N$ is $0$, but $N^2$ is the zero matrix.
So nilpotency cannot be seen from the zero entries alone.

### L2 human

Every nonzero nilpotent $2 \times 2$ matrix has this form: a rank-one matrix $x y^{\mathsf{T}}$ with $y^{\mathsf{T}} x = 0$.
Its image is its kernel.
