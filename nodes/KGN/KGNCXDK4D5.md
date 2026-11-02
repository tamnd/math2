---
tag: KGNCXDK4D5
kind: definition
name: Linear integral equation
msc: [45A05]
defines: AYZCKG34QK
uses: [R3SG1SN7JQ, GSMBXT7FPK, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Definition

Let $a < b$, let $a_0, f \colon [a, b] \to \C$ be given functions, let $K \colon [a, b] \times [a, b] \to \C$ be a given [[kernel|GSMBXT7FPK]], and let $\lambda \in \C$.
For each $x \in [a, b]$, let $I_x$ be either $[a, b]$ or $[a, x]$.
A *linear integral equation* for the unknown function $\varphi \colon [a, b] \to \C$ is an [[integral equation|R3SG1SN7JQ]] of the form
$$a_0(x) \varphi(x) = f(x) + \lambda \int_{I_x} K(x, s) \varphi(s) \, ds \quad \text{for all } x \in [a, b].$$

## Remarks

Example: $\varphi(x) = \sin x + \int_0^{\pi} \cos(x - s) \varphi(s) \, ds$ is linear, with $a_0 = 1$, $f = \sin$, $K(x, s) = \cos(x - s)$ and $\lambda = 1$.

Non-example: $\varphi(x) = 1 + \int_0^1 x s \, \varphi(s)^2 \, ds$ is not linear, because $\varphi$ enters through $\varphi(s)^2$.
If $\varphi$ solves it, then $2\varphi$ does not solve the equation with $f$ replaced by $2$.

The equation is of the first kind when $a_0 = 0$ and of the second kind when $a_0 = 1$.
It is of the third kind when $a_0$ is a [[continuous function|0X3WGX95FE]] that vanishes somewhere but not everywhere.
If $a_0$ has no zeros, dividing by $a_0$ gives an equation of the second kind.
In operator notation the equation reads $a_0 \varphi = f + \lambda K \varphi$, where $K$ also denotes the integral operator.
