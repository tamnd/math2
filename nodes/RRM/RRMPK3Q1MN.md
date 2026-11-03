---
tag: RRMPK3Q1MN
kind: definition
name: Particle horizon
msc: ["83F05"]
defines: 11F8FNHP9S
uses: [ECJMS4VDTF, J70F32P86W, CZ5PH864FG]
sources:
  - url: https://en.wikipedia.org/wiki/Particle_horizon
---

## Definition

Let $g = -dt^2 + a(t)^2 \gamma_k$ be a [[Friedmann–Lemaître–Robertson–Walker metric|ECJMS4VDTF]] on $(t_b, t_\infty) \times \Sigma$ with [[scale factor|J70F32P86W]] $a$, in units with $c = 1$, and fix a comoving observer and a time $t \in (t_b, t_\infty)$.
Suppose that
$$\chi_p(t) = \int_{t_b}^{t} \frac{dt'}{a(t')} < \infty.$$
The *particle horizon* of the observer at time $t$ is the set of comoving points at comoving distance $\chi_p(t)$ from the observer.
Its *proper distance* is $d_p(t) = a(t)\, \chi_p(t)$.

## Remarks

A radial light ray satisfies $d\chi = dt / a$, so $\chi_p(t)$ is the comoving distance that light can travel between $t_b$ and $t$; comoving points farther away cannot yet be seen.
Example: in the Einstein–de Sitter model $a(t) = (t/t_0)^{2/3}$ on $(0, \infty)$, $\chi_p(t) = 3 t_0^{2/3} t^{1/3}$ and $d_p(t) = 3t$.
For radiation, $a \propto t^{1/2}$, the same computation gives $d_p(t) = 2t$.
Non-example: for $a(t) = e^{Ht}$ on $(-\infty, \infty)$ the integral diverges, so there is no particle horizon.
It is one of the two [[cosmological horizons|CZ5PH864FG]], the other being the event horizon.
