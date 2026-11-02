---
tag: STSV9XY3R5
kind: definition
name: Krull dimension of a poset
msc: [06A06, 13C15]
defines: EX7N9D1YCD
uses: [0QV2JS9RJ3, 0S8FE7ZMFM]
sources:
  - url: https://en.wikipedia.org/wiki/Krull_dimension
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
A finite [[chain|0S8FE7ZMFM]] $x_0 < x_1 < \cdots < x_n$ in $P$ has length $n$.
The *Krull dimension* $\dim P$ of a nonempty $P$ is the supremum of the lengths of the finite chains in $P$, an element of $\N \cup \set{\infty}$.
The empty poset has Krull dimension $-\infty$ by convention; some authors use $-1$ instead.

## Remarks

Example: the power set of $\set{1, \ldots, n}$ ordered by inclusion has Krull dimension $n$.
The chain $\varnothing \subset \set{1} \subset \cdots \subset \set{1, \ldots, n}$ has length $n$, and a longer chain would need two subsets of the same size.
Example: $\N$ with its usual order has Krull dimension $\infty$.
The dimension can be infinite even when every chain is finite: the disjoint union of chains of lengths $1, 2, 3, \ldots$ has no infinite chain but has dimension $\infty$.
For a commutative ring $R$, the [[Krull dimension of the ring|MVGBS3J1P7]] is the Krull dimension of its set of prime ideals ordered by inclusion.
