---
tag: 1DFG72YV3N
kind: definition
name: Nonlinear Volterra equation
msc: [45D05, 45G10]
defines: F18MBATVVP
uses: [DND8CBEVXT, BSCYBP6AS6, 0X3WGX95FE, 0AW1E6YTJY]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_integral_equation
---

## Definition

Let $a < b$, let $\Delta = \set{(t, s) : a \le s \le t \le b}$, let $K \colon \Delta \times \R \to \R$ and $f \colon [a, b] \to \R$ be [[continuous|0X3WGX95FE]].
A *nonlinear Volterra equation of the second kind* for an unknown continuous function $\varphi$ is
$$\varphi(t) = f(t) + \int_a^t K\bigl(t, s, \varphi(s)\bigr)\, ds, \quad a \le t \le b.$$
A *nonlinear Volterra equation of the first kind* is $\int_a^t K(t, s, \varphi(s))\, ds = f(t)$.
A solution on a subinterval $[a, c]$ with $c \le b$ is a continuous function on $[a, c]$ that satisfies the equation there.

## Remarks

If $K(t, s, u) = k(t, s)\, u$, this is the linear [[Volterra integral equation|DND8CBEVXT]] of the second kind.
If $K$ satisfies a [[Lipschitz condition|0AW1E6YTJY]] $\abs{K(t, s, u) - K(t, s, v)} \le L \abs{u - v}$ on all of $\Delta \times \R$, the equation has exactly one continuous solution on $[a, b]$, and the successive approximations converge to it.
If the Lipschitz condition holds only for $u, v$ in bounded sets, there is still a unique solution on some interval $[a, c]$ with $c > a$.

Example: $\varphi(t) = 1 + \int_0^t \varphi(s)^2\, ds$ on $[0, 1)$, with $K(t, s, u) = u^2$.
The function $\varphi(t) = 1/(1 - t)$ solves it, since $1 + \int_0^t (1 - s)^{-2}\, ds = 1 + \frac{1}{1 - t} - 1 = \frac{1}{1 - t}$.
It is the integral form of $y' = y^2$, $y(0) = 1$, and the solution does not extend past $t = 1$.

Non-example: $\varphi(t) = f(t) + \int_a^b K(t, s, \varphi(s))\, ds$ has the fixed upper limit $b$; it is a Urysohn equation, not a Volterra one.
