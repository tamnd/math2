---
tag: EDF0ZJF141
kind: proof
name: Proof of Pascal's rule from the recursive definition
msc: [05A10]
proves: 0YRG241HQQ
uses: [092GEF38YD]
sources:
  - url: https://en.wikipedia.org/wiki/Pascal's_rule
    locator: lead section
---

## Proof

1. Let $n$ and $k$ be natural numbers.
2. The [[binomial coefficient|092GEF38YD]] is defined by the recursion $\binom{n}{0} = 1$, $\binom{0}{k+1} = 0$ and $\binom{n+1}{k+1} = \binom{n}{k} + \binom{n}{k+1}$.
3. The third clause of this definition, applied to $n$ and $k$, is the equation $\binom{n+1}{k+1} = \binom{n}{k} + \binom{n}{k+1}$.

## Idea

In this wiki the binomial coefficients are defined by Pascal's rule itself, so the rule holds by definition.
With other definitions, such as the factorial formula or the count of subsets, it needs a short computation or a counting argument.
