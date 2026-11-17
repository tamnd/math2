---
tag: WXNTPQGJ38
kind: statement
role: theorem
name: Unprovability of the graph minor theorem
msc: ["03F35", "05C83"]
topics: [T6FK1E7GJ1]
audience: research
uses: [WP3GDNWJJW, VYQ32ZBPEE, 12XRGBWH59, XVHKCX4F5Y, DC60FYCSPM, NH25G6GC07]
about: [WP3GDNWJJW, DC60FYCSPM]
history:
  first_stated: "1987"
  notes: "Friedman, Robertson and Seymour, 'The metamathematics of the graph minor theorem' (1987)."
sources:
  - wikipedia: en:351769@r1361823548
    locator: Robertson–Seymour theorem, section Finite form of the graph minor theorem
    note: adopted
    mention: wikipedia://en/351769#K9TO
    sections: [Statement]
  - url: https://en.wikipedia.org/wiki/Robertson–Seymour_theorem
    locator: Finite form of the graph minor theorem
inventory: [1GJ2V5WMKQ]
---

## Statement

The *size* of a finite graph is the number of its vertices plus the number of its edges.
Write $G \le H$ if $G$ is a [[minor|VYQ32ZBPEE]] of $H$.
Let $\mathrm{GM}$ be the following sentence.
For every $n \ge 1$ there is $m$ such that for every sequence $G_1, \dots, G_m$ of finite undirected graphs, where $G_i$ has size at most $n + i$, there are $i < j$ with $G_i \le G_j$.

**Theorem** (Friedman, Robertson and Seymour).

1. $\mathrm{GM}$ is true.
2. $\mathrm{GM}$, written in arithmetic, is not provable in $\Pi^1_1\text{-}\mathsf{CA}_0$, the subsystem of [[second-order arithmetic|DC60FYCSPM]] with $\Pi^1_1$ comprehension.
3. $\mathrm{GM}$ is provable in $\mathsf{ZFC}$, from the [[Robertson-Seymour theorem|WP3GDNWJJW]]. The Wikipedia article states that it is provable in systems much weaker than $\mathsf{ZFC}$.

The [[proof|NK9SK9FAY2]] derives part 1 from the Robertson-Seymour theorem, and it outlines part 2 with the cited lemmas marked.

## Remarks

### Why each hypothesis is needed

- The theory in part 2 is $\Pi^1_1\text{-}\mathsf{CA}_0$, much stronger than [[Peano arithmetic|MPSCREYC3M]] and than $\mathsf{ATR}_0$. The stronger theory $\mathsf{ZFC}$ proves $\mathrm{GM}$.
- The size bound $n + i$ is needed. Without it, the stars with $m, m - 1, \dots, 1$ edges form a sequence of length $m$ in which no graph is a minor of a later one.

### Consequences

- For each fixed $n$, the instance is a true $\Sigma_1$ sentence, so $\mathsf{PA}$ proves it. Only the sentence for all $n$ is unprovable in $\Pi^1_1\text{-}\mathsf{CA}_0$.
- The least $m$, as a function of $n$, is not provably total in $\Pi^1_1\text{-}\mathsf{CA}_0$.
- The infinite Robertson-Seymour theorem is not provable in $\Pi^1_1\text{-}\mathsf{CA}_0$ either, because part 1 follows from it by a tree argument that this system can carry out.

### Converse

The converse question is whether $\Pi^1_1\text{-}\mathsf{CA}_0$ proves the negation of $\mathrm{GM}$.
It does not, because $\mathrm{GM}$ is true and the system proves only true arithmetic sentences.

### Generalizations

- [[Friedman's finite form of Kruskal's theorem|12XRGBWH59]] is a statement of the same kind for trees with embeddings, and it is unprovable already in $\mathsf{ATR}_0$.
- The proof of part 2 goes through an extended Kruskal theorem for labelled trees, which is the part of the graph minor theorem that $\Pi^1_1\text{-}\mathsf{CA}_0$ cannot reach.
- Friedman used the same idea for simple subcubic graphs, and this gives the fast-growing function $\mathrm{SSCG}$, as the Wikipedia article states.

## History

Neil Robertson and Paul Seymour proved the graph minor theorem in the series of papers Graph Minors, published between 1983 and 2004.
In 1987 Harvey Friedman, Robertson and Seymour published "The metamathematics of the graph minor theorem", with the finite form and its unprovability.

## Explanations

### L1 human

A minor of a graph is what remains after deleting some vertices and edges and contracting some edges.
The graph minor theorem says that in every endless list of graphs, some graph is a minor of a later one.
The finite form says how long a list can be when the graphs are allowed to grow by one at each step.
The answer is always finite, but strong systems of axioms cannot prove that it exists for every starting size.

### L2 human

A small check, with $n = 1$, where the graph with no vertices counts as a graph.

1. $G_i$ has size at most $1 + i$. The graphs of size at most $2$ are the empty graph, one vertex $K_1$, and two vertices with no edge.
2. The empty graph is a minor of every graph. So it can only be the last graph of a bad sequence.
3. If $G_1 = K_1$, every later graph with a vertex has $G_1$ as a minor. So $G_2$ is empty, and the length is at most $2$.
4. If $G_1$ is two vertices with no edge, every later graph has at most one vertex. Then $G_2 = K_1$ and $G_3$ is empty gives length $3$.
5. No bad sequence has length $4$, by steps 2 to 4. So the least $m$ for $n = 1$ is $4$.

The trap: each instance is easy to check by a finite search, and only the uniform statement needs strong axioms.

### L3 human

Friedman, Robertson and Seymour showed that the graph minor theorem implies an extended Kruskal theorem for labelled trees.
That theorem codes ordinal notations up to the [[proof-theoretic ordinal|C72RBH0CDR]] of $\Pi^1_1\text{-}\mathsf{CA}_0$, so its finite form is not provable there.
The full proof by Robertson and Seymour uses much more than this, and the Wikipedia article states only that weaker systems than $\mathsf{ZFC}$ suffice.
