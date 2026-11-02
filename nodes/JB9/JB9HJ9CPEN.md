---
tag: JB9HJ9CPEN
kind: definition
name: Dense order
msc: [06A05, 06A06]
defines: K4D3S1MBZH
uses: [011C29Q1S1]
sources:
  - url: https://en.wikipedia.org/wiki/Dense_order
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|011C29Q1S1]], and write $x < y$ for $x \le y$ and $x \ne y$.
The order is *dense* when, for all $x, y \in P$ with $x < y$, there is $z \in P$ with $x < z < y$.

## Remarks

The order of $\Q$ is dense: for rationals $x < y$, the rational $z = (x + y)/2$ satisfies $x < z < y$.
The order of $\Z$ is not dense: for $x = 0$ and $y = 1$ there is no integer strictly between.
A dense order has no [[covering pairs|EHXHC4ZNPA]].
A poset with at most one element is dense, since there is no pair $x < y$ to check.
The term is used mostly for [[total orders|0316AYH1SC]], where it is a basic property in the study of [[order types|28PE4GRFD7]].
The order topology of a dense total order with more than one element has no isolated points.

## Explanations

### L1 human

Dense means that any two different elements have room between them.
The rationals are dense; the integers are not.
