---
tag: D5T6Q6MVXJ
kind: definition
name: Cosmological horizon
msc: ["83F05"]
defines: CZ5PH864FG
uses: [ECJMS4VDTF, J70F32P86W]
sources:
  - url: https://en.wikipedia.org/wiki/Cosmological_horizon
---

## Definition

Let $g = -dt^2 + a(t)^2 \gamma_k$ be a [[Friedmann–Lemaître–Robertson–Walker metric|ECJMS4VDTF]] on $(t_b, t_\infty) \times \Sigma$, with $-\infty \le t_b < t_\infty \le \infty$ and [[scale factor|J70F32P86W]] $a$, in units with $c = 1$.
Fix a comoving observer and a time $t$ in $(t_b, t_\infty)$.

1. If $\int_{t_b}^{t} \frac{dt'}{a(t')} < \infty$, the *particle horizon* at time $t$ is the sphere of comoving radius $\chi_p(t) = \int_{t_b}^{t} \frac{dt'}{a(t')}$ about the observer, and its proper distance is $d_p(t) = a(t)\chi_p(t)$.
2. If $\int_{t}^{t_\infty} \frac{dt'}{a(t')} < \infty$, the *event horizon* at time $t$ is the sphere of comoving radius $\chi_e(t) = \int_{t}^{t_\infty} \frac{dt'}{a(t')}$ about the observer, and its proper distance is $d_e(t) = a(t)\chi_e(t)$.

A *cosmological horizon* is a particle horizon or an event horizon.

## Remarks

Comoving sources beyond the particle horizon have sent no light that has reached the observer by time $t$.
Light emitted at time $t$ by comoving sources beyond the event horizon never reaches the observer.
Example: in the de Sitter model $a(t) = e^{Ht}$ on $(-\infty, \infty)$, $\int_t^\infty e^{-Ht'} dt' = e^{-Ht}/H$, so there is an event horizon with $d_e = 1/H$, while the integral to $-\infty$ diverges, so there is no particle horizon.
Non-example: in Minkowski space, viewed as $a \equiv 1$ on $(-\infty, \infty)$, both integrals diverge, so there is no cosmological horizon.
The Hubble radius $1/H$ is sometimes called the Hubble horizon, but it is not a horizon in the sense above.
