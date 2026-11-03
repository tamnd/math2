---
tag: Q7N6JJANT4
kind: definition
name: One-way function
msc: [94A60, 68Q17, 68P25]
defines: RA37YDW2TY
uses: [0XHDTE5YMZ, K99S0Q0814, GVT2NKN37K]
sources:
  - url: https://en.wikipedia.org/wiki/One-way_function
    locator: Definition
---

## Definition

A [[function|0XHDTE5YMZ]] $f \colon \set{0,1}^* \to \set{0,1}^*$ is *one-way* if it has these two properties.

1. Easy to compute: some deterministic algorithm computes $f(x)$ in time polynomial in $\abs{x}$.
2. Hard to invert: let $A$ be a [[probabilistic|K99S0Q0814]] polynomial-time algorithm and let $p$ be a polynomial.
Then for all sufficiently large $n$,
$$\Pr\big[f(A(1^n, f(x))) = f(x)\big] < \frac{1}{p(n)}.$$

The probability is over $x$ uniform in $\set{0,1}^n$ and over the random bits of $A$.
The input $1^n$ gives $A$ the length $n$ in unary.

## Remarks

The inverter succeeds if it finds any preimage of $f(x)$, not necessarily $x$ itself.

Example of a candidate: let $f(p, q) = pq$ on pairs of $n$-bit numbers.
Restricted to pairs of primes, this is believed to be one-way.
On arbitrary pairs of numbers the situation differs, since a random product often has small factors that are easy to find.

Non-example: the identity function satisfies clause 1 but fails clause 2, since $A(1^n, y) = y$ always inverts it.

If one-way functions exist, then $\mathrm{P} \ne \mathrm{NP}$.
Indeed, if $\mathrm{P} = \mathrm{NP}$, a preimage of $y$ can be found bit by bit in polynomial time with an NP oracle.
