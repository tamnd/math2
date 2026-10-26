---
tag: 0KF3J2KAER
kind: statement
role: theorem
name: Classification of Pythagorean triples
aliases: [euclid-formula]
msc: [11D09]
uses: [01G1WY1GVX, 0GFKP8F8AG]
sources:
  - url: https://en.wikipedia.org/wiki/Pythagorean_triple
    locator: Generating a triple
---

## Statement

Let $m$ and $n$ be [[coprime|0GFKP8F8AG]] positive integers with $m > n$ and $m - n$ odd.
Then $(m^2 - n^2, \, 2mn, \, m^2 + n^2)$ is a primitive [[Pythagorean triple|01G1WY1GVX]].
Conversely, each primitive Pythagorean triple $(a, b, c)$ with $b$ even arises in this way from exactly one such pair $(m, n)$.
Each Pythagorean triple is $(ka, kb, kc)$ for a positive integer $k$ and a primitive triple $(a, b, c)$, up to the order of the first two entries.

## Remarks

The formula is called Euclid's formula.
For example, $(m, n) = (2, 1)$ gives $(3, 4, 5)$, and $(m, n) = (3, 2)$ gives $(5, 12, 13)$.
One proof writes $b^2 = (c - a)(c + a)$ and uses unique factorization. Another uses the rational points on the unit circle.

## Explanations

### L1 human

Euclid's formula produces every right triangle with whole-number sides, from two numbers $m$ and $n$.
The identity $(m^2 - n^2)^2 + (2mn)^2 = (m^2 + n^2)^2$ shows that the formula always works.
