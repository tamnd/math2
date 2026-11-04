---
tag: WQPR4SSA29
kind: proof
name: Proof of Gallai–Hasse–Roy–Vitaver theorem
proves: CSS694B7NR
sources:
  - wikipedia: en:36620043@r1345571774
    locator: Gallai–Hasse–Roy–Vitaver theorem, section Proof
    note: adopted
    mention: wikipedia://en/36620043#9U0R
    sections: [Proof]
---

## Proof

To prove that the chromatic number is greater than or equal to the minimum number of vertices in a longest path, suppose that a given graph has a coloring with $k$ colors, for some number $k$. Then it may be acyclically oriented by numbering colors and by directing each edge from its lower-numbered endpoint to the higher-numbered endpoint. With this orientation, the numbers are strictly increasing along each directed path, so each path can include at most one vertex of each color, for a total of at most $k$ vertices per path.

To prove that the chromatic number is less than or equal to the minimum number of vertices in a longest path, suppose that a given graph has an orientation with at most $k$ vertices per simple directed path, for some number $k$. Then the vertices of the graph may be colored with $k$ colors by choosing a maximal acyclic subgraph of the orientation, and then coloring each vertex by the length of the longest path in the chosen subgraph that ends at that vertex. Each edge within the subgraph is oriented from a vertex with a lower number to a vertex with a higher number, and is therefore properly colored. For each edge that is not in the subgraph, there must exist a directed path within the subgraph connecting the same two vertices in the opposite direction, for otherwise the edge could have been included in the chosen subgraph; therefore, the edge is oriented from a higher number to a lower number and is again properly colored.

The proof of this theorem was used as a test case for a formalization of [[mathematical induction|0ASJVEFA9J]] by Yuri Matiyasevich.
