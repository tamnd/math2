---
tag: 09S3PFBEPM
kind: definition
name: Integral domain
msc: [13G05]
defines: 0QVD7WBFGN
uses: [0GYGHKX834, 0K26YKNBSA]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_domain
    locator: Definition
inventory: [JZCW37FSDA]
---

## Definition

An integral domain is a [[commutative ring|0GYGHKX834]] $R$ with these two properties.

1. $1 \neq 0$ in $R$.
2. For all $a, b \in R$, if $a b = 0$, then $a = 0$ or $b = 0$.

Equivalently, $R$ is a nonzero commutative ring in which $0$ is the only [[zero divisor|0K26YKNBSA]].

## Remarks

The integers $\mathbb{Z}$ and every [[field|0QA8CHH8MG]] are integral domains.
The ring $\mathbb{Z}/6\mathbb{Z}$ is not an integral domain, because $2 \cdot 3 = 0$.
In an integral domain, [[cancellation|0GJM24EXP9]] holds for nonzero factors.
Some authors, and Mathlib, also use the word domain for a noncommutative ring with property 2.

## Explanations

### L1 human

An integral domain is a ring that behaves like the integers for products.
If a product is zero, then one of the factors is zero.
This is what you use when you solve $(x - 2)(x - 3) = 0$.
