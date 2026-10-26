---
tag: 0RNXVVTJTJ
kind: example
name: Damped harmonic oscillator
msc: [70J30]
instance_of: [0SWTJ5VC07]
uses: [0YG0ZJPTWG, 0HJ0HDA6W7, 0HRVY67CNV, 0BEZX8F2XW]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_oscillator
    locator: Damped harmonic oscillator
---

## Example

Let $m > 0$, $k > 0$ and $c > 0$ be constants. The damped harmonic oscillator is the equation
$$m\, x'' + c\, x' + k\, x = 0, \quad \text{that is} \quad x'' + 2 \zeta \omega_0\, x' + \omega_0^2\, x = 0,$$
with $\omega_0 = \sqrt{k/m}$ and damping ratio $\zeta = c / \left(2 \sqrt{m k}\right)$.
The characteristic roots are $r = \omega_0 \left(-\zeta \pm \sqrt{\zeta^2 - 1}\right)$, and there are three cases.
If $\zeta > 1$ (overdamped), the roots are real, distinct and negative, and $x = c_1 e^{r_1 t} + c_2 e^{r_2 t}$.
If $\zeta = 1$ (critically damped), $r = -\omega_0$ is a double root, and $x = (c_1 + c_2 t) e^{-\omega_0 t}$.
If $0 < \zeta < 1$ ([[underdamped|0JJ6GDDE7Z]]), $x = e^{-\zeta \omega_0 t} \left(c_1 \cos \omega_1 t + c_2 \sin \omega_1 t\right)$ with $\omega_1 = \omega_0 \sqrt{1 - \zeta^2}$.

## Remarks

In each case, each solution tends to $0$ as $t \to \infty$. The origin is an asymptotically stable [[equilibrium point|0N8NGKDZDZ]] of the system for $(x, x')$.
The term $c x'$ models a friction force proportional to the velocity.
The energy $E = \frac{1}{2} m (x')^2 + \frac{1}{2} k x^2$ satisfies $E' = -c (x')^2 \le 0$. So the energy decreases along each solution.

## Explanations

### L1 human

Friction takes energy from the oscillating mass.
With little friction, the mass still oscillates, but the swings get smaller.
With much friction, the mass creeps back to rest without any swing.
