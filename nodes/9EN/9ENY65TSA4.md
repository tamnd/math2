---
tag: 9ENY65TSA4
kind: definition
name: Quantum tunnelling
msc: [81Q05, 81U05, 81Q20]
defines: 255PSST1YR
uses: [EPZR6H2WJN, E9WK6KJ4SM, VXDEQB46GV]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_tunnelling
---

## Definition

Let $m > 0$ be the mass of a particle on the line $\R$, and let $\hbar$ be the reduced Planck constant.
Let $V \colon \R \to \R$ be a bounded measurable potential with $V(x) = 0$ for $x \notin [a, b]$, where $a < b$.
Let $E = \hbar^2 k^2/(2m)$ with $k > 0$.
Consider the time-independent [[Schrödinger equation|EPZR6H2WJN]] $-\frac{\hbar^2}{2m}\psi'' + V \psi = E \psi$.
A *scattering solution* at energy $E$ is a solution $\psi$ of the following form, for complex numbers $r$ and $t$:
$$\psi(x) = e^{ikx} + r e^{-ikx} \text{ for } x < a, \qquad \psi(x) = t e^{ikx} \text{ for } x > b.$$
The number $T(E) = \abs{t}^2$ is the *transmission coefficient*.
Suppose that $E < V(x)$ for all $x$ in some interval $I \subseteq [a, b]$, so that a classical particle with energy $E$ could not cross $I$.
*Quantum tunnelling* is the fact that $T(E) > 0$ at such an energy.

## Remarks

Example: the rectangular barrier $V = V_0$ on $[0, d]$ and $V = 0$ elsewhere, with $0 < E < V_0$.
Let $\kappa = \sqrt{2m(V_0 - E)}/\hbar$.
Inside the barrier $\psi$ is a combination of $e^{\kappa x}$ and $e^{-\kappa x}$, and matching $\psi$ and $\psi'$ at $0$ and $d$ gives
$$T(E) = \left(1 + \frac{V_0^2 \sinh^2(\kappa d)}{4E(V_0 - E)}\right)^{-1} > 0.$$
For $\kappa d \gg 1$, $T(E) \approx \frac{16 E (V_0 - E)}{V_0^2} e^{-2\kappa d}$.

Non-example: in classical mechanics, a particle with energy $E$ cannot enter the region where $V(x) > E$, because its kinetic energy $E - V(x)$ would be negative; its transmission is $0$.

Conservation of probability gives $\abs{r}^2 + \abs{t}^2 = 1$.
For a smooth barrier, the WKB approximation gives $T(E) \approx \exp\left(-\frac{2}{\hbar}\int_{x_1}^{x_2} \sqrt{2m(V(x) - E)}\, dx\right)$, where $x_1 < x_2$ are the turning points with $V = E$.
