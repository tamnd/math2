---
tag: 0FHM8DB6PM
kind: statement
role: theorem
name: Characterization of bridges
msc: [05C40]
uses: [07CT9RDY7Q, 0D81KWH9ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Bridge_(graph_theory)
    locator: lead section
---

## Statement

Let $G$ be a [[graph|0JD5C82QMB]] and let $e$ be an edge of $G$.
Then $e$ is a [[bridge|0D81KWH9ZM]] of $G$ if and only if $e$ is not an edge of any [[cycle|07CT9RDY7Q]] of $G$.

## Remarks

Proof idea: let $e = uv$. If $e$ lies on a cycle, the rest of the cycle is a path from $u$ to $v$ in $G - e$. Conversely, a path from $u$ to $v$ in $G - e$ together with $e$ gives a cycle.
A consequence: a graph is a forest if and only if every edge is a bridge.

## Explanations

### L1 human

An edge on a cycle is never a bridge: if you delete it, you can still go around the other way.
An edge on no cycle has no detour, so deleting it splits the graph.
