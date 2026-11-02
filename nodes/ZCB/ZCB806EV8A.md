---
tag: ZCB806EV8A
kind: statement
role: theorem
name: Functional equation of the gamma function
msc: [33B15, 30D30]
uses: [0V3FZMVB4K, 0NSD1TPHR0]
about: [0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Gamma_function
---

## Statement

Let $\Gamma$ be the [[gamma function|0V3FZMVB4K]], extended to a [[meromorphic function|0NSD1TPHR0]] on $\C$ that is holomorphic on $\C \setminus \set{0, -1, -2, \ldots}$.
For every $z \in \C \setminus \set{0, -1, -2, \ldots}$,
$$\Gamma(z + 1) = z \, \Gamma(z).$$

## Remarks

For $\operatorname{Re} z > 0$, integration by parts in $\Gamma(z + 1) = \int_0^\infty t^{z} e^{-t} \, dt$ gives $z \int_0^\infty t^{z-1} e^{-t} \, dt$; the boundary terms vanish.
Both sides are holomorphic on the connected set $\C \setminus \set{0, -1, -2, \ldots}$, so the identity theorem extends the equation from the half-plane to this set.
Conversely the equation is the usual way to build the extension: for $\operatorname{Re} z > -n$ one sets $\Gamma(z) = \Gamma(z + n)/\big(z (z + 1) \cdots (z + n - 1)\big)$.
With $\Gamma(1) = 1$ the equation gives $\Gamma(n + 1) = n!$, see [[the gamma function extends the factorial|0FDCW77H44]].
For example $\Gamma(\tfrac32) = \tfrac12 \Gamma(\tfrac12) = \tfrac{\sqrt{\pi}}{2}$.
In Mathlib the statement is `Complex.Gamma_add_one`.

## Explanations

### L1 human

The gamma function obeys the same rule as the factorial: moving the argument up by one multiplies the value by the old argument.
For whole numbers this is the rule $(n+1)! = (n+1) \cdot n!$.
The rule holds at every complex number where $\Gamma$ is defined.

### L2 human

The functional equation reduces the values of $\Gamma$ anywhere to its values on a strip of width one, such as $1 \le \operatorname{Re} z < 2$.
It also shows where the poles are: dividing by $z$ at $z = 0$ creates a pole, and each further step to the left creates another.
Together with log-convexity it characterizes $\Gamma$ on $(0, \infty)$, by the [[Bohr–Mollerup theorem|QFF87AXWN2]], and together with boundedness on a strip it characterizes $\Gamma$ on the right half-plane, by [[Wielandt's theorem|WCM87QEEZW]].
