---
tag: SPV5SRAS9H
kind: example
name: Carleman's singular integral equation
msc: ["45E05", "45E99"]
instance_of: [E30EA6ETZ4]
uses: [0SYR10HD4R, 5JYBXH9BP6, RY8YQ9JZF9, RNB6QX0GCA, E30EA6ETZ4, W6Z6CWRE25]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_integral_operators_on_closed_curves
---

## Example

Let $a$ and $b$ be real constants with $b \ne 0$, and let $f$ be a given function on the interval $(-1, 1)$.
*Carleman's equation* asks for a function $\varphi$ on $(-1, 1)$ with
$$a\, \varphi(x) + \frac{b}{\pi}\, \mathrm{PV}\!\int_{-1}^{1} \frac{\varphi(t)}{t - x}\, dt = f(x), \quad -1 < x < 1,$$
where $\mathrm{PV}$ is the [[Cauchy principal value|0SYR10HD4R]].
It is a [[singular integral equation|E30EA6ETZ4]] of the second kind with constant coefficients on an arc, and its singular part is the [[finite Hilbert transform|5JYBXH9BP6]].

A check with an explicit solution uses two classical principal value integrals, valid for $-1 < x < 1$:
$$\frac{1}{\pi}\, \mathrm{PV}\!\int_{-1}^{1} \frac{\sqrt{1 - t^2}}{t - x}\, dt = -x, \qquad \frac{1}{\pi}\, \mathrm{PV}\!\int_{-1}^{1} \frac{dt}{\sqrt{1 - t^2}\,(t - x)} = 0.$$
Hence $\varphi(t) = \sqrt{1 - t^2}$ solves the equation with right side $f(x) = a\sqrt{1 - x^2} - b x$.
The function $(1 - t^2)^{-1/2}$ solves it with right side $f(x) = a (1 - x^2)^{-1/2}$.

## Remarks

Put $\Phi(z) = \frac{1}{2\pi i} \int_{-1}^{1} \frac{\varphi(t)}{t - z}\, dt$ for $z \notin [-1, 1]$.
By the [[Sokhotski–Plemelj theorem|RNB6QX0GCA]], $\Phi^+ - \Phi^- = \varphi$ and $\Phi^+ + \Phi^- = \frac{1}{\pi i}\, \mathrm{PV}\!\int_{-1}^{1} \frac{\varphi(t)}{t - x}\, dt$ on the cut.
The equation becomes $(a + ib)\, \Phi^+ = (a - ib)\, \Phi^- + f$, a [[Riemann–Hilbert problem|RY8YQ9JZF9]] on the segment with constant coefficient $(a - ib)/(a + ib)$ of modulus $1$.
Solving it gives the solutions in closed form, with powers of $1 - x$ and $1 + x$ at the endpoints whose exponents are fixed by the argument of $a + ib$.
For $a = 0$ the equation is the [[airfoil equation|W6Z6CWRE25]].

## Explanations

### L1 human

This is the simplest singular integral equation on an interval: the unknown appears once by itself and once inside a Cauchy principal value integral.
The integral blows up where $t = x$, so it is taken as a principal value.
Because the coefficients are constants, the equation can be solved exactly by turning it into a jump problem for holomorphic functions.
