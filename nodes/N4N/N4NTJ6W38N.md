---
tag: N4NTJ6W38N
kind: definition
name: Nonlinear integral equation
msc: [45G10]
defines: BSCYBP6AS6
uses: [R3SG1SN7JQ, AYZCKG34QK]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Definition

Let $a < b$.
A *nonlinear integral equation* on $[a, b]$ is an [[integral equation|R3SG1SN7JQ]] for an unknown function $\varphi \colon [a, b] \to \C$ that is not a [[linear integral equation|AYZCKG34QK]].
The most common form is the *Urysohn equation*
$$\varphi(x) = f(x) + \int_{I_x} H\left(x, s, \varphi(s)\right) ds \quad \text{for all } x \in [a, b].$$
Here $I_x$ is $[a, b]$ or $[a, x]$, $f$ is given, and $H \colon [a, b] \times [a, b] \times \C \to \C$ is a given function that is not affine in its third variable.

## Remarks

Example: $\varphi(x) = x + \int_0^1 \varphi(s)^2 \, ds$ on $[0, 1]$ is nonlinear, with $H(x, s, u) = u^2$.
A solution has the form $\varphi(x) = x + c$, where $c = \int_0^1 (s + c)^2 \, ds = 1/3 + c + c^2$.
This gives $c^2 = -1/3$, so the equation has the two complex solutions $\varphi(x) = x \pm i/\sqrt{3}$ and no real one.

Non-example: $\varphi(x) = x + \int_0^1 (x s \, \varphi(s) + s^2) \, ds$ is linear, since $H(x, s, u) = x s u + s^2$ is affine in $u$.

When $H(x, s, u) = K(x, s) \, g(s, u)$ the equation is called a *Hammerstein equation*.
