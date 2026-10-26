---
tag: 01T3TMGTTE
kind: definition
name: Neighbourhood
msc: [05C07]
defines: 0ZCY0Z80B6
uses: [0JD5C82QMB]
sources:
  - url: https://en.wikipedia.org/wiki/Neighbourhood_(graph_theory)
    locator: lead section
---

## Definition

Let $G$ be a [[graph|0JD5C82QMB]] with vertex set $V$, and let $v \in V$.
The neighbourhood of $v$ is the set
$$N(v) = \{ u \in V : u \sim v \}$$
of the vertices adjacent to $v$.
The elements of $N(v)$ are the neighbours of $v$.

## Remarks

This is the open neighbourhood. It does not contain $v$, because no vertex is adjacent to itself. The closed neighbourhood is $N[v] = N(v) \cup \{v\}$.
The [[degree|0T0F6CCS9W]] of $v$ is $|N(v)|$ when $N(v)$ is finite.
In the cycle with vertices $1, 2, 3, 4, 5$ in this order, $N(1) = \{2, 5\}$.

## Explanations

### L1 human

The neighbours of a vertex are the vertices joined to it by an edge.
In a friendship graph, the neighbourhood of a person is the set of that person's friends.
