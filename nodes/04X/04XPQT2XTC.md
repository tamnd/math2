---
tag: 04XPQT2XTC
kind: statement
role: theorem
name: Every connected graph has a spanning tree
msc: [05C05]
uses: [0FFAYNMAJZ, 0FQ5B8S1ZC]
sources:
  - url: https://en.wikipedia.org/wiki/Spanning_tree
    locator: Definitions
---

## Statement

Let $G$ be a [[connected|0FFAYNMAJZ]] [[graph|0JD5C82QMB]].
Then $G$ has a [[spanning tree|0FQ5B8S1ZC]].

## Remarks

For a finite graph, a proof deletes edges that lie on cycles, one at a time. Such an edge is not a [[bridge|0D81KWH9ZM]], so the graph stays connected, and the process ends with a tree.
For an infinite graph, the proof uses Zorn's lemma, or a well-ordering of the vertices.
The converse also holds: a graph with a spanning tree is connected.

## Explanations

### L1 human

If a connected graph has a loop, you can remove one edge of the loop and the graph stays in one piece.
Repeat until there are no loops. What is left is a spanning tree.
