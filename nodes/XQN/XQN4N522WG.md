---
tag: XQN4N522WG
kind: definition
name: Pseudo-differential operator
msc: [35S05, 47G30]
defines: FF27N0BWTP
uses: [AM4RNWVV4Q, DPVM34ADZV, CG9JEATW3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudo-differential_operator
---

## Definition

Let $n \ge 1$ and $m \in \R$, and let $a \in S^m(\R^n \times \R^n)$ be a symbol of order $m$ in the [[symbol class|AM4RNWVV4Q]] $S^m = S^m_{1,0}$.
For $u$ in the [[Schwartz space|CG9JEATW3Q]] $\mathcal{S}(\R^n)$, let $\hat{u}(\xi) = \int_{\R^n} e^{-i x \cdot \xi} u(x) \, dx$ be its [[Fourier transform|DPVM34ADZV]].
The *pseudo-differential operator* with symbol $a$ is the operator $\mathrm{Op}(a) \colon \mathcal{S}(\R^n) \to \mathcal{S}(\R^n)$ given by
$$\mathrm{Op}(a) u(x) = \frac{1}{(2\pi)^n} \int_{\R^n} e^{i x \cdot \xi} a(x, \xi) \, \hat{u}(\xi) \, d\xi.$$
An operator of this form is a pseudo-differential operator *of order $m$*, and the set of them is denoted $\Psi^m(\R^n)$.

## Remarks

Example: let $P = \sum_{\abs{\alpha} \le k} a_\alpha(x) D^\alpha$ with $D^\alpha = (-i)^{\abs{\alpha}} \partial^\alpha$ and coefficients $a_\alpha$ smooth and bounded with all their derivatives.
By Fourier inversion, $D^\alpha u(x) = (2\pi)^{-n} \int e^{i x \cdot \xi} \xi^\alpha \hat{u}(\xi) \, d\xi$, so $P = \mathrm{Op}(p)$ with $p(x, \xi) = \sum_\alpha a_\alpha(x) \xi^\alpha \in S^k$.

Non-example: the operator $u \mapsto \mathcal{F}^{-1}\big( e^{i\abs{\xi}^2} \hat{u} \big)$, a Schrödinger evolution operator, is not a pseudo-differential operator of any order.
The symbol of an operator of this form is determined by the operator, here $e^{i \abs{\xi}^2}$, and it is in no class $S^m$.

The composition of $\mathrm{Op}(a)$ with $a \in S^m$ and $\mathrm{Op}(b)$ with $b \in S^{m'}$ is $\mathrm{Op}(c)$ with $c \in S^{m + m'}$, and $c - ab \in S^{m + m' - 1}$.
Operators of order $0$ are bounded on $L^2(\R^n)$, and operators of order $-\infty$ are smoothing.
The same formula with a symbol in $S^m_{\rho, \delta}$ defines the larger classes $\Psi^m_{\rho, \delta}$.
