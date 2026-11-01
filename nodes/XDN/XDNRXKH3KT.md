---
tag: XDNRXKH3KT
kind: definition
name: Branch point
msc: [30B40, 30F10]
defines: XP5JC1VXKZ
uses: [0M3YQJ81NB, 03CPD1HGF3, 0DG0Z72CQD, 0CDMXGPSES]
sources:
  - url: https://en.wikipedia.org/wiki/Branch_point
---

## Definition

Let $a \in \C$ and $r > 0$, and let $D^* = \set{z : 0 < \abs{z - a} < r}$ be a punctured disc.
Let $F$ be a [[multivalued function|03CPD1HGF3]] on $D^*$ given by a [[holomorphic|0DG0Z72CQD]] function element that admits [[analytic continuation|0M3YQJ81NB]] along every path in $D^*$.
The point $a$ is a *branch point* of $F$ if some function element of $F$ changes after continuation once around a circle $\abs{z - a} = \rho$ with $0 < \rho < r$.
The point $\infty$ of the [[Riemann sphere|0CDMXGPSES]] is a branch point of $F$ if $0$ is a branch point of $w \mapsto F(1/w)$.

## Remarks

If $n$ turns around $a$ bring each element back to itself for some $n \ge 2$, the branch point is *algebraic*, and the least such $n$ is its order.
Otherwise $a$ is a *transcendental* branch point; a *logarithmic* branch point, where no number of turns brings any element back, is the main example.
Some authors call $n - 1$ the order instead of $n$.
Example: for $F(z) = \sqrt{z}$, continuing the element $e^{(\log z)/2}$ once around $\abs{z} = 1$ multiplies it by $e^{i\pi} = -1$.
So $0$ is an algebraic branch point of order $2$, and so is $\infty$, because $\sqrt{1/w}$ also changes sign around $w = 0$.
The [[complex logarithm|02QGGD5G87]] has logarithmic branch points at $0$ and $\infty$, since each turn adds $2\pi i$.
Non-example: $0$ is not a branch point of $1/z$, which is single-valued on $\C \setminus \set{0}$; it is a pole.
For a holomorphic map between [[Riemann surfaces|5K0N8QMV6Q]], a point where the map is not locally injective is also called a branch point or ramification point.
