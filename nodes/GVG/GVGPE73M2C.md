---
tag: GVGPE73M2C
kind: definition
name: Linear response function
msc: [82C10, 82C05]
defines: WJ78KR1K35
uses: [HM2HHE3J51, 0NEGN5CRSC, G1P1A0N7NZ]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_response_function
---

## Definition

Let $\mathcal{H}$ be a finite-dimensional [[Hilbert space|HM2HHE3J51]], and let $H$, $A$ and $B$ be [[self-adjoint operators|0NEGN5CRSC]] on $\mathcal{H}$.
Let $\rho_0$ be a state that commutes with $H$, for example the [[canonical ensemble|G1P1A0N7NZ]] state.
For a continuous function $f \colon \R \to \R$ with compact support and $\varepsilon \in \R$, let $\rho_\varepsilon(t)$ solve
$$i\hbar \, \partial_t \rho_\varepsilon(t) = [H - \varepsilon f(t) B, \rho_\varepsilon(t)],$$
with $\rho_\varepsilon(t) = \rho_0$ for all $t$ before the support of $f$.
The *linear response function* of $A$ to $B$ is the function $\chi_{AB} \colon \R \to \R$ such that, for every such $f$ and every $t$,
$$\frac{d}{d\varepsilon}\Big|_{\varepsilon = 0} \tr\big(\rho_\varepsilon(t) A\big) = \int_{-\infty}^{\infty} \chi_{AB}(t - s) f(s) \, ds.$$

## Remarks

The function exists and is unique, and $\chi_{AB}(t) = 0$ for $t < 0$; this is causality.
Its Fourier transform $\tilde\chi_{AB}(\omega) = \int_0^\infty e^{i\omega t} \chi_{AB}(t)\, dt$ is the dynamical susceptibility, and it satisfies the Kramers–Kronig relations.
Example: for a two-level system with $H = \tfrac{\hbar\Omega}{2}\sigma_z$, $A = B = \sigma_x$ and $\rho_0$ the ground state, one finds $\chi_{AB}(t) = \tfrac{2}{\hbar}\theta(t)\sin(\Omega t)$, which vanishes for $t < 0$ as required.
Non-example: the function $\psi(t) = \tfrac{2}{\hbar}\sin(\Omega t)$ for all $t$, without the factor $\theta(t)$, is not the linear response function of that system.
Take $f$ supported in $[1, 2]$ and $t = 0$: the left side is $0$ because the state has not yet been disturbed, while $\int \psi(-s) f(s)\, ds$ is nonzero for suitable $f$.
In classical mechanics the same definition is used with a probability density on phase space and the Liouville equation in place of $\rho$ and the von Neumann equation.
