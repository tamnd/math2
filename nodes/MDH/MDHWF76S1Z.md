---
tag: MDHWF76S1Z
kind: statement
role: theorem
name: Grötzsch's theorem
msc: [05C15, 05C10]
uses: [0JD5C82QMB, 029JQEK15B, 0Y7VDAX8Q3]
about: [029JQEK15B, 0Y7VDAX8Q3]
sources:
  - url: https://en.wikipedia.org/wiki/Grötzsch's_theorem
same_as:
  wikidata: Q5612871
  wikipedia: Grötzsch's theorem
---

## Statement

Let $G$ be a finite [[planar graph|029JQEK15B]] that contains no triangle, that is, no cycle of length $3$.
Then $G$ is [[$3$-colourable|0Y7VDAX8Q3]].

## Remarks

An easy weaker bound comes from [[Euler's formula|0W1C598HMS]].
A triangle-free planar graph with $n \ge 3$ vertices has at most $2n - 4$ edges, so it has a vertex of degree at most $3$.
Induction then gives a colouring with $4$ colours.
Getting down to $3$ colours needs a finer induction, which proves a stronger statement about extending colourings from a short precoloured face.
Herbert Grötzsch proved the theorem in 1959, and Carsten Thomassen later gave shorter proofs.
Both hypotheses are needed.
Without the triangle condition the bound fails: $K_4$ is planar and needs $4$ colours.
Without planarity it fails too: the Grötzsch graph, with $11$ vertices, is triangle-free and needs $4$ colours.
For example, every planar bipartite graph is triangle-free, and indeed $2$-colourable.

## Explanations

### L1 human

The four colour theorem says that $4$ colours suffice for every planar graph.
If the graph has no triangles, Grötzsch's theorem says that $3$ colours suffice.
Triangles are the main reason a planar graph might need a fourth colour.

### L2 human

The theorem is a sharp statement about the interplay of girth and colouring on surfaces.
Grünbaum and Aksenov extended it to planar graphs with at most three triangles.
The precoloured-face strengthening used in the proof is typical of colouring proofs for planar graphs, as in the proof that planar graphs are $5$-choosable.
