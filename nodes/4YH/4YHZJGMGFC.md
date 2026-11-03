---
tag: 4YHZJGMGFC
kind: concept
name: Signal-flow graph
msc: [94C15, 93C05, 05C20]
sources:
  - url: https://en.wikipedia.org/wiki/Signal-flow_graph
same_as:
  wikidata: Q1786523
  wikipedia: Signal-flow graph
---

## Summary

A signal-flow graph is a [[directed graph|0KFYGSHHF5]] that encodes a system of linear equations.
Each node is a variable, and each edge carries a gain.
A node equals the sum, over its incoming edges, of the gain times the variable at the tail.
It gives a picture of how signals move through a linear system, including feedback loops.
The transfer from an input to an output can be read off the graph by [[Mason's gain formula|7RGCG5QWRB]], without writing the equations.

## Explanations

### L1 human

Draw each quantity of a system as a dot and each "this quantity feeds into that one, multiplied by $a$" as an arrow labelled $a$.
The value at a dot is what all its incoming arrows bring.
A loop of arrows is a feedback loop.
For example, the graph with arrows $u \to x$ of gain $1$, $x \to x$ of gain $\tfrac12$ and $x \to y$ of gain $3$ encodes $x = u + \tfrac12 x$ and $y = 3x$, so $y = 6u$.
