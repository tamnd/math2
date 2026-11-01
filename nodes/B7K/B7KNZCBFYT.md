---
tag: B7KNZCBFYT
kind: concept
name: Splitting of prime ideals
msc: [11R04, 11R32]
sources:
  - url: https://en.wikipedia.org/wiki/Splitting_of_prime_ideals_in_Galois_extensions
---

## Summary

Let $L/K$ be an extension of [[algebraic number fields|MWBDFS2KJ5]].
A [[prime ideal|00MHHZ9SNE]] of the ring of integers of $K$ need not stay prime in the ring of integers of $L$.
It factors into a product of prime ideals of $L$.
The factorisation is described by the number of factors, their exponents, called [[ramification|H5RC67SD24]] indices, and their residue degrees.
These numbers satisfy the [[fundamental identity|REJDQ6BTQV]] $\sum_i e_i f_i = [L : K]$.
In a Galois extension the splitting is controlled by the [[decomposition group|7X92G8CQ33]] and the [[Frobenius element|H5145REFMW]].
This leads to [[Chebotarev's density theorem|X8VKW5Y1CZ]] and to [[class field theory|BEKCEYHCHX]].

## Explanations

### L1 human

A prime number can stop being prime in a bigger ring of integers.
In the Gaussian integers $\Z[i]$, the prime $5$ splits as $(2 + i)(2 - i)$, the prime $3$ stays prime, and $2 = -i(1 + i)^2$ becomes a square up to a unit.
These three behaviours are called splitting, staying inert and ramifying.
Which one happens depends on $p$ modulo $4$: odd primes $p \equiv 1 \pmod 4$ split and primes $p \equiv 3 \pmod 4$ stay inert.
Such rules for general extensions are a central topic of algebraic number theory.
