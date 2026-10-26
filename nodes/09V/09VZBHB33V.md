---
tag: 09VZBHB33V
kind: statement
role: proposition
name: Every walk contains a path
msc: [05C38]
uses: [0VJZM0F9YM, 0JDE56HWQ8]
sources:
  - url: https://en.wikipedia.org/wiki/Path_(graph_theory)
    locator: Walk, trail, and path
---

## Statement

Let $G$ be a [[graph|0JD5C82QMB]] and let $u, v$ be vertices of $G$.
Suppose that there is a [[walk|0VJZM0F9YM]] $W$ from $u$ to $v$.
Then there is a [[path|0JDE56HWQ8]] from $u$ to $v$ whose vertices and edges are vertices and edges of $W$.

## Remarks

Proof idea: if a walk visits a vertex $x$ twice, delete the closed part between the two visits. Each deletion makes the walk shorter, so the process stops with a path.
A consequence: a shortest walk from $u$ to $v$ is a path. Thus the [[distance|0WPZ5YPAGR]] can be defined with paths.

## Explanations

### L1 human

If you can walk from $u$ to $v$, you can also do it without visiting any place twice.
Whenever you come back to a place, cut out the loop that you just made.
