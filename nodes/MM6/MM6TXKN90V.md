---
tag: MM6TXKN90V
kind: definition
name: Rarefaction wave
msc: [35L65, 35L67, 76L05]
defines: MFN4Q5SH8H
uses: [8RA7AMWSAF, SJZX81A783]
sources:
  - url: https://en.wikipedia.org/wiki/Rarefaction
---

## Definition

Let $F \colon \R \to \R$ be a $C^2$ function with $F'' > 0$, and consider the scalar [[conservation law|8RA7AMWSAF]] $u_t + F(u)_x = 0$ on $\R \times (0, \infty)$.
Let $G$ be the inverse function of the strictly increasing function $F'$.
Let $u_l < u_r$ be two real numbers.
The *centered rarefaction wave* from $u_l$ to $u_r$ is the function
$$u(x, t) = \begin{cases} u_l & \text{if } x < F'(u_l)\, t, \\ G(x/t) & \text{if } F'(u_l)\, t \le x \le F'(u_r)\, t, \\ u_r & \text{if } x > F'(u_r)\, t. \end{cases}$$

## Remarks

The function is continuous, since $G(F'(u_l)) = u_l$ and $G(F'(u_r)) = u_r$.
Inside the fan, $F'(u) = x/t$, so $u_t = -\tfrac{x}{t^2} G'(x/t)$ and $u_x = \tfrac1t G'(x/t)$.
Hence $u_t + F'(u)\, u_x = 0$ there, and $u$ is a [[weak solution|SJZX81A783]] with the jump initial values $u_l$ for $x < 0$ and $u_r$ for $x > 0$.
It depends only on $x/t$, so it is self-similar.

Example: for [[Burgers' equation|NEGHXN8RE1]], $F(u) = u^2/2$, so $F'(u) = u$ and $G$ is the identity.
The rarefaction wave from $0$ to $1$ is $u = 0$ for $x < 0$, $u = x/t$ for $0 \le x \le t$, and $u = 1$ for $x > t$.
Check: $u_t + u u_x = -x/t^2 + (x/t)(1/t) = 0$ inside the fan.

Non-example: if $u_l > u_r$, then $F'(u_l) t > F'(u_r) t$ and the middle interval is empty.
The formula then gives no fan, and the admissible solution is a [[shock wave|JSDMGGTG7G]] instead.

## Explanations

### L1 human

A rarefaction wave is a fan of straight lines that spreads a jump into a smooth ramp.
Along each line through the origin with slope $x/t = c$, the solution takes the value whose characteristic speed is $c$.
So the solution moves continuously from the left state to the right state.
