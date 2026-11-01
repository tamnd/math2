---
tag: XR0WZJAM0R
kind: statement
role: theorem
name: Finiteness of associated primes
msc: ["13C05", "13E05"]
uses: [0MVH4Y1CRZ, 0XHM30WBVB, 1RJJ33KKSS]
about: [ERFZ6S8X0X]
sources:
  - url: https://en.wikipedia.org/wiki/Associated_prime
---

## Statement

Let $R$ be a commutative [[Noetherian ring|0MVH4Y1CRZ]] and let $M$ be a [[finitely generated|0XHM30WBVB]] $R$-module.
Then the set $\operatorname{Ass}_R(M)$ of [[associated primes|1RJJ33KKSS]] of $M$ is finite.

## Remarks

The proof builds a chain of submodules $0 = M_0 \subsetneq M_1 \subsetneq \cdots \subsetneq M_n = M$ with $M_i / M_{i-1} \cong R/P_i$ for prime ideals $P_i$.
Each step picks an associated prime of $M/M_{i-1}$, which exists when this module is nonzero, and the chain stops because $M$ is a [[Noetherian module|AK1ZRCXR32]].
Then $\operatorname{Ass}_R(M) \subseteq \set{P_1, \dots, P_n}$, because associated primes of an extension lie among those of the two pieces.
For example, $\operatorname{Ass}_\Z(\Z/n\Z)$ is the finite set of ideals $(p)$ for the primes $p$ dividing $n \ge 2$.
Finite generation is needed: the $\Z$-module $\bigoplus_p \Z/p\Z$, over all primes $p$, has every $(p)$ as an associated prime.

## Explanations

### L1 human

A finitely generated module over a Noetherian ring has only finitely many associated primes.
So it is "supported" by finitely many basic primes, like an integer with finitely many prime factors.

### L2 human

Associated primes of a nonzero module also exist, so $\operatorname{Ass}_R(M)$ is finite and nonempty when $M \ne 0$.
With the result that [[zero divisors are the union of associated primes|S37DQGW3TZ]], this lets one use [[prime avoidance|FMP5AWG6PR]] to find non-zero-divisors outside finitely many primes.
This is a key step in building regular sequences and in the theory of depth.
