---
tag: A6SPEDH8BK
kind: statement
role: theorem
name: FKT algorithm
msc: [05C70, 05C85, 82B20]
uses: [0NC9R64TXP, 0NHK9MFFW9, NH5HWBPWS9, 0PBY4E9GQF]
about: [0NHK9MFFW9, NH5HWBPWS9]
sources:
  - url: https://en.wikipedia.org/wiki/FKT_algorithm
same_as:
  wikidata: Q5426031
  wikipedia: FKT algorithm
---

## Statement

Let $G = (V, E)$ be a finite graph with vertex set $V = \set{1, \dots, 2n}$.
Fix an orientation $\vec{G}$ of its edges.
Let $A$ be the $2n \times 2n$ [[skew-symmetric matrix|0PBY4E9GQF]] with $A_{uv} = 1$ if $u \to v$, $A_{uv} = -1$ if $v \to u$, and $A_{uv} = 0$ otherwise.
The orientation is *Pfaffian* if all [[perfect matchings|0NHK9MFFW9]] of $G$ contribute with the same sign to the [[Pfaffian|NH5HWBPWS9]] $\mathrm{Pf}(A)$.
Then $\abs{\mathrm{Pf}(A)}$ is the number of perfect matchings of $G$.

If $G$ is [[planar|0NC9R64TXP]], then:

1. $G$ has a Pfaffian orientation, and the number of perfect matchings of $G$ equals $\abs{\mathrm{Pf}(A)} = \sqrt{\det A}$.
2. Such an orientation can be found, and the number of perfect matchings computed, in time polynomial in $\abs{V}$.

## Remarks

The Pfaffian expands as a signed sum over perfect matchings.
The symmetric difference of two matchings is a union of disjoint even cycles, and the orientations around these cycles govern their relative sign.
Kasteleyn's condition is that, in a planar embedding, every bounded face has an odd number of edges oriented clockwise along its boundary; this forces all signs to agree.
The algorithm takes a spanning tree and orients its edges arbitrarily.
It then orients the remaining edges one at a time, in an order given by a spanning tree of the dual graph.
Each such edge closes a face, and its direction is chosen to fix the parity of that face.
The determinant is computed by Gaussian elimination in polynomial time.
With positive edge weights placed in $A$ instead of $\pm 1$, the same method computes the partition function of the [[dimer model|TJHVHD5SH5]].
Planarity cannot be dropped in general: counting perfect matchings of general graphs is #P-complete by Valiant's theorem.

## Explanations

### L1 human

Counting the ways to pair up the vertices of a graph along edges is hard in general.
For graphs that can be drawn in the plane without crossings, a clever choice of arrows on the edges turns the count into a determinant.
Determinants are fast to compute, so the count becomes easy.

### L2 human

The result is named after Fisher, Kasteleyn and Temperley, who found it in the early 1960s to count dimer coverings and domino tilings.
It shows the gap between the permanent, which counts matchings and is hard, and the determinant, which is easy.
It extends to graphs of bounded genus with a sum of several Pfaffians, and it underlies the exact solution of the planar [[Ising model|R0KGM32QN6]] through a dimer representation.
