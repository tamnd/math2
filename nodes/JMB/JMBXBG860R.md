---
tag: JMBXBG860R
kind: definition
name: Ordered ring
msc: ["06F25", "12J15"]
defines: H6WXC7Q71A
uses: [0GYGHKX834, 0316AYH1SC, A0NP6HQNPX, 010JCV9J4E]
sources:
  - url: https://en.wikipedia.org/wiki/Ordered_ring
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $\le$ be a [[total order|0316AYH1SC]] on $R$.
The pair $(R, \le)$ is an *ordered ring* if for all $a, b, c \in R$:

1. if $a \le b$, then $a + c \le b + c$;
2. if $0 \le a$ and $0 \le b$, then $0 \le ab$.

## Remarks

So an ordered ring is a commutative [[partially ordered ring|A0NP6HQNPX]] whose order is total.
Example: $\Z$ with the usual order is an ordered ring, and so is every [[ordered field|010JCV9J4E]].
Example: $\Z[x]$ is an ordered ring if $p > 0$ means that the leading coefficient of $p$ is positive.
In any ordered ring, $a^2 \ge 0$ for all $a$: if $a \ge 0$ this is clause 2, and if $a < 0$ then $-a > 0$ by clause 1 and $a^2 = (-a)^2$.
Non-example: the ring $\Z[i]$ of Gaussian integers has no such order.
Squares would be nonnegative, so $1 = 1^2 \ge 0$ and $-1 = i^2 \ge 0$, and adding gives $0 \ge 1$; with $1 \ge 0$ this forces $1 = 0$.
