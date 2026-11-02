---
tag: FZYDPWMS46
kind: definition
name: Integral equation
msc: [45A05, 45G10]
defines: R3SG1SN7JQ
uses: [0EPAT51DXQ, 0W29TBTY12]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Definition

Let $a < b$ and let $\varphi \colon [a, b] \to \C$ be an unknown [[function|0EPAT51DXQ]].
For each $x \in [a, b]$, let $I_x \subseteq [a, b]$ be an interval of integration, either the fixed interval $[a, b]$ or the interval $[a, x]$.
An *integral equation* for $\varphi$ is an equation of the form
$$F\left(x, \varphi(x), \int_{I_x} H\left(x, s, \varphi(s)\right) ds\right) = 0 \quad \text{for all } x \in [a, b],$$
where $F$ and $H$ are given functions.
A *solution* is a function $\varphi$ for which the [[integrals|0W29TBTY12]] exist and the equation holds for every $x \in [a, b]$.

## Remarks

Example: $\varphi(x) = x + \int_0^1 x s \, \varphi(s) \, ds$ on $[0, 1]$ is an integral equation with $I_x = [0, 1]$.
Try $\varphi(x) = c x$: the integral is $c x / 3$, so $c = 1 + c/3$ and $c = 3/2$.
So $\varphi(x) = 3x/2$ is a solution.

Non-example: $\varphi'(x) = \varphi(x)$ is a differential equation, not an integral equation, since $\varphi$ does not appear under an integral.
Its integral form $\varphi(x) = \varphi(0) + \int_0^x \varphi(s) \, ds$ is an integral equation.

The same definition is used with a region of $\R^m$ in place of $[a, b]$, and with vector-valued unknowns.
When $I_x = [a, b]$ the equation is of Fredholm type; when $I_x = [a, x]$ it is of Volterra type.
