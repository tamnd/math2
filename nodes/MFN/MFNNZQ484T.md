---
tag: MFNNZQ484T
kind: statement
role: theorem
name: Strong perfect graph theorem
msc: [05C17, 05C75]
uses: [0JD5C82QMB, 1YZ7NV161A, 0V05FC4GKQ, 0RNMP6VCR2, 07CT9RDY7Q]
about: [1YZ7NV161A]
sources:
  - url: https://en.wikipedia.org/wiki/Strong_perfect_graph_theorem
same_as:
  wikidata: Q16680059
  wikipedia: Strong perfect graph theorem
---

## Statement

Let $G$ be a finite [[graph|0JD5C82QMB]], and let $\overline{G}$ be its [[complement|0RNMP6VCR2]].
An odd hole of a graph is an [[induced subgraph|0V05FC4GKQ]] that is a [[cycle|07CT9RDY7Q]] of odd length at least $5$.
Then $G$ is [[perfect|1YZ7NV161A]] if and only if neither $G$ nor $\overline{G}$ has an odd hole.

## Remarks

The complement of an odd hole is called an odd antihole, and graphs with neither are called Berge graphs.
The easy direction holds because an odd hole $C_{2k+1}$ with $k \ge 2$ has $\omega = 2$ and $\chi = 3$, and its complement has $\omega = k$ and $\chi = k + 1$.
The hard direction was conjectured by Claude Berge and proved by Maria Chudnovsky, Neil Robertson, Paul Seymour and Robin Thomas, with the proof published in 2006.
Their proof shows that every Berge graph lies in one of a few basic classes of perfect graphs or admits one of a few kinds of decomposition.
A smallest Berge graph that is not perfect can have neither property.
The theorem implies the weak perfect graph theorem, since the condition is symmetric in $G$ and $\overline{G}$.

## Explanations

### L1 human

A graph is perfect when, in every part of it, the colours needed equal the size of the largest clique.
The theorem says there are only two kinds of obstruction: an odd cycle of length at least five with no chords, or the complement of one.
If you cannot find either inside a graph, the graph is perfect.

### L2 human

The theorem turns a condition about all induced subgraphs into a finite list of forbidden patterns.
It was one of the main open problems of graph theory for about forty years.
Later work showed that Berge graphs, and hence perfect graphs, can be recognized in polynomial time.
