---
tag: M13GJHB8H9
kind: definition
name: Analytic signal
msc: [94A12, 44A15, 42A50]
defines: GVCRZH15Y0
uses: [NSCEBXM7ZM, SASP14MA1Z, DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_signal
---

## Definition

Let $f \in L^2(\R)$ be real-valued, an element of the [[$L^2$ space|SASP14MA1Z]].
Let $Hf$ be its [[Hilbert transform|NSCEBXM7ZM]].
The *analytic signal* of $f$ is the complex-valued function
$$f_a = f + i\, Hf.$$

## Remarks

With the [[Fourier transform|DPVM34ADZV]] $\hat f(\xi) = \int_\R f(x) e^{-2\pi i x \xi}\, dx$, one has $\widehat{Hf}(\xi) = -i \sgn(\xi) \hat f(\xi)$, so
$$\widehat{f_a}(\xi) = \big(1 + \sgn(\xi)\big) \hat f(\xi),$$
which is $2 \hat f(\xi)$ for $\xi > 0$ and $0$ for $\xi < 0$.
Since $f$ is real, $f = \operatorname{Re} f_a$, and $f_a$ is determined by $f$.
One writes $f_a(t) = A(t) e^{i\phi(t)}$ with $A = \abs{f_a}$ the instantaneous amplitude and $\phi$ the instantaneous phase.

Example: $f(x) = \frac{1}{1 + x^2}$.
Its Hilbert transform is $\frac{x}{1 + x^2}$, so $f_a(x) = \frac{1 + ix}{1 + x^2} = \frac{1}{1 - ix} = \frac{i}{x + i}$.
The function $z \mapsto \frac{i}{z + i}$ is holomorphic on the upper half-plane, as the definition predicts.

Non-example: the clause "real-valued" matters.
For the complex function $g = \frac{i}{x + i}$ one has $Hg = -i g$, so $g + i Hg = 2g \ne g$, and the real part of $g + iHg$ is $2 \operatorname{Re} g$, not $\operatorname{Re} g$.
