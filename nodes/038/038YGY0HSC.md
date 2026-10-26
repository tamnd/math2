---
tag: 038YGY0HSC
kind: definition
name: Chromatic polynomial
msc: [05C31, 05C15]
defines: 0B621RBVS9
uses: [0874138YP6]
sources:
  - url: https://en.wikipedia.org/wiki/Chromatic_polynomial
    locator: Definition
---

## Definition

Let $G$ be a finite [[graph|0JD5C82QMB]].
For each natural number $k$, let $P(G, k)$ be the number of [[colourings|0874138YP6]] of $G$ with the set of colours $\{1, \dots, k\}$.
There is a unique polynomial $P(G, x)$ whose value at each natural number $k$ is $P(G, k)$. It is the chromatic polynomial of $G$.

## Remarks

For the [[path graph|075WR6W3Y3]] $P_3$, $P(P_3, x) = x(x-1)^2$. For the [[complete graph|03WKB2H474]], $P(K_n, x) = x(x-1)\cdots(x-n+1)$.
For an edge $e$, the deletion–contraction rule says $P(G, x) = P(G - e, x) - P(G / e, x)$. Here $G / e$ merges the two ends of $e$.
The [[chromatic number|0C5M7AM6FH]] is the smallest positive integer $k$ with $P(G, k) > 0$.

## Explanations

### L1 human

The chromatic polynomial counts the proper colourings of a graph with $k$ colours, for each $k$.
George David Birkhoff introduced it in 1912 to study the four colour problem.
