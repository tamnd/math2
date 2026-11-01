---
tag: XMS1QRAQZC
kind: statement
role: lemma
name: Triangle removal lemma
msc: [05C35, 05D99]
uses: [00C0BR7D7H]
about: [SC5QB5F4TE]
sources:
  - url: https://en.wikipedia.org/wiki/Graph_removal_lemma
---

## Statement

For every real number $\varepsilon > 0$ there is a real number $\delta > 0$ with the following property.
Let $G$ be a finite simple [[graph|00C0BR7D7H]] with $n$ vertices that contains at most $\delta n^3$ triangles.
Then one can delete at most $\varepsilon n^2$ edges of $G$ so that the resulting graph has no triangle.

## Remarks

The standard proof applies the [[Szemerédi regularity lemma|ETMAPNQY7T]] with a small accuracy.
Delete the edges inside parts, between irregular pairs, and between pairs of low density; these are at most $\varepsilon n^2$ edges.
If a triangle survives, its three parts are pairwise regular and dense, and the counting lemma then gives more than $\delta n^3$ triangles.
The resulting $\delta$ is very small: the proof gives $1/\delta$ of tower type in $1/\varepsilon$.

A consequence: if every edge of a graph on $n$ vertices lies in exactly one triangle, then the graph has $o(n^2)$ edges.
Indeed, if it has $e$ edges, it has $e/3 \le n^2/6$ triangles, which is less than $\delta n^3$ for large $n$.
The triangles are edge-disjoint, so destroying them needs $e/3$ deletions, and the lemma gives $e/3 \le \varepsilon n^2$.
Applied to a graph built from a subset of $\Z/N\Z$, this gives [[Roth's theorem|E7H8NWXESF]] on three-term arithmetic progressions.

## Explanations

### L1 human

A graph with few triangles, compared with the $n^3$ triangles that are possible, is close to a graph with no triangles at all.
"Close" means that a small fraction of the $n^2$ edges is enough to destroy every triangle.
This sounds obvious but is not: the few triangles could share edges in a clever way, and the lemma says they cannot.

### L2 human

The lemma is the simplest case of the graph removal lemma.
There, any fixed graph $H$ takes the place of the triangle, and $\delta n^{|V(H)|}$ copies take the place of $\delta n^3$ triangles.
It is a central tool linking [[extremal graph theory|SC5QB5F4TE]] and [[additive combinatorics|3NM362A2JG]].
Its use for Roth's theorem shows how a statement about graphs can prove a statement about integers.
Better bounds for $\delta$ than tower type in this generality are a well-known open question.
