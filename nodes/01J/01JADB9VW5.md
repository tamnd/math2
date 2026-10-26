---
tag: 01JADB9VW5
kind: statement
role: theorem
name: Vandermonde's identity
msc: [05A19]
uses: [092GEF38YD]
sources:
  - url: https://en.wikipedia.org/wiki/Vandermonde's_identity
    locator: lead section
same_as:
  wikidata: Q3147827
  wikipedia: "Vandermonde's identity"
---

## Statement

Let $m$, $n$ and $r$ be natural numbers.
Then
$$\binom{m + n}{r} = \sum_{k=0}^{r} \binom{m}{k} \binom{n}{r - k}.$$

## Remarks

Combinatorial proof: take a set of $m$ men and $n$ women. An $r$-element committee has some number $k$ of men and $r - k$ women.
With $m = n = r$, and the [[symmetry of binomial coefficients|0R7JS3DP3W]], it gives $\binom{2n}{n} = \sum_{k=0}^{n} \binom{n}{k}^2$.

## Explanations

### L1 human

To choose $r$ people from two groups together, choose $k$ from the first group and $r - k$ from the second, for each possible $k$.
Then add the counts for all values of $k$.
