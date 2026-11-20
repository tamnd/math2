---
tag: 8YRP1P4XRX
kind: example
name: A real matrix with zero diagonal that is not skew-symmetric
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
not_instance_of:
  - target: 0PBY4E9GQF
    note: the real matrix (0, 1; 1, 0) has zero diagonal, but it is symmetric and a12 = 1 is not -a21 = -1
uses: [03RNVFDEAN, 0N28QN4CYA]
sources:
  - url: https://en.wikipedia.org/wiki/Skew-symmetric_matrix
    locator: Properties
---

## Example

Let $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ over $\mathbb{R}$.

1. $B^{\mathsf{T}} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = B$, so $B$ is [[symmetric|0N28QN4CYA]].
2. $-B = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$, and its entry $(1, 2)$ is $-1 \neq 1$. So $B^{\mathsf{T}} \neq -B$.
3. So $B$ is not [[skew-symmetric|03RNVFDEAN]], although its diagonal is $0$.
4. Over $\mathbb{F}_2$ the same matrix is skew-symmetric, because $-1 = 1$ there.

## Remarks

A zero diagonal is necessary for a real skew-symmetric matrix, but it is not sufficient.
For $x = (1, 1)$, $x^{\mathsf{T}} B x = 2 \neq 0$, while $x^{\mathsf{T}} K x = 0$ for every real skew-symmetric $K$.

## Explanations

### L1 human

This matrix has zeros on the diagonal, but its two mirror entries are equal, not opposite.
So it is symmetric, not skew-symmetric.

### L2 human

Over $\mathbb{R}$, a nonzero matrix cannot be both symmetric and skew-symmetric.
Step 4 shows that the answer depends on the field.
