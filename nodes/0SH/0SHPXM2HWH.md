---
tag: 0SHPXM2HWH
kind: example
name: Pendulum equation
msc: [70K05, 34C15]
instance_of: [0EDKGA2FAK, 0673D85QKZ]
uses: [0YG0ZJPTWG, 0SS1P1YC9A, 0C5PREPZWG]
sources:
  - url: https://en.wikipedia.org/wiki/Pendulum_(mechanics)
    locator: Simple gravity pendulum
  - url: https://en.wikipedia.org/wiki/Pendulum_(mechanics)
    locator: Small-angle approximation
---

## Example

Let $g > 0$ be the acceleration of gravity and $\ell > 0$ the length of a rigid massless rod, with a point mass at its end. Let $\theta(t)$ be the angle of the rod from the downward vertical at time $t$.
Without friction, the motion satisfies the pendulum equation
$$\theta''(t) + \frac{g}{\ell} \sin \theta(t) = 0.$$
As a first-order system, it is $\theta' = \omega$, $\omega' = -\frac{g}{\ell} \sin \theta$. The function $E(\theta, \omega) = \frac{1}{2} \omega^2 - \frac{g}{\ell} \cos \theta$ is a [[first integral|0SS1P1YC9A]].

## Remarks

For small angles, $\sin \theta \approx \theta$. This gives the [[harmonic oscillator|0YG0ZJPTWG]] $\theta'' + \frac{g}{\ell} \theta = 0$, with the solution $\theta(t) = \theta_0 \cos\left(\sqrt{g/\ell}\, t\right)$ for $\theta(0) = \theta_0$, $\theta'(0) = 0$, and the period $2 \pi \sqrt{\ell / g}$.
For the nonlinear equation, the period depends on the amplitude. It is given by an elliptic integral and it is longer than $2 \pi \sqrt{\ell / g}$.
The equilibrium $(0, 0)$, hanging down, is stable. The equilibrium $(\pi, 0)$, standing up, is a [[hyperbolic|0C5PREPZWG]] saddle, so it is unstable.

## Explanations

### L1 human

Gravity pulls the mass back toward the lowest point, with a force proportional to $\sin \theta$.
For small swings, this is nearly proportional to $\theta$, and the pendulum behaves like a spring.
For large swings, the motion is slower, and with enough energy the pendulum turns over the top.
