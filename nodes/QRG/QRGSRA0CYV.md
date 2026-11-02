---
tag: QRGSRA0CYV
kind: definition
name: Fractional differential equation
msc: [34A08, 26A33]
defines: YY4XSJX81P
uses: [T73XK15SA2, 6VMGQYF8RW, JTKCZ44NN3, 0H5SYBSED9, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Fractional_calculus
---

## Definition

Let $\alpha > 0$ be a real number that is not an integer, let $n = \ceil{\alpha}$, let $a < b$ be real numbers, and let $f \colon [a, b] \times \R \to \R$ be a function.
Write ${}^C D_a^\alpha$ for the [[Caputo fractional derivative|6VMGQYF8RW]] of order $\alpha$ with base point $a$.
The *fractional differential equation* of Caputo type with right side $f$ is
$$ {}^C D_a^\alpha y(t) = f(t, y(t)), \qquad t \in (a, b],$$
usually with initial conditions $y^{(k)}(a) = y_k$ for $k = 0, 1, \ldots, n - 1$.
More generally, a fractional differential equation relates an unknown function to some of its derivatives in the sense of [[fractional calculus|T73XK15SA2]].
At least one of these derivatives has non-integer order.

## Remarks

Let $f$ be continuous.
A continuous function $y$ solves the initial value problem if and only if it solves the Volterra integral equation
$$y(t) = \sum_{k=0}^{n-1} \frac{y_k}{k!} (t - a)^k + \frac{1}{\Gamma(\alpha)} \int_a^t (t - s)^{\alpha - 1} f(s, y(s)) \, ds.$$
Here $\Gamma$ is the [[gamma function|0H5SYBSED9]], and the integral is the [[Riemann–Liouville integral|JTKCZ44NN3]] of order $\alpha$.
Example: for $0 < \alpha < 1$, $a = 0$, $f \equiv 1$ and $y(0) = 0$, the integral equation gives $y(t) = t^\alpha / \Gamma(\alpha + 1)$, and indeed ${}^C D_0^\alpha t^\alpha = \Gamma(\alpha + 1)$.
For $0 < \alpha < 1$, the equation ${}^C D_0^\alpha y = \lambda y$ with $y(0) = 1$ has the solution $y(t) = \sum_{k \ge 0} \lambda^k t^{\alpha k} / \Gamma(\alpha k + 1)$, a Mittag-Leffler function of $\lambda t^\alpha$; it reduces to $e^{\lambda t}$ when $\alpha = 1$.
Non-example: the delay equation $y'(t) = y(t - 1)$ is not a fractional differential equation, since it contains only a derivative of integer order.
Equations with the Riemann–Liouville derivative are also common; their natural initial conditions are on fractional integrals of $y$ at $a$ rather than on $y^{(k)}(a)$.
