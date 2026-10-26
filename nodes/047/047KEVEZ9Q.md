---
tag: 047KEVEZ9Q
kind: statement
role: theorem
name: Every real number has a decimal expansion
msc: [11A63]
uses: [06XY4X9430, 0YVRNEDSVG, 0AXWET80YW]
sources:
  - url: https://en.wikipedia.org/wiki/Decimal_representation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Decimal_representation
    locator: Finite decimal approximations
---

## Statement

Let $x$ be a real number with $x \ge 0$.
Then $x$ has a [[decimal expansion|06XY4X9430]]: there are a natural number $a_0$ and digits $d_k \in \{0, \dots, 9\}$ for $k \ge 1$ with $x = a_0 + \sum_{k=1}^{\infty} d_k 10^{-k}$.

## Remarks

One choice is $a_0 = \lfloor x \rfloor$ and $d_k = \lfloor 10^k x \rfloor - 10 \lfloor 10^{k-1} x \rfloor$, with the [[floor function|0YVRNEDSVG]].
With this choice, the truncation $a_0.d_1 \dots d_k$ satisfies $0 \le x - a_0.d_1 \dots d_k < 10^{-k}$.
The expansion is unique, except for the numbers with a finite expansion. They also have a second expansion that ends in infinitely many $9$.

## Explanations

### L1 human

You can find the digits of a number one at a time.
At each step, you choose the largest digit that keeps the truncated decimal at or below the number.
The truncations then get closer to the number by a factor of ten at each step.
