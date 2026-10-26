---
tag: 0JP0ZF57PN
kind: statement
role: theorem
name: Kőnig's theorem
msc: [05C70]
uses: [07DVHJ8N0A, 0Z87BHAFTB, 0KDADE9RQ8]
sources:
  - url: https://en.wikipedia.org/wiki/Kőnig's_theorem_(graph_theory)
    locator: Statement of the theorem
same_as:
  wikidata: Q897769
  wikipedia: Kőnig's theorem (graph theory)
---

## Statement

Let $G$ be a finite [[bipartite graph|07DVHJ8N0A]].
Then the largest number of edges in a [[matching|0Z87BHAFTB]] of $G$ is equal to the smallest number of vertices in a [[vertex cover|0KDADE9RQ8]] of $G$.

## Remarks

In every graph, a vertex cover has at least as many vertices as a matching has edges. Kőnig's theorem says that equality holds for bipartite graphs.
The theorem fails for other graphs. The triangle $K_3$ has matchings with $1$ edge only, but each vertex cover has $2$ vertices.

## History

Dénes Kőnig published the theorem in 1931.
Jenő Egerváry found it independently in the same year, in a more general form with weights.

## Explanations

### L1 human

In a bipartite graph, the most pairs that you can match at once is the same as the fewest vertices that touch every edge.
Each of the two numbers gives a certificate that the other one is optimal.
