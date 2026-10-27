---
tag: 00GXTQMY8Z
kind: definition
name: Modular multiplicative inverse
aliases: [modular-inverse, inverse-modulo-n]
msc: [11A07]
defines: 0CEC45PRJN
uses: [0TPW25CBN6]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
    locator: lead section
inventory: [DSSNDJQX1B]
---

## Definition

Let $n$ be a positive integer and let $a$ be an integer.
A modular multiplicative inverse of $a$ modulo $n$ is an integer $x$ such that $a x \equiv 1 \pmod n$.

## Remarks

An inverse of $a$ modulo $n$ exists if and only if $\gcd(a, n) = 1$. See [[existence of inverses modulo n|0M67FWZWPQ]].
If $x$ is an inverse of $a$, then the inverses of $a$ are exactly the integers $y \equiv x \pmod n$. So the inverse is unique as a residue class, and we write it as $a^{-1} \bmod n$.
In the ring of [[integers modulo n|01N3AYAA6N]], the class $\overline{x}$ is the inverse of $\overline{a}$.
For example, $3^{-1} \equiv 5 \pmod 7$, because $3 \cdot 5 = 15 \equiv 1 \pmod 7$.

## Explanations

### L1 human

Modulo $n$, the inverse of $a$ plays the part of the fraction $1/a$.
To solve $3 x \equiv 4 \pmod 7$, multiply both sides by $5$, the inverse of $3$. You get $x \equiv 20 \equiv 6 \pmod 7$.
