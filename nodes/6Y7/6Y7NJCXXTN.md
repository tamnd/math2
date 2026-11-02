---
tag: 6Y7NJCXXTN
kind: definition
name: Generalized convolution of an integral transform
msc: [44A35, 44A05]
defines: EAP9N3VEBV
uses: [YCK709QB06, ERP5737VZ1, FCKX8KFVGN, A2PMJG7J68]
sources:
  - url: https://en.wikipedia.org/wiki/Convolution
---

## Definition

Let $V$ be a complex vector space of functions, and let $\Omega$ be a set.
Let $T$ be an [[integral transform|YCK709QB06]], a linear map from $V$ to the space of complex functions on $\Omega$.
A *convolution* of $T$ is a bilinear map $\circledast \colon V \times V \to V$ such that
$$T(f \circledast g)(\omega) = (Tf)(\omega) \, (Tg)(\omega)$$
for all $f, g \in V$ and all $\omega \in \Omega$.

## Remarks

The identity $T(f \circledast g) = Tf \cdot Tg$ is called the factorization identity or convolution theorem of $T$.
If $T$ is injective, then $T$ has at most one convolution, namely $f \circledast g = T^{-1}(Tf \cdot Tg)$, and then $\circledast$ is automatically commutative and associative.
Variants allow a fixed weight function $\gamma$ on $\Omega$, with $T(f \circledast g) = \gamma \cdot Tf \cdot Tg$, or mix several transforms.

Example: for the Mellin transform $(\mathcal{M} f)(s) = \int_0^\infty x^{s-1} f(x) \, dx$, the [[Mellin convolution|A2PMJG7J68]]
$$(f \circledast g)(x) = \int_0^\infty f(x/y) \, g(y) \, \frac{dy}{y}$$
is a convolution.
Indeed, the substitution $x = uy$ gives $\int_0^\infty x^{s-1} \int_0^\infty f(x/y) g(y) \frac{dy}{y} dx = \int_0^\infty u^{s-1} f(u) \, du \int_0^\infty y^{s-1} g(y) \, dy$ when the integrals converge absolutely.
The [[convolution on the line|ERP5737VZ1]] is a convolution of the Fourier transform, and the [[convolution on the half-line|FCKX8KFVGN]] is one of the Laplace transform.

Non-example: the pointwise product $fg$ is not a convolution of the Fourier transform $\hat f(\xi) = \int_\R f(x) e^{-i x \xi} \, dx$ on $L^1(\R) \cap L^2(\R)$.
For $f = g = \mathbf{1}_{[0,1]}$, the product is $\mathbf{1}_{[0,1]}$ with $\hat{f}(0) = 1$, but the factorization identity would need $\widehat{fg}(\xi) = \hat f(\xi)^2$, and $\hat f(\xi)^2 \ne \hat f(\xi)$ at $\xi = \pi$, where $\hat f(\pi) = 2/(i\pi) \ne 0$.
