---
tag: EBPYD73Y8S
kind: proof
name: Proof that if 2^n − 1 is prime then n is prime
msc: [11A41]
proves: 07MMWAXMYD
uses: [0SN0MAEKYX, 0GJBJ19NXR, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/Mersenne_prime
    locator: Theorems about Mersenne numbers
---

## Proof

We prove the contrapositive: if $n$ is not prime, then $2^n - 1$ is not prime.

1. Let $n$ be a natural number that is not a [[prime number|0SN0MAEKYX]]. Then $n = 0$, $n = 1$, or $n$ is composite.
2. If $n = 0$, then $2^n - 1 = 0$. If $n = 1$, then $2^n - 1 = 1$. Neither $0$ nor $1$ is prime.
3. Let $n$ be composite. Then $n = ab$ with integers $a$ and $b$ such that $1 < a < n$ and $1 < b < n$.
4. For every number $x$ and every integer $b \ge 1$, $(x - 1)(1 + x + x^2 + \dots + x^{b-1}) = x^b - 1$. Indeed, the product telescopes: $\sum_{i=0}^{b-1} (x^{i+1} - x^i) = x^b - 1$.
5. Put $x = 2^a$. Then $2^n - 1 = x^b - 1 = (2^a - 1) \cdot s$, where $s = 1 + 2^a + \dots + 2^{a(b-1)}$ is a positive integer.
6. So $2^a - 1$ [[divides|096PW7Q014]] $2^n - 1$.
7. Since $1 < a < n$, we have $1 < 2^2 - 1 \le 2^a - 1 < 2^n - 1$.
8. So $2^n - 1$ has a divisor strictly between $1$ and itself, and it is not prime.
9. By contraposition, if $2^n - 1$ is prime, then $n$ is prime.

## Idea

If $n = ab$, then $2^n - 1 = (2^a)^b - 1$, and $y - 1$ always divides $y^b - 1$. This gives a proper factor $2^a - 1$ of $2^n - 1$. So a composite exponent never gives a prime.
