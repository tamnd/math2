---
tag: 0VTCABADBE
kind: example
name: Turán graph
msc: [05C35]
instance_of: [00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Turán_graph
    locator: lead section
same_as:
  wikidata: Q720459
  wikipedia: Turán graph
---

## Example

Let $n \ge r \ge 1$ be integers.
The Turán graph $T(n, r)$ has $n$ vertices, split into $r$ parts whose sizes differ by at most $1$.
Two vertices are adjacent if and only if they are in different parts.

## Remarks

Two vertices in the same part are not adjacent. Among any $r + 1$ vertices, two are in the same part, so $T(n, r)$ has no [[clique|0G52BPNPKG]] with $r + 1$ vertices.
The number of edges of $T(n, r)$ is $\left\lfloor \left(1 - \frac{1}{r}\right) \frac{n^2}{2} \right\rfloor$.
$T(n, 2)$ is the [[complete bipartite graph|0V0GC7BQAN]] $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$, and $T(n, n)$ is the [[complete graph|03WKB2H474]] $K_n$.

## Explanations

### L1 human

To build $T(n, r)$, split $n$ people into $r$ teams of almost equal size, and join two people when they are in different teams.
It is the graph with the most edges that has no clique of size $r + 1$.
