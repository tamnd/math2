---
tag: 5JYBXH9BP6
kind: concept
name: Finite Hilbert transform
msc: [44A15, "45E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_transform
---

## Summary

The finite Hilbert transform sends a function $f$ on the interval $(-1, 1)$ to the [[Cauchy principal value|0SYR10HD4R]] integral $\frac{1}{\pi}\, \mathrm{PV}\!\int_{-1}^{1} \frac{f(t)}{t - x}\, dt$.
Up to sign, it is the [[Hilbert transform|NSCEBXM7ZM]] of $f$ extended by zero, looked at only on the interval.
It is the singular part of most singular integral equations on an arc, such as the [[airfoil equation|W6Z6CWRE25]].
Unlike the Hilbert transform on the line, it is not invertible on $L^p(-1, 1)$ for any $1 < p < \infty$.
For $1 < p < 2$ it even sends a nonzero function to $0$.

## Explanations

### L1 human

Take a function on a segment and average it against $1/(t - x)$, which is large and changes sign at $t = x$.
The two sides of the singularity nearly cancel, and the principal value keeps what is left.
For example, the transform of $\sqrt{1 - t^2}$ is $-x$, and the transform of $1/\sqrt{1 - t^2}$ is $0$.
So the transform kills a nonzero function, which is why equations with it need an extra condition to have one solution.
