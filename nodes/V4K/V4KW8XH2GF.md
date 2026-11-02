---
tag: V4KW8XH2GF
kind: definition
name: Trace of an integral operator
msc: [45C05, 47G10, 47B10]
defines: 3JVT83K8A1
uses: [R3SG1SN7JQ, ZM5G144PZG, 0XC1RDBY7A]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_class
---

## Definition

Let $a < b$ and let $K \colon [a, b] \times [a, b] \to \C$ be a [[continuous kernel|ZM5G144PZG]].
Let $T$ be the integral operator $(T x)(s) = \int_a^b K(s, t) \, x(t) \, dt$ of an [[integral equation|R3SG1SN7JQ]] with kernel $K$.
The *trace* of $T$, or of the kernel $K$, is the number
$$\operatorname{tr} K = \int_a^b K(s, s) \, ds.$$

## Remarks

Example: for $K(s, t) = \min(s, t)$ on $[0, 1]$, the kernel is continuous and $\operatorname{tr} K = \int_0^1 s \, ds = 1/2$.
Non-example: the weakly singular kernel $K(s, t) = \abs{s - t}^{-1/2}$ on $[0, 1]$ is not continuous, and it is infinite on the diagonal, so the formula gives no number.
For a degenerate kernel $K(s, t) = \sum_{i=1}^n u_i(s) v_i(t)$, the trace is $\sum_{i=1}^n \int_a^b u_i(s) v_i(s) \, ds$.
This is the [[trace|0XC1RDBY7A]] of the $n \times n$ matrix with entries $\int_a^b v_i(s) u_j(s) \, ds$, which represents $T$ on the span of $u_1, \dots, u_n$.
The traces $\int_a^b K_m(s, s) \, ds$ of the iterated kernels $K_m$, $m \ge 2$, appear in the power series of the Fredholm determinant.
A continuous kernel need not define a [[trace class operator|Z2CP530WDE]] on $L^2(a, b)$; when it does, the number above equals the operator trace.
