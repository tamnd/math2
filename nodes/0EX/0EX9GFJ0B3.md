---
tag: 0EX9GFJ0B3
kind: statement
role: theorem
name: The exponential function is its own derivative
msc: [33B10, 26A24]
uses: [0RMVS7RXZX, 0E8HNVBCSP, 0F1WR9C83K]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_function
    locator: Differential equation
---

## Statement

The [[exponential function|0RMVS7RXZX]] is differentiable on $\mathbb{R}$, and $\exp'(x) = \exp(x)$ for all real $x$.

## Remarks

By [[the sum rule|0E8HNVBCSP]], $\frac{\exp(x + h) - \exp(x)}{h} = \exp(x) \cdot \frac{\exp(h) - 1}{h}$. The series gives $\frac{\exp(h) - 1}{h} \to 1$ as $h \to 0$.
Term-by-term differentiation of the power series gives the same result.
The exponential function is the only solution of $f' = f$ with $f(0) = 1$. Mathlib states the derivative as `Real.hasDerivAt_exp`.

## Explanations

### L1 human

The slope of the graph of $e^x$ at each point equals its height there.
No other function with value $1$ at $0$ has this property.
