---
tag: B8AKSVBE5Z
kind: concept
name: Chebyshev functions
msc: [11N05, 11A41]
sources:
  - url: https://en.wikipedia.org/wiki/Chebyshev_function
same_as:
  wikidata: Q1046711
  wikipedia: Chebyshev function
---

## Summary

The Chebyshev functions $\vartheta(x)$ and $\psi(x)$ count the [[prime numbers|01826KMG2H]] up to $x$ with the weight $\log p$.
The first sums $\log p$ over primes $p \le x$, and the second also counts the prime powers $p^k \le x$.
They are easier to handle analytically than the [[prime-counting function|0RQSNVTFVZ]] $\pi(x)$, and the [[prime number theorem|0EHBY5Y84N]] is equivalent to $\psi(x) \sim x$.

## Explanations

### L1 human

Instead of counting each prime as $1$, give the prime $p$ the weight $\log p$.
Then large primes count more, in the right amount to make the total grow like $x$ itself.
For $x = 10$, the primes $2, 3, 5, 7$ give $\vartheta(10) = \log 210 \approx 5.35$.
The function $\psi$ also counts $4, 8, 9$, and $\psi(10) = \log 2520 \approx 7.83$, the logarithm of the least common multiple of $1, \dots, 10$.
