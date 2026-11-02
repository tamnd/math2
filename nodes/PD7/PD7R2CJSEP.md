---
tag: PD7R2CJSEP
kind: definition
name: Polydisc
msc: [32A10, 32Q02]
defines: DJBWP7D3M8
uses: [BH57D2FBNR, 8G5ABXRK85]
sources:
  - url: https://en.wikipedia.org/wiki/Polydisc
---

## Definition

Let $n \ge 1$, let $a = (a_1, \dots, a_n) \in \C^n$ and let $r = (r_1, \dots, r_n)$ with each $r_j > 0$.
The *open polydisc* with centre $a$ and polyradius $r$ is
$$P(a, r) = \set{z \in \C^n : \abs{z_j - a_j} < r_j \text{ for } j = 1, \dots, n}.$$
The *closed polydisc* $\overline{P}(a, r)$ is defined in the same way with $\le$ in place of $<$.

## Remarks

So $P(a, r) = D(a_1, r_1) \times \cdots \times D(a_n, r_n)$, a product of open discs in $\C$.
The *unit polydisc* is $\Delta^n = P(0, (1, \dots, 1))$, the $n$-fold product of the [[unit disc|8G5ABXRK85]].
Example: $(1/2, i/2) \in \Delta^2$, since both coordinates have modulus $1/2 < 1$.
Non-example: $(0, 1) \notin \Delta^2$, since the second coordinate has modulus $1$, which fails the strict inequality.
The open polydisc is the open ball of radius $1$ about $a$ for the norm $\max_j \abs{z_j - a_j}/r_j$.
For $n = 1$ a polydisc is an ordinary disc.
