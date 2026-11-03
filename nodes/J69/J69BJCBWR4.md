---
tag: J69BJCBWR4
kind: definition
name: Chance-constrained programming
msc: [90C15]
defines: AM28DZ62KY
uses: [2YW60J1GT6, 0NFPJVJJHX, 0PNRKMRC55]
sources:
  - url: https://en.wikipedia.org/wiki/Chance_constrained_programming
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0NFPJVJJHX]] and let $\xi$ be a [[random vector|0PNRKMRC55]] with values in $\Xi \subseteq \R^d$.
Let $X \subseteq \R^n$, let $f \colon X \to \R$, and let $g \colon X \times \Xi \to \R^m$ be such that each event below is measurable.
Fix a risk level $\varepsilon \in (0, 1)$.
A *chance-constrained program* is the problem
$$\min_{x \in X} f(x) \quad \text{subject to} \quad P\big(g_i(x, \xi) \le 0 \text{ for } i = 1, \dots, m\big) \ge 1 - \varepsilon.$$
The constraint is a *joint* chance constraint.
Requiring $P(g_i(x, \xi) \le 0) \ge 1 - \varepsilon_i$ separately for each $i$ gives *individual* chance constraints.

## Remarks

Example: let $\xi$ be normal with mean $\mu$ and standard deviation $\sigma > 0$, and require $P(\xi \le x) \ge 1 - \varepsilon$ for a capacity $x \in \R$.
With $\Phi$ the standard normal distribution function, $P(\xi \le x) = \Phi((x - \mu)/\sigma)$.
So the constraint is equivalent to the linear constraint $x \ge \mu + \sigma \Phi^{-1}(1 - \varepsilon)$.

Non-example: the constraint $g(x, \mathbb{E}[\xi]) \le 0$, which uses only the mean, is not a chance constraint.
In the example it gives $x \ge \mu$, which is violated with probability $1/2$.

In general the feasible set of a chance constraint is not convex, even when each $g_i(\cdot, \xi)$ is linear.
