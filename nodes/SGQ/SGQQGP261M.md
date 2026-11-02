---
tag: SGQQGP261M
kind: example
name: Duffing equation
msc: [34C15, 70K40, 34C28]
instance_of: [0NT64JV96A]
uses: [0EDKGA2FAK, 0C5PREPZWG, 6DBSQKZK4W, A755BDRP1A]
sources:
  - url: https://en.wikipedia.org/wiki/Duffing_equation
---

## Example

Let $\delta, \alpha, \beta, \gamma, \omega$ be real constants.
The Duffing equation is the second-order [[ordinary differential equation|0NT64JV96A]]
$$x'' + \delta x' + \alpha x + \beta x^3 = \gamma \cos(\omega t).$$
Here $\delta$ is a damping coefficient, $\alpha x + \beta x^3$ is a restoring force with a cubic term, and $\gamma \cos(\omega t)$ is a periodic forcing.

Take $\delta = \gamma = 0$, $\alpha = -1$ and $\beta = 1$, so $x'' - x + x^3 = 0$.
This is a [[Hamiltonian system|0EDKGA2FAK]] with $H(x, y) = \frac{1}{2} y^2 - \frac{1}{2} x^2 + \frac{1}{4} x^4$ and $y = x'$.
Its equilibria are $(0, 0)$, a [[hyperbolic|0C5PREPZWG]] saddle, and $(\pm 1, 0)$, two centres.
The function $x(t) = \sqrt{2}\, \operatorname{sech} t$ is a solution.
Check: with $u = \operatorname{sech} t$ one has $u'' = u - 2u^3$, so $x'' - x + x^3 = \sqrt{2}(u - 2u^3) - \sqrt{2} u + 2\sqrt{2} u^3 = 0$.
Since $x(t) \to 0$ and $x'(t) \to 0$ as $t \to \pm\infty$, this solution is a [[homoclinic orbit|6DBSQKZK4W]] of the saddle.
By the symmetry $x \mapsto -x$, there is a second one in the half-plane $x < 0$.

## Remarks

Solutions of the unforced, undamped equation stay on level sets of $H$.
So each solution is an equilibrium, a periodic solution, or a homoclinic solution.
With small damping and small forcing, the two homoclinic orbits can break into a tangle of stable and unstable manifolds.
The [[Melnikov method|A755BDRP1A]] decides when this happens in terms of $\gamma$, $\delta$ and $\omega$.
In that regime, numerical solutions of the Duffing equation look chaotic.
For $\alpha > 0$ and small $\beta$, the equation is a perturbed harmonic oscillator whose frequency depends on the amplitude.

## Explanations

### L1 human

The Duffing equation is a spring whose force is not exactly proportional to the stretch, pushed back and forth periodically.
With $\alpha < 0 < \beta$ the spring has two stable rest positions, like a ball in a double well.
A forced ball can jump between the two wells in an irregular way, which is a classical example of chaos.
