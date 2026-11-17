---
tag: 0JPYSD5E0B
kind: definition
name: Order of an element
msc: [20A05]
topics: [BAZT8JJ70S]
audience: ug1
defines: 0WE2NHZJ7B
uses: [G5S1M9, 00DRK90Z6K]
formal:
  - system: lean4
    library: mathlib
    decl: orderOf
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Order_(group_theory)
    locator: lead section
  - book: isbn:9781305657960
    locator: Chapter 3
inventory: [2WR87G5VKX]
---

## Definition

Let $G$ be a [[group|G5S1M9]] with identity element $e$, and let $g \in G$.
For an integer $n$, let $g^n$ be the $n$th power of $g$, as in the [[laws of exponents|00DRK90Z6K]].
When there is a positive integer $n$ with $g^n = e$, the order of $g$ is the smallest such $n$.
When there is no such $n$, the element $g$ has infinite order.

## Notation

The order of $g$ is written $\ord(g)$, $|g|$ or $o(g)$.
In additive notation the condition $g^n = e$ becomes $n g = 0$.
In Mathlib, `orderOf g` is a natural number, and it is $0$ when $g$ has infinite order.
For an element of finite order the two definitions give the same number.

## Remarks

The smallest such $n$ exists when the set of such $n$ is not empty, by the [[well-ordering principle|01BX15HSRR]].
The identity element is the only element of order $1$.
In $(\mathbb{Z}, +)$, each nonzero element has infinite order.
In the multiplicative group $\{1, i, -1, -i\}$, the element $-1$ has order $2$ and the element $i$ has order $4$.
In a finite group, each element has finite order, and the order of $g$ equals the [[order|0B85S2V2DR]] of the subgroup that $g$ generates.
The concept page [[order of an element|0WE2NHZJ7B]] gives the examples, the non-examples and the first properties.

## Explanations

### L1 human

Take an element and multiply it by itself again and again.
The order is the number of steps that are necessary to come back to the identity for the first time.
For a rotation by $90$ degrees, $4$ steps are necessary, so its order is $4$.

### L2 human

To find the order of $g$, we compute $g, g^2, g^3, \ldots$ and stop at the first power that is $e$.
For example, take $-1$ in the multiplicative group $\{1, i, -1, -i\}$.

1. $(-1)^1 = -1 \neq 1$.
2. $(-1)^2 = 1$.

So the order of $-1$ is $2$.
A trap is to stop at a power that is $e$ but is not the first one: $(-1)^4 = 1$ too, but the order is $2$, not $4$.
