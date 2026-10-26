---
tag: 0CDVDGWGEG
kind: statement
role: theorem
name: Degrees along an Eulerian trail
msc: [05C45]
uses: [0T0F6CCS9W, 0NNYDD1AVR]
sources:
  - url: https://en.wikipedia.org/wiki/Eulerian_path
    locator: Properties
---

## Statement

Let $G$ be a finite [[graph|0JD5C82QMB]], and let $W$ be an [[Eulerian trail|0NNYDD1AVR]] of $G$ from $u$ to $v$.
If $u = v$, then every vertex of $G$ has even [[degree|0T0F6CCS9W]].
If $u \neq v$, then $u$ and $v$ have odd degree and every other vertex has even degree.

## Remarks

Proof idea: each time $W$ passes through a vertex, it uses two edges at that vertex. Only the start and the end use one edge without a partner.
Thus a graph with an Eulerian trail has $0$ or $2$ vertices of odd degree. The [[Seven Bridges of Königsberg|0YCW781Q9D]] have $4$.

## Explanations

### L1 human

Count the edges at a vertex as a walk uses them.
Every visit in the middle of the walk uses one edge in and one edge out.
Only the first and last vertices can be left with an odd count.
