---
tag: 0WPZ5YPAGR
kind: definition
name: Distance in a graph
msc: [05C12]
defines: 0QV9VNNB4Z
uses: [0VJZM0F9YM, 0J8XE7W68F]
sources:
  - url: https://en.wikipedia.org/wiki/Distance_(graph_theory)
    locator: lead section
---

## Definition

Let $G$ be a [[graph|0JD5C82QMB]] and let $u, v$ be vertices of $G$.
If $v$ is [[reachable|0J8XE7W68F]] from $u$, the distance $d(u, v)$ is the smallest length of a [[walk|0VJZM0F9YM]] from $u$ to $v$.
If $v$ is not reachable from $u$, then $d(u, v) = \infty$.

## Remarks

A shortest walk is a [[path|0JDE56HWQ8]], so $d(u, v)$ is also the smallest length of a path. Such a path is a geodesic.
On a [[connected|0FFAYNMAJZ]] graph, $d$ is a metric: $d(u, v) = 0$ only for $u = v$, it is symmetric, and it satisfies the triangle inequality.

## Explanations

### L1 human

The distance between two vertices is the smallest number of edges that you must cross to go from one to the other.
In the cycle $C_6$, opposite vertices have distance $3$.
