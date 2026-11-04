---
tag: KFVHE9P0K9
kind: proof
name: Proof that if 2^n + 1 is prime then n is a power of 2
msc: [11A41]
proves: 0VN4H8M12X
uses: [0SN0MAEKYX, 0R03B54V4Z, 084HH1NDCB, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat_number
---

## Proof

We prove the contrapositive: if $n$ is not a power of $2$, then $2^n + 1$ is not prime.

1. Let $n$ be a positive integer. By the [[fundamental theorem of arithmetic|084HH1NDCB]], $n = 2^k m$ with $k \ge 0$ and $m$ a positive odd integer.
2. Assume $n$ is not a power of $2$. Then $m \ne 1$, so $m \ge 3$.
3. Put $x = 2^{2^k}$, so that $2^n + 1 = x^m + 1$ and $x \ge 2$.
4. For odd $m$, $(x + 1)(x^{m-1} - x^{m-2} + \dots - x + 1) = x^m + 1$. Indeed, the product is $\sum_{i=0}^{m-1} (-1)^{m-1-i} (x^{i+1} + x^i)$, which telescopes to $x^m + (-1)^{m-1} = x^m + 1$.
5. So $x + 1$ [[divides|096PW7Q014]] $2^n + 1$.
6. We have $x + 1 \ge 3 > 1$. Also $x + 1 < x^m + 1$, because $x \ge 2$ and $m \ge 3$ give $x^m > x$.
7. So $2^n + 1$ has a divisor strictly between $1$ and itself, and it is not a [[prime number|0SN0MAEKYX]].
8. By contraposition, if $2^n + 1$ is prime, then $n = 2^k$ for a natural number $k$.
9. Then $2^n + 1 = 2^{2^k} + 1$, which is the [[Fermat number|0R03B54V4Z]] $F_k$. So every prime of the form $2^n + 1$ with $n \ge 1$ is a Fermat number.

## Idea

An odd factor $m > 1$ of the exponent lets us factor $y^m + 1$ by $y + 1$, because $-1$ is a root of $y^m + 1$ when $m$ is odd. This gives a proper divisor. So only exponents with no odd factor, the powers of $2$, can give primes.
