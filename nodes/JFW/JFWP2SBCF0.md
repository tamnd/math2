---
tag: JFWP2SBCF0
kind: example
name: Matrices of graphs as linear algebra examples
msc: ["05C50", "15A06", "94C15"]
topics: [K0FNC6CWZN]
audience: ug1
instance_of: [08B9CX109G, 9DNFN8M83X]
illustrates: [0W4FSW1TVB]
uses: [00C0BR7D7H, 08B9CX109G, 9DNFN8M83X, 085CH3CYMX, 032Q9FB8MT, 0XC1RDBY7A, 0ZC9YTXZRY, 0PHDYNR24D, 0W4FSW1TVB]
sources:
  - url: https://en.wikipedia.org/wiki/Adjacency_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Incidence_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Laplacian_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kirchhoff%27s_circuit_laws
    locator: lead section
---

## Example

Four towns are joined by roads, or four junctions of a circuit are joined by wires, and the same picture answers two practical questions.
How many routes of a given length lead from one town to another?
If each wire is a resistor, what current flows when a battery is connected between two junctions?
Both questions become matrix computations once we store the network as a matrix.

Let $\Gamma$ be the [[graph|00C0BR7D7H]] with the vertices $1, 2, 3, 4$ and the edges $12$, $13$, $23$, $34$, which is a triangle with a pendant vertex $4$.
We use its adjacency matrix to count walks, and its incidence matrix to write Kirchhoff's laws for an electric network on $\Gamma$.

**Part 1: powers of the adjacency matrix count walks.**
The [[adjacency matrix|08B9CX109G]] has $a_{ij} = 1$ when $ij$ is an edge, and $a_{ij} = 0$ otherwise, so
$$A = \begin{pmatrix} 0 & 1 & 1 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}.$$

1. By [[matrix multiplication|032Q9FB8MT]], $(A^2)_{ij} = \sum_k a_{ik} a_{kj}$.
   A term is $1$ exactly when $i k$ and $k j$ are edges.
   So $(A^2)_{ij}$ is the number of [[walks|085CH3CYMX]] of length $2$ from $i$ to $j$.
2. By induction on $k$, $(A^k)_{ij}$ is the number of walks of length $k$ from $i$ to $j$.
   The reason is that a walk of length $k + 1$ is a walk of length $k$ from $i$ to some $l$, followed by an edge $l j$.
3. Here
$$A^2 = \begin{pmatrix} 2 & 1 & 1 & 1 \\ 1 & 2 & 1 & 1 \\ 1 & 1 & 3 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix}.$$
   The diagonal entry $(A^2)_{ii}$ counts the walks $i \to k \to i$, so it is the degree of $i$, and the degrees are $2, 2, 3, 1$.
4. The entry $(A^2)_{14} = 1$ counts the one walk $1 \to 3 \to 4$.
   The entry $(A^2)_{34} = 0$, because no walk of length $2$ joins the neighbors $3$ and $4$.
5. Next,
$$A^3 = \begin{pmatrix} 2 & 3 & 4 & 1 \\ 3 & 2 & 4 & 1 \\ 4 & 4 & 2 & 3 \\ 1 & 1 & 3 & 0 \end{pmatrix}.$$
   For example, $(A^3)_{13} = 4$ counts $1 \to 2 \to 1 \to 3$, $1 \to 3 \to 1 \to 3$, $1 \to 3 \to 2 \to 3$ and $1 \to 3 \to 4 \to 3$.
6. A closed walk of length $3$ goes around a triangle.
   Each triangle gives $6$ such walks, with $3$ starting vertices and $2$ directions.
   So the number of triangles is $\tr(A^3) / 6 = (2 + 2 + 2 + 0)/6 = 1$, by the definition of the [[trace|0XC1RDBY7A]].

**Part 2: the incidence matrix and Kirchhoff's laws.**
Orient each edge from the smaller to the larger vertex, so $e_1 = 1 \to 2$, $e_2 = 1 \to 3$, $e_3 = 2 \to 3$ and $e_4 = 3 \to 4$.
The [[incidence matrix|9DNFN8M83X]] $B$ has the entry $-1$ at the tail and $+1$ at the head of each edge, so
$$B = \begin{pmatrix} -1 & -1 & 0 & 0 \\ 1 & 0 & -1 & 0 \\ 0 & 1 & 1 & -1 \\ 0 & 0 & 0 & 1 \end{pmatrix}.$$

1. For a vector $y$ of currents on the edges, $(B y)_v$ is the current into $v$ minus the current out of $v$.
   So the current law at every vertex is $B y = 0$, or $B y = -s$ when external currents $s$ are fed in at the vertices.
2. Each column of $B$ has one $-1$ and one $+1$, so the four rows add up to the zero row.
   The graph is connected, and so $B$ has [[rank|0ZC9YTXZRY]] $3 = 4 - 1$.
3. By the [[rank-nullity theorem|0W4FSW1TVB]], the [[null space|0PHDYNR24D]] of $B$ has dimension $4 - 3 = 1$.
   It is spanned by $z = (1, -1, 1, 0)$, since $B z = (-1 + 1,\ 1 - 1,\ -1 + 1,\ 0) = 0$.
4. The vector $z$ is the cycle $1 \to 2 \to 3 \to 1$, which uses $e_1$ and $e_3$ forwards and $e_2$ backwards.
   So the currents that satisfy the current law without external sources are the currents around the cycle.
5. For potentials $\varphi$ at the vertices, $(B^{\mathsf T} \varphi)_e = \varphi_{\text{head}} - \varphi_{\text{tail}}$.
   The voltage law says that the voltage drops $u$ around every cycle add to $0$, that is, $u \cdot z = 0$.
   This holds for $u = B^{\mathsf T} \varphi$, because $z^{\mathsf T} B^{\mathsf T} \varphi = (B z)^{\mathsf T} \varphi = 0$.
6. With resistors of $1\ \Omega$ on all edges, Ohm's law gives $y = -B^{\mathsf T} \varphi$.
   The current law $B y = -s$ becomes $L \varphi = s$ with the Laplacian
$$L = B B^{\mathsf T} = \begin{pmatrix} 2 & -1 & -1 & 0 \\ -1 & 2 & -1 & 0 \\ -1 & -1 & 3 & -1 \\ 0 & 0 & -1 & 1 \end{pmatrix} = D - A,$$
   where $D = \operatorname{diag}(2, 2, 3, 1)$ is the matrix of degrees.
7. Feed $1$ A in at vertex $1$ and take it out at vertex $4$, so $s = (1, 0, 0, -1)$.
   With $\varphi_4 = 0$, the solution is $\varphi = (5/3, 4/3, 1, 0)$.
   Check: $L \varphi = (10/3 - 4/3 - 1,\ -5/3 + 8/3 - 1,\ -5/3 - 4/3 + 3,\ -1) = (1, 0, 0, -1)$.
8. The currents are $y = -B^{\mathsf T} \varphi = (1/3, 2/3, 1/3, 1)$ on $e_1, \dots, e_4$.
   At vertex $1$, the currents $1/3$ and $2/3$ leave, and together they carry the $1$ A fed in.
9. The voltage between vertices $1$ and $4$ is $5/3$ V for $1$ A, so the effective resistance is $5/3\ \Omega$.
   Check by the series and parallel rules: the paths $1$-$2$-$3$ ($2\ \Omega$) and $1$-$3$ ($1\ \Omega$) in parallel give $2/3\ \Omega$, and the edge $34$ adds $1\ \Omega$.

## Remarks

### What the example shows

Two standard matrices turn questions about a graph into linear algebra.
Matrix powers count walks, the rank of the incidence matrix counts components, and its null space is the space of cycles.
For a connected graph with $n$ vertices and $m$ edges, the cycle space has dimension $m - n + 1$, and here $4 - 4 + 1 = 1$.

### Add one edge

Add the edge $24$ to $\Gamma$.
Then $m = 5$, and the cycle space has dimension $2$.
The trace of $A^3$ becomes $12$, for the two triangles $123$ and $234$.

### Watch out

A walk may repeat vertices and edges, and $A^k$ counts walks, not paths.
For example, $(A^3)_{13} = 4$ includes $1 \to 3 \to 1 \to 3$, which goes along the same road three times.
The sign convention of $B$ is a second trap.
Changing the orientation of an edge changes the sign of a column of $B$, but it does not change $L = B B^{\mathsf T}$.

### Where the theory lives

The eigenvalues of $L$ are $0$, $1$, $3$ and $4$.
The eigenvalue $0$ is simple because the graph is connected.
By the matrix-tree theorem, the product $1 \cdot 3 \cdot 4 / 4 = 3$ is the number of spanning trees.
These facts, and the study of graphs through the eigenvalues of their matrices, belong to [[spectral graph theory|5JESM2ZN48]].
The physical laws themselves are [[Kirchhoff's circuit laws|9B0V41V2F8]], which Kirchhoff first described in 1845.
The same balance equations appear in the traffic and circuit problems of [[applications of linear systems|1QXFM0DNAH]].

### Try it

First, find the number of walks of length $2$ from vertex $2$ to vertex $4$.
Row $2$ of $A$ times column $4$ of $A$ gives $(A^2)_{24} = 1$, the walk $2 \to 3 \to 4$.

Second, find the effective resistance between vertices $1$ and $3$.
The path $1$-$2$-$3$ ($2\ \Omega$) and the edge $13$ ($1\ \Omega$) are in parallel, which gives $2 \cdot 1 / (2 + 1) = 2/3\ \Omega$.
The pendant edge $34$ carries no current, so it does not matter.

## Explanations

### L1 human

A network of points and lines can be stored as a table of $0$s and $1$s.
Multiplying the table by itself counts the ways to walk from one point to another in two steps.
For example, from point $1$ to point $4$ there is one walk of two steps, through point $3$.
A second table, with the directions of the lines, turns the rules of electric currents into equations that we can solve.

### L2 human

Here is a typical problem: count the closed walks of length $4$ from vertex $1$ in $\Gamma$.

1. Row $1$ of $A^2$ is $(2, 1, 1, 1)$, and column $1$ of $A^2$ is the same, since $A^2$ is symmetric.
2. So $(A^4)_{11} = \sum_k (A^2)_{1k} (A^2)_{k1} = 4 + 1 + 1 + 1 = 7$.
3. There are $7$ closed walks of length $4$ from $1$.
   Two of them are $1 \to 2 \to 1 \to 2 \to 1$ and $1 \to 3 \to 4 \to 3 \to 1$.

The typical use is to compute paths and connections in networks, and to set up the equations of electric and flow networks.

### L3 human

The incidence matrix is the boundary map from edges to vertices in the chain complex of the graph as a one-dimensional cell complex.
Its kernel is the first homology, the cycle space, and its cokernel has dimension equal to the number of components.
The Laplacian $L = B B^{\mathsf T}$ is a discrete analogue of the Laplace operator, and the second smallest eigenvalue of $L$ measures how well the graph is connected.
For directed graphs, $A^k$ still counts directed walks, and a damped and normalized version of the link matrix gives rankings such as [[PageRank|9ZPQYZ5NDP]].
