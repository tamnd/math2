---
tag: QJWRZZTPF7
kind: definition
name: Phase response curve
msc: [92B25, 37N25, 34C15]
defines: K3DDKRWM9H
uses: [0NT64JV96A, 0AAQ73WRFB, 0NB689782W, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Phase_response_curve
---

## Definition

Let $F \colon \R^n \to \R^n$ be continuously differentiable.
Let the [[ordinary differential equation|0NT64JV96A]] $\dot x = F(x)$ have an asymptotically stable hyperbolic [[limit cycle|0AAQ73WRFB]] $\gamma$ of period $T > 0$, with basin $B$.
Fix a point $\gamma(0)$ on the cycle, and let $\gamma(\theta)$ for $\theta \in [0, T)$ be the point reached after time $\theta$.
The *asymptotic phase* $\Phi \colon B \to \R / T\Z$ is the map with $\Phi(\gamma(\theta)) = \theta$ such that the solution $x(t)$ from any $x(0) \in B$ satisfies $\abs{x(t) - \gamma(t + \Phi(x(0)))} \to 0$ as $t \to \infty$.
For a perturbation vector $v \in \R^n$, the *phase response curve* is the function
$$\Delta_v(\theta) = \Phi(\gamma(\theta) + v) - \theta \pmod T, \qquad \theta \in [0, T),$$
defined when $\gamma(\theta) + v \in B$.
The *infinitesimal phase response curve* is $Z(\theta) = \nabla \Phi(\gamma(\theta))$, so that $\Delta_{\varepsilon v}(\theta) = \varepsilon\, Z(\theta) \cdot v + O(\varepsilon^2)$.

## Remarks

A positive value of $\Delta_v(\theta)$ means a phase advance: the next event comes earlier.
Example: for $\dot r = r(1 - r^2)$, $\dot \vartheta = 1$ in polar coordinates, the unit circle is a stable limit cycle of period $2\pi$ and $\Phi(r, \vartheta) = \vartheta$ for $r > 0$.
A radial kick $v$ gives $\Delta_v \equiv 0$, while a kick that rotates by angle $\delta$ gives $\Delta \equiv \delta$.
Non-example: the harmonic oscillator $\ddot x = -x$ has periodic orbits but no asymptotically stable one, so its phase response curve is not defined in this sense.
In experiments the curve is often measured as $(T - T')/T$, where $T'$ is the length of the cycle that contains the stimulus.
The function $Z$ is also called the phase sensitivity function.
