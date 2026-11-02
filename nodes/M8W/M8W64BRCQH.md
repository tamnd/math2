---
tag: M8W64BRCQH
kind: definition
name: Wiener–Hopf equation
msc: ["45E10", 47B35]
defines: QYY4NMDY5H
uses: [EY75YD988Z, B5AB451TB7, SASP14MA1Z, EV6ZDQ0NDY]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener%E2%80%93Hopf_method
---

## Definition

Let $k \in L^1(\R)$, a function in the [[$L^1$ space|SASP14MA1Z]] of $\R$, and let $f$ be a given function on $[0, \infty)$.
A *Wiener–Hopf equation of the second kind* for an unknown function $\varphi$ on $[0, \infty)$ is
$$\varphi(x) - \int_0^\infty k(x - t)\, \varphi(t)\, dt = f(x), \quad x \ge 0.$$
A *Wiener–Hopf equation of the first kind* is
$$\int_0^\infty k(x - t)\, \varphi(t)\, dt = f(x), \quad x \ge 0.$$
The kernel $k(x - t)$ is a [[difference kernel|B5AB451TB7]], and both $x$ and $t$ range over the half-line $[0, \infty)$.

## Remarks

The unknown is usually sought in $L^p(0, \infty)$ with $1 \le p \le \infty$, or in a space of bounded or of polynomially growing functions.
Kernels such as $\frac{1}{2} E_1(\abs{x})$, with $E_1$ the [[exponential integral|EV6ZDQ0NDY]], are also used; this one is in $L^1(\R)$.

Example: $k(x) = \frac{1}{2} e^{-\abs{x}}$ and $f(x) = \frac{1}{2} e^{-x}$.
The constant $\varphi = 1$ is a solution.
Check: $\int_0^\infty \frac{1}{2} e^{-\abs{x - t}}\, dt = \frac{1}{2}(1 - e^{-x}) + \frac{1}{2} = 1 - \frac{1}{2} e^{-x}$, so $\varphi - \int_0^\infty k(x - t) \varphi(t)\, dt = \frac{1}{2} e^{-x}$.
The function $1 + x$ solves the homogeneous equation with the same kernel, so this equation has more than one solution among functions of linear growth.

Non-example: $\varphi(x) - \int_{-\infty}^{\infty} k(x - t)\, \varphi(t)\, dt = f(x)$ for all $x \in \R$ is a convolution equation on the whole line.
It is not a Wiener–Hopf equation, and the Fourier transform solves it directly when $1 - \hat k$ has no zeros.

The integral operator $\varphi \mapsto \int_0^\infty k(x - t) \varphi(t)\, dt$ is the continuous analogue of a Toeplitz matrix, and it is called a Wiener–Hopf operator.
