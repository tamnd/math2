---
tag: T4EGXYA8H3
kind: example
name: The symmetric and skew-symmetric parts of a 2 × 2 matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [0PBY4E9GQF]
illustrates: [K284W6D15Z]
uses: [03RNVFDEAN, 0N28QN4CYA]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_matrix
    locator: Decomposition into symmetric and skew-symmetric
---

## Example

Let
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \qquad A^{\mathsf{T}} = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$$
over $\mathbb{Q}$.
We split $A$ into a symmetric part and a skew-symmetric part.

1. Add $A$ and $A^{\mathsf{T}}$ and halve:
$$A + A^{\mathsf{T}} = \begin{pmatrix} 2 & 5 \\ 5 & 8 \end{pmatrix}, \qquad S = \tfrac12 (A + A^{\mathsf{T}}) = \begin{pmatrix} 1 & 5/2 \\ 5/2 & 4 \end{pmatrix}.$$
2. Subtract and halve:
$$A - A^{\mathsf{T}} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad K = \tfrac12 (A - A^{\mathsf{T}}) = \begin{pmatrix} 0 & -1/2 \\ 1/2 & 0 \end{pmatrix}.$$
3. The two entries of $S$ off the diagonal are equal, so $S$ is [[symmetric|0N28QN4CYA]]; the two entries of $K$ off the diagonal are opposite and its diagonal is $0$, so $K$ is [[skew-symmetric|03RNVFDEAN]].
4. Add the parts entry by entry:
$$S + K = \begin{pmatrix} 1 + 0 & 5/2 - 1/2 \\ 5/2 + 1/2 & 4 + 0 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = A.$$

## Remarks

The [[decomposition theorem|K284W6D15Z]] says that no other pair works.
Indeed, if $A = S' + K'$ with $S'$ symmetric and $K'$ skew-symmetric, then entry $(1, 2)$ gives $s + k = 2$ and entry $(2, 1)$ gives $s - k = 3$, where $s = s'_{12}$ and $k = k'_{12}$; so $s = 5/2$ and $k = -1/2$.

The skew part is invisible to the quadratic form of $A$.
For $x = (x_1, x_2)$,
$$x^{\mathsf{T}} A x = x_1^2 + (2 + 3) x_1 x_2 + 4 x_2^2 = x_1^2 + 5 x_1 x_2 + 4 x_2^2 = x^{\mathsf{T}} S x,$$
since $x^{\mathsf{T}} K x = -\tfrac12 x_1 x_2 + \tfrac12 x_2 x_1 = 0$.

Over $\mathbb{Z}$ the same matrix has no such splitting, since the entries $5/2$ and $1/2$ are not integers.

## Explanations

### L1 human

The symmetric part replaces the two mirror entries $2$ and $3$ by their average, $5/2$.
The skew part keeps half their difference, $-1/2$ above the diagonal and $1/2$ below it.
Adding the two parts gives back $A$.

### L2 human

The typical use is to simplify a quadratic form: replace $A$ by its symmetric part $S$, which gives the same values $x^{\mathsf{T}} A x$.
The diagonal of $A$ goes entirely into $S$, because a skew-symmetric matrix over $\mathbb{Q}$ has zero diagonal.
Watch out: the halves are needed, which is why the theorem asks for $2$ to be invertible.
