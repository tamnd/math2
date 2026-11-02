---
tag: KR1F39C0SP
kind: definition
name: Omega-complete partial order
msc: [06B35, 06A06, 68Q55]
defines: T4BCQHR68Y
uses: [0QV2JS9RJ3, 0R3H5PANRQ, 7TSXP95QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_partial_order
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
An *$\omega$-chain* in $P$ is a sequence $(x_n)_{n \in \N}$ with $x_0 \le x_1 \le x_2 \le \cdots$.
The poset $P$ is an *omega-complete partial order*, or *$\omega$-cpo*, if every $\omega$-chain in $P$ has a [[supremum|0R3H5PANRQ]] $\bigvee_n x_n$ in $P$.

## Remarks

Some authors also require a least element.
Every [[directed-complete partial order|7TSXP95QN6]] is an $\omega$-cpo, since the set of terms of an $\omega$-chain is directed.
Example: $\N \cup \set{\infty}$ with $n \le \infty$ for all $n$; an $\omega$-chain is either eventually constant, with supremum its final value, or unbounded in $\N$, with supremum $\infty$.
Non-example: $\N$ itself, since the chain $0 \le 1 \le 2 \le \cdots$ has no supremum.
The converse fails for the set $\omega_1$ of countable ordinals with their usual order.
It is an $\omega$-cpo, because a countable set of countable ordinals has a countable supremum.
But the directed set $\omega_1$ itself has no supremum in $\omega_1$.
