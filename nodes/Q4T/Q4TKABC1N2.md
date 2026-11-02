---
tag: Q4TKABC1N2
kind: definition
name: Integral transform
msc: [44A05]
defines: YCK709QB06
uses: [0XHDTE5YMZ, XVEWR93EMV]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_transform
---

## Definition

Let $I$ and $J$ be intervals of $\R$, with $-\infty \le t_1 < t_2 \le \infty$ the endpoints of $I$.
Let $K \colon I \times J \to \C$ be a measurable function.
Let $f \colon I \to \C$ be a [[function|0XHDTE5YMZ]].
The *integral transform* of $f$ with kernel $K$ is the function $Tf$ given by
$$(Tf)(u) = \int_{t_1}^{t_2} f(t)\, K(t, u)\, dt$$
at each $u \in J$ for which the integral converges.
The integral is a [[Lebesgue integral|XVEWR93EMV]] or an improper Riemann integral, depending on the setting.

## Remarks

Example: take $I = [0, \infty)$, $J = (0, \infty)$ and $K(t, u) = e^{-ut}$.
This is the Laplace transform; for $f = 1$ the integral $\int_0^\infty e^{-ut}\, dt = 1/u$ converges for every $u \in J$.
Non-example: the map $f \mapsto f'$ is linear but is not an integral transform with a function kernel.
The value $f'(u)$ depends only on the values of $f$ near $u$, and no integrable kernel produces this for all smooth $f$.
The map $f \mapsto Tf$ is linear wherever both sides converge.
The same definition works with $I$ and $J$ replaced by measure spaces, for example subsets of $\R^n$.
