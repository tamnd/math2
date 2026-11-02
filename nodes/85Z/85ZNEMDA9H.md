---
tag: 85ZNEMDA9H
kind: definition
name: Ring of convergent power series
msc: [32B05, 13J07, 32A05]
defines: EVPZ7ZG1HB
uses: [KCBFS516DE, R3QTCPTJK7]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Definition

Let $n \ge 0$ and let $\C[\![z_1, \dots, z_n]\!]$ be the ring of [[formal power series|KCBFS516DE]] in $n$ variables over $\C$.
For a multi-index $\alpha = (\alpha_1, \dots, \alpha_n) \in \N^n$ write $z^\alpha = z_1^{\alpha_1} \cdots z_n^{\alpha_n}$ and $\abs{\alpha} = \alpha_1 + \cdots + \alpha_n$.
A [[power series|R3QTCPTJK7]] $f = \sum_{\alpha} c_\alpha z^\alpha$ is *convergent* if there is a real number $r > 0$ with
$$\sum_{\alpha \in \N^n} \abs{c_\alpha}\, r^{\abs{\alpha}} < \infty.$$
The *ring of convergent power series* $\C\{z_1, \dots, z_n\}$ is the set of convergent power series, with the addition and multiplication of formal power series.

## Remarks

The condition says that the series converges absolutely on the closed polydisc of radius $r$ about $0$; it is equivalent to convergence on some neighbourhood of $0$.
Sums and products of convergent series are convergent, so $\C\{z_1, \dots, z_n\}$ is a subring of $\C[\![z_1, \dots, z_n]\!]$.
Example: $f = \sum_{k \ge 0} z_1^k z_2^k$ is convergent: with $r = 1/2$, $\sum_k r^{2k} = 4/3 < \infty$.
Non-example: $g = \sum_{k \ge 0} k!\, z_1^k$ is not convergent, since $k!\, r^k \to \infty$ for every $r > 0$.
For $n = 0$ the ring is $\C$.
A convergent series is a unit if and only if its constant term is nonzero, so the ring is local with maximal ideal $(z_1, \dots, z_n)$.
Sending a series to its sum near $0$ gives an isomorphism with the ring $\mathcal{O}_{n,0}$ of germs of holomorphic functions at $0$.
