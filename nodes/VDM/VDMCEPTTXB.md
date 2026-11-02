---
tag: VDMCEPTTXB
kind: definition
name: Convolution on the half-line
msc: [44A35, 44A40]
defines: FCKX8KFVGN
uses: [DWJF7ABPR1, ERP5737VZ1]
sources:
  - url: https://en.wikipedia.org/wiki/Convolution
---

## Definition

Let $f, g \colon [0, \infty) \to \C$ be locally integrable, that is, Lebesgue integrable on $[0, T]$ for every $T > 0$.
The *convolution* of $f$ and $g$ is the function $f * g$ on $[0, \infty)$ given by
$$(f * g)(t) = \int_0^t f(\tau) \, g(t - \tau) \, d\tau$$
at each $t \ge 0$ at which the [[Lebesgue integral|DWJF7ABPR1]] converges absolutely.

## Remarks

The integral converges for almost every $t$, and $f * g$ is again locally integrable.
If $f$ and $g$ are continuous, then $f * g$ is defined everywhere and continuous, with $(f * g)(0) = 0$.
Extending $f$ and $g$ by $0$ on $(-\infty, 0)$ turns this into the [[convolution on the line|ERP5737VZ1]].

Example: for integers $m, n \ge 0$, the functions $t^m$ and $t^n$ give
$$(t^m * t^n)(t) = \int_0^t \tau^m (t - \tau)^n \, d\tau = \frac{m! \, n!}{(m + n + 1)!} \, t^{m + n + 1},$$
by the Beta integral; for $m = n = 0$ this is $1 * 1 = t$.

Non-example: $f(t) = 1/t$ for $t > 0$ is not integrable on $[0, 1]$, so it is not locally integrable on $[0, \infty)$.
Indeed $(f * 1)(t) = \int_0^t d\tau / \tau$ diverges for every $t > 0$.
