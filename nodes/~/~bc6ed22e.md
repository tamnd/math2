---
tag: ~bc6ed22e
kind: definition
name: Distance in a graph
msc: [05C12]
defines: ~77a391ce
uses: [~8945d13d, ~fb98409f]
sources:
  - url: https://en.wikipedia.org/wiki/Distance_(graph_theory)
    locator: lead section
---

## Definition

Let $G$ be a [[graph|~3f82cef4]] and let $u, v$ be vertices of $G$.
If $v$ is [[reachable|~fb98409f]] from $u$, the distance $d(u, v)$ is the smallest length of a [[walk|~8945d13d]] from $u$ to $v$.
If $v$ is not reachable from $u$, then $d(u, v) = \infty$.

## Remarks

A shortest walk is a [[path|~ab8676be]], so $d(u, v)$ is also the smallest length of a path. Such a path is a geodesic.
On a [[connected|~c1305259]] graph, $d$ is a metric: $d(u, v) = 0$ only for $u = v$, it is symmetric, and it satisfies the triangle inequality.

## Explanations

### L1 human

The distance between two vertices is the smallest number of edges that you must cross to go from one to the other.
In the cycle $C_6$, opposite vertices have distance $3$.
