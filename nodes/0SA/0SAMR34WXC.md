---
tag: 0SAMR34WXC
kind: statement
role: proposition
name: Derivative of tangent
msc: [33B10, 26A24]
uses: [06T0HS14PP, 0BS0NJPKVE, 00R4MWW532, 0V2DV29EGT, 03H7WZ4T3K]
sources:
  - url: https://en.wikipedia.org/wiki/Differentiation_of_trigonometric_functions
    locator: From the quotient rule
---

## Statement

The tangent function is differentiable at every $x$ with $\cos x \ne 0$, and
$$\tan'(x) = \frac{1}{\cos^2 x} = 1 + \tan^2 x.$$

## Remarks

The [[quotient rule|0BS0NJPKVE]] gives $\tan' = \frac{\cos \cdot \cos - \sin \cdot (-\sin)}{\cos^2}$. The [[Pythagorean identity|03H7WZ4T3K]] turns the numerator into $1$.
The derivative is positive. So $\tan$ is strictly increasing on $(-\pi/2, \pi/2)$.
Mathlib states it as `Real.hasDerivAt_tan`.

## Explanations

### L1 human

The tangent function always rises, and it rises faster and faster near its asymptotes.
Its slope at $0$ is $1$.
