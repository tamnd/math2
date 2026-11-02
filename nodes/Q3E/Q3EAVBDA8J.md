---
tag: Q3EAVBDA8J
kind: definition
name: Linear extension
msc: [06A05, 06A07]
defines: W8DZ5KGGHN
uses: [0QV2JS9RJ3, 0FRXBVVR03]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_extension
---

## Definition

Let $X$ be a set and let $\le$ be a [[partial order|0QV2JS9RJ3]] on $X$.
A *linear extension* of $\le$ is a [[total order|0FRXBVVR03]] $\preceq$ on $X$ such that $x \le y$ implies $x \preceq y$ for all $x, y \in X$.

## Remarks

Example: on $\set{1, 2, 3, 6}$ ordered by divisibility, the usual order $1 < 2 < 3 < 6$ is a linear extension, because each divisor of a positive integer is at most that integer.
Non-example: the order $1 \prec 3 \prec 6 \prec 2$ is total but not a linear extension, because $2 \mid 6$ and yet $6 \prec 2$.
If $X$ is finite with $n$ elements, a linear extension is the same as a bijection $f \colon X \to \set{1, \ldots, n}$ with $f(x) < f(y)$ whenever $x < y$.
The number of linear extensions of a finite poset $P$ is often written $e(P)$.
A total order has exactly one linear extension, itself, and an antichain with $n$ elements has $n!$.
