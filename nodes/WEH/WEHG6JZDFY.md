---
tag: WEHG6JZDFY
kind: definition
name: Hypersingular integral equation
msc: ["45E99", "45E05"]
defines: QVRP8FSAZM
uses: [G7VE41JHHH, GSMBXT7FPK, 0SYR10HD4R]
sources:
  - url: https://en.wikipedia.org/wiki/Hadamard_regularization
---

## Definition

Let $a, b \colon (-1, 1) \to \R$ and $f \colon (-1, 1) \to \R$ be given functions, and let $K$ be a [[kernel|GSMBXT7FPK]] on $(-1, 1)^2$ that is integrable in $t$ for each $x$.
A *hypersingular integral equation* on $(-1, 1)$ for an unknown $\varphi$ is
$$a(x)\, \varphi(x) + \frac{b(x)}{\pi}\, \mathrm{f.p.}\!\int_{-1}^{1} \frac{\varphi(t)}{(t - x)^2}\, dt + \int_{-1}^{1} K(x, t)\, \varphi(t)\, dt = f(x), \quad -1 < x < 1,$$
where $\mathrm{f.p.}$ denotes the [[Hadamard finite part|G7VE41JHHH]] and $b$ does not vanish identically.
The unknown $\varphi$ is sought among functions for which the finite part exists, for instance functions whose derivative is Hölder continuous on each compact subinterval.
If $a = 0$, the equation is of the *first kind*.

## Remarks

More generally, an integral equation on a domain or surface of dimension $m$ is called hypersingular when its kernel grows like $\abs{x - t}^{-m-1}$ or faster near the diagonal.

Example: the first kind equation $\frac{1}{\pi}\, \mathrm{f.p.}\!\int_{-1}^{1} \frac{\varphi(t)}{(t - x)^2}\, dt = -1$ has the solution $\varphi(t) = \sqrt{1 - t^2}$.
Check: the finite part is the $x$-derivative of $\frac{1}{\pi}\, \mathrm{PV}\!\int_{-1}^{1} \frac{\sqrt{1 - t^2}}{t - x}\, dt = -x$, which is $-1$.
Here $\mathrm{PV}$ is the [[Cauchy principal value|0SYR10HD4R]].
Equations of this form, with the condition $\varphi(\pm 1) = 0$, describe the opening of a straight crack under uniform pressure.

Non-example: $\frac{1}{\pi}\, \mathrm{PV}\!\int_{-1}^{1} \frac{\varphi(t)}{t - x}\, dt = f(x)$ has a Cauchy kernel of order $1$, so it is a singular but not a hypersingular equation.

The finite part is the derivative of a principal value.
So, when $\varphi(\pm 1) = 0$, an integration by parts turns a hypersingular equation of the first kind for $\varphi$ into a Cauchy singular equation for $\varphi'$.
