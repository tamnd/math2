---
tag: FW2J04QXGZ
kind: definition
name: Feynman diagram
msc: [81T18, 81Q30]
defines: BS6HVNMTWC
uses: [0C62PZXX02, K9SR95P4NJ, HVGDXMPB29]
sources:
  - url: https://en.wikipedia.org/wiki/Feynman_diagram
---

## Definition

Fix the Euclidean [[quartic interaction|HVGDXMPB29]] on $\R^d$ with coupling $\lambda$ and [[propagator|K9SR95P4NJ]] $G$.
Let $n \ge 0$ and let $x_1, \dots, x_n \in \R^d$.
A *Feynman diagram* with $n$ external points is a finite [[multigraph|0C62PZXX02]] $\Gamma$, with self-loops allowed, with these properties.

1. It has $n$ external vertices, labelled $1, \dots, n$, each of degree $1$.
2. Its other vertices, the internal vertices, are unlabelled and have degree $4$.

Let $V$ be the set of internal vertices, and let $z_v \in \R^d$ be a variable for each $v \in V$.
For the external vertex $i$, put $z_i = x_i$.
The *Feynman amplitude* of $\Gamma$ is
$$I(\Gamma) = \frac{(-\lambda)^{\abs{V}}}{S(\Gamma)} \int_{(\R^d)^{V}} \prod_{e} G(z_{s(e)} - z_{t(e)}) \prod_{v \in V} dz_v.$$
Here the first product is over the edges $e$ of $\Gamma$, with endpoints $s(e)$ and $t(e)$.
The number $S(\Gamma)$ is the symmetry factor of $\Gamma$, defined below.

## Remarks

The symmetry factor $S(\Gamma)$ is the number of permutations of the internal vertices and of the half-edges at them that fix the external vertices and preserve the graph.
In perturbation theory, the $n$-point Schwinger function is formally the sum of $I(\Gamma)$ over all such diagrams in which every connected component contains an external vertex.
The components without external vertices (vacuum diagrams) cancel against the normalization of the measure.

Example: the diagram with no external vertex, one internal vertex and two self-loops (the "figure eight") is a Feynman diagram.
Its degree is $4$, and its symmetry factor is $8$: the two loops can be swapped, and each loop can be reversed.
This matches the count $3/4! = 1/8$, since there are $3$ ways to pair four legs at one vertex.

Non-example: a graph with an internal vertex of degree $3$ is not a Feynman diagram of the $\phi^4$ model; it fails clause 2.
It is a diagram of the $\phi^3$ model, whose vertices have degree $3$.

For other theories one changes the allowed degrees, labels edges by field types, and attaches the corresponding propagators and vertex factors.
In momentum space one assigns a momentum to each edge, imposes conservation at each vertex, and integrates over one momentum per independent cycle (loop).
