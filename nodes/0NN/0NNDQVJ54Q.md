---
tag: 0NNDQVJ54Q
kind: statement
role: theorem
name: Closed formula for Catalan numbers
msc: [05A15]
uses: [092GEF38YD, 01WHD9T0V6, 092DRBFKMG]
sources:
  - url: https://en.wikipedia.org/wiki/Catalan_number
    locator: Proof of the formula
---

## Statement

Let $n$ be a natural number, and let $C_n$ be the $n$-th [[Catalan number|092DRBFKMG]].
Then
$$C_n = \frac{1}{n + 1} \binom{2n}{n} = \frac{(2n)!}{(n + 1)!\, n!}.$$

## Remarks

The fraction is an integer, because $C_n = \binom{2n}{n} - \binom{2n}{n+1}$.
The numerator $\binom{2n}{n}$ is the [[central binomial coefficient|01WHD9T0V6]].
Example: $C_4 = \frac{1}{5} \binom{8}{4} = \frac{70}{5} = 14$.

## Explanations

### L1 human

Among the $\binom{2n}{n}$ grid paths from $(0, 0)$ to $(n, n)$, exactly one in $n + 1$ stays below the diagonal.
So the Catalan number is the central binomial coefficient divided by $n + 1$.
