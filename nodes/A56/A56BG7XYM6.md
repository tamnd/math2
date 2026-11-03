---
tag: A56BG7XYM6
kind: problem
name: Utility maximization problem
msc: [91B42, 91B16]
uses: [GZZS4MTDG9, 0X3WGX95FE, 0TVJZYB6SH, 0VKKP8X6Q6]
about: [GZZS4MTDG9]
sources:
  - url: https://en.wikipedia.org/wiki/Utility_maximization_problem
same_as:
  wikidata: Q3274096
  wikipedia: Utility maximization problem
history:
  posed_by: "unknown"
  first_stated: "unknown"
---

## Problem

Let $n \ge 1$ be the number of goods and let $u \colon \R^n_{\ge 0} \to \R$ be a [[utility function|GZZS4MTDG9]].
Let $p \in \R^n$ be a price vector with all entries positive and let $w > 0$ be the wealth of the consumer.
The budget set is $B(p, w) = \set{x \in \R^n_{\ge 0} : p \cdot x \le w}$.
The problem asks for a bundle $x \in B(p, w)$ that maximizes $u(x)$ over $B(p, w)$.

## Remarks

If $u$ is [[continuous|0X3WGX95FE]], a solution exists, since $B(p, w)$ is closed and bounded, hence [[compact|0TVJZYB6SH]], and nonempty.
If $u$ is locally nonsatiated, every solution spends all the wealth: $p \cdot x = w$.
If $u$ is also strictly quasiconcave, the solution is unique; it is then called the Marshallian demand $x(p, w)$, and $u(x(p, w))$ is the indirect utility $v(p, w)$.
Let $u$ be differentiable, and let $x$ be an interior solution with $\nabla u(x) \ne 0$.
Then the method of [[Lagrange multipliers|0VKKP8X6Q6]] gives $\nabla u(x) = \lambda p$ for some $\lambda > 0$.
So the marginal rate of substitution between two goods equals their price ratio.
Example: for $u(x_1, x_2) = x_1^{a} x_2^{1 - a}$ with $0 < a < 1$, the solution is $x_1 = a w / p_1$ and $x_2 = (1 - a) w / p_2$, so the consumer spends the share $a$ of wealth on good $1$.
Without the positivity of prices the budget set can be unbounded, and a solution need not exist.

## Explanations

### L1 human

A shopper has a fixed amount of money and a list of prices.
Among all baskets of goods they can afford, they want the one they like best.
This is the basic problem of consumer theory, and its answer, the demand, tells how much of each good is bought at each price and income.
