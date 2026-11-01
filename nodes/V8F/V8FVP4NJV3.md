---
tag: V8FVP4NJV3
kind: definition
name: Perfect closure
msc: [12F15]
defines: PWNZQVQ175
uses: [0P7CH1CND5, 0MCXX29HWY, MY8BG4EE0F, 7FR2PZ141W]
sources:
  - url: https://en.wikipedia.org/wiki/Perfect_field
---

## Definition

Let $K$ be a field of [[characteristic|0P7CH1CND5]] $p > 0$ and let $\overline{K}$ be an [[algebraic closure|0MCXX29HWY]] of $K$.
The *perfect closure* of $K$ is the set
$$K^{p^{-\infty}} = \set{\alpha \in \overline{K} : \alpha^{p^n} \in K \text{ for some integer } n \ge 0}.$$
For a field $K$ of characteristic $0$, the perfect closure of $K$ is $K$.

## Remarks

The set $K^{p^{-\infty}}$ is a subfield of $\overline{K}$, because $(\alpha + \beta)^{p^n} = \alpha^{p^n} + \beta^{p^n}$ in characteristic $p$.
It is a [[perfect field|MY8BG4EE0F]], it is [[purely inseparable|7FR2PZ141W]] over $K$, and it is contained in every perfect subfield of $\overline{K}$ that contains $K$.
It is unique up to a unique isomorphism over $K$.

Example: for $K = \F_p(t)$, the perfect closure is $\bigcup_{n \ge 0} \F_p(t^{1/p^n})$.
Check: each $\F_p(t^{1/p^n})$ is purely inseparable over $K$, and the union is perfect because every element of $\F_p(t^{1/p^n})$ has a $p$-th root in $\F_p(t^{1/p^{n+1}})$.

Non-example: for $p$ odd, the field $\overline{K}$ is perfect and contains $K$, but it is not the perfect closure.
It contains $\sqrt{t}$, and no power $\sqrt{t}^{\,p^n}$ lies in $K$, since $p^n$ is odd.
