---
tag: X7S41PARF5
kind: statement
role: theorem
name: Bondy's theorem
msc: [05D05]
uses: [0C21Q694AG, 0ME21QN125]
about: [0C21Q694AG]
sources:
  - url: https://en.wikipedia.org/wiki/Bondy's_theorem
same_as:
  wikidata: Q3443426
  wikipedia: Bondy's theorem
---

## Statement

Let $n \ge 1$ and let $X$ be a set with $n$ elements.
Let $S_1, \ldots, S_n$ be $n$ distinct subsets of $X$.
Then there is an element $x \in X$ such that the sets $S_1 \setminus \set{x}, \ldots, S_n \setminus \set{x}$ are still distinct.

## Remarks

Suppose that no such $x$ exists.
Then for each $x \in X$ there are $i \ne j$ with [[symmetric difference|0ME21QN125]] $S_i \mathbin{\triangle} S_j = \set{x}$; join $S_i$ and $S_j$ by an edge labelled $x$.
This gives a graph on the $n$ sets with $n$ edges, all with distinct labels, so it contains a cycle.
Going around the cycle, the symmetric differences of the edges combine to $\emptyset$, but a symmetric difference of distinct singletons is not empty, a contradiction.

Example: $X = \set{1, 2}$ with $S_1 = \emptyset$ and $S_2 = \set{1}$.
Removing $x = 2$ leaves $\emptyset$ and $\set{1}$, which are still distinct.
The bound is sharp: for $X = \set{1, \ldots, n}$ the $n + 1$ sets $\emptyset, \set{1}, \ldots, \set{n}$ become non-distinct after removing any element $x$, since $\set{x}$ becomes $\emptyset$.

## Explanations

### L1 human

Describe $n$ different objects by $n$ yes/no features.
Bondy's theorem says that one of the features is redundant: you can drop it and still tell all the objects apart.
With $n + 1$ objects this can fail.

### L2 human

The theorem is a small result of extremal set theory with a short graph proof.
It says that $n$ distinct rows of a $0$–$1$ matrix with $n$ columns stay distinct after deleting a suitable column.
Its proof is a typical use of a graph to encode a family of sets.
