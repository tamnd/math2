---
tag: 080RWVVSB6
kind: statement
role: theorem
name: Linearity of the integral
msc: [26A42]
uses: [021WEM680W, 0HBY48G8G1]
sources:
  - url: https://en.wikipedia.org/wiki/Integral
    locator: Linearity
---

## Statement

Let $f, g \colon [a, b] \to \mathbb{R}$ be Riemann integrable, and let $\alpha, \beta \in \mathbb{R}$.
Then $\alpha f + \beta g$ is Riemann integrable on $[a, b]$, and
$$\int_a^b (\alpha f(x) + \beta g(x)) \, dx = \alpha \int_a^b f(x) \, dx + \beta \int_a^b g(x) \, dx.$$

## Remarks

The [[Riemann sums|0HBY48G8G1]] satisfy $S(\alpha f + \beta g, P, t) = \alpha S(f, P, t) + \beta S(g, P, t)$. Pass to the limit.
So the Riemann integrable functions on $[a, b]$ form a vector space, and the integral is a linear map on it.
Mathlib states additivity as `intervalIntegral.integral_add`.

## Explanations

### L1 human

The integral of a sum is the sum of the integrals.
Constant factors can move out of the integral.
