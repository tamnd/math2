---
tag: BB4FJ1FFGM
kind: conjecture
name: Artin's conjecture on primitive roots
msc: [11A07, 11N36]
uses: [0F33KX9Q6F, 01826KMG2H, 02RRHJ7R98]
about: [0F33KX9Q6F]
sources:
  - url: https://en.wikipedia.org/wiki/Artin%27s_conjecture_on_primitive_roots
same_as:
  wikidata: Q2319635
  wikipedia: Artin's conjecture on primitive roots
history:
  posed_by: "Emil Artin"
  first_stated: "1927"
---

## Statement

Let $a$ be an integer that is not a perfect square and is not $-1$.
Then there are infinitely many [[prime numbers|01826KMG2H]] $p$ such that $a$ is a [[primitive root modulo|0F33KX9Q6F]] $p$.

## Remarks

The conjecture is open for every single value of $a$.
The full conjecture also predicts a positive density for this set of primes; for many $a$ the predicted density is Artin's constant, about $0.3739558$.
Christopher Hooley proved the conjecture in 1967 under the assumption of the [[generalized Riemann hypothesis|DNKA4WBKDS]].
Roger Heath-Brown proved in 1986 that at most two primes $a$ fail the conjecture; so at least one of $2$, $3$, $5$ is a primitive root modulo infinitely many primes.
The two hypotheses are needed: if $a = b^2$ is a square and $p \nmid a$, then $a^{(p-1)/2} \equiv b^{p-1} \equiv 1 \pmod p$, so $a$ is never a primitive root modulo an odd prime $p$.
For $a = -1$, the [[multiplicative order|02RRHJ7R98]] of $-1$ is at most $2$, so it is a primitive root only modulo $2$ and $3$.
For example, $2$ is a primitive root modulo $3$, $5$, $11$, $13$, $19$ and $29$.

## Explanations

### L1 human

A primitive root modulo $p$ is a number whose powers run through all nonzero remainders modulo $p$.
Artin guessed that a fixed number such as $2$ is a primitive root for infinitely many primes, unless there is an obvious reason against it.
Squares are such an obvious reason, and so is $-1$.
The guess is still unproved, even for $a = 2$.
