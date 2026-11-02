---
tag: A0NP6HQNPX
kind: definition
name: Partially ordered ring
msc: ["06F25", "16W80"]
defines: 7EN0FYFTVE
uses: [0894J980RK, 011C29Q1S1]
sources:
  - url: https://en.wikipedia.org/wiki/Partially_ordered_ring
---

## Definition

Let $R$ be a [[ring|0894J980RK]] and let $\le$ be a [[partial order|011C29Q1S1]] on $R$.
The pair $(R, \le)$ is a *partially ordered ring* if for all $a, b, c \in R$:

1. if $a \le b$, then $a + c \le b + c$;
2. if $0 \le a$ and $0 \le b$, then $0 \le ab$.

## Remarks

Example: $\R^n$ with componentwise addition and multiplication and the componentwise order is a partially ordered ring.
Clause 1 holds coordinatewise, and the product of nonnegative real numbers is nonnegative, which gives clause 2.
Non-example: $\R$ with the reversed order $a \preceq b \iff a \ge b$ satisfies clause 1 but not clause 2.
Indeed $0 \preceq -1$, but $(-1)(-1) = 1$ and $0 \not\preceq 1$.
The set $P = \set{a \in R : 0 \le a}$ is the *positive cone*.
It satisfies $P + P \subseteq P$, $PP \subseteq P$ and $P \cap (-P) = \set{0}$, and the order is recovered as $a \le b \iff b - a \in P$.
