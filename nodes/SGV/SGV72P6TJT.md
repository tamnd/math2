---
tag: SGV72P6TJT
kind: definition
name: Stochastic programming
msc: [90C15]
defines: 2YW60J1GT6
uses: [0NFPJVJJHX, 0PNRKMRC55, 0WQNRCNY3M, NS0Q42Y3FX]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_programming
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0NFPJVJJHX]] and let $\xi$ be a [[random vector|0PNRKMRC55]] on it with values in $\Xi \subseteq \R^d$.
Let $X \subseteq \R^n$ be nonempty and let $F \colon X \times \Xi \to \R$ be such that $F(x, \xi)$ is integrable for each $x \in X$.
A *stochastic program* is the [[optimization problem|NS0Q42Y3FX]]
$$\min_{x \in X} \; \mathbb{E}[F(x, \xi)],$$
where $\mathbb{E}$ is the [[expected value|0WQNRCNY3M]].
In a *two-stage stochastic linear program*, $F(x, \xi) = c^T x + Q(x, \xi)$.
Here the recourse cost is
$$Q(x, \xi) = \min_{y \ge 0} \set{q(\xi)^T y : W y = h(\xi) - T(\xi) x},$$
with a fixed matrix $W$ and data $q(\xi)$, $h(\xi)$, $T(\xi)$ that depend on $\xi$.

## Remarks

The vector $x$ is the first-stage decision, chosen before $\xi$ is observed; $y$ is the second-stage decision, chosen after.
When $\xi$ takes finitely many values $\xi^1, \dots, \xi^N$ with probabilities $p_1, \dots, p_N$, and $X$ is a polyhedron, the two-stage program is one large linear program, the deterministic equivalent.

Example: the [[newsvendor model|RMQ4JB26AT]].
A seller orders $x \ge 0$ units at unit cost $c$ and sells $\min(x, \xi)$ units at price $p > c$, where the demand $\xi \ge 0$ is random.
Here $F(x, \xi) = c x - p \min(x, \xi)$.
If $\xi$ has a continuous distribution function $\Phi$, then $\frac{d}{dx} \mathbb{E}[F(x, \xi)] = c - p (1 - \Phi(x))$.
So an optimal order satisfies $\Phi(x) = (p - c)/p$.

Non-example: replacing $\xi$ by its mean $\mathbb{E}[\xi]$ and minimizing $F(x, \mathbb{E}[\xi])$ gives the expected value problem, not the stochastic program.
In the newsvendor model it orders exactly $\mathbb{E}[\xi]$, which is not optimal in general.
