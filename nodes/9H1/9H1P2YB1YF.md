---
tag: 9H1P2YB1YF
kind: definition
name: Certainty equivalent
msc: [91B16, 91B06]
defines: FZNYZWR7MY
uses: [8C2N37XPJ8, 0WQNRCNY3M, 0X3WGX95FE, 011EJQWWJS, RJG35DZXTH]
sources:
  - url: https://en.wikipedia.org/wiki/Expected_utility_hypothesis
---

## Definition

Let $I \subseteq \R$ be an interval and let $u \colon I \to \R$ be a [[continuous|0X3WGX95FE]] and [[strictly increasing|011EJQWWJS]] utility function of an agent who follows the [[expected utility hypothesis|8C2N37XPJ8]].
Let $W$ be a random variable with finitely many values, all in $I$.
The *certainty equivalent* of $W$ is the unique number $c(W) \in I$ with
$$u(c(W)) = \mathbb{E}[u(W)].$$
The *risk premium* of $W$ is $\pi(W) = \mathbb{E}[W] - c(W)$.

## Remarks

The number $c(W)$ exists and is unique: $\mathbb{E}[u(W)]$ lies between the least and the largest value of $u(W)$, so the intermediate value theorem gives $c(W)$, and strict monotonicity gives uniqueness.
Example: for $u(w) = \ln w$ on $(0, \infty)$ and $W$ equal to $1$ or $4$ with probability $1/2$ each, $\mathbb{E}[u(W)] = \ln 2$, so $c(W) = 2$ and $\pi(W) = 2.5 - 2 = 0.5$.
Without strict monotonicity the number need not be unique: for $u$ constant on $I$, every point of $I$ satisfies the equation.
The agent is [[risk averse|RJG35DZXTH]] exactly when $\pi(W) \ge 0$ for every such $W$, and risk neutral exactly when $c(W) = \mathbb{E}[W]$ for every $W$.
In formulas, $c(W) = u^{-1}(\mathbb{E}[u(W)])$.
