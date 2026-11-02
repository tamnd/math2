---
tag: JP9VD777AE
kind: definition
name: Inverse transform
msc: [44A05]
defines: GC96MQC0PP
uses: [YCK709QB06, 0W766JAPSN]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_transform
---

## Definition

Let $T$ be an [[integral transform|YCK709QB06]], defined on a class $A$ of functions, and assume that $T$ is injective on $A$.
The *inverse transform* of $T$ is the map $T^{-1} \colon T(A) \to A$ that sends $F$ to the unique $f \in A$ with $Tf = F$.
It is the [[inverse function|0W766JAPSN]] of $T$ viewed as a bijection from $A$ onto $T(A)$.

## Remarks

Example: the Fourier transform $\hat f(\xi) = \int_\R f(x) e^{-2\pi i x \xi}\, dx$ is a bijection of the Schwartz space onto itself, and its inverse is $f(x) = \int_\R \hat f(\xi) e^{2\pi i x \xi}\, d\xi$.
So here the inverse transform is again an integral transform, with kernel $e^{2\pi i x \xi}$.
Non-example: the transform $Tf(u) = \int_0^1 f(t)\, dt$ with kernel $K(t, u) = 1$ on $[0,1] \times \R$ has no inverse transform on the continuous functions, since $f(t) = 0$ and $f(t) = 2t - 1$ both have $Tf = 0$.
When the inverse is an integral transform with kernel $H$, one writes $f(t) = \int F(u)\, H(u, t)\, du$, and $(f, F)$ is a transform pair.
