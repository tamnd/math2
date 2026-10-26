---
tag: 0KNAN9F27P
kind: definition
name: Maximum degree
msc: [05C07]
defines: 0FJY6G7FNA
uses: [0T0F6CCS9W]
sources:
  - url: https://en.wikipedia.org/wiki/Degree_(graph_theory)
    locator: Special values
---

## Definition

Let $G$ be a finite [[graph|0JD5C82QMB]] with a nonempty vertex set $V$.
The maximum degree of $G$ is
$$\Delta(G) = \max_{v \in V} \deg(v),$$
the largest [[degree|0T0F6CCS9W]] of a vertex of $G$.

## Remarks

The complete graph $K_n$ has $\Delta = n - 1$.
A [[greedy colouring|04AAKZNXHD]] uses at most $\Delta(G) + 1$ colours. [[Brooks' theorem|0Y4TV2D5RQ]] improves this to $\Delta(G)$ in most cases.

## Explanations

### L1 human

The maximum degree is the largest number of edges at any vertex.
In a star with one centre and $5$ leaves, the maximum degree is $5$.
