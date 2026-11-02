---
tag: A5GDAAYNM0
kind: definition
name: Shock wave
msc: [35L67, 35L65, 76L05]
defines: JSDMGGTG7G
uses: [8RA7AMWSAF, SJZX81A783]
sources:
  - url: https://en.wikipedia.org/wiki/Shock_wave
---

## Definition

Let $F \colon \R \to \R$ be a $C^1$ function and consider the scalar [[conservation law|8RA7AMWSAF]] $u_t + F(u)_x = 0$ on $\R \times (0, \infty)$.
Let $u$ be a [[weak solution|SJZX81A783]] and let $C = \set{(s(t), t) : t \in I}$ be a curve, with $I$ an open interval and $s \colon I \to \R$ of class $C^1$.
Suppose that $u$ is $C^1$ on each side of $C$ near $C$.
Let $u_l(t)$ and $u_r(t)$ be its one-sided limits from the left and from the right of $(s(t), t)$.
The curve $C$ is a *shock* of $u$ if $u_l(t) \ne u_r(t)$ for all $t \in I$, so that $u$ jumps across $C$.
The shock is *admissible*, or satisfies the *Lax entropy condition*, if
$$F'(u_l(t)) > s'(t) > F'(u_r(t)) \qquad \text{for all } t \in I.$$

## Remarks

Because $u$ is a weak solution, the shock speed is forced by the [[Rankine–Hugoniot condition|S4XMYJ3V42]] $s'(t) = \dfrac{F(u_l) - F(u_r)}{u_l - u_r}$.
The entropy condition says that characteristics run into the shock from both sides, so the shock does not create information.
For uniformly convex $F$ it is equivalent to $u_l > u_r$.
For systems a shock of the $k$-th family is admissible when $\lambda_k(u_l) > s' > \lambda_k(u_r)$ together with conditions on the other eigenvalues.

Example: for [[Burgers' equation|NEGHXN8RE1]], $F(u) = u^2/2$, the function $u = 1$ for $x < t/2$ and $u = 0$ for $x > t/2$ has an admissible shock along $s(t) = t/2$.
Check: the speed $1/2 = (\tfrac12 - 0)/(1 - 0)$ satisfies the Rankine–Hugoniot condition, which makes $u$ a weak solution, and $F'(1) = 1 > \tfrac12 > 0 = F'(0)$.

Non-example: the function $u = 0$ for $x < t/2$ and $u = 1$ for $x > t/2$ is also a weak solution of Burgers' equation with a jump along $s(t) = t/2$.
It fails the entropy condition, since $F'(0) = 0 < \tfrac12$.
The admissible solution with these initial values is a [[rarefaction wave|MFN4Q5SH8H]] instead.
