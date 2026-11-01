---
tag: H5145REFMW
kind: concept
name: Frobenius element
msc: [11R32, 11R37]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_endomorphism
---

## Summary

Let $L/K$ be a Galois extension of number fields, and let $\mathfrak{P}$ be a prime of $L$ that is unramified over $K$.
Let $q$ be the size of the residue field of the prime of $K$ below $\mathfrak{P}$.
The Frobenius element of $\mathfrak{P}$ is the unique element of the [[decomposition group|7X92G8CQ33]] that acts on the residue field as the [[Frobenius automorphism|0CGCPX8Z70]] $x \mapsto x^q$.
Its conjugacy class depends only on the prime of $K$ below $\mathfrak{P}$.
Frobenius elements encode how primes split, and they are the input of the Artin map in [[class field theory|BEKCEYHCHX]] and of [[Chebotarev's density theorem|X8VKW5Y1CZ]].

## Explanations

### L1 human

Over a finite field with $q$ elements, raising to the power $q$ is a symmetry of every larger finite field.
A Frobenius element lifts this symmetry from the residue field to the number field itself.
In $\Q(i)/\Q$, the Frobenius element at an odd prime $p$ is the identity if $p \equiv 1 \pmod 4$ and complex conjugation if $p \equiv 3 \pmod 4$.
This matches whether $p$ splits or stays prime in $\Z[i]$.
So one group element records the splitting of a prime.
