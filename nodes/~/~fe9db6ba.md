---
tag: ~fe9db6ba
kind: concept
name: Analytic continuation
aliases: [holomorphic-extension]
msc: [30B40]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_continuation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Analytic_continuation
    locator: Initial discussion
same_as:
  wikidata: Q485287
  wikipedia: Analytic continuation
---

## Summary

Let $U \subseteq V$ be open subsets of $\mathbb{C}$, with $U$ nonempty and $V$ a [[domain|~6387ec34]], and let $f$ be [[holomorphic|~1a187203]] on $U$.
An analytic continuation of $f$ to $V$ is a function $F$ that is holomorphic on $V$ with $F(z) = f(z)$ for each $z \in U$.
By the [[identity theorem|~4d17c114]], $f$ has at most one analytic continuation to $V$.

## Remarks

The geometric series $\sum_{n \ge 0} z^n$ is holomorphic on the unit disc, and $1/(1 - z)$ is its analytic continuation to $\mathbb{C} \setminus \{1\}$.
The Riemann zeta function $\sum_{n \ge 1} n^{-s}$ on $\operatorname{Re} s > 1$ has an analytic continuation to $\mathbb{C} \setminus \{1\}$.
Continuation along a path is a more general process. Its result can depend on the path: the [[logarithm|~bdd037c1]] continued once around $0$ changes by $2\pi i$.

## Explanations

### L1 human

A formula such as a power series often defines a function only on a small region.
Analytic continuation extends the function to a larger region in the only possible holomorphic way.
