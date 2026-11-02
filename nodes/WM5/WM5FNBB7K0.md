---
tag: WM5FNBB7K0
kind: statement
role: proposition
name: Gamma of one half
msc: [33B15]
uses: [0V3FZMVB4K]
about: [0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Particular_values_of_the_gamma_function
---

## Statement

Let $\Gamma$ be the [[gamma function|0V3FZMVB4K]].
Then
$$\Gamma\!\left(\tfrac12\right) = \sqrt{\pi}.$$

## Remarks

By definition $\Gamma(\tfrac12) = \int_0^\infty t^{-1/2} e^{-t}\, dt$.
The substitution $t = x^2$, $dt = 2x\,dx$, turns this into $2\int_0^\infty e^{-x^2}\,dx$, and the [[Gaussian integral|0DFT1GP1JP]] gives $2 \cdot \tfrac{\sqrt{\pi}}{2} = \sqrt{\pi}$.
Another proof uses the [[reflection formula|WF7KQAQTS2]] at $z = \tfrac12$: $\Gamma(\tfrac12)^2 = \pi/\sin(\tfrac{\pi}{2}) = \pi$, and $\Gamma(\tfrac12) > 0$.
With the functional equation it gives all half-integer values, for example $\Gamma(\tfrac32) = \tfrac{\sqrt\pi}{2}$ and $\Gamma(-\tfrac12) = -2\sqrt{\pi}$.
In Mathlib the statement is `Complex.Gamma_one_half_eq`.

## Explanations

### L1 human

The gamma function at one half equals the square root of $\pi$, about $1.7725$.
In factorial language, this says that "$(-\tfrac12)!$" is $\sqrt{\pi}$.

### L2 human

The value is the gamma-function form of the Gaussian integral $\int_{-\infty}^\infty e^{-x^2}\,dx = \sqrt{\pi}$.
It is the reason $\pi$ appears in the volume of balls in odd dimension and in the normalisation of the normal and chi-squared distributions.
