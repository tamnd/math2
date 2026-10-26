---
tag: 0HPHKCGEQ0
kind: statement
role: theorem
name: Generalised Stokes theorem
aliases: [stokes-cartan-theorem]
msc: [58C35]
uses: [004FRCXH6M, 0QHTX7WQEY, 0EKZW08FQ5, 0SD237FEJD, 0HR3N02317, 0AKRKVHW94, 0JX86PSSA9]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_Stokes_theorem
    locator: Formulation for smooth manifolds with boundary
  - url: https://en.wikipedia.org/wiki/Generalized_Stokes_theorem
    locator: Introduction
  - url: https://en.wikipedia.org/wiki/Generalized_Stokes_theorem
    locator: Classical (vector calculus) case
same_as:
  wikidata: Q10861254
  wikipedia: Generalized Stokes theorem
---

## Statement

Let $\Omega$ be an oriented smooth manifold of dimension $n$ with boundary $\partial \Omega$, and give $\partial \Omega$ the induced orientation.
Let $\omega$ be a smooth [[differential form|0QHTX7WQEY]] of degree $n - 1$ on $\Omega$ with compact support, and let $d\omega$ be its [[exterior derivative|004FRCXH6M]]. Then
$$\int_\Omega d\omega = \int_{\partial \Omega} \omega.$$

## Remarks

For $\Omega = [a, b]$ and a function $f$, the theorem is the fundamental theorem of calculus, $\int_a^b f'(x) \, dx = f(b) - f(a)$. The boundary point $a$ gets the negative orientation.
For a curve and a 0-form, it is the [[gradient theorem|0SD237FEJD]]. For a plane region and a 1-form, it is [[Green's theorem|0HR3N02317]].
For a surface in $\mathbb{R}^3$ and a 1-form, it is the classical [[Stokes' theorem|0AKRKVHW94]]. For a solid in $\mathbb{R}^3$ and a 2-form, it is the [[divergence theorem|0JX86PSSA9]].
The orientation and the compact support are needed so that both integrals are defined.

## Explanations

### L1 human

The integral of a derivative over a region equals the integral of the original form over the boundary of the region.
One formula covers the fundamental theorem of calculus and the three integral theorems of vector calculus.
