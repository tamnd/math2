---
tag: 5KNAXNHRY6
kind: concept
name: Bromwich integral
msc: [44A10, "30E20"]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_Laplace_transform
---

## Summary

The Bromwich integral is the complex line integral $\frac{1}{2 \pi i} \int_{\gamma - i \infty}^{\gamma + i \infty} e^{s t} F(s) \, ds$ along a vertical line $\operatorname{Re} s = \gamma$ in the half-plane where a [[Laplace transform|0V49JEZW06]] $F$ is defined.
It is the standard integral formula for the [[inverse Laplace transform|07WBTX1MHA]]: under mild conditions it returns the function $f$ with $\mathcal{L}\{f\} = F$.
It also opens the way to computing inverse transforms by [[contour integration|06ZGPYTWK8]] and residues.

## Explanations

### L1 human

The Laplace transform packs a function of time into a function of a complex variable $s$.
The Bromwich integral unpacks it: it adds up the exponentials $e^{s t}$, weighted by $F(s)$, over a vertical line in the complex plane.
For example, for $F(s) = 1/s$ and any line $\operatorname{Re} s = \gamma > 0$, the integral gives $1$ for $t > 0$ and $0$ for $t < 0$, which is the step function whose transform is $1/s$.
The line must lie to the right of all singularities of $F$.
