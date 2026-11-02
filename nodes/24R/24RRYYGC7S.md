---
tag: 24RRYYGC7S
kind: definition
name: Urysohn integral equation
msc: [45G10]
defines: WZ4Z26XSVC
uses: [BSCYBP6AS6, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Definition

Let $\Omega$ be a measurable subset of $\R^m$, for example a closed interval $[a, b]$.
Let $K \colon \Omega \times \Omega \times \R \to \R$ and $f \colon \Omega \to \R$ be given functions.
A *Urysohn integral equation* for an unknown function $\varphi \colon \Omega \to \R$ is
$$\varphi(x) = f(x) + \int_\Omega K\bigl(x, t, \varphi(t)\bigr)\, dt, \quad x \in \Omega.$$
The function $K$ is the *Urysohn kernel*, and the map $\varphi \mapsto \int_\Omega K(x, t, \varphi(t))\, dt$ is the *Urysohn operator*.

## Remarks

In the classical setting $\Omega = [a, b]$, $K$ and $f$ are [[continuous|0X3WGX95FE]], and $\varphi$ is sought among continuous functions.
If $K(x, t, u) = k(x, t)\, u$, the equation is a linear Fredholm equation of the second kind.
If $K(x, t, u) = k(x, t)\, g(t, u)$, it is a Hammerstein equation.
Some authors also call $\int_\Omega K(x, t, \varphi(t))\, dt = f(x)$ a Urysohn equation of the first kind.

Example: on $[0, 1]$, take $f(x) = x$ and $K(x, t, u) = \sin\bigl(x(u - t)\bigr)$.
Then $\varphi(x) = x$ is a solution: the integrand is $\sin 0 = 0$, so the right side is $x$.

Non-example: $\varphi(x)^3 = f(x) + \int_\Omega k(x, t)\, \varphi(t)\, dt$ is a nonlinear integral equation, but not a Urysohn equation, since the unknown appears outside the integral through $\varphi(x)^3$ and not alone.
