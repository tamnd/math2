---
tag: ~8ebefd7b
kind: definition
name: Coprime ideals
msc: [13A15]
defines: ~6b772458
uses: [~87bc362c]
sources:
  - url: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    locator: Generalization to arbitrary rings
---

## Definition

Let $R$ be a [[commutative ring|~79bc52c4]] and let $I$ and $J$ be ideals of $R$.
The ideals $I$ and $J$ are coprime if $I + J = R$, where $I + J$ is the [[sum of the ideals|~87bc362c]].
Equivalently, there are $a \in I$ and $b \in J$ with $a + b = 1$.

## Remarks

In $\mathbb{Z}$, $m\mathbb{Z} + n\mathbb{Z} = \gcd(m, n)\mathbb{Z}$. So $m\mathbb{Z}$ and $n\mathbb{Z}$ are coprime if and only if $\gcd(m, n) = 1$.
If $I$ and $J$ are coprime, then $I \cap J = I J$.
Two distinct [[maximal ideals|~3f9701c1]] are always coprime.

## Explanations

### L1 human

For integers, $3$ and $5$ are coprime, and $2 \cdot 3 - 1 \cdot 5 = 1$.
So $1$ is a multiple of $3$ plus a multiple of $5$.
Coprime ideals generalize this: $1$ is an element of $I$ plus an element of $J$.
