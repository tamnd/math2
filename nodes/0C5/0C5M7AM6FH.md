---
tag: 0C5M7AM6FH
kind: definition
name: Chromatic number
msc: [05C15]
defines: 0VHJRXNAAS
uses: [0Y7VDAX8Q3]
sources:
  - url: https://en.wikipedia.org/wiki/Graph_coloring
    locator: Vertex coloring
---

## Definition

Let $G$ be a finite [[graph|0JD5C82QMB]].
The chromatic number $\chi(G)$ is the smallest natural number $k$ such that $G$ is [[$k$-colourable|0Y7VDAX8Q3]].

## Remarks

For the [[complete graph|03WKB2H474]], $\chi(K_n) = n$. For the [[cycle graph|0QQ0F12962]] $C_n$, $\chi(C_n)$ is $2$ if $n$ is even and $3$ if $n$ is odd.
A [[greedy colouring|04AAKZNXHD]] shows that $\chi(G) \le \Delta(G) + 1$, where $\Delta(G)$ is the [[maximum degree|0KNAN9F27P]].
The chromatic number is at least the [[clique number|0WCKRBHFFD]].

## Explanations

### L1 human

The chromatic number is the least number of colours that you need to colour a graph properly.
For a map, it is the least number of colours that keeps neighbouring countries in different colours.
