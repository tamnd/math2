---
tag: 85G9HBA7ND
kind: proof
name: Proof of Euclid's lemma
msc: [11A05]
proves: 051VYKA1EX
uses: [0SN0MAEKYX, 096PW7Q014, 02WF878BH1, 0GFKP8F8AG, 03BAREW1Z5]
sources:
  - url: https://en.wikipedia.org/wiki/Euclid%27s_lemma
    locator: Proofs
---

## Proof

We deduce the lemma from the generalized Euclid's lemma.

1. Let $p$ be a [[prime number|0SN0MAEKYX]] and let $a$, $b$ be integers with $p \mid ab$. If $p \mid a$, we are done. So assume $p \nmid a$.
2. Let $g = \gcd(p, a)$ be the [[greatest common divisor|02WF878BH1]]. It is defined as the largest common divisor, because $p \neq 0$.
3. The number $1$ is a common divisor of $p$ and $a$, so $g \ge 1$.
4. The number $g$ is a positive [[divisor|096PW7Q014]] of $p$. Since $p$ is prime, $g = 1$ or $g = p$.
5. If $g = p$, then $p \mid a$, which is false. So $g = 1$, and $p$ and $a$ are [[coprime|0GFKP8F8AG]].
6. By the [[generalized Euclid's lemma|03BAREW1Z5]], $p \mid ab$ and $\gcd(p, a) = 1$ give $p \mid b$.
7. So $p \mid a$ or $p \mid b$.

## Idea

A prime has only two positive divisors, so a prime that does not divide $a$ has nothing in common with $a$. Then the coprime case of the lemma forces $p$ to divide $b$.
