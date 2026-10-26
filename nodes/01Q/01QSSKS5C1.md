---
tag: 01QSSKS5C1
kind: statement
role: proposition
name: sin x / x tends to 1
msc: [33B10]
uses: [00R4MWW532, 0F1WR9C83K, 02KTRHQMHN]
sources:
  - url: https://en.wikipedia.org/wiki/Differentiation_of_trigonometric_functions
    locator: Limit of sin(θ)/θ as θ tends to 0
  - url: https://en.wikipedia.org/wiki/Sinc_function
    locator: Properties
---

## Statement

$$\lim_{x \to 0} \frac{\sin x}{x} = 1.$$

## Remarks

The quotient is the difference quotient of $\sin$ at $0$. So the limit is $\sin'(0) = \cos 0 = 1$, by the [[derivative of sine|00R4MWW532]].
The [[series|02KTRHQMHN]] gives $\frac{\sin x}{x} = 1 - \frac{x^2}{6} + \cdots$ for $x \ne 0$.
A geometric proof uses $\cos x \le \frac{\sin x}{x} \le 1$ for $0 < |x| < \pi/2$ and the squeeze theorem. Mathlib states it as `Real.tendsto_sin_div_nhdsNE_zero`.

## Explanations

### L1 human

For small angles in radians, $\sin x$ is almost equal to $x$.
The ratio of the two tends to $1$.
