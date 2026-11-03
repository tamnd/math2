---
tag: ZCG75PZ30B
kind: example
name: Karp's 21 NP-complete problems
msc: [68Q17]
instance_of: [JGZWHWA8P8]
uses: [CTK8AH98Z1, 3QKF32ZAKN, V0K79AD81V, 0BYX1D7C2E, 0AHKWBQSWV, 0HF30P75G4]
sources:
  - url: https://en.wikipedia.org/wiki/Karp%27s_21_NP-complete_problems
same_as:
  wikidata: Q1734364
  wikipedia: Karp's 21 NP-complete problems
---

## Example

In 1972 Richard Karp showed that 21 combinatorial decision problems are [[NP-complete|JGZWHWA8P8]].
In his naming they are:

1. satisfiability, 0-1 integer programming, clique, set packing, node cover, set covering, feedback node set;
2. feedback arc set, directed Hamilton circuit, undirected Hamilton circuit, satisfiability with at most 3 literals per clause;
3. chromatic number, clique cover, exact cover, hitting set, Steiner tree, 3-dimensional matching;
4. knapsack, job sequencing, partition, max cut.

Each problem lies in NP, since a proposed solution can be checked in polynomial time.
Hardness comes from a tree of [[polynomial-time reductions|V0K79AD81V]] rooted at [[satisfiability|3QKF32ZAKN]], which is NP-complete by the [[Cook–Levin theorem|CTK8AH98Z1]].

Check of one link: [[clique|0BYX1D7C2E]] reduces to node cover, which is [[vertex cover|0AHKWBQSWV]].
Let $G$ be a graph with $n$ vertices and let $\overline{G}$ be its complement.
A set $S$ of vertices is a clique in $G$ exactly when no edge of $\overline{G}$ has both ends in $S$.
That holds exactly when every edge of $\overline{G}$ has an end in the complement $V \setminus S$, so $V \setminus S$ is a vertex cover of $\overline{G}$.
So $G$ has a clique of size $k$ exactly when $\overline{G}$ has a vertex cover of size $n - k$.
So the map $(G, k) \mapsto (\overline{G}, n - k)$ is a polynomial-time reduction.
Undirected Hamilton circuit is the [[Hamiltonian cycle|0HF30P75G4]] problem.

## Explanations

### L1 human

Before 1972 only a few problems were known to be NP-complete.
Karp's paper showed that many problems that practitioners had long tried to solve fast, from scheduling jobs to colouring graphs, are all equally hard in this sense.
A fast algorithm for any one of the 21 would give fast algorithms for all of them.
The list made NP-completeness a central notion of computer science.
