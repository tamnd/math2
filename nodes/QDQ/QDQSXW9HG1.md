---
tag: QDQSXW9HG1
kind: definition
name: Hammerstein integral equation
msc: [45G10]
defines: T7E2EW2T0G
uses: [WZ4Z26XSVC, W8G3AZ0DNG, GSMBXT7FPK]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Definition

Let $\Omega$ be a measurable subset of $\R^m$, for example a closed interval $[a, b]$.
Let $k \colon \Omega \times \Omega \to \R$ be a [[kernel|GSMBXT7FPK]], let $g \colon \Omega \times \R \to \R$ be a function, and let $f \colon \Omega \to \R$ be given.
A *Hammerstein integral equation* for an unknown function $\varphi \colon \Omega \to \R$ is
$$\varphi(x) = f(x) + \int_\Omega k(x, t)\, g\bigl(t, \varphi(t)\bigr)\, dt, \quad x \in \Omega.$$
With the linear operator $(K v)(x) = \int_\Omega k(x, t)\, v(t)\, dt$ and the [[Nemytskii operator|W8G3AZ0DNG]] $(N_g \varphi)(t) = g(t, \varphi(t))$, it reads $\varphi = f + K N_g \varphi$.

## Remarks

It is the [[Urysohn equation|WZ4Z26XSVC]] with the product kernel $K(x, t, u) = k(x, t)\, g(t, u)$.
Many authors write it as $\varphi + K N_g \varphi = f$, which only changes the sign of $g$.

Example: on $[0, 1]$, take $f = 0$, $k(x, t) = x t$ and $g(t, u) = u^2$.
Try $\varphi(x) = c x$; the right side is $x \int_0^1 t \cdot c^2 t^2\, dt = \frac{c^2}{4} x$, so $c = c^2/4$, that is $c = 0$ or $c = 4$.
So $\varphi = 0$ and $\varphi(x) = 4x$ are two solutions, and the equation has no uniqueness.

Non-example: $\varphi(x) = \int_0^1 \sin\bigl(x\, \varphi(t)\bigr)\, dt$ is a Urysohn equation but not a Hammerstein one with a single product kernel, because $\sin(xu)$ is not of the form $k(x, t)\, g(t, u)$.
Indeed, the functions $u \mapsto \sin(x u)$ for different $x$ are not all multiples of one function.

Example of origin: on $[0, 1]$ the problem $-u'' = h(x, u)$, $u(0) = u(1) = 0$, with continuous $h$, is equivalent to $u(x) = \int_0^1 G(x, t)\, h(t, u(t))\, dt$, where $G(x, t) = \min(x, t)\bigl(1 - \max(x, t)\bigr)$ is the Green's function.
