---
tag: ~eb39caba
kind: definition
name: Definite integral
msc: [26A42]
defines: ~fe945a04
uses: [~d843dc28]
sources:
  - url: https://en.wikipedia.org/wiki/Integral
    locator: Conventions
---

## Definition

Let $I$ be an interval, let $f \colon I \to \mathbb{R}$, and let $a, b \in I$.
Assume that $f$ is Riemann integrable on the closed interval between $a$ and $b$.
The definite integral of $f$ from $a$ to $b$ is the number $\int_a^b f(x) \, dx$ defined as follows.
If $a < b$, it is the [[Riemann integral|~d843dc28]] of $f$ over $[a, b]$.
If $a = b$, it is $0$. If $a > b$, it is $-\int_b^a f(x) \, dx$.

## Remarks

With this sign convention, $\int_a^b f + \int_b^c f = \int_a^c f$ holds for all $a, b, c$ in $I$.
The numbers $a$ and $b$ are the limits of integration, and $f$ is the integrand.
Mathlib writes the definite integral as `∫ x in a..b, f x`, through `intervalIntegral`.

## Explanations

### L1 human

The definite integral of $f$ from $a$ to $b$ is a number. It measures signed area under the graph between $a$ and $b$.
The order of the limits matters: swapping them changes the sign.
