---
tag: GBN9F8FAQ3
kind: definition
name: p-adic integer
msc: [12J25, 11S99]
defines: V6TJAFZ4MD
uses: [BT6T702C28, WGN82TCEF2, MGM3CNJW9V]
sources:
  - url: https://en.wikipedia.org/wiki/P-adic_number
---

## Definition

Let $p$ be a prime number and let $\Q_p$ be the field of [[p-adic numbers|BT6T702C28]], with the [[p-adic absolute value|WGN82TCEF2]] $\abs{\cdot}_p$.
A *$p$-adic integer* is an element $x \in \Q_p$ with $\abs{x}_p \le 1$.
The set of $p$-adic integers is denoted $\Z_p$.

## Remarks

By the strong triangle inequality, $\Z_p$ is a subring of $\Q_p$.
Its units are the $x$ with $\abs{x}_p = 1$, and its only nonzero prime ideal is $p \Z_p$.
Equivalently, $\Z_p$ is the set of sums $\sum_{n \ge 0} a_n p^n$ with digits $a_n \in \set{0, \ldots, p - 1}$.
Equivalently, $\Z_p$ is the inverse limit of the rings $\Z / p^n \Z$ under reduction maps.
Example: $1/2 \in \Z_3$, because $3$ does not divide $2$, so $\abs{1/2}_3 = 1$.
Non-example: $1/3 \notin \Z_3$, because $\abs{1/3}_3 = 3 > 1$.
A rational number lies in $\Z_p$ exactly when its reduced denominator is not divisible by $p$.
