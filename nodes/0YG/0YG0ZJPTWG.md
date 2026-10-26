---
tag: 0YG0ZJPTWG
kind: example
name: Harmonic oscillator
aliases: [simple-harmonic-oscillator]
msc: [70J30]
instance_of: [0SWTJ5VC07]
uses: [0BEZX8F2XW]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_oscillator
    locator: Simple harmonic oscillator
same_as:
  wikidata: Q190070
  wikipedia: Harmonic oscillator
---

## Example

Let $m > 0$ and $k > 0$ be constants, and let $\omega_0 = \sqrt{k/m}$.
The equation of the harmonic oscillator is
$$m\, x''(t) + k\, x(t) = 0, \quad \text{that is} \quad x'' + \omega_0^2\, x = 0.$$
It models a mass $m$ on a spring with stiffness $k$, where $x$ is the displacement from the rest position.
Its characteristic roots are $\pm i \omega_0$, so its solutions are $x(t) = c_1 \cos(\omega_0 t) + c_2 \sin(\omega_0 t) = A \cos(\omega_0 t + \varphi)$ with constants $A \ge 0$ and $\varphi$.

## Remarks

Each nonzero solution is periodic with period $2 \pi / \omega_0$. The period does not depend on the amplitude $A$.
The energy $E = \frac{1}{2} m (x')^2 + \frac{1}{2} k x^2$ is constant along each solution. It is a [[first integral|0SS1P1YC9A]].
With friction, the equation becomes the [[damped harmonic oscillator|0RNXVVTJTJ]].

## Explanations

### L1 human

The spring pulls the mass back with a force proportional to the displacement.
The mass overshoots the rest position, and the motion repeats forever as a sine wave.
A stiffer spring or a lighter mass gives a faster oscillation.
