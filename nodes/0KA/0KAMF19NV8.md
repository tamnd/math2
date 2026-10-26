---
tag: 0KAMF19NV8
kind: statement
role: theorem
name: Sum of binomial coefficients
msc: [05A10]
uses: [092GEF38YD]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_coefficient
    locator: Sums of the binomial coefficients
---

## Statement

Let $n$ be a natural number.
Then
$$\sum_{k=0}^{n} \binom{n}{k} = 2^n.$$

## Remarks

For $n = 4$: $1 + 4 + 6 + 4 + 1 = 16$.
The identity is the [[binomial theorem|0EHWPWGHB2]] with $x = y = 1$.
Combinatorially, both sides count the subsets of an $n$-element set. The [[number of subsets of a finite set|0C5RDJE73X]] is $2^n$, and $\binom{n}{k}$ of them have size $k$.

## Explanations

### L1 human

The numbers in row $n$ of [[Pascal's triangle|05DME4TZ3K]] add up to $2^n$.
This is because each subset of an $n$-element set has some size $k$ from $0$ to $n$, and there are $2^n$ subsets in total.
