---
tag: SD89TZ1PHR
kind: definition
name: Fourier multiplier
msc: ["42B15", "42A45"]
defines: ZQEFCY61T7
uses: [DPVM34ADZV, SASP14MA1Z, HPZHRZ0502, NSCEBXM7ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplier_(Fourier_analysis)
---

## Definition

Let $n \ge 1$ and let $\mathcal{F} \colon L^2(\R^n) \to L^2(\R^n)$ be the [[Fourier transform|DPVM34ADZV]] on $L^2$, extended from $\mathcal{F} f(\xi) = \int_{\R^n} f(x) e^{-2\pi i x \cdot \xi}\, dx$ by the [[Plancherel theorem|HPZHRZ0502]].
Let $m \colon \R^n \to \C$ be a bounded measurable function.
The *Fourier multiplier* with symbol $m$ is the operator $T_m \colon L^2(\R^n) \to L^2(\R^n)$ given by
$$T_m f = \mathcal{F}^{-1}\big( m \cdot \mathcal{F} f \big).$$

## Remarks

By Plancherel, $T_m$ is a bounded linear operator on [[$L^2(\R^n)$|SASP14MA1Z]] with operator norm equal to $\norm{m}_{L^\infty}$.
It commutes with every translation, and conversely every bounded operator on $L^2(\R^n)$ that commutes with all translations is $T_m$ for a unique $m \in L^\infty(\R^n)$.

Example: on $\R$, the symbol $m(\xi) = -i \operatorname{sgn}(\xi)$ is bounded, and $T_m$ is the [[Hilbert transform|NSCEBXM7ZM]].
Example: for $t > 0$, the symbol $m(\xi) = e^{-4\pi^2 t \abs{\xi}^2}$ gives the heat semigroup: $u(t, \cdot) = T_m f$ solves $\partial_t u = \Delta u$ with $u(0, \cdot) = f$, because $\Delta$ acts on the Fourier side as multiplication by $-4\pi^2 \abs{\xi}^2$.

Non-example: the symbol $m(\xi) = 2\pi i \xi$ on $\R$ is not bounded; the corresponding operator is differentiation, which is not defined on all of $L^2(\R)$.
It is still a Fourier multiplier in the wider sense of an operator on the Schwartz space or on tempered distributions.

For the torus $\mathbb{T}^n$ the same definition uses a bounded sequence $(m(k))_{k \in \Z^n}$ that multiplies the Fourier coefficients.
The symbol $m$ is called an $L^p$ multiplier when $T_m$, restricted to $L^2 \cap L^p$, extends to a bounded operator on $L^p$.
