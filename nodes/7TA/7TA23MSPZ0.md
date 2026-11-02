---
tag: 7TA23MSPZ0
kind: definition
name: X-ray transform
msc: [44A12, 92C55, 53C65]
defines: V9G9J2C10P
uses: [YCK709QB06, P9CM4GQ2T0, X7GTF3D98F]
sources:
  - url: https://en.wikipedia.org/wiki/X-ray_transform
---

## Definition

Let $n \ge 2$ and let $S^{n-1}$ be the unit [[sphere|P9CM4GQ2T0]] in $\R^n$.
Each line in $\R^n$ is $\set{x + t\theta : t \in \R}$ for a direction $\theta \in S^{n-1}$ and a point $x \in \theta^\perp = \set{y : y \cdot \theta = 0}$.
Let $f \colon \R^n \to \C$ be continuous and [[integrable|X7GTF3D98F]] on every line.
The *X-ray transform* of $f$ is the function
$$(P f)(\theta, x) = \int_\R f(x + t\theta)\, dt, \qquad \theta \in S^{n-1},\ x \in \theta^\perp.$$

## Remarks

The same line is given by $(\theta, x)$ and $(-\theta, x)$, and $P f(-\theta, x) = P f(\theta, x)$.
For $f \in L^1(\R^n)$ the transform is defined for almost every $x \in \theta^\perp$, for each $\theta$.
By Fubini's theorem, $\int_{\theta^\perp} P f(\theta, x)\, e^{-i x \cdot \xi}\, dx = \hat f(\xi)$ for $\xi \in \theta^\perp$, where $\hat f(\xi) = \int f(y)\, e^{-i y \cdot \xi}\, dy$; this is the projection-slice theorem for lines.

Example: $f(y) = e^{-\abs{y}^2}$.
For $x \perp \theta$, $\abs{x + t\theta}^2 = \abs{x}^2 + t^2$, so $P f(\theta, x) = \sqrt{\pi}\, e^{-\abs{x}^2}$.

Non-example: $f(y) = (1 + \abs{y})^{-1}$ is continuous and bounded but has no X-ray transform, since $\int_\R (1 + \abs{x + t\theta})^{-1}\, dt$ diverges like $\int dt / \abs{t}$.

For $n = 2$, let $\theta'$ be $\theta$ rotated by a right angle.
Then $P f(\theta, s\theta')$ equals the [[Radon transform|VJNZJ352PC]] $R f(\theta', s)$, since both integrate $f$ over the line $y \cdot \theta' = s$.
