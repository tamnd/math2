---
tag: PTFTEAFZ7G
kind: definition
name: Chaplygin's equation
msc: [76N15, 76H05, 35M10]
defines: GC17HMC8FN
uses: [9AR4ZZRRAM, 470A1RJWBP, SN4J6KP03C, GFHJ858AN1]
sources:
  - url: https://en.wikipedia.org/wiki/Chaplygin%27s_equation
---

## Definition

Consider a steady planar irrotational isentropic flow of a gas, with velocity $(u, v) = (q \cos\theta, q \sin\theta)$, speed $q > 0$ and flow angle $\theta$.
Let $c(q) > 0$ be the [[speed of sound|SN4J6KP03C]] as a function of the speed, given by Bernoulli's law.
Let $\varphi$ be the [[velocity potential|470A1RJWBP]], and let $\Phi = xu + yv - \varphi$ be its Legendre transform, regarded as a function of $(q, \theta)$ through the [[hodograph transformation|9AR4ZZRRAM]].
*Chaplygin's equation* is the equation
$$\frac{\partial^2 \Phi}{\partial \theta^2} + \frac{q^2}{1 - q^2/c^2}\, \frac{\partial^2 \Phi}{\partial q^2} + q\, \frac{\partial \Phi}{\partial q} = 0,$$
which $\Phi$ satisfies wherever $q \ne c$.

## Remarks

The equation is linear, and its coefficients depend only on $q$.
It is elliptic where $q < c$ and hyperbolic where $q > c$, that is, where the [[Mach number|GFHJ858AN1]] $q/c$ is below or above $1$.
In the incompressible limit $c \to \infty$ it becomes $q^2 \Phi_{qq} + q \Phi_q + \Phi_{\theta\theta} = 0$, which is Laplace's equation in polar coordinates $(q, \theta)$.
The stream function satisfies a similar linear equation in the variables $(q, \theta)$.

Example: $\Phi = A\theta$ with a constant $A \ne 0$ satisfies the equation, since all three terms vanish.
From $x = \Phi_q \cos\theta - \Phi_\theta \sin\theta / q$ and $y = \Phi_q \sin\theta + \Phi_\theta \cos\theta / q$ one gets $(x, y) = (A/q)(-\sin\theta, \cos\theta)$.
So the velocity is perpendicular to the position vector and $q = \abs{A}/r$ at distance $r$ from the origin: this is a potential vortex.

Non-example: $\Phi = \theta^2$ is not a solution, since $\Phi_{\theta\theta} = 2$ while the other two terms vanish.
