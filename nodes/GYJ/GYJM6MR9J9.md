---
tag: GYJM6MR9J9
kind: definition
name: Topological sorting
msc: [05C85, 05C20, 06A06]
defines: HMK2MT9FYZ
uses: [0KFYGSHHF5, 0Z05VCBQ7Y, 0FRXBVVR03, 0QV2JS9RJ3, W8DZ5KGGHN]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_sorting
---

## Definition

Let $G = (V, E)$ be a finite [[directed graph|0KFYGSHHF5]] with $n$ vertices.
A *topological sorting* of $G$ is an enumeration $v_1, v_2, \dots, v_n$ of $V$, each vertex listed exactly once, such that $i < j$ for every edge $(v_i, v_j) \in E$.

## Remarks

Example: let $V = \set{a, b, c, d}$ with edges $a \to b$, $a \to c$, $b \to d$ and $c \to d$.
The order $a, b, c, d$ is a topological sorting, since each of the four edges goes from an earlier vertex to a later one.
The order $a, c, b, d$ is another one, so a topological sorting need not be unique.

Non-example: the graph with edges $a \to b$, $b \to c$ and $c \to a$ has no topological sorting.
In any listing, the [[cycle|0Z05VCBQ7Y]] $a \to b \to c \to a$ has an edge that goes from a later vertex to an earlier one.

A finite directed graph has a topological sorting if and only if it has no directed cycle.
For such a graph, the topological sortings are exactly the [[linear extensions|W8DZ5KGGHN]], that is, compatible [[total orders|0FRXBVVR03]], of the reachability [[partial order|0QV2JS9RJ3]] on $V$.
Kahn's algorithm, which repeatedly removes a vertex with no incoming edge, finds one in time $O(n + \abs{E})$.
