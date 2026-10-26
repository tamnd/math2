---
tag: 0SPBEDVNW1
kind: statement
role: proposition
name: Existence of a prime divisor
msc: [11A41]
uses: [0SN0MAEKYX, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_number
    locator: Unique factorization
---

## Statement

Let $n$ be a natural number with $n \ge 2$.
Then there is a [[prime number|0SN0MAEKYX]] $p$ such that $p \mid n$.

## Remarks

One proof takes the smallest divisor $d$ of $n$ with $d > 1$. Each divisor $e$ of $d$ with $e > 1$ also divides $n$, so $e = d$. Thus $d$ is prime.
This smallest divisor is the [[smallest prime factor|0S2SYHTWPY]] of $n$.
The result is also true for $n = 0$, since each prime divides $0$. It is false for $n = 1$.

## Explanations

### L1 human

Split $n$ into two smaller factors when you can, and repeat with one of the factors.
The numbers get smaller each time, so the process stops at a number that you cannot split. This number is a prime, and it divides $n$.
For example, $60 = 2 \cdot 30$, so $2$ is a prime divisor of $60$.
