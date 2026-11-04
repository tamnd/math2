---
tag: 18Z4GBYZDH
kind: proof
name: Proof of the number of edges of a complete graph
msc: [05C30]
proves: 05RN90E14Y
uses: [03WKB2H474, 0JD5C82QMB, 0BFMR2FQ8B, 092GEF38YD, 033KTKKRV6]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_graph
    locator: Properties
---

## Proof

1. The [[complete graph|03WKB2H474]] $K_n$ has vertex set $V = \set{1, \dots, n}$, and any two distinct vertices are adjacent.
2. Each edge of a [[graph|0JD5C82QMB]] is a $2$-element subset of $V$. By step 1, every $2$-element subset $\set{u, v}$ of $V$ is an edge of $K_n$.
3. So the edges of $K_n$ are exactly the $2$-element subsets of $V$. By the [[number of k-element subsets|0BFMR2FQ8B]], there are $\binom{n}{2}$ of them.
4. If $n \ge 2$, the [[factorial formula|033KTKKRV6]] gives $\binom{n}{2} = \frac{n!}{2!\,(n-2)!} = \frac{n(n-1)}{2}$.
5. Let $n \in \set{0, 1}$. The recursion that defines the [[binomial coefficient|092GEF38YD]] gives $\binom{0}{1} = \binom{0}{2} = 0$. Hence $\binom{1}{2} = \binom{0}{1} + \binom{0}{2} = 0$.
6. For $n \in \set{0, 1}$ also $\frac{n(n-1)}{2} = 0$. So in all cases $K_n$ has $\binom{n}{2} = \frac{n(n-1)}{2}$ edges.

## Idea

In $K_n$ every pair of distinct vertices is an edge, so counting edges is counting pairs. Choosing an ordered pair gives $n(n-1)$ options, and each unordered pair is counted twice.
