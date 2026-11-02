---
tag: HWHNY5854A
kind: concept
name: Mellin transform method
msc: [45H05, 44A15]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Summary

The Mellin transform method solves integral equations on $(0, \infty)$ whose kernel depends only on the ratio $x / t$ of the variables.
Such an integral is a [[Mellin convolution|A2PMJG7J68]], and the [[Mellin transform|N5PVGRJE1T]] turns it into a product.
The integral equation becomes an algebraic equation in a vertical strip of the complex plane, and the [[Mellin inversion theorem|XJWC13NY9E]] brings the solution back.
The method covers all kernels that are homogeneous of degree $-1$, such as $\frac{1}{x + t}$.
Such kernels arise in problems with scaling symmetry, such as wedges, cones and cracks.

## Explanations

### L1 human

The [[Fourier transform method|NRG03YP2PW]] works when the kernel is unchanged by shifts $x \mapsto x + c$.
The Mellin method works when the kernel is unchanged by stretches $x \mapsto c x$.
The substitution $x = e^{u}$ turns stretches into shifts, so the Mellin method is the Fourier method in logarithmic coordinates.
For example, $\int_0^\infty \frac{\varphi(t)}{x + t} \, dt = f(x)$ has a kernel that depends only on $x / t$ after taking out a factor $\frac{1}{t}$.
After the Mellin transform it reads $\frac{\pi}{\sin \pi s} \Phi(s) = F(s)$, which is solved by division.
