---
tag: GTS394XJ7Y
kind: definition
name: Cerf theory
msc: [57R70, 58K05, 57R65]
defines: W6SSJN7TVW
uses: [F45VQ47GPV, KPQ96640ZJ, 0YTCMFB4HC]
sources:
  - url: https://en.wikipedia.org/wiki/Cerf_theory
---

## Definition

Let $M$ be a compact [[smooth manifold|F45VQ47GPV]] of dimension $n$ without boundary.
*Cerf theory* is the study of smooth one-parameter families $f_t \colon M \to \R$, $t \in [0, 1]$, of smooth functions, with $(x, t) \mapsto f_t(x)$ smooth.
Its basic notion is a *generic path*, also called a *Cerf path*.
A family $(f_t)$ is a generic path if it satisfies the following conditions.

1. For all but finitely many $t$, $f_t$ is a [[Morse function|KPQ96640ZJ]] with distinct critical values.
2. At each remaining time $t_0$, one of two cases occurs.
3. In the first case, $f_{t_0}$ is Morse, exactly two [[critical points|0YTCMFB4HC]] share a critical value, and these two values cross transversally at $t_0$.
4. In the second case, $f_{t_0}$ has distinct critical values and exactly one degenerate critical point $p_0$.
5. In the second case, near $p_0$ there are local coordinates $(x_1, \dots, x_n)$ and a local time parameter $s$ with $s = 0$ at $t_0$ with the following form.
   For some $0 \le \lambda \le n - 1$ and a smooth function $c$, one has $f_t = c(s) + x_1^3 + s x_1 - x_2^2 - \cdots - x_{\lambda+1}^2 + x_{\lambda+2}^2 + \cdots + x_n^2$.

## Remarks

In item 5, for $s < 0$ there are two critical points near the origin, of indices $\lambda$ and $\lambda + 1$, and for $s > 0$ there are none; this is a *birth–death* singularity.
Cerf's theorem says that generic paths are dense in the space of smooth paths between two given endpoints.
Here the endpoints are Morse functions with distinct critical values.
The *Cerf graphic* of a generic path is the subset $\set{(t, f_t(p)) : p \text{ critical for } f_t}$ of $[0, 1] \times \R$; it shows births, deaths and crossings as cusps and crossings of curves.
Example, in a chart of a $1$-dimensional $M$: $f_t(x) = x^3 - (t - \tfrac{1}{2}) x$ satisfies item 5 at $t_0 = \tfrac{1}{2}$ with $s = -(t - \tfrac{1}{2})$ and $\lambda = 0$.
Non-example: the constant path $f_t(x) = x^3$ fails item 1, because the degenerate critical point $0$ occurs at every time.
