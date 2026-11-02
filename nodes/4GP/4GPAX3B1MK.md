---
tag: 4GPAX3B1MK
kind: definition
name: Radon transform
msc: [44A12, 92C55, 53C65]
defines: VJNZJ352PC
uses: [YCK709QB06, P9CM4GQ2T0, X7GTF3D98F]
sources:
  - url: https://en.wikipedia.org/wiki/Radon_transform
---

## Definition

Let $n \ge 2$, and let $S^{n-1}$ be the unit [[sphere|P9CM4GQ2T0]] in $\R^n$.
For $\theta \in S^{n-1}$ and $s \in \R$, the set $\set{x \in \R^n : x \cdot \theta = s}$ is a hyperplane, and every hyperplane is of this form.
Let $\theta^\perp = \set{y \in \R^n : y \cdot \theta = 0}$, with its $(n-1)$-dimensional Lebesgue measure $dy$.
Let $f \colon \R^n \to \C$ be continuous and [[integrable|X7GTF3D98F]] on every hyperplane.
The *Radon transform* of $f$ is the function on $S^{n-1} \times \R$ given by
$$(R f)(\theta, s) = \int_{\theta^\perp} f(s\theta + y)\, dy.$$

## Remarks

$R f(\theta, s)$ is the integral of $f$ over the hyperplane $x \cdot \theta = s$.
Since $(-\theta, -s)$ gives the same hyperplane, $R f(-\theta, -s) = R f(\theta, s)$.
The transform is also defined for $f \in L^1(\R^n)$, at almost every $(\theta, s)$, by Fubini's theorem.
One often writes $R_\theta f(s) = R f(\theta, s)$.

Example: $f(x) = e^{-\abs{x}^2}$.
For $y \in \theta^\perp$, $\abs{s\theta + y}^2 = s^2 + \abs{y}^2$, so $R f(\theta, s) = e^{-s^2} \int_{\R^{n-1}} e^{-\abs{y}^2}\, dy = \pi^{(n-1)/2} e^{-s^2}$.

Example: in $\R^2$, the indicator of the unit disk has $R f(\theta, s) = 2\sqrt{1 - s^2}$ for $\abs{s} \le 1$ and $0$ otherwise.

Non-example: $f = 1$ is not integrable on any hyperplane, so it has no Radon transform.

For $n = 2$ the Radon transform coincides with the [[X-ray transform|V9G9J2C10P]] up to the parametrization of lines.
