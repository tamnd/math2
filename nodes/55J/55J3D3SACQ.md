---
tag: 55J3D3SACQ
kind: definition
name: p-adic absolute value
msc: [12J25, 11S99]
defines: WGN82TCEF2
uses: [01826KMG2H, 03HDF50VN4, 0NCJ5WXN6Z, 0FFXKTKKQC]
sources:
  - url: https://en.wikipedia.org/wiki/P-adic_valuation
---

## Definition

Let $p$ be a [[prime number|01826KMG2H]].
For a nonzero rational number $x$, let $v_p(x)$ be its [[p-adic valuation|03HDF50VN4]], the integer $k$ with $x = p^k a / b$ for integers $a, b$ not divisible by $p$.
The *$p$-adic absolute value* is the map $\abs{\cdot}_p \colon \Q \to \R$ given by
$$\abs{x}_p = p^{-v_p(x)} \text{ for } x \neq 0, \qquad \abs{0}_p = 0.$$

## Remarks

It is an [[absolute value|0FFXKTKKQC]] on $\Q$ in the sense of fields:

1. $\abs{x}_p = 0$ exactly when $x = 0$;
2. $\abs{xy}_p = \abs{x}_p \abs{y}_p$;
3. $\abs{x + y}_p \le \max(\abs{x}_p, \abs{y}_p)$, which is stronger than the triangle inequality.

Example: $\abs{12}_2 = 2^{-2} = 1/4$ and $\abs{3/8}_2 = 2^{3} = 8$.
Non-example: the map $x \mapsto p^{v_p(x)}$, without the minus sign, is not an absolute value.
Indeed, it gives $1$ to both $p^2 - 1$ and $1$, but $p^2$ to their sum $p^2$, so the triangle inequality fails.
Product formula: for every nonzero rational $x$, $\abs{x} \prod_p \abs{x}_p = 1$, where $\abs{x}$ is the usual absolute value.
