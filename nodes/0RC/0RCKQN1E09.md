---
tag: 0RCKQN1E09
kind: definition
name: Cluster point of a sequence
aliases: [accumulation-point-of-a-sequence]
msc: [40A05]
defines: 0XTNJ6SVAC
uses: [0CTV783HYT, 0R8J3ZQMJS]
sources:
  - url: https://en.wikipedia.org/wiki/Accumulation_point
    locator: Accumulation points of sequences and nets
---

## Definition

Let $(a_n)$ be a [[real sequence|0CTV783HYT]] and let $c$ be a real number.
The number $c$ is a cluster point of $(a_n)$ if the following holds for each $\varepsilon > 0$ and each natural number $N$.
There is a natural number $n \ge N$ such that $|a_n - c| < \varepsilon$.

## Remarks

Equivalently, for each $\varepsilon > 0$ there are infinitely many indices $n$ with $|a_n - c| < \varepsilon$.
In $\mathbb{R}$, the number $c$ is a cluster point of $(a_n)$ if and only if some [[subsequence|0R8J3ZQMJS]] of $(a_n)$ converges to $c$.
The sequence $(-1)^n$ has the two cluster points $1$ and $-1$, and no limit.
For a bounded sequence, the [[limit superior|0P8BA7T7S5]] is the largest cluster point and the [[limit inferior|0H4R3RESGV]] is the smallest.

## Explanations

### L1 human

A cluster point is a number that the sequence visits again and again, as closely as you like.
A limit is a cluster point that the sequence approaches with all its late terms, not only with some of them.
