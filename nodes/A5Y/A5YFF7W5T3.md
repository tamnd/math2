---
tag: A5YFF7W5T3
kind: definition
name: Laser rate equations
msc: [78A60, 34C60]
defines: ZMRAWA0HE2
uses: [07VX34QXAV]
sources:
  - url: https://en.wikipedia.org/wiki/Rate_equation
---

## Definition

Consider a single-mode laser with an ideal four-level gain medium.
Let $N(t) \ge 0$ be the population inversion density and $\phi(t) \ge 0$ the photon density in the cavity.
Let $R_p \ge 0$ be the pump rate and $B > 0$ the coefficient of stimulated emission.
Let $\tau > 0$ be the lifetime of the upper laser level and $\tau_c > 0$ the photon lifetime in the cavity.
The *laser rate equations*, without spontaneous emission into the mode, are the system of [[ordinary differential equations|07VX34QXAV]]
$$\frac{dN}{dt} = R_p - \frac{N}{\tau} - B N \phi, \qquad \frac{d\phi}{dt} = B N \phi - \frac{\phi}{\tau_c}.$$

## Remarks

The steady states give the threshold.
A steady state with $\phi > 0$ needs $B N = 1/\tau_c$, so $N = N_{\mathrm{th}} = 1/(B \tau_c)$.
The first equation then gives $\phi = \tau_c (R_p - N_{\mathrm{th}}/\tau)$, which is positive exactly when $R_p > N_{\mathrm{th}}/\tau$, the threshold pump rate.
Above threshold the inversion is clamped at $N_{\mathrm{th}}$ and the photon density grows linearly with the pump.
Below threshold the only steady state is $\phi = 0$, $N = R_p \tau$.

Example: with $\tau_c = 1$, $\tau = 1$, $B = 1$ and $R_p = 3$, the threshold is $N_{\mathrm{th}} = 1$ and the steady state is $N = 1$, $\phi = 2$; one checks $3 - 1 - 2 = 0$ and $2 - 2 = 0$.

Non-example: the equations do not track the phase of the field or the polarization of the medium.
So they cannot describe effects such as the Lorenz-type chaos of the Maxwell–Bloch equations.
Many variants exist, for example with a term for spontaneous emission into the mode or for three-level media.
