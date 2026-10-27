---
tag: 0VFW4Y69BT
kind: definition
name: Quotient ring
msc: [16D25]
defines: 0076HWHGHQ
uses: [0DDA6CY7GJ, 0894J980RK]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_ring
    locator: Formal quotient ring construction
inventory: [20Z8XK08MP]
---

## Definition

Let $R$ be a [[ring|0894J980RK]] and let $I$ be a [[two-sided ideal|0DDA6CY7GJ]] of $R$.
For $a \in R$, the coset of $a$ is $a + I = \{a + x : x \in I\}$.
The quotient ring $R/I$ is the set of the cosets of $I$, with these operations:
$$(a + I) + (b + I) = (a + b) + I, \qquad (a + I)(b + I) = a b + I.$$
These operations do not depend on the choice of $a$ and $b$ in their cosets.
With them, $R/I$ is a ring with zero $0 + I = I$ and identity $1 + I$.

## Remarks

Two elements $a, b \in R$ have the same coset if and only if $a - b \in I$.
The map $\pi \colon R \to R/I$, $\pi(a) = a + I$, is a surjective [[ring homomorphism|0GGE0Z0JQ1]] with [[kernel|0AAHE7GEW6]] $I$.
For $n \ge 1$, the quotient $\mathbb{Z}/n\mathbb{Z}$ is the ring of integers modulo $n$.
The quotient $R/R$ is the [[zero ring|008TBCYDPX]].

## Explanations

### L1 human

To make the quotient ring, you declare all the elements of $I$ to be zero.
Two elements become equal when their difference is in $I$.
For $\mathbb{Z}/5\mathbb{Z}$, the numbers $2$ and $7$ become the same element.
