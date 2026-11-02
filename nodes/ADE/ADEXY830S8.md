---
tag: ADEXY830S8
kind: example
name: Birkhoff polytope
msc: [52B12, 15B51, 52B05]
instance_of: [300K6CB1KH]
uses: [JJA90EB2PS, 08SP3DF8NB, 3KY1RMEDMJ, R7V3S9V891, DPDXN2FJC4]
sources:
  - url: https://en.wikipedia.org/wiki/Birkhoff_polytope
same_as:
  wikidata: Q4916482
  wikipedia: Birkhoff polytope
---

## Example

Let $n \ge 1$.
The *Birkhoff polytope* $B_n$ is the set of $n \times n$ [[doubly stochastic matrices|JJA90EB2PS]], seen as points of $\R^{n \times n}$:
$$B_n = \set{X \in \R^{n \times n} : x_{ij} \ge 0, \ \textstyle\sum_{j} x_{ij} = 1 \text{ for all } i, \ \sum_{i} x_{ij} = 1 \text{ for all } j}.$$
It is bounded, since $0 \le x_{ij} \le 1$, and is cut out by finitely many linear inequalities and equations, so it is a [[convex polytope|300K6CB1KH]].
By the [[Birkhoff–von Neumann theorem|3KY1RMEDMJ]], $B_n$ is the convex hull of the $n!$ [[permutation matrices|08SP3DF8NB]], and these are its [[vertices|R7V3S9V891]].
The $2n$ equations have rank $2n - 1$, so $\dim B_n = n^2 - (2n - 1) = (n-1)^2$.
For $n \ge 3$ the [[facets|DPDXN2FJC4]] are the $n^2$ sets $\set{X \in B_n : x_{ij} = 0}$.

## Remarks

For $n = 2$, $B_2$ is the segment of matrices $\begin{pmatrix} t & 1-t \\ 1-t & t \end{pmatrix}$, $0 \le t \le 1$, with the two permutation matrices as endpoints.
For $n = 3$, $B_3$ is a $4$-dimensional polytope with $6$ vertices and $9$ facets.
Its role in optimisation is that a linear function on $B_n$ attains its maximum at a permutation matrix, which solves the assignment problem by linear programming.

## Explanations

### L1 human

A doubly stochastic matrix is a square table of nonnegative numbers in which every row and every column adds up to $1$.
All such tables together form a solid shape, the Birkhoff polytope.
Its corners are the permutation matrices, tables of zeros with a single $1$ in each row and each column.
Every doubly stochastic matrix is therefore an average of permutation matrices.
