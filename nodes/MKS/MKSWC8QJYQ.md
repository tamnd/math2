---
tag: MKSWC8QJYQ
kind: example
name: Kronig–Penney model
msc: [82D20, 81Q05, 34L40]
illustrates: [QP0TK2M29V]
uses: [89AA6XJY5K]
sources:
  - url: https://en.wikipedia.org/wiki/Particle_in_a_one-dimensional_lattice
---

## Example

The *Kronig–Penney model* is the one-dimensional [[Schrödinger operator|89AA6XJY5K]] $H = -\dfrac{d^2}{dx^2} + V$ (units with $\hbar^2/2m = 1$) with an $a$-periodic potential made of square barriers.
In each period, $V = V_0 > 0$ on an interval of width $b$ and $V = 0$ on the rest, of width $a - b$.
For $0 < E < V_0$, put $q = \sqrt{E}$ and $\kappa = \sqrt{V_0 - E}$.
Solving $-\psi'' + V\psi = E\psi$ piece by piece and imposing the Bloch condition $\psi(x + a) = e^{ika}\psi(x)$ gives the relation
$$\cos(ka) = \cos\big(q(a - b)\big)\cosh(\kappa b) + \frac{\kappa^2 - q^2}{2q\kappa} \sin\big(q(a - b)\big)\sinh(\kappa b).$$
The energy $E$ lies in a band exactly when the right-hand side lies in $[-1, 1]$.

Check in the limit of thin high barriers, $b \to 0$ with $V_0 b = \alpha$ fixed (a Dirac comb $V = \alpha \sum_{n} \delta(x - na)$): then $\kappa^2 b \to \alpha$ and $\kappa b \to 0$, and the relation becomes
$$\cos(ka) = \cos(qa) + \frac{\alpha}{2q} \sin(qa).$$
At $qa = \pi$ the right side equals $-1$, a band edge.
Take $\alpha > 0$ and $qa$ slightly above $\pi$.
Then $\cos(qa)$ is close to $-1$ and $\sin(qa) < 0$, so the right side is below $-1$ and $E = q^2$ lies in a gap.
So gaps open at $qa = \pi, 2\pi, \dots$, where the free bands would cross.

## Explanations

### L1 human

The Kronig–Penney model is a toy crystal: a particle on a line that meets the same rectangular bump again and again.
It can be solved with pencil and paper, and the answer is a single equation that says which energies are allowed.
Plotting the right-hand side against the energy shows a wavy curve, and the energies where it leaves the strip between $-1$ and $1$ are the gaps.
It is the simplest way to see [[band structure|QP0TK2M29V]] appear from a periodic potential.
