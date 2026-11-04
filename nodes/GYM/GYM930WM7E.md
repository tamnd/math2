---
tag: GYM930WM7E
kind: proof
name: Proof of the alternating sum of binomial coefficients from the binomial theorem
msc: [05A10]
proves: 0PQQGFAWSH
uses: [0EHWPWGHB2, 092GEF38YD]
sources:
  - url: https://proofwiki.org/wiki/Alternating_Sum_and_Difference_of_Binomial_Coefficients_for_Given_n
---

## Proof

1. Let $n \ge 1$. The integers $\Z$ form a commutative ring. Apply the [[binomial theorem|0EHWPWGHB2]] in $\Z$ with $x = -1$ and $y = 1$.
2. It gives $(-1 + 1)^n = \sum_{k=0}^{n} \binom{n}{k} (-1)^k 1^{n-k} = \sum_{k=0}^{n} (-1)^k \binom{n}{k}$.
3. The left side is $0^n$. Since $n \ge 1$, we have $0^n = 0 \cdot 0^{n-1} = 0$.
4. Hence $\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0$.

## Idea

Putting $x = -1$ and $y = 1$ in the binomial theorem gives each coefficient the sign $(-1)^k$.
The left side becomes $0^n$, which is $0$ as soon as $n \ge 1$.
