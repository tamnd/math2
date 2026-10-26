---
tag: ~6bd4a5ff
kind: definition
name: Integral domain
msc: [13G05]
defines: ~840272cc
uses: [~79bc52c4, ~2f380c28]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_domain
    locator: Definition
---

## Definition

An integral domain is a [[commutative ring|~79bc52c4]] $R$ with these two properties.

1. $1 \neq 0$ in $R$.
2. For all $a, b \in R$, if $a b = 0$, then $a = 0$ or $b = 0$.

Equivalently, $R$ is a nonzero commutative ring in which $0$ is the only [[zero divisor|~2f380c28]].

## Remarks

The integers $\mathbb{Z}$ and every [[field|~92ce2090]] are integral domains.
The ring $\mathbb{Z}/6\mathbb{Z}$ is not an integral domain, because $2 \cdot 3 = 0$.
In an integral domain, [[cancellation|~1ab69f02]] holds for nonzero factors.
Some authors, and Mathlib, also use the word domain for a noncommutative ring with property 2.

## Explanations

### L1 human

An integral domain is a ring that behaves like the integers for products.
If a product is zero, then one of the factors is zero.
This is what you use when you solve $(x - 2)(x - 3) = 0$.
