---
tag: YBBS082ZY1
kind: definition
name: Kadomtsev–Petviashvili equation
msc: [35Q53, 35Q51]
defines: P93R13XP0P
uses: [GC5BDZ6QBC, KTT75QC72Z, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Kadomtsev–Petviashvili_equation
---

## Definition

Let $\sigma \in \set{1, -1}$.
The *Kadomtsev–Petviashvili equation* is the [[partial differential equation|GC5BDZ6QBC]]
$$\partial_x \big( u_t + 6 u u_x + u_{xxx} \big) + 3 \sigma u_{yy} = 0$$
for an unknown real function $u(x, y, t)$ of $(x, y) \in \R^2$ and $t \in \R$, where subscripts denote [[partial derivatives|09EGC6F8PT]].
The case $\sigma = 1$ is called *KP-II* and the case $\sigma = -1$ is called *KP-I*.

## Remarks

Example: let $v(x, t)$ be a solution of the [[Korteweg–De Vries equation|KTT75QC72Z]] $v_t + 6 v v_x + v_{xxx} = 0$, and put $u(x, y, t) = v(x, t)$.
Then the bracket vanishes and $u_{yy} = 0$, so $u$ solves both KP-I and KP-II.

Non-example: $u(x, y, t) = y^2$ is not a solution, because the first term is $0$ while $3 \sigma u_{yy} = 6 \sigma \ne 0$.

Other normalisations are used, for example $\partial_x(u_t + u u_x + \varepsilon^2 u_{xxx}) + \lambda u_{yy} = 0$ with $\lambda = \pm 1$.
They reduce to the form above by scaling the variables, and the sign of the $u_{yy}$ term relative to the dispersive term decides between KP-I and KP-II.
