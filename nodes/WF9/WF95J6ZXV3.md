---
tag: WF95J6ZXV3
kind: definition
name: Rate function
msc: [60F10]
defines: 140N2PQSTE
uses: [0CQHFPGJ45, RN4G8SGP6P, 0ZCK8DQYN1, 0TVJZYB6SH]
sources:
  - url: https://en.wikipedia.org/wiki/Rate_function
---

## Definition

Let $\mathcal{X}$ be a [[topological space|0CQHFPGJ45]].
A *rate function* on $\mathcal{X}$ is a function $I \colon \mathcal{X} \to [0, \infty]$ that is [[lower semicontinuous|RN4G8SGP6P]].
Equivalently, for every $a \ge 0$, the sublevel set $\set{x \in \mathcal{X} : I(x) \le a}$ is [[closed|0ZCK8DQYN1]].
A rate function $I$ is *good* if every sublevel set $\set{x : I(x) \le a}$, for $a \ge 0$, is [[compact|0TVJZYB6SH]].

## Remarks

Example: $I(x) = x^2/2$ on $\R$ is a good rate function.
It is continuous, so lower semicontinuous, and $\set{I \le a} = [-\sqrt{2a}, \sqrt{2a}]$ is compact.

Example: on $\R$, let $I(x) = x \log x + (1 - x) \log(1 - x) + \log 2$ for $x \in [0, 1]$, with $0 \log 0 = 0$, and $I(x) = \infty$ otherwise.
It is a good rate function, the one for fair coin tossing in [[Cramér's theorem|RZZK51CXMN]].

Non-example: on $\R$, let $I(0) = 1$ and $I(x) = 0$ for $x \neq 0$.
Then $\set{I \le 0} = \R \setminus \set{0}$ is not closed, so $I$ is not lower semicontinuous.

Non-example of goodness: $I = 0$ on $\R$ is a rate function, but $\set{I \le 0} = \R$ is not compact.

In a large deviation principle, the rate function is unique when $\mathcal{X}$ is a regular topological space, for example a metric space.
A good rate function attains its infimum on every non-empty closed set.
