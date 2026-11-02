---
tag: XY2MRKDA23
kind: definition
name: Volterra equation of the second kind
msc: [45D05]
defines: ATPSAHYG7C
uses: [DND8CBEVXT, GSMBXT7FPK, 0W29TBTY12]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_integral_equation
---

## Definition

Let $a < b$, let $\Delta = \set{(t, s) : a \le s \le t \le b}$, let $K \colon \Delta \to \C$ be a [[kernel|GSMBXT7FPK]], let $f \colon [a, b] \to \C$ be a given function, and let $\lambda \in \C$.
A *linear Volterra equation of the second kind* is the equation
$$x(t) = f(t) + \lambda \int_a^t K(t, s) \, x(s) \, ds, \quad t \in [a, b],$$
for an unknown function $x$ on $[a, b]$.
The unknown appears outside the [[integral|0W29TBTY12]] with coefficient $1$, and the upper limit of integration is the variable $t$.
The equation is *homogeneous* when $f = 0$.

## Remarks

Example: $x(t) = t + \int_0^t (s - t) \, x(s) \, ds$ on $[0, 1]$, with $K(t, s) = s - t$ and $\lambda = 1$.
The function $x = \sin$ solves it: $\int_0^t (s - t) \sin s \, ds = \sin t - t$, so the right side is $\sin t$.
This is the integral form of $x'' = -x$, $x(0) = 0$, $x'(0) = 1$.
Non-example: $x(t) = f(t) + \int_a^b K(t, s) \, x(s) \, ds$ has the fixed upper limit $b$, so it is a Fredholm equation, not a Volterra one.
The usual standing hypotheses are that $K$ is continuous on $\Delta$ and $f$ is continuous on $[a, b]$; then the [[unique solvability theorem|WG4GVC9HR8]] applies.
Setting $K(t, s) = 0$ for $s > t$ shows that a Volterra equation is a Fredholm equation with a kernel that vanishes above the diagonal.
