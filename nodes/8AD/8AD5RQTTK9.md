---
tag: 8AD5RQTTK9
kind: definition
name: Lusin area integral
msc: [42B25, 31B10]
defines: KHY35P4AKF
uses: [TCYSWCTYYM, 0DEB0JMN0W, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Littlewood%E2%80%93Paley_theory
---

## Definition

Let $n \ge 1$ and let $\R^{n+1}_+ = \set{(y, t) : y \in \R^n, \ t > 0}$ be the upper half-space.
Let $f$ be in the [[Lp space|SASP14MA1Z]] $L^p(\R^n)$ for some $1 \le p \le \infty$.
Let $u(y, t) = (P_t * f)(y)$ be its Poisson integral, where $P_t$ is the [[Poisson kernel|TCYSWCTYYM]] of the half-space, so that $u$ is [[harmonic|0DEB0JMN0W]] on $\R^{n+1}_+$.
Let $\nabla u = (\partial_{y_1} u, \dots, \partial_{y_n} u, \partial_t u)$ be its full gradient.
For $x \in \R^n$ let $\Gamma(x) = \set{(y, t) \in \R^{n+1}_+ : \abs{y - x} < t}$ be the cone with vertex $x$.
The *Lusin area integral* of $f$ is the function $S(f) \colon \R^n \to [0, \infty]$ given by
$$S(f)(x) = \left( \iint_{\Gamma(x)} \abs{\nabla u(y, t)}^2 \, t^{1 - n} \, dy \, dt \right)^{1/2}.$$

## Remarks

The power $t^{1 - n}$ makes $S(f)$ invariant under dilations: $S(f(\delta \cdot))(x) = S(f)(\delta x)$.
For $1 < p < \infty$ one has $c \norm{f}_p \le \norm{S(f)}_p \le C \norm{f}_p$ with constants depending only on $n$ and $p$.
Replacing the cone by the vertical half-line over $x$, with the weight $t$, gives the Littlewood–Paley $g$-function.

Example: the $L^2$ identity.
Integrating over $x$ first, $\int_{\R^n} S(f)(x)^2 \, dx = \omega_n \iint_{\R^{n+1}_+} t \abs{\nabla u(y, t)}^2 \, dy \, dt$, where $\omega_n$ is the volume of the unit ball of $\R^n$.
With $\hat f(\xi) = \int f(x) e^{-2\pi i x \cdot \xi} dx$, one has $\hat u(\xi, t) = e^{-2\pi t \abs{\xi}} \hat f(\xi)$, so $\int \abs{\nabla u(y, t)}^2 dy = 8\pi^2 \int \abs{\xi}^2 e^{-4\pi t \abs{\xi}} \abs{\hat f(\xi)}^2 \, d\xi$.
Since $\int_0^\infty t e^{-4\pi t \abs{\xi}} \, dt = (4\pi\abs{\xi})^{-2}$, this gives $\norm{S(f)}_2^2 = \frac{\omega_n}{2} \norm{f}_2^2$.

Non-example: $f = 1$ is bounded but in no $L^p$ with $p < \infty$.
Its Poisson integral is $u = 1$, so $\nabla u = 0$ and $S(f) = 0$ although $f \neq 0$.
So the lower bound $c \norm{f}_p \le \norm{S(f)}_p$ cannot hold for $p = \infty$.
