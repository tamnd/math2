---
tag: WH10W2GWZX
kind: definition
name: Order polynomial
msc: [06A07, 05A15]
defines: VDBDJZWPEA
uses: [0QV2JS9RJ3, 0A7KV2WB7A, W8DZ5KGGHN]
sources:
  - url: https://en.wikipedia.org/wiki/Order_polynomial
---

## Definition

Let $(P, \le)$ be a finite [[partially ordered set|0QV2JS9RJ3]] with $p$ elements.
For an integer $m \ge 1$, let $[m] = \set{1, \ldots, m}$ with the usual order.
Let $\Omega(P, m)$ be the number of [[order-preserving|0A7KV2WB7A]] maps $f \colon P \to [m]$, that is, maps with $f(x) \le f(y)$ whenever $x \le y$.
The *order polynomial* of $P$ is the unique polynomial $\Omega(P, t)$ in $t$ that takes the value $\Omega(P, m)$ at every integer $m \ge 1$.

## Remarks

Such a polynomial exists, and it has degree $p$ with leading coefficient $e(P)/p!$, where $e(P)$ is the number of [[linear extensions|W8DZ5KGGHN]] of $P$.

Example: for the chain $x_1 < x_2 < \cdots < x_p$, $\Omega(P, m) = \binom{m + p - 1}{p}$.
Check: an order-preserving map is a weakly increasing sequence $f(x_1) \le \cdots \le f(x_p)$ in $[m]$, that is, a multiset of size $p$ from $m$ values; the leading coefficient is $1/p!$, and $e(P) = 1$.

Non-example: the count $m^p$ of all maps $P \to [m]$ is not the order polynomial of the chain when $p \ge 2$.
It also counts maps that break the order, such as $f(x_1) = 2$, $f(x_2) = 1$.

The strict order polynomial $\Omega^\circ(P, m)$ counts the maps with $x < y \Rightarrow f(x) < f(y)$.
Stanley's reciprocity theorem says $\Omega^\circ(P, t) = (-1)^p \, \Omega(P, -t)$.
