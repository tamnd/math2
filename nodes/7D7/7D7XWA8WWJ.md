---
tag: 7D7XWA8WWJ
kind: definition
name: Torus integral
msc: [32A26, 32A10]
defines: R49Q9M519Z
uses: [A6HN207Y2T, 06ZGPYTWK8, DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_integral_formula
---

## Definition

Let $c = (c_1, \dots, c_n) \in \C^n$ and $r = (r_1, \dots, r_n)$ with each $r_j > 0$.
Let $T(c, r)$ be the [[distinguished boundary|A6HN207Y2T]] $\set{\zeta : \abs{\zeta_j - c_j} = r_j \text{ for all } j}$.
For $\theta = (\theta_1, \dots, \theta_n) \in [0, 2\pi]^n$, put $\gamma(\theta) = (c_1 + r_1 e^{i\theta_1}, \dots, c_n + r_n e^{i\theta_n})$.
Let $f \colon T(c, r) \to \C$ be a function such that $\theta \mapsto f(\gamma(\theta))$ is [[Lebesgue integrable|DWJF7ABPR1]] on $[0, 2\pi]^n$, for example a continuous function.
The *torus integral* of $f$ over $T(c, r)$ is
$$\int_{T(c, r)} f(\zeta) \, d\zeta_1 \cdots d\zeta_n = \int_{[0, 2\pi]^n} f(\gamma(\theta)) \prod_{j=1}^n \left( i r_j e^{i\theta_j} \right) d\theta_1 \cdots d\theta_n.$$

## Remarks

The factor $i r_j e^{i\theta_j} \, d\theta_j$ is $d\zeta_j$ along the circle $\zeta_j = c_j + r_j e^{i\theta_j}$, so for $n = 1$ this is the [[contour integral|06ZGPYTWK8]] over the positively oriented circle.
For continuous $f$, Fubini's theorem makes it equal to the iterated integral of $n$ one-variable contour integrals, in any order.
Example: for $f(\zeta) = 1/(\zeta_1 \zeta_2)$ on $T(0, (1, 1))$, the integrand is $e^{-i\theta_1} e^{-i\theta_2} \cdot i e^{i\theta_1} \cdot i e^{i\theta_2} = -1$, so the integral is $-(2\pi)^2 = (2\pi i)^2$.
Non-example: $f(\zeta) = 1/(\zeta_1 - 1)$ is not defined at the points of $T(0, (1, 1))$ with $\zeta_1 = 1$.
Near $\theta_1 = 0$, $\abs{f(\gamma(\theta))}$ behaves like $1/\abs{\theta_1}$, so it is not integrable and the torus integral is not defined.
Other notation: $\oint_{T(c, r)} f(\zeta) \, d\zeta$.
