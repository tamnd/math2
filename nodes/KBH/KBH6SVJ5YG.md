---
tag: KBH6SVJ5YG
kind: problem
name: Circulation problem
msc: [90C35, 90B10, 05C21]
uses: [ZSNXTW5E2K, 0KFYGSHHF5]
about: [ZSNXTW5E2K]
sources:
  - url: https://en.wikipedia.org/wiki/Circulation_problem
same_as:
  wikidata: Q5121696
  wikipedia: Circulation problem
history:
  posed_by: "unknown"
  first_stated: "unknown"
---

## Problem

Let $(V, E)$ be a finite [[directed graph|0KFYGSHHF5]].
Each edge $e \in E$ has a lower bound $l_e$ and an upper bound $u_e$ with $0 \le l_e \le u_e$, and a cost per unit $a_e \in \R$.
A *circulation* is a function $f \colon E \to \R$ such that:

1. $l_e \le f_e \le u_e$ for every edge $e$.
2. $\sum_{e \text{ enters } v} f_e = \sum_{e \text{ leaves } v} f_e$ for every vertex $v$.

The *circulation problem* asks whether a circulation exists and, if so, to find one.
The *minimum-cost circulation problem* asks for a circulation that minimizes $\sum_{e \in E} a_e f_e$.

## Remarks

There are no source and sink: flow is conserved at every vertex.
Hoffman's circulation theorem (1960) gives a test for existence.
A circulation exists if and only if, for every $S \subseteq V$, the lower bounds of edges entering $S$ sum to at most the upper bounds of edges leaving $S$.
Feasibility reduces to one [[maximum flow problem|EXMR7RYRTP]] after shifting each lower bound into supplies and demands.
The minimum-cost circulation problem is equivalent to the [[minimum-cost flow problem|899795HN7H]].
For instance, add an edge from $t$ to $s$ of cost $-1$ and unbounded capacity, and give all other edges cost $0$ and lower bound $0$.
Then a maximum $s$-$t$ flow is a minimum-cost circulation in the new graph.
With integer bounds, if a circulation exists then an integral one exists.

Example: on a directed triangle $x \to y \to z \to x$ with $l_e = 1$ and $u_e = 2$ on each edge, the constant flow $f_e = 1$ is a circulation.
If instead the edge $x \to y$ had $l = 3$, no circulation would exist, since then $3 \le f_{xy} = f_{yz} \le 2$.

## Explanations

### L1 human

A circulation is a flow that goes round and round with nothing entering or leaving the network.
Each pipe must carry at least a minimum amount and at most a maximum amount.
The question is whether such a flow exists, and which one is cheapest.
Many scheduling and transport problems become circulation problems after adding a return edge.
