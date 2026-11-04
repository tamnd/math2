---
tag: GS2SF16HQY
kind: proof
name: Proof of the sum of binomial coefficients from the binomial theorem
msc: [05A10]
proves: 0KAMF19NV8
uses: [0EHWPWGHB2, 092GEF38YD]
sources:
  - url: https://proofwiki.org/wiki/Sum_of_Binomial_Coefficients_over_Lower_Index
---

## Proof

1. The integers $\Z$ form a commutative ring. Apply the [[binomial theorem|0EHWPWGHB2]] in $\Z$ with $x = y = 1$.
2. It gives $(1 + 1)^n = \sum_{k=0}^{n} \binom{n}{k} 1^k 1^{n-k}$.
3. Every power of $1$ equals $1$, so the right side is $\sum_{k=0}^{n} \binom{n}{k}$.
4. The left side is $2^n$. Hence $\sum_{k=0}^{n} \binom{n}{k} = 2^n$.

## Idea

The binomial theorem with both variables equal to $1$ removes the monomials and leaves only the coefficients.
Their sum is then $(1 + 1)^n = 2^n$.
