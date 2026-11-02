---
tag: MSMD2BS9C5
kind: definition
name: Fourier integral operator
msc: [35S30, 58J40]
defines: EVS4JPEE45
uses: [AM4RNWVV4Q, FF27N0BWTP, DPVM34ADZV, CG9JEATW3Q, H8ACPTMX08]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_integral_operator
---

## Definition

Let $n \ge 1$ and $m \in \R$.
Let $\varphi \colon \R^n \times (\R^n \setminus \set{0}) \to \R$ be a smooth function such that:

1. $\varphi(x, t\xi) = t \, \varphi(x, \xi)$ for all $t > 0$, $x \in \R^n$ and $\xi \ne 0$.
2. $\det \big( \partial^2 \varphi / \partial x_j \partial \xi_k \big)_{j,k} \ne 0$ everywhere.

Let $a \in S^m(\R^n \times \R^n)$ be a symbol in the [[symbol class|AM4RNWVV4Q]] $S^m = S^m_{1,0}$ with $a(x, \xi) = 0$ for $\abs{\xi} \le 1$.
For $u$ in the [[Schwartz space|CG9JEATW3Q]] $\mathcal{S}(\R^n)$ with [[Fourier transform|DPVM34ADZV]] $\hat{u}$, put
$$T u(x) = \frac{1}{(2\pi)^n} \int_{\R^n} e^{i \varphi(x, \xi)} a(x, \xi) \, \hat{u}(\xi) \, d\xi.$$
The operator $T$ is a *Fourier integral operator* of order $m$ with *phase function* $\varphi$ and *amplitude* $a$.

## Remarks

Example: the phase $\varphi(x, \xi) = x \cdot \xi$ satisfies both conditions, with mixed Hessian the identity matrix, and gives the [[pseudo-differential operator|FF27N0BWTP]] $\mathrm{Op}(a)$.
For fixed $t \in \R$, the phase $\varphi(x, \xi) = x \cdot \xi + t \abs{\xi}$ also satisfies both conditions, and with a symbol $a$ equal to $1$ for $\abs{\xi} \ge 2$ it gives $e^{i t \sqrt{-\Delta}}$ up to a smoothing operator.

Non-example: $\varphi(x, \xi) = x \cdot \xi + \abs{\xi}^2$ fails the first condition, since it is not homogeneous of degree one in $\xi$; it is the phase of a Schrödinger evolution.

The general definition, due to Hörmander, allows phases $\varphi(x, y, \theta)$ with extra variables and works on manifolds.
There a Fourier integral operator is associated with a canonical relation, a [[Lagrangian submanifold|H8ACPTMX08]] of the product of the cotangent bundles, and it moves wave front sets along that relation.
