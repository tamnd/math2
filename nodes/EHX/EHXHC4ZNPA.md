---
tag: EHXHC4ZNPA
kind: definition
name: Covering relation
msc: [06A06]
defines: 4HHDPZ4BDY
uses: [011C29Q1S1]
sources:
  - url: https://en.wikipedia.org/wiki/Covering_relation
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|011C29Q1S1]], and write $x < y$ for $x \le y$ and $x \ne y$.
For $x, y \in P$, the element $y$ *covers* $x$, written $x \lessdot y$, when both conditions hold.

1. $x < y$.
2. There is no $z \in P$ with $x < z < y$.

The covering relation of $P$ is the set of pairs $(x, y)$ with $x \lessdot y$.

## Remarks

Order the positive integers by divisibility.
Then $2 \lessdot 6$: the only divisors of $6$ that $2$ divides are $2$ and $6$, so nothing lies strictly between.
In general $m \lessdot n$ exactly when $m \mid n$ and $n / m$ is prime.
The pair $2 < 8$ is not a cover, since $2 < 4 < 8$, so the second condition fails.
In a finite poset, $x < y$ holds if and only if there is a finite sequence $x = z_0 \lessdot z_1 \lessdot \cdots \lessdot z_k = y$ with $k \ge 1$.
So the covering relation determines a finite partial order.
This fails for infinite posets: in $\Q$ the covering relation is empty.

## Explanations

### L1 human

A cover is a single step up in the order, with no room for anything in between.
The lines of a Hasse diagram are exactly the covers.
