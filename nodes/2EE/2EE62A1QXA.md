---
tag: 2EE62A1QXA
kind: definition
name: Spherical mean transform
msc: [44A12, 53C65, 35L05]
defines: P4B2Z6GS0R
uses: [P9CM4GQ2T0, YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Spherical_mean
---

## Definition

Let $n \ge 2$, let $S^{n-1} = \set{\theta \in \R^n : \abs{\theta} = 1}$ be the unit [[sphere|P9CM4GQ2T0]], let $\sigma$ be its surface measure, and let $\omega_{n-1} = \sigma(S^{n-1})$.
Let $f \colon \R^n \to \C$ be continuous.
The *spherical mean transform* of $f$ is the function on $\R^n \times [0, \infty)$ given by
$$(M f)(x, r) = \frac{1}{\omega_{n-1}} \int_{S^{n-1}} f(x + r\theta)\, d\sigma(\theta).$$

## Remarks

$M f(x, r)$ is the average of $f$ over the sphere of center $x$ and radius $r$, and $M f(x, 0) = f(x)$.
If $f$ is of class $C^2$, then $M f$ satisfies the Darboux equation
$$\Delta_x M f(x, r) = \left( \frac{\partial^2}{\partial r^2} + \frac{n - 1}{r} \frac{\partial}{\partial r} \right) M f(x, r), \qquad r > 0.$$

Example: $f(x) = \abs{x}^2$.
Since $\abs{x + r\theta}^2 = \abs{x}^2 + 2r\, x \cdot \theta + r^2$ and $\theta \mapsto x \cdot \theta$ has mean $0$ over the sphere, $M f(x, r) = \abs{x}^2 + r^2$.
Both sides of the Darboux equation equal $2n$.

Non-example: $f(y) = \abs{y}^{1-n}$ for $y \ne 0$ and $f(0) = 0$ is not continuous.
Its mean over the sphere of center $x \ne 0$ and radius $r = \abs{x}$, which passes through $0$, is $+\infty$.

The function $f$ may also be only locally integrable, and then $M f(x, r)$ is defined for almost every $(x, r)$.
