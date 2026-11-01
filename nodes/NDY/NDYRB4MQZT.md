---
tag: NDYRB4MQZT
kind: definition
name: Petersson inner product
msc: [11F11, 11F25]
defines: EMZTGD63V3
uses: [A50Y012RBP, GWKN5VG78A, VEKV1EM77B, X6XGGH5FPW, 0NB0AWGJBW]
sources:
  - url: https://en.wikipedia.org/wiki/Petersson_inner_product
---

## Definition

Let $k$ be an integer, and let $\mathbb{H}$ be the [[upper half-plane|X6XGGH5FPW]] with coordinates $\tau = x + iy$.
Let
$$\mathcal{F} = \set{\tau \in \mathbb{H} : \abs{\tau} \ge 1, \ \abs{x} \le 1/2}$$
be the standard fundamental domain of the [[modular group|VEKV1EM77B]].
Let $f$ and $g$ be [[modular forms|GWKN5VG78A]] of weight $k$ for $\mathrm{SL}_2(\Z)$.
Assume that $f$ or $g$ is a [[cusp form|A50Y012RBP]].
Their *Petersson inner product* is
$$\langle f, g \rangle = \int_{\mathcal{F}} f(\tau)\, \overline{g(\tau)}\, y^k \, \frac{dx\, dy}{y^2}.$$

## Remarks

The function $f \overline{g} y^k$ and the measure $dx\, dy / y^2$ are invariant under $\mathrm{SL}_2(\Z)$, so any fundamental domain gives the same value.
A cusp form decays like $e^{-2\pi y}$ as $y \to \infty$, so the integral converges.
On the space $S_k$ of cusp forms, $\langle \cdot, \cdot \rangle$ is a positive definite Hermitian [[inner product|0NB0AWGJBW]].
Example: $\langle \Delta, \Delta \rangle > 0$, since $\Delta$ has no zeros on $\mathbb{H}$, so the integrand $\abs{\Delta}^2 y^{12} \cdot y^{-2}$ is positive on $\mathcal{F}$.
Non-example: for $f = g = E_4$ the integral diverges, because $\abs{E_4}^2 y^4 \cdot y^{-2}$ tends to infinity like $y^2$ as $y \to \infty$; this is why one form must be a cusp form.
For a congruence subgroup $\Gamma$, the integral is taken over a fundamental domain of $\Gamma$, often divided by the index of $\Gamma$ in $\mathrm{SL}_2(\Z)$.
