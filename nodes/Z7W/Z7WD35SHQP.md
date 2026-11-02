---
tag: Z7WD35SHQP
kind: definition
name: Symmetric and self-reciprocal kernels
msc: [44A05, 44A15]
defines: RRZGEFJS7H
uses: [YCK709QB06, 9M0NNNFJGM, 7KGF78FGEF]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_transform
---

## Definition

Let $K \colon (0, \infty) \times (0, \infty) \to \C$ be the [[kernel|9M0NNNFJGM]] of an [[integral transform|YCK709QB06]]
$$(Tf)(x) = \int_0^\infty K(x, y)\, f(y)\, dy.$$
Let $A$ be a class of functions on which $T$ is defined, such as the [[Lebesgue space|7KGF78FGEF]] $L^2(0, \infty)$, with $T(A) \subseteq A$.

1. $K$ is *symmetric* if $K(x, y) = K(y, x)$ for all $x, y > 0$.
2. $K$ is *self-reciprocal* on $A$ (a *Fourier kernel*) if $T(Tf) = f$ for every $f \in A$; that is, $g = Tf$ implies $f = Tg$.

## Remarks

Example: $K(x, y) = \sqrt{2/\pi}\, \cos(xy)$ is symmetric, since $\cos(xy) = \cos(yx)$.
It is self-reciprocal on $L^2(0, \infty)$: this is the inversion theorem for the Fourier cosine transform, which follows from the Fourier inversion theorem applied to the even extension of $f$.
The sine kernel $\sqrt{2/\pi}\, \sin(xy)$ and the Hankel kernel $\sqrt{xy}\, J_\nu(xy)$ for $\nu \ge -1/2$, with $J_\nu$ the Bessel function of the first kind, are also symmetric and self-reciprocal.
Non-example: the Laplace kernel $e^{-xy}$ is symmetric but not self-reciprocal.
For $f(y) = e^{-y}$, $(Tf)(x) = 1/(1 + x)$, and $T(Tf)(x) = \int_0^\infty e^{-xy}/(1 + y)\, dy$ tends to $+\infty$ as $x \to 0^+$, while $f(x) \to 1$.
