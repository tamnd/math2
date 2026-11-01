---
tag: S1PG1N2VEX
kind: statement
role: theorem
name: Kirchhoff's matrix tree theorem
msc: [05C50, 05C05, 05C30]
uses: [0C62PZXX02, 0S4ZEZM7KE, TN6M6DVZRP, 0XPKR18APA, 00KDZRW4C0]
about: [0S4ZEZM7KE, TN6M6DVZRP]
sources:
  - url: https://en.wikipedia.org/wiki/Kirchhoff%27s_theorem
same_as:
  wikidata: Q2226691
  wikipedia: Kirchhoff's theorem
---

## Statement

Let $G$ be a finite [[multigraph|0C62PZXX02]] without loops, with vertices $v_1, \dots, v_n$ and $n \ge 2$.
Let $D$ be the diagonal matrix of the vertex degrees.
Let $A$ be the matrix with $A_{ii} = 0$ and $A_{ij}$ the number of edges between $v_i$ and $v_j$ for $i \ne j$.
Let $L = D - A$ be the [[Laplacian matrix|TN6M6DVZRP]] of $G$.
For each $i$, let $L_i$ be the matrix obtained from $L$ by deleting row $i$ and column $i$.
Then the number of [[spanning trees|0S4ZEZM7KE]] of $G$ equals $\det L_i$, for every $i \in \set{1, \dots, n}$.

## Remarks

Orient each edge and let $B$ be the $n \times m$ incidence matrix, with entries $+1$ and $-1$ at the head and tail of each edge; then $L = B B^T$.
Delete row $i$ of $B$ to get $B_i$, so that $L_i = B_i B_i^T$.
By the [[Cauchy–Binet formula|08WE2W7DYS]], $\det L_i$ is the sum of $(\det N)^2$ over the $(n-1) \times (n-1)$ submatrices $N$ of $B_i$.
Such a minor is $\pm 1$ if its $n - 1$ edges form a spanning tree and $0$ otherwise, which gives the count.

Example: for the triangle $K_3$, every vertex has degree $2$ and
$$L_3 = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}, \qquad \det L_3 = 3,$$
which matches the $3$ spanning trees obtained by removing one edge.
For the complete graph $K_n$ the theorem gives $n^{n-2}$, which is [[Cayley's formula|0M2SSGSYPE]].
If $G$ is not connected, both sides are $0$.

## Explanations

### L1 human

Counting spanning trees by hand is hard even for small graphs.
The theorem gives a recipe.
Write the degree of each vertex on the diagonal and $-1$ for each edge off the diagonal.
Cross out one row and the matching column, and take the [[determinant|00KDZRW4C0]].
The number you get is the number of spanning trees, whichever row you crossed out.

### L2 human

An equivalent form uses the eigenvalues $0 = \mu_1 \le \mu_2 \le \dots \le \mu_n$ of $L$: the number of spanning trees is $\frac{1}{n} \mu_2 \cdots \mu_n$.
This links spectral graph theory to enumeration.
The theorem goes back to Kirchhoff's study of electrical networks.
It has a weighted version, where each edge carries a variable and the determinant sums the weights of the spanning trees, and a version for directed graphs that counts arborescences.
