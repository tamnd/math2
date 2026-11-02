---
tag: WBS4NM1TFC
kind: statement
role: theorem
name: Gamma function has no zeros
msc: [33B15, 30D30]
uses: [0V3FZMVB4K, 0NSD1TPHR0]
about: [0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Gamma_function
---

## Statement

Let $\Gamma$ be the [[gamma function|0V3FZMVB4K]], extended to a [[meromorphic function|0NSD1TPHR0]] on $\C$.
For every $z \in \C \setminus \set{0, -1, -2, \ldots}$, $\Gamma(z) \ne 0$.

## Remarks

For $z \notin \Z$, the [[reflection formula|WF7KQAQTS2]] gives $\Gamma(z)\Gamma(1 - z) = \pi/\sin(\pi z)$, and the right side is finite and nonzero, so $\Gamma(z) \ne 0$.
For a positive integer $n$, $\Gamma(n) = (n-1)! \ne 0$.
The points $0, -1, -2, \ldots$ are excluded because $\Gamma$ has poles there, not values.
A consequence is that the [[reciprocal gamma function|PY6K9AWR33]] $1/\Gamma$ is entire, with zeros exactly at $0, -1, -2, \ldots$.
In Mathlib the statement is `Complex.Gamma_ne_zero`.

## Explanations

### L1 human

The gamma function never takes the value zero.
It can become very large near its poles and very small for large negative arguments, but it never vanishes.

### L2 human

Because $\Gamma$ has no zeros, its logarithmic derivative, the [[digamma function|HWRRXB0YXS]] $\psi = \Gamma'/\Gamma$, is meromorphic with poles only at $0, -1, -2, \ldots$.
It also allows a holomorphic logarithm of $\Gamma$ on the slit plane, the [[log-gamma function|JT95B44G4G]].
