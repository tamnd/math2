---
tag: K2S5TAW2BF
kind: definition
name: Order of a zero or pole
msc: [30D30, 30C15]
defines: 23ASRP0MWR
uses: [0NSD1TPHR0, 064N002TX4, 0YK27TJ4WF, 0X3XD2ATB0, 0DG0Z72CQD]
sources:
  - url: https://en.wikipedia.org/wiki/Zeros_and_poles
---

## Definition

Let $U \subseteq \C$ be an open set, let $f$ be a [[meromorphic function|0NSD1TPHR0]] on $U$, and let $a \in U$.
Assume that $f$ is not identically $0$ on any punctured disc around $a$.
The *order* of $f$ at $a$, written $\operatorname{ord}_a f$, is the unique integer $n$ with the following property.
There are $r > 0$ and a [[holomorphic|0DG0Z72CQD]] function $g$ on $\set{z : \abs{z - a} < r}$ with $g(a) \neq 0$ and $f(z) = (z - a)^n g(z)$ for $0 < \abs{z - a} < r$.
If $f$ is identically $0$ near $a$, one sets $\operatorname{ord}_a f = \infty$.

## Remarks

If $n > 0$, then $a$ is a zero of [[order|064N002TX4]] $n$; if $n < 0$, then $a$ is a pole of [[order|0YK27TJ4WF]] $-n$; if $n = 0$, then $f(a)$ is defined and nonzero.
Equivalently, $n$ is the least index with a nonzero coefficient in the [[Laurent series|0X3XD2ATB0]] of $f$ at $a$.
Example: $f(z) = \dfrac{\sin z}{z^3}$ has $\operatorname{ord}_0 f = -2$, since $\sin z = z \, h(z)$ with $h$ holomorphic and $h(0) = 1$.
Non-example: $e^{1/z}$ is not meromorphic near $0$ and has no order there.
Its Laurent series at $0$ has infinitely many nonzero terms of negative index.
The order satisfies $\operatorname{ord}_a(fg) = \operatorname{ord}_a f + \operatorname{ord}_a g$ and $\operatorname{ord}_a(f + g) \ge \min(\operatorname{ord}_a f, \operatorname{ord}_a g)$.
Some authors call it the valuation of $f$ at $a$.
