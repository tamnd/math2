---
tag: ~09ecfec0
kind: statement
role: proposition
name: Dijkstra's algorithm fixes vertices in nondecreasing order of label
msc: [05C85, 05C38]
uses: [0WPZ5YPAGR]
about: [0WPZ5YPAGR]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_graphalgorithms_shortest-paths.ptx#L238
    locator: source/s_graphalgorithms_shortest-paths.ptx:238
---

## Statement

Run Dijkstra's algorithm on a graph with nonnegative edge weights, from a chosen start vertex, until it halts.
Each vertex $v$ that the algorithm makes permanent carries a final label $\delta(v)$, the length of a shortest path found to it, in the sense of [[distance in a graph|0WPZ5YPAGR]] for weighted edges.
Let $\sigma=(v_1,v_2,\dots,v_n)$ be the list of these vertices in the order in which the algorithm made them permanent.
Then the labels never decrease along this list:
$$\delta(v_1)\le \delta(v_2)\le \dots \le \delta(v_n).$$

## Remarks

The result says that the algorithm settles vertices from the nearest to the farthest.
It is a step in the proof that the final labels are the true distances from the start vertex.
