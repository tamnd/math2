---
tag: XT32T13KBY
kind: problem
name: Heilbronn triangle problem
msc: [52C10, 51M04]
uses: [0CTNFGYMM2, 0RYTGBJAGN]
about: [0CTNFGYMM2]
sources:
  - url: https://en.wikipedia.org/wiki/Heilbronn_triangle_problem
same_as:
  wikidata: Q5699425
  wikipedia: Heilbronn triangle problem
history:
  posed_by: "Hans Heilbronn"
  first_stated: "1951"
---

## Problem

Let $n \ge 3$ and let $P$ be a set of $n$ points in the unit square $[0, 1]^2$.
Let $\delta(P)$ be the smallest area of a [[triangle|0CTNFGYMM2]] whose vertices are three points of $P$.
Three collinear points count as a triangle of area $0$.
Let $\Delta(n)$ be the supremum of $\delta(P)$ over all such $P$.
Determine the order of growth of $\Delta(n)$ as $n \to \infty$.

## Remarks

Hans Heilbronn conjectured that $\Delta(n) = O(1/n^2)$, with $O$ the [[big O notation|0RYTGBJAGN]]; the problem first appeared in print in a 1951 paper of Klaus Roth.
Erdős showed $\Delta(n) \ge c/n^2$ for a constant $c > 0$, so $1/n^2$ would be the right order.
Komlós, Pintz and Szemerédi disproved the conjecture in 1982 by showing $\Delta(n) \ge c \log n / n^2$.
On the other side, Roth proved $\Delta(n) = o(1/n)$, and Komlós, Pintz and Szemerédi proved $\Delta(n) \le n^{-8/7 + o(1)}$ in 1981.
In 2023 Cohen, Pohoata and Zakharov improved the exponent $-8/7$ for the first time.
The exact order of growth remains open.

## Explanations

### L1 human

Scatter $n$ points in a square so that every triangle formed by three of them has a large area.
Since there are many points, some triangle must be small; the question is how small.
The answer lies somewhere between about $(\log n)/n^2$ and a little below $n^{-8/7}$, and nobody knows exactly where.
