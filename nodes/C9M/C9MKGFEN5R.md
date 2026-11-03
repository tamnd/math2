---
tag: C9MKGFEN5R
kind: statement
role: proposition
name: Exchange principle for spanning trees
msc: [05C05]
uses: [0FQ5B8S1ZC, 0JD5C82QMB, 0JDE56HWQ8, 0MJ0JS72DZ]
about: [0S4ZEZM7KE]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_graphalgorithms_min-wt-span.ptx#L42
    locator: source/s_graphalgorithms_min-wt-span.ptx:42
---

## Statement

Let $G$ be a [[graph|0JD5C82QMB]] and let $T$ be a [[spanning tree|0FQ5B8S1ZC]] of $G$ with edge set $S$. Let $e = xy$ be an edge of $G$ that is not in $S$.

Then the following two claims hold.

1. There is exactly one [[path|0JDE56HWQ8]] $x = x_0, x_1, \dots, x_t = y$ in $T$ from $x$ to $y$. Every edge $x_i x_{i+1}$ of it lies in $S$.
2. For each $i$ with $0 \le i \le t-1$, put $f_i = x_i x_{i+1}$. Remove $f_i$ from $S$ and add $e$. The result is the edge set $S_i = (S \setminus \{f_i\}) \cup \{e\}$, and the graph on the same vertices with edge set $S_i$ is again a spanning tree of $G$.

## Remarks

The first claim holds because $T$ is a [[tree|0MJ0JS72DZ]], so two vertices are joined by one path. Adding $e$ to $T$ closes this path into a single cycle. Removing any edge of that cycle breaks the cycle and keeps the graph connected, which gives the second claim.
