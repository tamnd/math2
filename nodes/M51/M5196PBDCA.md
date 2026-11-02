---
tag: M5196PBDCA
kind: definition
name: j-invariant of an elliptic curve
msc: [14H52, 11G05]
defines: 9538W1K1EX
uses: [Z3C8B6QTS6, 427N6S6QQW, 0PF6TM8TWT]
sources:
  - url: https://en.wikipedia.org/wiki/J-invariant
---

## Definition

Let $K$ be a field, and let $E$ be an elliptic curve over $K$.
Let $y^2 + a_1 xy + a_3 y = x^3 + a_2 x^2 + a_4 x + a_6$ be a [[Weierstrass equation|Z3C8B6QTS6]] of $E$, with quantities $b_2, b_4$ and discriminant $\Delta \ne 0$.
Put $c_4 = b_2^2 - 24 b_4$.
The *$j$-invariant* of $E$ is
$$j(E) = \frac{c_4^3}{\Delta} \in K.$$

## Remarks

If the characteristic of $K$ is not $2$ or $3$ and $E$ is $y^2 = x^3 + Ax + B$, then $c_4 = -48A$ and $\Delta = -16(4A^3 + 27B^2)$, so
$$j(E) = 1728 \, \frac{4A^3}{4A^3 + 27B^2}.$$
The value does not depend on the chosen Weierstrass equation of $E$.
Over an [[algebraically closed field|0PF6TM8TWT]], two [[elliptic curves|427N6S6QQW]] are isomorphic if and only if they have the same $j$-invariant.
Moreover, every element of the field is the $j$-invariant of some elliptic curve.
Example: $y^2 = x^3 - x$ has $A = -1$ and $B = 0$, so $j = 1728 \cdot (-4)/(-4) = 1728$.
Non-example: $y^2 = x^3$ has $\Delta = 0$, so it is not an elliptic curve and $c_4^3/\Delta$ is not defined.
Over a field that is not algebraically closed, curves with the same $j$-invariant can fail to be isomorphic: $y^2 = x^3 - x$ and $y^2 = x^3 + x$ both have $j = 1728$ but are not isomorphic over $\Q$.
