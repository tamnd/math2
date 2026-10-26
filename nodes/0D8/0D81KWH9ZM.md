---
tag: 0D81KWH9ZM
kind: definition
name: Bridge
msc: [05C40]
defines: 0BANA3XYPF
uses: [01VVP10MWJ]
sources:
  - url: https://en.wikipedia.org/wiki/Bridge_(graph_theory)
    locator: lead section
---

## Definition

Let $G$ be a [[graph|0JD5C82QMB]] and let $e$ be an edge of $G$.
Let $G - e$ be the graph that $G$ gives when $e$ is deleted and all vertices are kept.
The edge $e$ is a bridge of $G$ if $G - e$ has more [[connected components|01VVP10MWJ]] than $G$.

## Remarks

Let $e = uv$. Then $e$ is a bridge if and only if $u$ and $v$ are not [[reachable|0J8XE7W68F]] from each other in $G - e$. In this case, deleting $e$ increases the number of components by exactly one.
In a [[tree|0MJ0JS72DZ]] every edge is a bridge. In a [[cycle graph|0QQ0F12962]] no edge is a bridge.
[[Bridges are the edges on no cycle|0FHM8DB6PM]].

## Explanations

### L1 human

A bridge is an edge that holds the graph together: delete it, and one piece breaks into two.
Think of the only road between two towns.
