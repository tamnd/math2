---
tag: FWPYXMK52W
kind: definition
name: Integral equation of the first kind
msc: [45A05, 45B05]
defines: ZDS77Q0F06
uses: [AYZCKG34QK, GSMBXT7FPK]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Definition

Let $a < b$, let $K \colon [a, b] \times [a, b] \to \C$ be a [[kernel|GSMBXT7FPK]], and let $f \colon [a, b] \to \C$ be given.
For each $x \in [a, b]$, let $I_x$ be either $[a, b]$ or $[a, x]$.
An *integral equation of the first kind* is a [[linear integral equation|AYZCKG34QK]] of the form
$$\int_{I_x} K(x, s) \varphi(s) \, ds = f(x) \quad \text{for all } x \in [a, b],$$
for the unknown function $\varphi \colon [a, b] \to \C$.

## Remarks

Example: $\int_0^1 (x + s) \varphi(s) \, ds = x$ on $[0, 1]$ is of the first kind.
With $\alpha = \int_0^1 \varphi$ and $\beta = \int_0^1 s \varphi(s) \, ds$ it says $\alpha x + \beta = x$, so $\alpha = 1$ and $\beta = 0$.
The function $\varphi(s) = 4 - 6s$ satisfies both, since $\int_0^1 (4 - 6s) \, ds = 1$ and $\int_0^1 (4s - 6s^2) \, ds = 0$; so do infinitely many others.

Non-example: $\varphi(x) = x + \int_0^1 (x + s) \varphi(s) \, ds$ is not of the first kind, because $\varphi$ also appears outside the integral.

With $I_x = [a, b]$ it is a Fredholm equation of the first kind; with $I_x = [a, x]$ it is a Volterra equation of the first kind.
The example shows that the solution need not be unique.
The right side $f(x) = x^2$ shows that it need not exist, since the left side is always affine in $x$.
