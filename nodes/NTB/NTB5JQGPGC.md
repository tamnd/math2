---
tag: NTB5JQGPGC
kind: definition
name: Resonance
msc: [34C15, 34A30]
defines: 4F812GHFZK
uses: [0QQRP17Z7S, 0GZWXM2DKE]
sources:
  - url: https://en.wikipedia.org/wiki/Resonance
---

## Definition

Let $p(r) = r^n + a_{n-1} r^{n-1} + \cdots + a_0$ be a polynomial with complex coefficients, and write $D = \frac{d}{dt}$.
Consider the [[linear equation|0QQRP17Z7S]] with constant coefficients and exponential forcing
$$p(D)\, y = e^{\lambda t}, \qquad \lambda \in \C.$$
The equation is *resonant*, and $\lambda$ is a *resonant frequency*, if $p(\lambda) = 0$, that is, if $\lambda$ is a root of the [[characteristic equation|0GZWXM2DKE]] of $p(D) y = 0$.

## Remarks

If $p(\lambda) \ne 0$, then $y = \frac{e^{\lambda t}}{p(\lambda)}$ is a particular solution.
If $\lambda$ is a root of multiplicity $m \ge 1$, then $y = \frac{t^m e^{\lambda t}}{p^{(m)}(\lambda)}$ is a particular solution.
This follows from $p(D)(t^m e^{\lambda t}) = \frac{\partial^m}{\partial \lambda^m} \left( p(\lambda) e^{\lambda t} \right)$ and $p(\lambda) = \cdots = p^{(m-1)}(\lambda) = 0$.

Example: $y'' + \omega_0^2 y = e^{i \omega_0 t}$ with $\omega_0 > 0$ is resonant, since $p(r) = r^2 + \omega_0^2$ vanishes at $i \omega_0$.
Taking real parts, $y'' + \omega_0^2 y = \cos(\omega_0 t)$ has the solution $y = \frac{t \sin(\omega_0 t)}{2 \omega_0}$.
Indeed $y'' = \cos(\omega_0 t) - \frac{\omega_0 t \sin(\omega_0 t)}{2}$, so $y'' + \omega_0^2 y = \cos(\omega_0 t)$; this solution is unbounded.

Non-example: $y'' + y = e^{2 i t}$ is not resonant, since $p(2i) = -3 \ne 0$; the particular solution $-\frac{1}{3} e^{2 i t}$ is bounded.

For a damped oscillator, $p(r) = r^2 + c r + \omega_0^2$ with $c > 0$, the roots of $p$ have negative real part, so a forcing $e^{i \omega t}$ with real $\omega$ is never resonant in this sense.
When the damping is small, the amplitude $\frac{1}{\abs{p(i \omega)}}$ still has a sharp peak near the natural frequency; this is also called resonance.
