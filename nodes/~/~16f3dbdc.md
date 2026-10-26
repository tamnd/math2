---
tag: ~16f3dbdc
kind: statement
role: theorem
name: Solution formula for linear first-order equations
msc: [34A30]
uses: [~e63ef4b9, ~896b0dd0, ~40f94cf8]
sources:
  - url: https://en.wikipedia.org/wiki/Integrating_factor
    locator: Solving first order linear ordinary differential equations
  - url: https://en.wikipedia.org/wiki/Linear_differential_equation
    locator: First-order equation with variable coefficients
---

## Statement

Let $I$ be an open interval, let $p, q : I \to \mathbb{R}$ be continuous, let $x_0 \in I$ and let $y_0 \in \mathbb{R}$.
Let $P(x) = \int_{x_0}^{x} p(s)\, ds$ for $x \in I$.
Then the [[initial value problem|~40f94cf8]] $y' + p(x)\, y = q(x)$, $y(x_0) = y_0$ has exactly one solution on $I$, and it is
$$y(x) = e^{-P(x)} \left( y_0 + \int_{x_0}^{x} e^{P(s)}\, q(s)\, ds \right), \qquad x \in I.$$

## Remarks

Proof idea: $\mu = e^{P}$ is an [[integrating factor|~896b0dd0]], so a solution satisfies $(\mu y)' = \mu q$. Integrate from $x_0$ to $x$ and use $\mu(x_0) = 1$.
The solution exists on all of $I$. A linear equation has no solution that blows up inside the interval of continuity of $p$ and $q$.
Example: for $y' + y = 1$, $y(0) = 0$, the formula gives $y(x) = 1 - e^{-x}$.

## Explanations

### L1 human

The formula has two parts.
The term $y_0 e^{-P(x)}$ is the solution of the equation without the right side $q$.
The integral term adds the effect of $q$, collected over the time from $x_0$ to $x$.
