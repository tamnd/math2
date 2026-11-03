---
tag: N0E8BESVJT
kind: definition
name: Airy wave theory
msc: [76B15]
defines: CNCGSCVQB8
uses: [R9WC0Z7Z69, 470A1RJWBP, S8RG6N1PRT]
sources:
  - url: https://en.wikipedia.org/wiki/Airy_wave_theory
---

## Definition

Keep the setting of the [[water wave problem|R9WC0Z7Z69]]: depth $h > 0$, gravity $g > 0$, surface elevation $\eta(x, t)$ and [[velocity potential|470A1RJWBP]] $\phi(x, z, t)$, here with one horizontal variable $x$.
*Airy wave theory* is the linearisation of this problem about the state of rest.
It drops all products of $\eta$, $\phi$ and their derivatives, and imposes the surface conditions at $z = 0$ instead of $z = \eta$.
The resulting linear problem is:

1. $\phi_{xx} + \phi_{zz} = 0$ for $-h < z < 0$.
2. $\phi_z = 0$ at $z = -h$.
3. $\eta_t = \phi_z$ at $z = 0$.
4. $\phi_t + g\eta = 0$ at $z = 0$.

## Remarks

Example: for amplitude $a$, wavenumber $k > 0$ and $\theta = kx - \omega t$, the pair
$$\eta = a\cos\theta, \qquad \phi = \frac{a\omega}{k} \frac{\cosh(k(z + h))}{\sinh(kh)} \sin\theta$$
solves the problem exactly when $\omega^2 = gk\tanh(kh)$.
Check: clauses 1 and 2 hold because $\cosh(k(z+h))$ has second derivative $k^2\cosh(k(z+h))$ and zero derivative at $z = -h$.
At $z = 0$, $\phi_z = a\omega\sin\theta = \eta_t$, so clause 3 holds, and $\phi_t + g\eta = \left(g - \frac{\omega^2}{k\tanh(kh)}\right) a\cos\theta$, which vanishes exactly under the stated relation.
Non-example: the same pair with $\omega^2 \neq gk\tanh(kh)$ satisfies clauses 1 to 3 but fails clause 4.
The theory is valid when $ka \ll 1$ and $a \ll h$; the ratio $a\lambda^2/h^3$, where $\lambda = 2\pi/k$ is the wavelength, must also be small in shallow water.
