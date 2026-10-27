---
tag: 0R5HTV7REV
kind: definition
name: Directed graph
msc: [05C20]
defines: 0KFYGSHHF5
sources:
  - url: https://en.wikipedia.org/wiki/Directed_graph
    locator: Definition
inventory: [9B5F4MJKB0]
---

## Definition

A directed graph, or digraph, is a pair $D = (V, A)$ of a set $V$ and a relation $A \subseteq V \times V$.
The elements of $V$ are the vertices of $D$.
The elements of $A$ are the arcs, or directed edges, of $D$.
An arc $(u, v)$ goes from its tail $u$ to its head $v$.

## Remarks

With this definition a digraph can have loops $(v, v)$, and it has at most one arc from $u$ to $v$. Some authors exclude loops.
A [[graph|0JD5C82QMB]] is the same as a digraph whose relation is symmetric and irreflexive.
The out-degree of $v$ is the number of arcs with tail $v$, and the in-degree is the number of arcs with head $v$.

## Explanations

### L1 human

A directed graph is a graph whose lines are arrows.
One-way streets between crossings form a directed graph.
