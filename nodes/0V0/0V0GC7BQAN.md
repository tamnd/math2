---
tag: 0V0GC7BQAN
kind: example
name: Complete bipartite graph
msc: [05C99]
instance_of: [00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_bipartite_graph
    locator: Definition
same_as:
  wikidata: Q913598
  wikipedia: Complete bipartite graph
---

## Example

Let $m$ and $n$ be natural numbers.
The complete bipartite graph $K_{m,n}$ is the [[graph|0JD5C82QMB]] whose vertex set is a disjoint union $A \sqcup B$ with $|A| = m$ and $|B| = n$.
Two vertices are adjacent if and only if one is in $A$ and the other is in $B$.

## Remarks

$K_{m,n}$ has $m + n$ vertices and $mn$ edges.
It is [[bipartite|07DVHJ8N0A]] with parts $A$ and $B$. For $m, n \ge 1$ its [[chromatic number|0FJBBCXYPS]] is $2$.
$K_{1,n}$ is a star. [[$K_{3,3}$ is not planar|030A3FHN14]].

## Explanations

### L1 human

Split the vertices into two groups and join every vertex of one group to every vertex of the other group.
There are no edges inside a group.
