---
tag: PV82BVXE1A
kind: conjecture
name: Lindelöf hypothesis
msc: [11M06, 11M26]
uses: [1XWBY4N0VT, 0TGV80E6A4, VCGF9YR36X]
about: [1XWBY4N0VT]
sources:
  - url: https://en.wikipedia.org/wiki/Lindelöf_hypothesis
same_as:
  wikidata: Q911528
  wikipedia: Lindelöf hypothesis
history:
  posed_by: "Ernst Lindelöf"
  first_stated: "1908"
---

## Statement

Let $\zeta$ be the [[Riemann zeta function|1XWBY4N0VT]].
For every $\varepsilon > 0$ there is a constant $C_\varepsilon$ such that
$$\abs{\zeta(\tfrac12 + it)} \le C_\varepsilon \abs{t}^{\varepsilon}$$
for all real $t$ with $\abs{t} \ge 1$.

## Remarks

The conjecture is open.
The [[Riemann hypothesis|VCGF9YR36X]] implies it.
The functional equation and the Phragmén–Lindelöf principle give the convexity bound $\zeta(\tfrac12 + it) = O(\abs{t}^{1/4 + \varepsilon})$.
Every improvement of the exponent $1/4$ is called a subconvexity bound; Hardy and Littlewood obtained $1/6 + \varepsilon$ with Weyl's method, and Bourgain obtained $13/84 + \varepsilon$.
An equivalent form: for every integer $k \ge 1$ and every $\varepsilon > 0$,
$$\frac{1}{T} \int_{0}^{T} \abs{\zeta(\tfrac12 + it)}^{2k} \, dt = O(T^{\varepsilon}).$$

## Explanations

### L1 human

On the critical line $\operatorname{Re} s = 1/2$, the zeta function oscillates and its size grows slowly with the height $t$.
The Lindelöf hypothesis says that it grows more slowly than any power of $t$, however small.
It is weaker than the Riemann hypothesis but still out of reach.
It would imply strong bounds on the moments of zeta and on the number of zeros off the critical line.
