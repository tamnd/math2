---
tag: 0EZMAY1FQD
kind: example
name: x sin(1/x) is continuous at 0
msc: [26A15]
instance_of: [0X3WGX95FE]
uses: [0XMF00T4XQ, 0EEE2CZB2A]
sources:
  - url: https://en.wikipedia.org/wiki/Topologist%27s_sine_curve
    locator: Variants
---

## Example

Let $f(x) = x \sin(1/x)$ for $x \ne 0$, and let $f(0) = 0$.
Then $f$ is [[continuous|0EEE2CZB2A]] at $0$, and so $f$ is continuous on $\mathbb{R}$.
Indeed, $|f(x)| \le |x|$ for all $x$, so $f(x) \to 0$ as $x \to 0$ by the [[squeeze theorem|0XMF00T4XQ]].

## Remarks

The factor $x$ damps the oscillation of $\sin(1/x)$.
The function is not differentiable at $0$. The difference quotient $(f(x) - f(0))/x = \sin(1/x)$ has no limit.
The function $x^2 \sin(1/x)$ is [[differentiable with a discontinuous derivative|0WDAKKN4NC]].

## Explanations

### L1 human

The graph of $x \sin(1/x)$ oscillates infinitely often near $0$.
But it stays between the lines $y = x$ and $y = -x$, which meet at the origin.
