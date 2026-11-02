---
tag: T4BCQHR68Y
kind: concept
name: Omega-complete partial order
msc: [06B35, 06A06, 68Q55]
specializes: [0QV2JS9RJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_partial_order
---

## Summary

An omega-complete partial order, or $\omega$-cpo, is a partially ordered set in which every increasing sequence has a supremum.
It is a weaker form of a [[directed-complete partial order|7TSXP95QN6]] that is enough for the fixed-point semantics of recursive programs.
Let the $\omega$-cpo have a least element $\bot$.
Then a monotone map that preserves suprema of increasing sequences has a least fixed point, the supremum of its iterates on $\bot$.

## Explanations

### L1 human

A computation that runs step by step produces a sequence of better and better approximations $x_0 \le x_1 \le x_2 \le \cdots$.
In an $\omega$-cpo such a sequence always has a limit, its least upper bound.
For example, in $\N \cup \set{\infty}$ every increasing sequence has a supremum, either its largest value or $\infty$.
Only countable increasing sequences are required, which makes the notion easy to use in programming language semantics.
