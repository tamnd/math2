---
tag: S37DQGW3TZ
kind: statement
role: theorem
name: Zero divisors are the union of associated primes
msc: ["13C05", "13E05"]
uses: [0MVH4Y1CRZ, 09VDS2W1E8, 1RJJ33KKSS, 0K26YKNBSA, HB4XDKJTW8]
about: [ERFZ6S8X0X, 0NNRDW10RZ]
sources:
  - url: https://en.wikipedia.org/wiki/Associated_prime
---

## Statement

Let $R$ be a commutative [[Noetherian ring|0MVH4Y1CRZ]] and let $M$ be an $R$-[[module|09VDS2W1E8]].
An element $r \in R$ is a zero divisor on $M$ if $rm = 0$ for some nonzero $m \in M$.
Then the set of zero divisors on $M$ is the union of the [[associated primes|1RJJ33KKSS]] of $M$.

## Remarks

If $P = \operatorname{Ann}(m)$ is associated, then each $r \in P$ kills $m \ne 0$, so $r$ is a zero divisor.
Conversely, if $rm = 0$ with $m \ne 0$, the set of [[annihilators|HB4XDKJTW8]] of nonzero elements that contain $\operatorname{Ann}(m)$ has a maximal member, since $R$ is Noetherian.
A maximal annihilator $\operatorname{Ann}(m')$ is prime: if $ab \in \operatorname{Ann}(m')$ and $b m' \ne 0$, then $\operatorname{Ann}(b m') \supseteq \operatorname{Ann}(m') + (a)$, so $a \in \operatorname{Ann}(m')$.
For example, an integer $r$ is a zero divisor on $\Z/12\Z$ if and only if $\gcd(r, 12) > 1$, that is, $r \in (2) \cup (3)$.
Taking $M = R$, the set of [[zero divisors|0K26YKNBSA]] of $R$, together with $0$, is a finite union of prime ideals.

## Explanations

### L1 human

The elements of the ring that kill some nonzero element of the module are exactly the elements of the associated primes.
So the zero divisors, which form a messy set in general, are a union of a few prime ideals.

### L2 human

Combine it with [[finiteness of associated primes|XR0WZJAM0R]] and [[prime avoidance|FMP5AWG6PR]].
This shows: if an ideal $I$ consists of zero divisors on a finitely generated module $M$, then $I$ kills a nonzero element of $M$.
This is the basic step in the theory of regular sequences and depth.
It is also used to show that $R$ has a non-zero-divisor in an ideal not contained in any associated prime of $R$.
