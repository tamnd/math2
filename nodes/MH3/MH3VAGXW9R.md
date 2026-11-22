---
tag: MH3VAGXW9R
kind: example
name: A line through three of four points is not the least-squares line
msc: [65F20]
topics: [8GQVME4SZZ]
audience: ug1
not_instance_of:
  - target: 0BYTQ4X1HC
    note: the line y = 1 + t fits the points (0, 1), (1, 2), (2, 2), (3, 4) with residual sum of squares 1, more than 7/10, and its residual is not orthogonal to the columns
uses: [0W809K6AW0, V9AH43ZY91]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_least_squares
    locator: Basic formulation
---

## Example

Take the four points $(0, 1)$, $(1, 2)$, $(2, 2)$ and $(3, 4)$, and the matrix $A$ with rows $(1, t_i)$, as in [[the least-squares line|H2D0QA4AXV]].
The line $y = 1 + t$ corresponds to $x = (1, 1)$, and we show that it is not a least-squares solution.

1. The line passes through $(0, 1)$, $(1, 2)$ and $(3, 4)$, since $1 + 0 = 1$, $1 + 1 = 2$ and $1 + 3 = 4$.
2. At $t = 2$ it gives $3$, so it misses the point $(2, 2)$ by $1$.
3. The residual is $r = y - Ax = (0, 0, -1, 0)$, so $\norm{r}^2 = 1$.
4. The least-squares line $y = 0.9 + 0.9t$ has residual sum of squares $0.7 < 1$, so $x = (1, 1)$ does not minimize $\norm{y - Ax}$.
5. The test by orthogonality gives the same answer without knowing the best line:
$$A^{\mathsf{T}} r = \begin{pmatrix} 0 + 0 - 1 + 0 \\ 0 + 0 - 2 + 0 \end{pmatrix} = \begin{pmatrix} -1 \\ -2 \end{pmatrix} \ne 0.$$
6. So $r$ is not orthogonal to the column space, and by the [[normal equations|4D7MRG4D91]] the vector $(1, 1)$ is not a least-squares solution.

## Remarks

A line that hits most of the points can still be a poor fit in the least-squares sense, because one large miss costs a lot once it is squared.
The least-squares line spreads the error instead: it misses each point by at most $0.7$, and it hits none of them.

The verdict depends on the data.
If the point $(2, 2)$ is replaced by $(2, 3)$, all four points lie on $y = 1 + t$.
Then the residual is $0$, and this line becomes the least-squares line.

## Explanations

### L1 human

Passing exactly through three points out of four looks good, but the fourth miss is a whole unit.
Squaring makes that one miss cost $1$, while the best line pays only $0.7$ in total, spread over small misses.
Least squares prefers many small misses to one large miss.

### L2 human

To test whether a candidate $x$ is a least-squares solution, compute $A^{\mathsf{T}} (y - Ax)$.
It must be the zero vector, and here it is $(-1, -2)$.
This test needs no solving at all, so it is the fastest way to check a claimed fit.
A common mistake is to judge a fit by how many points it hits.
