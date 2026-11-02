---
tag: VDWKE1KK4H
kind: definition
name: Method of characteristics
msc: [35F20, 35A30, 35L02]
defines: 7XAPBCJK3B
uses: [7X9N9H3RK6, 0NT64JV96A, 0FXDW992DS, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_characteristics
---

## Definition

Let $U \subseteq \R^n$ be open, and let $a = (a_1, \dots, a_n) \colon U \times \R \to \R^n$ and $c \colon U \times \R \to \R$ be $C^1$ functions.
Consider the first-order [[quasilinear equation|7X9N9H3RK6]]
$$\sum_{i=1}^n a_i(x, u)\, \partial_i u = c(x, u)$$
for an unknown $C^1$ function $u$ on $U$, where $\partial_i u$ is the [[partial derivative|09EGC6F8PT]] in $x_i$.
Its *characteristic equations* are the [[ordinary differential equations|0NT64JV96A]]
$$\frac{dx}{ds} = a(x, z), \qquad \frac{dz}{ds} = c(x, z)$$
for a curve $s \mapsto (x(s), z(s))$ in $U \times \R$; the curves $s \mapsto x(s)$ are the *characteristics*.
The *method of characteristics* solves the equation with data $u = g$ on a hypersurface $\Gamma \subseteq U$ as follows.

1. For each $y \in \Gamma$, solve the characteristic equations with [[initial values|0FXDW992DS]] $x(0) = y$ and $z(0) = g(y)$.
2. Invert the map $(y, s) \mapsto x(y, s)$ near $\Gamma$, which is possible when $\Gamma$ is non-characteristic, that is, $a(y, g(y))$ is not tangent to $\Gamma$.
3. Set $u(x(y, s)) = z(y, s)$.

## Remarks

The key fact is that if $u$ is a $C^1$ solution and $x(s)$ solves $x' = a(x, u(x))$, then $z(s) = u(x(s))$ satisfies $z' = \sum_i a_i\, \partial_i u = c(x, z)$.
So the graph of a solution is a union of solutions of the characteristic system.
For a fully nonlinear equation $F(Du, u, x) = 0$ the method uses the larger system $\dot x = D_p F$, $\dot z = D_p F \cdot p$, $\dot p = -D_x F - D_z F\, p$, where $p$ stands for $Du$.

Example: for $u_t + u\, u_x = 0$ in the variables $(x, t)$ with $u(x, 0) = g(x)$, the characteristic equations are $\dot t = 1$, $\dot x = z$, $\dot z = 0$.
So $z$ is constant and the characteristics are the lines $x = y + g(y) t$, which gives the implicit solution $u = g(x - ut)$.
Check: differentiating $u = g(x - ut)$ gives $u_t = -g'\,(u + t u_t)$ and $u_x = g'\,(1 - t u_x)$, so $u_t = -u g'/(1 + t g')$ and $u_x = g'/(1 + t g')$, and $u_t + u u_x = 0$.

Non-example: data given on a characteristic curve.
Take $\partial_1 u = 0$ on $\R^2$ with data $u(x_1, 0) = g(x_1)$ on $\Gamma = \set{x_2 = 0}$.
Here $a = (1, 0)$ is tangent to $\Gamma$, so step 2 fails.
Indeed no solution exists unless $g$ is constant, and if $g$ is constant there are infinitely many, such as $u = g + h(x_2)$ with $h(0) = 0$.
