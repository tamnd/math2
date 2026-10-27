---
tag: 0SBRX5CZ5R
kind: definition
name: Multiplicative order
aliases: [order-modulo-n]
msc: [11A07]
defines: 02RRHJ7R98
uses: [0TPW25CBN6, 0GFKP8F8AG, 0VC4DVE7DQ]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplicative_order
    locator: lead section
inventory: [3XXXW0DHF3]
---

## Definition

Let $n$ be a positive integer and let $a$ be an integer [[coprime|0GFKP8F8AG]] to $n$.
The multiplicative order of $a$ modulo $n$ is the smallest positive integer $k$ such that $a^k \equiv 1 \pmod n$.
The notation for it is $\operatorname{ord}_n(a)$.

## Remarks

The order exists, because $a^{\varphi(n)} \equiv 1 \pmod n$ by [[Euler's theorem|0VC4DVE7DQ]].
For each integer $m \ge 0$, $a^m \equiv 1 \pmod n$ if and only if $\operatorname{ord}_n(a) \mid m$. In particular, $\operatorname{ord}_n(a) \mid \varphi(n)$.
The order of $a$ modulo $n$ is the order of $\overline{a}$ in the group $(\mathbb{Z}/n\mathbb{Z})^\times$.
For example, $\operatorname{ord}_7(2) = 3$, because $2^1 = 2$, $2^2 = 4$ and $2^3 = 8 \equiv 1 \pmod 7$.

## Explanations

### L1 human

Compute the powers $a, a^2, a^3, \dots$ modulo $n$, until you reach $1$. The number of steps is the order.
Modulo $10$, the powers of $3$ are $3, 9, 7, 1$, so the order of $3$ modulo $10$ is $4$.
