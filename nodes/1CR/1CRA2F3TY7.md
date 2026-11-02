---
tag: 1CRA2F3TY7
kind: definition
name: Kernel of an integral equation
msc: [45A05, 45P05]
defines: GSMBXT7FPK
uses: [R3SG1SN7JQ, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_transform
---

## Definition

Let $a < b$, let $K \colon [a, b] \times [a, b] \to \C$ and $f \colon [a, b] \to \C$ be given [[functions|0EPAT51DXQ]], and let $\lambda \in \C$.
Consider an [[integral equation|R3SG1SN7JQ]] of one of the forms
$$\int_a^b K(x, s) \varphi(s) \, ds = f(x), \qquad \varphi(x) - \lambda \int_a^b K(x, s) \varphi(s) \, ds = f(x),$$
or the same forms with the upper limit $b$ replaced by $x$.
The function $K$ is the *kernel* of the equation.
The map $\varphi \mapsto \int_a^b K(\cdot, s) \varphi(s) \, ds$ is the *integral operator* with kernel $K$.

## Remarks

Example: in $\varphi(x) - \int_0^1 e^{x - s} \varphi(s) \, ds = x$ the kernel is $K(x, s) = e^{x - s}$ and $\lambda = 1$.

Non-example: in $\varphi(x) = x + \int_0^1 \varphi(s)^2 \, ds$ the unknown does not enter linearly under the integral, so the equation has no kernel in this sense.
For a nonlinear equation $\varphi(x) = f(x) + \int_a^b H(x, s, \varphi(s)) \, ds$, the function $H$ of three variables is sometimes also called the kernel.

For a Volterra equation, with upper limit $x$, only the values of $K$ with $s \le x$ matter, and one may set $K(x, s) = 0$ for $s > x$.
