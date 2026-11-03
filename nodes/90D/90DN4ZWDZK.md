---
tag: 90DN4ZWDZK
kind: statement
role: theorem
name: Landau damping
msc: [82D10, 35Q83, 76X05]
uses: [SJH7M2VCTE, DWK5N5SKTK, DPVM34ADZV]
about: [SJH7M2VCTE]
sources:
  - url: https://en.wikipedia.org/wiki/Landau_damping
same_as:
  wikidata: Q675721
  wikipedia: Landau damping
---

## Statement

Let $L > 0$ and let $\mathbb{T}_L = \R / L\Z$.
Let $f_0(v) = (2\pi)^{-1/2} e^{-v^2/2}$ be the Maxwellian velocity distribution.
Consider the linearised [[Vlasov|SJH7M2VCTE]]–[[Poisson|DWK5N5SKTK]] system for a perturbation $f(t, x, v)$ on $\mathbb{T}_L \times \R$:
$$\partial_t f + v \, \partial_x f - E(t, x) \, f_0'(v) = 0, \qquad \partial_x E = -\int_\R f \, dv, \qquad \int_{\mathbb{T}_L} E \, dx = 0.$$
Assume that the initial perturbation $f(0, x, v)$ has zero total mass and that its [[Fourier transform|DPVM34ADZV]] $\hat f_{\mathrm{in}}(k, \xi)$ in $(x, v)$ satisfies $\abs{\hat f_{\mathrm{in}}(k, \xi)} \le C e^{-\lambda (\abs{k} + \abs{\xi})}$ for some $C, \lambda > 0$.
Then there are constants $C', \gamma > 0$ such that
$$\abs{E(t, x)} \le C' e^{-\gamma t} \quad \text{for all } t \ge 0 \text{ and } x \in \mathbb{T}_L.$$

## Remarks

The mechanism is phase mixing: under free transport $\partial_t f + v \partial_x f = 0$, the Fourier mode at time $t$ is $\hat f(t, k, \xi) = \hat f_{\mathrm{in}}(k, \xi + k t)$.
So the density mode $\hat f(t, k, 0) = \hat f_{\mathrm{in}}(k, k t)$ decays as fast as the data are smooth in $v$.
The proof treats the field term as a perturbation, which gives a Volterra equation for $\hat E(t, k)$.
The Maxwellian satisfies the Penrose stability condition, so this equation has no growing modes.
The decay is not dissipation: the Vlasov equation is time-reversible, and the information moves to ever finer oscillations in $v$.
The smoothness hypothesis is needed: for data with only finite regularity in $v$, the field decays only at a polynomial rate.
Lev Landau predicted the effect in 1946, and Clément Mouhot and Cédric Villani proved in 2011 that it persists for the nonlinear Vlasov–Poisson system with small analytic or Gevrey perturbations.

## Explanations

### L1 human

In a hot plasma, a wave of electric field dies out by itself, even though there is no friction.
The reason is that the electrons move at many different speeds.
The wave is made by electrons bunching up, but since they move at different speeds the bunches smear out, and the electric field they create averages away.
The energy of the wave is not lost; it goes into finer and finer ripples in the distribution of speeds.

### L2 human

This is the linear theorem, in units where the plasma frequency and the Debye length are $1$, with electrons moving in a fixed neutralising ion background.
The damping rate is the imaginary part of the root of Landau's dispersion relation, obtained by continuing the Laplace transform of the kernel analytically.
For long waves the rate is exponentially small in $1/k^2$, so damping is weak at large scales and strong at the Debye scale.
The nonlinear result of Mouhot and Villani needs new estimates to control plasma echoes, in which nonlinear interactions bring old oscillations back.
