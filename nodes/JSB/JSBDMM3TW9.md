---
tag: JSBDMM3TW9
kind: proof
name: Proof of the existence of prime factorization
msc: [11A51]
proves: 020K0X7HVR
uses: [0KMVFSHFGZ, 0SPBEDVNW1, 0SN0MAEKYX, 0AEKDFCYFA]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
    locator: Proof, Existence
---

## Proof

We argue by [[strong induction|0KMVFSHFGZ]] on $n$.

1. For a natural number $n$, let $P(n)$ say: if $n \ge 1$, then $n = p_1 p_2 \cdots p_k$ for some [[prime numbers|0SN0MAEKYX]] $p_1, \dots, p_k$ with $k \ge 0$.
2. Let $n$ be a natural number, and assume that $P(m)$ holds for every natural number $m < n$. We prove $P(n)$.
3. If $n = 0$, then $P(n)$ holds, because its hypothesis $n \ge 1$ is false.
4. If $n = 1$, take $k = 0$. The empty product is $1$, so $n$ is a product of primes.
5. Let $n \ge 2$. By the [[existence of a prime divisor|0SPBEDVNW1]], there is a prime $p$ with $p \mid n$. Write $n = p m$ with an integer $m$.
6. Since $n > 0$ and $p > 0$, $m \ge 1$. Since $p \ge 2$, $n = p m \ge 2m > m$. So $1 \le m < n$.
7. By the induction hypothesis $P(m)$, $m = q_1 \cdots q_j$ for some primes $q_1, \dots, q_j$ with $j \ge 0$.
8. Then $n = p q_1 \cdots q_j$ is a product of $j + 1$ primes, so $P(n)$ holds.
9. By strong induction, $P(n)$ holds for all $n$. So each positive integer is a product of primes.
10. Listing these primes in increasing order gives $p_1 \le \dots \le p_k$ with the same product. This is a [[prime factorization|0AEKDFCYFA]] of $n$.

## Idea

Split off one prime factor of $n$. What is left is a smaller positive integer, which is a product of primes by induction. Putting the prime back gives a product of primes for $n$.
