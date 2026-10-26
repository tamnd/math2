---
tag: 0FJTGZA4GS
kind: statement
role: theorem
name: Bertrand's postulate
aliases: [bertrand-chebyshev-theorem, chebyshev-theorem]
msc: [11N05]
uses: [0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Bertrand%27s_postulate
    locator: lead section
same_as:
  wikidata: Q632546
  wikipedia: Bertrand's postulate
---

## Statement

Let $n$ be a positive integer.
Then there is a [[prime number|0SN0MAEKYX]] $p$ such that $n < p \le 2 n$.

## Remarks

For example, for $n = 10$ the primes $11, 13, 17, 19$ are in the range $10 < p \le 20$.
An equivalent form: if $p_k$ is the $k$-th prime, then $p_{k+1} < 2 p_k$ for each $k \ge 1$.
The [[prime number theorem|0EHBY5Y84N]] gives a stronger result for large $n$, but Bertrand's postulate holds for each $n \ge 1$.

## History

Joseph Bertrand stated the result as a conjecture in 1845. Chebyshev proved it in 1852.

## Explanations

### L1 human

Between each number and its double, there is always at least one prime.
So the gap after a prime $p$ to the next prime is always smaller than $p$.
