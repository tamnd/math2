---
tag: 02V2GYAC8P
kind: statement
role: corollary
name: Decreasing sequence bounded below converges
msc: [40A05]
uses: [0FM6N4R0VB]
sources:
  - url: https://en.wikipedia.org/wiki/Monotone_convergence_theorem
    locator: Convergence of a monotone sequence of real numbers
---

## Statement

Let $(a_n)$ be a decreasing real sequence: $a_n \ge a_{n+1}$ for all $n \in \mathbb{N}$.
Assume that $(a_n)$ is bounded below.
Then $(a_n)$ converges, and its limit is the infimum $\inf \{a_n : n \in \mathbb{N}\}$.

## Remarks

The proof applies the [[monotone convergence theorem|0FM6N4R0VB]] to the increasing sequence $(-a_n)$.
For example, $1/n$ decreases and is bounded below by $0$. Its limit is its infimum $0$.
Together, the two statements say that a monotone sequence converges if and only if it is bounded.

## Explanations

### L1 human

A decreasing sequence that cannot pass a floor must settle down.
It settles at the highest floor, which is the infimum of its terms.
