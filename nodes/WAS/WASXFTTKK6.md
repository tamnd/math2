---
tag: WASXFTTKK6
kind: statement
role: theorem
name: Range conditions for the Radon transform
msc: [44A12, 53C65]
uses: [VJNZJ352PC, GE020MY43M, P9CM4GQ2T0]
about: [VJNZJ352PC]
sources:
  - url: https://en.wikipedia.org/wiki/Radon_transform
---

## Statement

Let $n \ge 2$, and let $R$ be the [[Radon transform|VJNZJ352PC]] on the [[Schwartz space|GE020MY43M]] $\mathcal{S}(\R^n)$.
Let $\mathcal{S}(S^{n-1} \times \R)$ be the space of smooth functions $g(\theta, s)$ on $S^{n-1} \times \R$ that decay rapidly in $s$ with all derivatives.
That is, each derivative of $g$ in $\theta$ along the [[sphere|P9CM4GQ2T0]] and in $s$, times any power of $\abs{s}$, is bounded.
A function $g \in \mathcal{S}(S^{n-1} \times \R)$ is of the form $g = R f$ for some $f \in \mathcal{S}(\R^n)$ if and only if both conditions hold:

1. $g(-\theta, -s) = g(\theta, s)$ for all $(\theta, s)$.
2. For every integer $k \ge 0$, the function $\theta \mapsto \int_\R g(\theta, s)\, s^k\, ds$ is the restriction to $S^{n-1}$ of a homogeneous polynomial of degree $k$ in $\theta = (\theta_1, \dots, \theta_n)$.

## Remarks

Necessity is a direct computation.
Condition 1 holds because $(\theta, s)$ and $(-\theta, -s)$ give the same hyperplane.
For condition 2, Fubini's theorem gives $\int_\R R f(\theta, s)\, s^k\, ds = \int_{\R^n} f(x)\, (x \cdot \theta)^k\, dx$, and expanding $(x \cdot \theta)^k$ shows a homogeneous polynomial of degree $k$ in $\theta$.
Sufficiency is the deep part.
Following the projection-slice theorem, one defines $\hat f(\sigma\theta)$ as the Fourier transform of $g(\theta, \cdot)$.
The moment conditions are what make this function smooth at the origin $\xi = 0$.

Example: for $n = 2$, $g(\theta, s) = \sqrt{\pi}\, e^{-s^2}$ is the Radon transform of $e^{-\abs{x}^2}$.
Its moments vanish for odd $k$ and are constants $c_k$ for even $k$.
On the circle, $c_k = c_k (\theta_1^2 + \theta_2^2)^{k/2}$, a homogeneous polynomial of degree $k$.

Non-example: for $n = 2$, $g(\theta, s) = \theta_1^2 e^{-s^2}$ satisfies condition 1.
But for $k = 0$ its integral in $s$ is $\sqrt{\pi}\, \theta_1^2$, which is not constant on the circle.
So condition 2 fails, and $g$ is not a Radon transform.

These are often called the Helgason–Ludwig consistency conditions.

## Explanations

### L1 human

Not every function of lines is the Radon transform of something.
The theorem lists the conditions.
The data must not depend on how a line is labeled, and its moments in the offset must be polynomials of the right degree in the direction.
For example, the total integral of the data over each parallel family of lines must be the same number for every direction, namely the total mass of the function.

### L2 human

In tomography, measured data are noisy and usually violate these conditions.
Projecting the data onto the range, or checking the conditions, helps to detect errors, to estimate unknown calibration parameters and to fill in missing data.
The case $k = 0$ says that the mass is the same in every direction, and $k = 1$ says that the center of mass is a single point of $\R^n$.
The theorem describes the range of $R$ on $\mathcal{S}(\R^n)$; for other function spaces the range is described by similar conditions.
