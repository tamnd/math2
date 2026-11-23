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

If the first graph of a list has size at most $2$ and each later graph may be one unit larger, then in every list of $4$ graphs some graph is a minor of a later one.
The finite graph minor theorem says that such a bound exists for every start, and $\Pi^1_1\text{-}\mathsf{CA}_0$ cannot prove it.

The *size* of a finite graph is the number of its vertices plus the number of its edges.
Write $G \le H$ if $G$ is a [[minor|VYQ32ZBPEE]] of $H$.
Let $\mathrm{GM}$ be the following sentence.
For every $n \ge 1$ there is $m$ such that for every sequence $G_1, \dots, G_m$ of finite undirected graphs, where $G_i$ has size at most $n + i$, there are $i < j$ with $G_i \le G_j$.

**Theorem** (Friedman, Robertson and Seymour).

1. $\mathrm{GM}$ is true.
2. $\mathrm{GM}$, written in arithmetic, is not provable in $\Pi^1_1\text{-}\mathsf{CA}_0$, the subsystem of [[second-order arithmetic|DC60FYCSPM]] with $\Pi^1_1$ comprehension.
3. $\mathrm{GM}$ is provable in $\mathsf{ZFC}$, from the [[Robertson-Seymour theorem|WP3GDNWJJW]].

The [[proof|NK9SK9FAY2]] derives part 1 from the Robertson-Seymour theorem, and it outlines part 2 with the cited lemmas marked.

## Remarks

### A first case by hand

We take $n = 1$, so $G_i$ has size at most $1 + i$, and we count the graph with no vertices as a graph.
A sequence is *bad* if no graph in it is a minor of a later one.
The graphs of size at most $2$ are the empty graph, one vertex $K_1$, and two vertices with no edge; an edge needs size $3$.

The empty graph is a minor of every graph, so it can only come last in a bad sequence.
If $G_1 = K_1$, then every later graph with a vertex has $G_1$ as a minor, so $G_2$ is empty and the length is $2$.
If $G_1$ is two vertices with no edge, then every later graph with two or more vertices has $G_1$ as a minor, by deleting edges.
So the best choice is $G_2 = K_1$ and $G_3$ empty, which gives length $3$.
No bad sequence has length $4$, and the least $m$ for $n = 1$ is $4$.

### Why each hypothesis is needed

The theory in part 2 is $\Pi^1_1\text{-}\mathsf{CA}_0$, which is stronger than [[Peano arithmetic|MPSCREYC3M]] and than $\mathsf{ATR}_0$.
The stronger theory $\mathsf{ZFC}$ proves $\mathrm{GM}$.

The size bound $n + i$ is needed.
Without it, the stars with $m, m - 1, \dots, 1$ edges form a sequence of length $m$ in which no graph is a minor of a later one, because a minor never has more edges than the graph it comes from.

### What it gives you

For each fixed $n$, the instance is a true $\Sigma_1$ sentence, so $\mathsf{PA}$ proves it by a finite search.
Only the sentence for all $n$ is unprovable in $\Pi^1_1\text{-}\mathsf{CA}_0$, and so the least $m$, as a function of $n$, is not provably total there.

The infinite Robertson-Seymour theorem is not provable in $\Pi^1_1\text{-}\mathsf{CA}_0$ either.
The reason is that $\mathrm{GM}$ follows from it by a compactness argument that this system can carry out.

The converse question asks whether $\Pi^1_1\text{-}\mathsf{CA}_0$ proves the negation of $\mathrm{GM}$.
It does not, because $\mathrm{GM}$ is true and the system proves only true arithmetic sentences.

### Generalizations

[[Friedman's finite form of Kruskal's theorem|12XRGBWH59]] is a statement of the same kind for trees with embeddings, and it is unprovable already in the weaker system $\mathsf{ATR}_0$.
The proof of part 2 goes through an extended Kruskal theorem for labeled trees with a gap condition.
That extended theorem follows from the graph minor theorem, and it is the part that $\Pi^1_1\text{-}\mathsf{CA}_0$ cannot reach.

### Watch out

A minor is not a subgraph.
Contracting an edge merges its two ends, so the cycle with four vertices has the triangle as a minor, although it has no triangle as a subgraph.
So the minor relation holds more often than "is a subgraph of", and a bad sequence for minors is harder to build.

### Try it

First, explain why the empty graph can only be the last graph of a bad sequence.
It is a minor of every graph, by deleting all vertices, so any graph after it would make the sequence good.

Second, find the least $m$ for the variant where $G_i$ has size at most $i$.
Then $G_1$ is $K_1$ or empty, so the longest bad sequence is $K_1$ followed by the empty graph, and the least $m$ is $3$.

## History

Neil Robertson and Paul Seymour proved the graph minor theorem in the series of papers Graph Minors, published from 1983 to 2004.
In 1987 Harvey Friedman, Robertson and Seymour published "The metamathematics of the graph minor theorem", with the finite form and its unprovability.

## Explanations

### L1 human

A minor of a graph is what remains after deleting some vertices and edges and merging the two ends of some edges.
The graph minor theorem says that in every endless list of graphs, some graph is a minor of a later one.
The finite form says how long a list can be when the graphs may grow by one at each step.
The answer is always finite, but strong systems of axioms cannot prove that it exists for every starting size.

### L2 human

We find the least $m$ for $n = 2$, where $G_i$ has size at most $2 + i$.
The best start avoids small graphs that many later graphs contain, so we try $G_1$ to be three vertices with no edge, of size $3$.
Every later graph must have at most two vertices.
We take $G_2$ to be the edge $K_2$, of size $3$, then $G_3$ two vertices with no edge, then $G_4 = K_1$ and $G_5$ empty.
Each of these avoids the earlier ones, since each has fewer vertices or fewer edges than every earlier graph.
So the least $m$ for $n = 2$ is at least $6$.

The pattern is the same as for trees: a bad sequence begins with a graph that forbids a whole family, and then uses up the smaller graphs.
The trap is to think that the bound must be easy to find for every $n$; each instance is a finite search, but no single method in $\Pi^1_1\text{-}\mathsf{CA}_0$ works for all $n$.

### L3 human

Friedman, Robertson and Seymour showed that the graph minor theorem implies an extended Kruskal theorem for labeled trees.
That theorem codes ordinal notations up to the [[proof-theoretic ordinal|C72RBH0CDR]] of $\Pi^1_1\text{-}\mathsf{CA}_0$, so its finite form, and with it $\mathrm{GM}$, is not provable there.
The proof of the graph minor theorem by Robertson and Seymour is very long, and it uses far more than the extended Kruskal theorem.
