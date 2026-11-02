---
tag: NYTZ1VQGJ2
kind: definition
name: Coulomb wave function
msc: [33C15, 81Q05]
defines: CJ9MSY7CRM
uses: [6AZ4ZBN1M8, 0H5SYBSED9, 0QQRP17Z7S]
sources:
  - url: https://en.wikipedia.org/wiki/Coulomb_wave_function
---

## Definition

Let $L$ be a nonnegative integer, let $\eta$ be a real number, and let $\rho > 0$.
The *Coulomb wave equation* is the [[linear differential equation|0QQRP17Z7S]]
$$\frac{d^2 u}{d\rho^2} + \left( 1 - \frac{2\eta}{\rho} - \frac{L(L + 1)}{\rho^2} \right) u = 0.$$
Let $M(a, b, z)$ be [[Kummer's function|6AZ4ZBN1M8]] and $\Gamma$ the [[gamma function|0H5SYBSED9]].
The *regular Coulomb wave function* is
$$F_L(\eta, \rho) = C_L(\eta)\, \rho^{L + 1} e^{-i\rho}\, M(L + 1 - i\eta,\ 2L + 2,\ 2i\rho),$$
where the *Coulomb normalising constant* is
$$C_L(\eta) = \frac{2^L e^{-\pi\eta/2} \abs{\Gamma(L + 1 + i\eta)}}{\Gamma(2L + 2)}.$$

## Remarks

The function $F_L(\eta, \rho)$ is real, solves the Coulomb wave equation, and satisfies $F_L(\eta, \rho) \sim C_L(\eta) \rho^{L + 1}$ as $\rho \to 0^+$.
The constant $C_L(\eta)$ is chosen so that $F_L(\eta, \rho) = \sin \theta_L(\eta, \rho) + o(1)$ as $\rho \to \infty$, with phase $\theta_L = \rho - \eta \log 2\rho - \frac{L\pi}{2} + \arg \Gamma(L + 1 + i\eta)$.
The *irregular Coulomb wave function* $G_L(\eta, \rho)$ is the solution with $G_L(\eta, \rho) = \cos \theta_L(\eta, \rho) + o(1)$ as $\rho \to \infty$.
Example: for $\eta = 0$ and $L = 0$, one has $C_0(0) = 1$ and $M(1, 2, 2i\rho) = \frac{e^{2i\rho} - 1}{2i\rho}$, so
$$F_0(0, \rho) = \rho\, e^{-i\rho} \frac{e^{2i\rho} - 1}{2i\rho} = \frac{e^{i\rho} - e^{-i\rho}}{2i} = \sin \rho.$$
Non-example: $\cos \rho$ also solves the equation for $\eta = 0$ and $L = 0$, but it is not a multiple of $F_0(0, \rho)$, since it does not vanish at $\rho = 0$; it is $G_0(0, \rho)$.
For $\eta = 0$, $F_L(0, \rho) = \rho\, j_L(\rho)$, where $j_L$ is the spherical Bessel function of the first kind.
