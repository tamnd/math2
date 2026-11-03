---
tag: RX1NWE1WMD
kind: definition
name: Dynkin quiver
msc: [16G20, 16G60]
defines: 92RQG73SC5
uses: [RE9YFFS3TS]
sources:
  - url: https://en.wikipedia.org/wiki/Gabriel%27s_theorem
---

## Definition

Let $Q$ be a finite [[quiver|RE9YFFS3TS]].
The *underlying graph* of $Q$ is the graph with vertex set $Q_0$ and one undirected edge between $s(a)$ and $t(a)$ for each arrow $a \in Q_1$.
The quiver $Q$ is a *Dynkin quiver* if its underlying graph is one of the simply laced [[Dynkin diagrams|CS73JZQS66]]:

1. $A_n$ for $n \ge 1$, a path with $n$ vertices;
2. $D_n$ for $n \ge 4$, a path with $n - 2$ vertices and two extra vertices joined to one end vertex;
3. $E_6$, $E_7$ or $E_8$, a path with $n - 1$ vertices and one extra vertex joined to the third vertex from one end, for $n = 6, 7, 8$.

## Remarks

Example: $1 \to 2 \leftarrow 3$ is a Dynkin quiver, since its underlying graph is the path with $3$ vertices, of type $A_3$.
Non-example: the Kronecker quiver, with two arrows $1 \to 2$, is not Dynkin, since its underlying graph has a double edge.
Non-example: a quiver with a loop, or whose underlying graph is a cycle, is not Dynkin.
A Dynkin quiver is connected and has no oriented cycles, and every orientation of a Dynkin diagram is a Dynkin quiver.
