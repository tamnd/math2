---
tag: BJMEXPKRYM
kind: definition
name: Perfect ring
msc: [16L30]
defines: 49Y9Q949PK
uses: [0894J980RK, XA0DCNH7WY, YH75M7XAM1]
sources:
  - url: https://en.wikipedia.org/wiki/Perfect_ring
---

## Definition

Let $R$ be a [[ring|0894J980RK]] with identity and $J = J(R)$ its [[Jacobson radical|XA0DCNH7WY]].
A subset $S \subseteq R$ is *left T-nilpotent* if for every sequence $a_1, a_2, a_3, \ldots$ of elements of $S$ there is $n \ge 1$ with $a_1 a_2 \cdots a_n = 0$.
$R$ is *left perfect* if the following hold.

1. $R$ is [[semilocal|YH75M7XAM1]], that is, $R/J$ is a semisimple ring.
2. $J$ is left T-nilpotent.

*Right perfect* rings are defined with *right T-nilpotent*, which asks for $a_n \cdots a_2 a_1 = 0$ instead.

## Remarks

Example: a left Artinian ring is left and right perfect: $R/J$ is semisimple, and $J^n = 0$ for some $n$, so every product of $n$ elements of $J$ is $0$.
Non-example: $\Z_{(p)}$ is semilocal, but $J = p\Z_{(p)}$ is not left T-nilpotent, since the constant sequence $p, p, p, \ldots$ has all products $p^n \ne 0$.
By [[Bass's theorem P|D2M8BSW720]], $R$ is left perfect if and only if every left $R$-module has a projective cover.
This is also equivalent to the descending chain condition on principal right ideals.
Many authors take one of these equivalent conditions as the definition.
