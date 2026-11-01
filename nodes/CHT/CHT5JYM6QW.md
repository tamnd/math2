---
tag: CHT5JYM6QW
kind: definition
name: p-adic number
msc: [12J25, 11S99]
defines: BT6T702C28
uses: [01826KMG2H, WGN82TCEF2, 06RW4RKWH7, 0NCJ5WXN6Z, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/P-adic_number
---

## Definition

Let $p$ be a [[prime number|01826KMG2H]] and let $\abs{\cdot}_p$ be the [[p-adic absolute value|WGN82TCEF2]] on the [[rational numbers|0NCJ5WXN6Z]] $\Q$.
The field $\Q_p$ of *$p$-adic numbers* is the [[completion|06RW4RKWH7]] of $\Q$ for the metric $d(x, y) = \abs{x - y}_p$.
A $p$-adic number is an element of $\Q_p$.
The field operations and the absolute value $\abs{\cdot}_p$ extend from $\Q$ to $\Q_p$ by continuity.

## Remarks

Every $x \in \Q_p$ with $x \neq 0$ has a unique expansion $x = \sum_{n \ge m} a_n p^n$ with $m \in \Z$, digits $a_n \in \set{0, 1, \ldots, p - 1}$ and $a_m \neq 0$.
Then $\abs{x}_p = p^{-m}$.
Example: $-1 = \sum_{n \ge 0} (p - 1) p^n$ in $\Q_p$.
Check: the partial sum up to $p^{N-1}$ is $p^N - 1$, and $\abs{(p^N - 1) - (-1)}_p = p^{-N}$ tends to $0$.
Non-example: the formal sum $\sum_{n \ge 0} p^{-n}$ is not a $p$-adic number, because its terms have $\abs{p^{-n}}_p = p^n$ and do not tend to $0$.
The elements with $\abs{x}_p \le 1$ are the [[p-adic integers|V6TJAFZ4MD]] $\Z_p$.
By [[Ostrowski's theorem|GCQ23XT6VD]], the completions of $\Q$ are $\R$ and the fields $\Q_p$.
