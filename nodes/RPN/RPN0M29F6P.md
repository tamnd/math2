---
tag: RPN0M29F6P
kind: proof
name: Proof of the sum of the first n natural numbers by induction
msc: [05A19]
proves: 01QZNHQWYD
uses: [0ASJVEFA9J]
methods: [0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_number
    locator: Formula
---

## Proof

We argue by [[induction|0ASJVEFA9J]] on $n$.
For each natural number $n$, let $T_n = \sum_{k=0}^{n} k$, and let $P(n)$ be the claim $T_n = \frac{n(n+1)}{2}$.
We compute with rational numbers, so division by $2$ is allowed.

1. Base case: $T_0 = 0$, and $\frac{0 \cdot 1}{2} = 0$. So $P(0)$ holds.
2. Induction step: suppose that $P(n)$ holds for some natural number $n$.
3. The sum up to $n + 1$ is the sum up to $n$ plus the last term: $T_{n+1} = T_n + (n + 1)$.
4. By the hypothesis, $T_{n+1} = \frac{n(n+1)}{2} + (n + 1)$.
5. We rewrite: $\frac{n(n+1)}{2} + \frac{2(n+1)}{2} = \frac{(n+1)(n+2)}{2}$, by factoring out $n + 1$.
6. So $T_{n+1} = \frac{(n+1)((n+1)+1)}{2}$, which is $P(n + 1)$.
7. By induction, $P(n)$ holds for every natural number $n$, that is, $0 + 1 + \dots + n = \frac{n(n+1)}{2}$.

## Idea

Going from $n$ to $n + 1$ adds the term $n + 1$ to the sum.
The formula grows by the same amount, because $\frac{(n+1)(n+2)}{2} - \frac{n(n+1)}{2} = n + 1$.
