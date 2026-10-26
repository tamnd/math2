---
tag: 0R7JS3DP3W
kind: statement
role: theorem
name: Symmetry of binomial coefficients
msc: [05A10]
uses: [092GEF38YD]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_coefficient
    locator: Factorial formula
---

## Statement

Let $n$ and $k$ be natural numbers with $k \le n$.
Then
$$\binom{n}{k} = \binom{n}{n - k}.$$

## Remarks

For a set $X$ with $n$ elements, the map $S \mapsto X \setminus S$ is a bijection from the $k$-subsets of $X$ to the $(n-k)$-subsets. This is a [[bijective proof|0GV2573FP4]] of the identity.
The identity makes each row of [[Pascal's triangle|05DME4TZ3K]] read the same from left to right and from right to left.

## Explanations

### L1 human

To choose $k$ people for a team is the same as to choose the $n - k$ people who stay out.
For example, $\binom{5}{2} = \binom{5}{3} = 10$.
