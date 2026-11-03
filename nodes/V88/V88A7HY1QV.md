---
tag: V88A7HY1QV
kind: example
name: Delta potential
msc: [81Q05, 81U15, 81U05]
illustrates: [3XZFX39KH9, 255PSST1YR]
uses: [0KPHENZ5S7, VXDEQB46GV, EPZR6H2WJN, 3XZFX39KH9, 255PSST1YR]
sources:
  - url: https://en.wikipedia.org/wiki/Delta_potential
same_as:
  wikidata: Q2381860
  wikipedia: Delta potential
---

## Example

Let $m > 0$ be the mass of a particle on the line $\R$, let $\hbar$ be the reduced Planck constant, and let $\alpha \in \R \setminus \set{0}$.
The *delta potential* is $V(x) = -\alpha\, \delta(x)$, where $\delta$ is the [[Dirac delta|0KPHENZ5S7]].
The time-independent [[Schrödinger equation|EPZR6H2WJN]] $-\frac{\hbar^2}{2m}\psi'' + V\psi = E\psi$ means the following.
The function $\psi$ is continuous, it satisfies $-\frac{\hbar^2}{2m}\psi'' = E\psi$ for $x \ne 0$, and its derivative jumps at $0$:
$$\psi'(0^+) - \psi'(0^-) = -\frac{2 m \alpha}{\hbar^2}\, \psi(0).$$

Bound state: let $\alpha > 0$, so the potential is attractive, and let $\kappa = m\alpha/\hbar^2$.
Then $\psi(x) = \sqrt{\kappa}\, e^{-\kappa \abs{x}}$ is the unique normalised [[bound state|3XZFX39KH9]], with energy $E = -m\alpha^2/(2\hbar^2)$.
Check: for $x \ne 0$, $\psi'' = \kappa^2 \psi$, so $E = -\hbar^2\kappa^2/(2m) = -m\alpha^2/(2\hbar^2)$.
The jump is $\psi'(0^+) - \psi'(0^-) = -2\kappa\sqrt\kappa = -\frac{2m\alpha}{\hbar^2}\psi(0)$.
The norm is $\int_\R \kappa e^{-2\kappa\abs{x}}\, dx = 1$.

Scattering: for an energy $E = \hbar^2 k^2/(2m) > 0$, a wave coming from the left is partly reflected and partly transmitted.
The transmission coefficient is
$$T = \frac{1}{1 + \dfrac{m \alpha^2}{2 \hbar^2 E}},$$
and the reflection coefficient is $1 - T$.
For $\alpha < 0$ the potential is an infinitely high and infinitely thin barrier, and there is no bound state.
Still $T > 0$ at every energy, an instance of [[quantum tunnelling|255PSST1YR]].

## Explanations

### L1 human

The delta potential is a single point that attracts or repels the particle with infinite strength but zero width.
It is the simplest model with a bound state: an attractive delta traps exactly one state, which decays exponentially away from the point.
A repulsive delta reflects part of an incoming wave and lets the rest through, however high the spike.
Because everything can be computed by hand, it is a standard first model of bound states and of scattering.
