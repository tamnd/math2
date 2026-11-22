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

Let
$$B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$
over $\mathbb{R}$.
Its diagonal is $0$, and we check that it is still not skew-symmetric.

1. Swapping rows and columns gives $B^{\mathsf{T}} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = B$, so $B$ is [[symmetric|0N28QN4CYA]].
2. The negative is $-B = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$, whose entry $(1, 2)$ is $-1$, while the entry $(1, 2)$ of $B^{\mathsf{T}}$ is $1$.
3. So $B^{\mathsf{T}} \neq -B$, and $B$ is not [[skew-symmetric|03RNVFDEAN]], although its diagonal is $0$.
4. Over $\mathbb{F}_2$ the same matrix is skew-symmetric, because $-1 = 1$ there, so $-B = B = B^{\mathsf{T}}$.

## Remarks

Over $\mathbb{R}$ a zero diagonal is necessary for skew-symmetry but not sufficient.
A test with a vector shows the difference: every real skew-symmetric $K$ has $x^{\mathsf{T}} K x = 0$, but for $x = (1, 1)$,
$$x^{\mathsf{T}} B x = 0 + 1 + 1 + 0 = 2 \neq 0.$$

The changed matrix $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ is skew-symmetric, and it is the smallest repair: only the sign of one entry off the diagonal changes.

## Explanations

### L1 human

This matrix has zeros on the diagonal, but its two mirror entries are equal, not opposite.
So it is symmetric, not skew-symmetric.

### L2 human

The typical use of this example is as a warning when you check skew-symmetry: a zero diagonal is the first test, not the last.
Over $\mathbb{R}$, a matrix that is both symmetric and skew-symmetric satisfies $A = -A$, so $2A = 0$ and $A = 0$; since $B \neq 0$, its symmetry already rules out skew-symmetry.
Watch out: step 4 shows that the answer depends on the field.
