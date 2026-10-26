---
tag: 07CZYE06ZJ
kind: statement
role: corollary
name: Lcm of coprime integers
msc: [11A05]
uses: [0GFKP8F8AG, 09S5SN35DJ, 0TDY6JZHKS]
sources:
  - url: https://en.wikipedia.org/wiki/Least_common_multiple
    locator: Using the greatest common divisor
---

## Statement

Let $a$ and $b$ be natural numbers that are [[coprime|0GFKP8F8AG]].
Then $\operatorname{lcm}(a, b) = a b$.

## Remarks

This follows from the [[product of the gcd and the lcm|0TDY6JZHKS]], because $\gcd(a, b) = 1$.
The converse is also true when $a$ and $b$ are positive: if $\operatorname{lcm}(a, b) = a b$, then $a$ and $b$ are coprime.
For example, $\operatorname{lcm}(8, 15) = 120$.

## Explanations

### L1 human

When $a$ and $b$ have no common factor, a multiple of both must contain all the factors of $a$ and all the factors of $b$.
No factor can serve both numbers at the same time, so the smallest common multiple is $a b$.
