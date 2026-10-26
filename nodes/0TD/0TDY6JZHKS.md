---
tag: 0TDY6JZHKS
kind: statement
role: proposition
name: Product of the gcd and the lcm
msc: [11A05]
uses: [02WF878BH1, 09S5SN35DJ]
sources:
  - url: https://en.wikipedia.org/wiki/Least_common_multiple
    locator: Using the greatest common divisor
---

## Statement

Let $a$ and $b$ be natural numbers.
Then $\gcd(a, b) \cdot \operatorname{lcm}(a, b) = a b$, where $\gcd$ is the [[greatest common divisor|02WF878BH1]] and $\operatorname{lcm}$ is the [[least common multiple|09S5SN35DJ]].

## Remarks

For integers $a$ and $b$ of any sign, the same argument gives $\gcd(a, b) \cdot \operatorname{lcm}(a, b) = |a b|$.
Thus $\operatorname{lcm}(a, b) = a b / \gcd(a, b)$ when $a$ and $b$ are not both $0$. This is the usual way to compute the lcm, with the [[Euclidean algorithm|0TRNT4X7J0]].
For example, $\gcd(4, 6) = 2$, $\operatorname{lcm}(4, 6) = 12$ and $2 \cdot 12 = 24 = 4 \cdot 6$.

## Explanations

### L1 human

Think of the prime factors of $a$ and $b$. The gcd takes, for each prime, the smaller of the two exponents, and the lcm takes the larger one.
The smaller exponent plus the larger exponent is the sum of the two exponents.
So the product of the gcd and the lcm has the same prime factors as $a b$.
