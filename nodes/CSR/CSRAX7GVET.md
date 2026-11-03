---
tag: CSRAX7GVET
kind: definition
name: Digital signature
msc: [94A62, 94A60]
defines: 9TE67WRBWK
uses: [K99S0Q0814, Z5CCVBME2V, 01E9MNJYEX, 0HM584C465]
sources:
  - url: https://en.wikipedia.org/wiki/Digital_signature
---

## Definition

Let $\lambda$ be the security parameter.
A *digital signature scheme* is a triple $(\mathsf{Gen}, \mathsf{Sign}, \mathsf{Verify})$ of [[probabilistic algorithms|K99S0Q0814]] that run in time polynomial in $\lambda$, such that:

1. $\mathsf{Gen}(1^\lambda)$ outputs a pair $(pk, sk)$ of a public key and a private key.
2. $\mathsf{Sign}(sk, m)$ outputs a signature $\sigma$ for a message $m \in \set{0,1}^*$.
3. $\mathsf{Verify}(pk, m, \sigma)$ outputs $1$ (accept) or $0$ (reject).
4. Correctness: $\mathsf{Verify}(pk, m, \mathsf{Sign}(sk, m)) = 1$ for every key pair output by $\mathsf{Gen}$ and every message $m$.

The scheme is *existentially unforgeable under chosen-message attack* if the following holds.
Let $A$ be a probabilistic polynomial-time adversary that gets $pk$ and [[oracle|Z5CCVBME2V]] access to $\mathsf{Sign}(sk, \cdot)$.
A forgery is a pair $(m^*, \sigma^*)$ with $\mathsf{Verify}(pk, m^*, \sigma^*) = 1$ such that $m^*$ was never queried to the oracle.
The probability that $A$ outputs a forgery must be negligible in $\lambda$.
A function $\nu$ is negligible if $\nu(\lambda) < 1/p(\lambda)$ for every polynomial $p$ and all large $\lambda$.

## Remarks

Example: textbook [[RSA|0HM584C465]] signatures satisfy clauses 1 to 4.
Here $pk = (N, e)$ and $sk = d$ with $ed \equiv 1$ modulo the order of $(\Z/N\Z)^\times$, $\mathsf{Sign}(sk, m) = m^d \bmod N$, and $\mathsf{Verify}$ accepts when $\sigma^e \equiv m \pmod N$.
Messages are taken in $\set{0, \dots, N - 1}$.
Correctness holds, since $(m^d)^e \equiv m \pmod N$ for every such $m$ when $N$ is a product of two distinct primes.

Non-example: the same scheme is not existentially unforgeable.
An adversary picks any $\sigma$, sets $m^* = \sigma^e \bmod N$, and outputs $(m^*, \sigma)$ without any query; it is accepted with probability $1$.
Hashing the message before signing, as in full-domain-hash RSA, removes this attack.
