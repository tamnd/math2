---
tag: 0R8JR0ARJ4
kind: example
name: Geometric series as a power series
msc: [13F25]
instance_of: [033WGN00BF]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_series
    locator: Connection to the power series
---

## Example

Let $R$ be a commutative ring and let $a \in R$.
In the ring $R[\![X]\!]$ of [[formal power series|072W67KFYK]],
$$(1 - aX) \sum_{n \ge 0} a^n X^n = 1.$$
Thus $1 - aX$ is a unit, and
$$\frac{1}{1 - aX} = \sum_{n \ge 0} a^n X^n.$$

## Remarks

The proof is a telescoping product. The coefficient of $X^n$ in the product is $a^n - a \cdot a^{n-1} = 0$ for $n \ge 1$, and it is $1$ for $n = 0$.
With $a = 1$, it gives $\frac{1}{1 - X} = 1 + X + X^2 + \dots$, the [[generating function|0HH6JX5WZZ]] of the constant sequence $1$.
Over $\mathbb{R}$ the same identity holds as a convergent series for $|aX| < 1$, but the formal identity needs no convergence.

## Explanations

### L1 human

Multiply $1 + aX + a^2 X^2 + \dots$ by $1 - aX$. Every term cancels with the next one, and only $1$ is left.
So the geometric series is the inverse of $1 - aX$.
