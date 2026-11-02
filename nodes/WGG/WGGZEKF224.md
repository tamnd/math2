---
tag: WGGZEKF224
kind: problem
name: Lüroth problem
msc: ["14E08", 14M20]
uses: [HV6YBS0YDH, YF1SE8WJK3, XV4K9GREJ9, 0PF6TM8TWT]
about: [YF1SE8WJK3, XV4K9GREJ9]
sources:
  - url: https://en.wikipedia.org/wiki/L%C3%BCroth%27s_theorem
history:
  posed_by: "Jacob Lüroth"
  first_stated: "1876"
---

## Problem

Let $k$ be an [[algebraically closed field|0PF6TM8TWT]] and let $X$ be an integral [[algebraic variety|HV6YBS0YDH]] over $k$.
Suppose that $X$ is [[unirational|YF1SE8WJK3]].
Must $X$ be [[rational|XV4K9GREJ9]]?

## Remarks

In dimension $1$ the answer is yes, by [[Lüroth's theorem|AVCZ6HVBA7]].
In dimension $2$ over an algebraically closed field of characteristic $0$, the answer is yes, by [[Castelnuovo's rationality criterion|QXHMMQX1D7]].
In dimension $2$ over an algebraically closed field of characteristic $p > 0$, the answer is no: Zariski found unirational surfaces that are not rational.
In dimension $3$ over $\C$, the answer is no.
Clemens and Griffiths showed that a smooth cubic threefold in $\mathbb{P}^4$ is unirational but not rational.
Iskovskikh and Manin showed that a smooth quartic threefold in $\mathbb{P}^4$ is not rational, and some of these are unirational.
Artin and Mumford gave another unirational threefold that is not rational, detected by torsion in its third cohomology group.
So the problem is settled in the negative in general, and the open questions now concern specific families of varieties.

## Explanations

### L1 human

A variety is rational when it can be parametrised one-to-one, up to small exceptions, by free parameters.
It is unirational when it can be covered by such a parametrisation, perhaps many-to-one.
The problem asks whether a many-to-one parametrisation can always be improved to a one-to-one parametrisation.
For curves and for complex surfaces it can.
For complex threefolds it cannot, and the cubic threefold is the standard example.
