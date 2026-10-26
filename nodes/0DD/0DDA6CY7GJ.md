---
tag: 0DDA6CY7GJ
kind: definition
name: Two-sided ideal
msc: [16D25]
defines: 0CD87SFM2N
uses: [0MYSA6MYNA]
sources:
  - url: https://en.wikipedia.org/wiki/Ideal_(ring_theory)
    locator: Definitions
---

## Definition

Let $R$ be a [[ring|0894J980RK]].
A two-sided ideal of $R$ is a subset $I \subseteq R$ with these properties.

1. $I$ is a subgroup of the additive group $(R, +)$.
2. For all $r \in R$ and $a \in I$, $r a \in I$ and $a r \in I$.

So a two-sided ideal is a [[left ideal|0MYSA6MYNA]] that is also a right ideal.

## Remarks

In a [[commutative ring|0GYGHKX834]], left ideals, right ideals and two-sided ideals are the same.
The [[kernel|0AAHE7GEW6]] of every [[ring homomorphism|0GGE0Z0JQ1]] is a two-sided ideal.
The [[quotient ring|0VFW4Y69BT]] $R/I$ exists exactly when $I$ is a two-sided ideal.
In the ring of $n \times n$ matrices over a field, the only two-sided ideals are $\{0\}$ and the whole ring.

## Explanations

### L1 human

In a noncommutative ring, $r a$ and $a r$ can be different.
A two-sided ideal must absorb products from both sides.
This is the condition that makes the quotient ring work.
