---
tag: 07MMWAXMYD
kind: statement
role: proposition
name: If 2^p − 1 is prime then p is prime
msc: [11A41]
uses: [0GJBJ19NXR, 0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Mersenne_prime
    locator: Theorems about Mersenne numbers
---

## Statement

Let $n$ be a natural number.
If $2^n - 1$ is a [[prime number|0SN0MAEKYX]], then $n$ is a prime number.

## Remarks

The proof: if $n = ab$ with $1 < a < n$, then $2^a - 1$ divides $2^n - 1$, because $x - 1$ divides $x^b - 1$ for $x = 2^a$. And $1 < 2^a - 1 < 2^n - 1$.
For example, $2^6 - 1 = 63$ is divisible by $2^2 - 1 = 3$ and by $2^3 - 1 = 7$.
The converse is false: $11$ is prime, but $2^{11} - 1 = 23 \cdot 89$.

## Explanations

### L1 human

To look for primes of the form $2^n - 1$, you only need to try prime exponents $n$.
A factorization of $n$ always gives a factorization of $2^n - 1$.
