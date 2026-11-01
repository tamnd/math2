---
tag: 3KY1RMEDMJ
kind: statement
role: theorem
name: Birkhoff–von Neumann theorem
msc: [15B51, 05C70, 52B12]
uses: [JJA90EB2PS, 0Q5SM60HTH, 0TCHAS04WK]
about: [JJA90EB2PS]
sources:
  - url: https://en.wikipedia.org/wiki/Doubly_stochastic_matrix
    locator: Birkhoff–von Neumann theorem
---

## Statement

Let $n \ge 1$ and let $A$ be an $n \times n$ [[doubly stochastic matrix|JJA90EB2PS]].
So $A$ has real nonnegative entries, and its rows and columns each sum to $1$.
Then $A$ is a convex combination of $n \times n$ [[permutation matrices|0Q5SM60HTH]].
That is, there are permutation matrices $P_1, \dots, P_k$ and real numbers $\theta_1, \dots, \theta_k \ge 0$ with $\theta_1 + \cdots + \theta_k = 1$ such that
$$A = \theta_1 P_1 + \cdots + \theta_k P_k.$$

## Remarks

The proof is by induction on the number of nonzero entries of $A$.
Form the bipartite graph whose two sides are the rows and the columns, with an edge for each nonzero entry.
Any $r$ rows carry total mass $r$, and this mass lies in the columns joined to them, which carry at most $1$ each.
So [[Hall's marriage theorem|08WCB90WND]] gives a perfect matching.
It is a permutation matrix $P$ supported on nonzero entries of $A$.
If $\theta$ is the least entry of $A$ on this support and $A \ne P$, then $(A - \theta P)/(1 - \theta)$ is doubly stochastic with fewer nonzero entries.
For example,
$$\begin{pmatrix} 1/2 & 1/2 \\ 1/2 & 1/2 \end{pmatrix} = \frac12 \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + \frac12 \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.$$
Equivalently, the set of doubly stochastic matrices, the Birkhoff polytope, is the [[convex hull|0TCHAS04WK]] of the $n!$ permutation matrices, and these are its vertices.

## Explanations

### L1 human

A doubly stochastic matrix spreads one unit from each row over the columns so that every column also receives one unit.
The theorem says that every such spreading is a mixture of perfect one-to-one assignments.
So a fractional assignment can always be written as a weighted average of whole assignments.

### L2 human

The theorem is the matrix form of Hall's and Kőnig's theorems on bipartite matchings.
It shows that the linear program for the assignment problem has a permutation matrix among its optimal solutions.
It is also used in the theory of majorization and in proofs of inequalities for permanents and eigenvalues.
