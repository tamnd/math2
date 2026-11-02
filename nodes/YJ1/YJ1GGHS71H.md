---
tag: YJ1GGHS71H
kind: definition
name: Fredholm integral equation
msc: [45B05]
defines: 526TCVMSHP
uses: [AYZCKG34QK, GSMBXT7FPK]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_integral_equation
---

## Definition

Let $a < b$, let $K \colon [a, b] \times [a, b] \to \C$ be a [[kernel|GSMBXT7FPK]], let $f \colon [a, b] \to \C$ be given, and let $\lambda \in \C$.
A *Fredholm integral equation of the first kind* is the equation
$$\int_a^b K(x, s) \varphi(s) \, ds = f(x) \quad \text{for all } x \in [a, b].$$
A *Fredholm integral equation of the second kind* is the equation
$$\varphi(x) = f(x) + \lambda \int_a^b K(x, s) \varphi(s) \, ds \quad \text{for all } x \in [a, b].$$
In both, $\varphi \colon [a, b] \to \C$ is the unknown function, and both limits of integration are the fixed numbers $a$ and $b$.
A *Fredholm integral equation* is a [[linear integral equation|AYZCKG34QK]] of one of these two forms.

## Remarks

Example: $\varphi(x) = x + \int_0^1 x s \, \varphi(s) \, ds$ on $[0, 1]$ is of the second kind.
A solution has the form $\varphi(x) = c x$ with $c = 1 + c/3$, so $\varphi(x) = 3x/2$.

Non-example: $\varphi(x) = x + \int_0^x x s \, \varphi(s) \, ds$ is not a Fredholm equation, since the upper limit is the variable $x$; it is a Volterra equation.

A Volterra equation can be written as a Fredholm equation with the kernel set to $0$ for $s > x$, but this kernel is in general discontinuous on the diagonal.
The same definitions are used with $[a, b]$ replaced by a region of $\R^m$ or a measure space.
