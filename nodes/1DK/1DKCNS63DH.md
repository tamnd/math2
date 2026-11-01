---
tag: 1DKCNS63DH
kind: counterexample
name: Long line
msc: [54G20, 54F05, 57N99]
uses: [0YSCSX5YZC, 0B68KNPGCG, 0FRMJH3CY7, 0TVJZYB6SH, 0V032VWTHD, 091GJ3FYD7]
sources:
  - url: https://en.wikipedia.org/wiki/Long_line_(topology)
---

## Counterexample

Let $\omega_1$ be the first uncountable [[ordinal|0YSCSX5YZC]].
The closed long ray is the set $L = \omega_1 \times [0, 1)$ with the [[lexicographic order|0B68KNPGCG]] and the order topology.
The long line is obtained by gluing two copies of $L$ along their least point $(0, 0)$, one of them with the reversed order.
The closed long ray $L$ is Hausdorff, [[connected|0V032VWTHD]] and [[sequentially compact|0FRMJH3CY7]], but it is not [[compact|0TVJZYB6SH]] and not [[metrizable|091GJ3FYD7]].

## Remarks

For each countable ordinal $\beta \ge 1$, the initial segment of $L$ below $(\beta, 0)$ is a countable stack of half-open intervals, and it is homeomorphic to $[0, 1)$.
So every point of $L$ other than $(0, 0)$ has a neighbourhood homeomorphic to an open interval of $\R$.
A sequence $(\alpha_n, t_n)$ in $L$ has a countable supremum $\gamma$ of the $\alpha_n$, because a countable union of countable sets is countable.
So the sequence lies in the set of points up to $(\gamma + 1, 0)$, which is homeomorphic to $[0, 1]$, and it has a convergent subsequence.
The open sets $\set{p \in L : p < (\alpha, 0)}$ for $\alpha < \omega_1$ cover $L$, but no finitely many of them do, because $\omega_1$ has no largest element.
A sequentially compact metrizable space is compact, so $L$ is not metrizable.
For the same reason the long line is a connected Hausdorff space, locally homeomorphic to $\R$, that is not second-countable and not metrizable.
So being Hausdorff and locally Euclidean does not make a space a topological manifold in the usual sense, which also asks for second countability.

## Explanations

### L1 human

The long line is made by laying uncountably many copies of the interval $[0, 1)$ end to end.
Near each of its points it looks just like the real line.
But it is so long that no sequence can climb to its end.
It shows that "looks like a line near every point" does not give a space that can be measured by a distance.
