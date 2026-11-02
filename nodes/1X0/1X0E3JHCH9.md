---
tag: 1X0E3JHCH9
kind: statement
role: proposition
name: Cuthill–McKee algorithm
msc: [65F50, 05C85]
uses: [JGACZYEEY7, Z58FRZCF8P, 0VR671PHE5, 00C0BR7D7H, 0KS0KRDV4Y, 08SP3DF8NB, 0WKG8CYY6A]
about: [JGACZYEEY7]
sources:
  - url: https://en.wikipedia.org/wiki/Cuthill–McKee_algorithm
same_as:
  wikidata: Q1146458
  wikipedia: Cuthill–McKee algorithm
---

## Statement

Let $A$ be a [[symmetric|0VR671PHE5]] $n \times n$ matrix.
Its [[graph|00C0BR7D7H]] $G$ has vertices $1, \dots, n$ and an edge between $i \ne j$ when $a_{ij} \ne 0$; assume $G$ is connected.
The *bandwidth* of $A$ is $\max \set{\abs{i - j} : a_{ij} \ne 0}$.
The *Cuthill–McKee algorithm* orders the vertices as follows.
It picks a start vertex $v_1$.
For $k = 1, 2, \dots$ it appends to the list the neighbours of $v_k$ not yet listed, in order of increasing [[degree|0KS0KRDV4Y]].
Let $L_0 = \set{v_1}$ and, for $d \ge 1$, let $L_d$ be the set of vertices at distance $d$ from $v_1$ in $G$.
Then:

1. the algorithm lists every vertex exactly once, and each level $L_d$ forms a contiguous block of the list, in the order $L_0, L_1, L_2, \dots$;
2. if $P$ is the [[permutation matrix|08SP3DF8NB]] of this ordering, the bandwidth of $P A P^T$ is at most $\max_d \big(\abs{L_d} + \abs{L_{d+1}}\big) - 1$;
3. the reversed ordering, called *reverse Cuthill–McKee*, gives a matrix with the same bandwidth.

## Remarks

The list is built exactly as a breadth-first search from $v_1$ would build its queue, which lists the vertices by nondecreasing distance from $v_1$; this gives clause 1.
In a breadth-first level structure, every edge joins two vertices of the same level or of adjacent levels.
Two adjacent levels occupy $\abs{L_d} + \abs{L_{d+1}}$ consecutive positions, so the positions of the ends of an edge differ by at most $\abs{L_d} + \abs{L_{d+1}} - 1$; this gives clause 2.
Clause 3 holds because reversing the order maps the positions $p, q$ to $n + 1 - p, n + 1 - q$, which have the same difference.
So a start vertex with many small levels, such as a vertex far from the rest of the graph, gives a narrow [[band|Z58FRZCF8P]].
In practice one starts from a vertex of minimum degree or a pseudo-peripheral vertex.
Example: for the path graph $2 - 1 - 3$ (with $a_{12}, a_{13} \ne 0$), starting at $v_1 = 2$ gives the order $2, 1, 3$, and the reordered matrix is tridiagonal, with bandwidth $1$.
The reverse ordering usually produces less fill-in in a [[Cholesky factorization|0WKG8CYY6A]], which is why it is the version used in sparse solvers.

## Explanations

### L1 human

A [[sparse matrix|JGACZYEEY7]] is easier to factor when its nonzero entries sit close to the diagonal.
The Cuthill–McKee algorithm renumbers the unknowns so that this happens.
It starts at one unknown and numbers its neighbours, then their neighbours, and so on, layer by layer, like ripples spreading on a pond.

### L2 human

The algorithm is a heuristic: it does not find the smallest possible bandwidth, which is an NP-hard problem, but it is fast and usually good.
It runs in time roughly proportional to the number of nonzero entries, up to the sorting by degree.
Reverse Cuthill–McKee is a standard preprocessing step before banded or envelope Cholesky factorization of symmetric sparse matrices.
