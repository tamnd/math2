---
tag: E16HJZ3W4R
kind: definition
name: Heat potential
msc: [35K08, 35K05, 31C99]
defines: ZAT4TV4030
uses: [VP2HN86VAG, KD404MF042, HZNEQQBCW4]
sources:
  - url: https://en.wikipedia.org/wiki/Heat_equation
---

## Definition

Let $n \ge 1$, and let $\Phi \colon \R^n \times \R \to [0, \infty)$ be the fundamental solution of the [[heat equation|VP2HN86VAG]] $\partial_t u = \Delta u$:
$$\Phi(x, t) = (4\pi t)^{-n/2} \exp\!\left(-\frac{\abs{x}^2}{4t}\right) \text{ for } t > 0, \qquad \Phi(x, t) = 0 \text{ for } t \le 0.$$
Let $\mu$ be a positive [[Radon measure|HZNEQQBCW4]] on $\R^n \times \R$.
The *heat potential* of $\mu$ is the function $\Phi\mu \colon \R^n \times \R \to [0, \infty]$ given by
$$\Phi\mu(x, t) = \int_{\R^n \times \R} \Phi(x - y, t - s) \, d\mu(y, s).$$
When $d\mu = f \, dy \, ds$ for a function $f \ge 0$, the heat potential $\Phi\mu$ is also called the volume potential of $f$.

## Remarks

Only the part of $\mu$ with $s < t$ contributes to $\Phi\mu(x, t)$, since $\Phi$ vanishes for nonpositive times.
Example: for the unit point mass $\mu = \delta_{(0, 0)}$, the heat potential is $\Phi$ itself, the [[heat kernel|KD404MF042]] started at time $0$; it solves the heat equation away from $(0, 0)$.
Degenerate case: for Lebesgue measure on $\R^n \times \R$, $\Phi\mu(x, t) = \int_{-\infty}^{t} \int_{\R^n} \Phi(x - y, t - s) \, dy \, ds = \int_{-\infty}^t 1 \, ds = \infty$ at every point, so finiteness of a heat potential needs growth conditions on $\mu$.
For a bounded function $f$ on $\R^n \times (0, T)$ that is locally Hölder continuous, the function $u(x, t) = \int_0^t \int_{\R^n} \Phi(x - y, t - s) f(y, s) \, dy \, ds$ solves $\partial_t u - \Delta u = f$ with $u(\cdot, 0) = 0$.
A measure carried by the lateral boundary of a space-time cylinder gives a single layer heat potential.
Using a normal derivative of $\Phi$ instead gives a double layer heat potential.
Both are used to solve boundary value problems for the heat equation.
