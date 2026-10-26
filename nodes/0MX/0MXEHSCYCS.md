---
tag: 0MXEHSCYCS
kind: statement
role: theorem
name: Mantel's theorem
msc: [05C35]
uses: [03WKB2H474]
sources:
  - url: https://en.wikipedia.org/wiki/Turán's_theorem
    locator: "Mantel's theorem"
---

## Statement

Let $G$ be a finite simple [[graph|0JD5C82QMB]] with $n$ vertices and no cycle of length $3$.
Then $G$ has at most $\lfloor n^2/4 \rfloor$ edges.

## Remarks

The bound is sharp: the [[complete bipartite graph|0V0GC7BQAN]] $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$ has no triangle and has $\lfloor n^2/4 \rfloor$ edges.
The theorem is the case $r = 2$ of [[Turán's theorem|0JG1KZSPFZ]].

## History

Willem Mantel stated the theorem in 1907.

## Explanations

### L1 human

A graph on $n$ vertices without a triangle can have at most about a quarter of $n^2$ edges.
Split the vertices into two equal halves and join each pair across: this graph reaches the bound.
