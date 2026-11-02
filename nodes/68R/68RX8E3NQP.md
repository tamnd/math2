---
tag: 68RX8E3NQP
kind: definition
name: Null set
msc: [28A12, 28A05]
defines: VQQM4Y550T
uses: [P15VQS5DJ9, 01TQB88H4C, 0BXNDZFQME]
sources:
  - url: https://en.wikipedia.org/wiki/Null_set
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]].
A set $N \subseteq X$ is a *null set*, or a $\mu$-null set, if $N \in \Sigma$ and $\mu(N) = 0$.

## Remarks

For Lebesgue measure $\lambda$ on $\R$, every [[countable set|01TQB88H4C]] $\set{x_1, x_2, \ldots}$ is null.
Each point has measure $0$, since $\set{x} \subseteq [x - \varepsilon, x + \varepsilon]$ for every $\varepsilon > 0$, and countable additivity gives total $0$.
The [[Cantor set|0BXNDZFQME]] is also a Lebesgue null set, though it is uncountable.
The interval $[0, 1]$ is not a null set, since $\lambda([0, 1]) = 1$.
A countable union of null sets is null, by countable subadditivity.
Some authors call a set null when it is merely contained in a measurable set of measure $0$; the two notions agree when the measure is complete.
