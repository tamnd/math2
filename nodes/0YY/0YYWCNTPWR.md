---
tag: 0YYWCNTPWR
kind: definition
name: Quotient group
msc: [20A05]
defines: 0KYX2N69J0
uses: [0W77CVBCHQ, 05FD317V2W, 01E7SWYJX3]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_group
    locator: Definition
---

## Definition

Let $G$ be a [[group|G5S1M9]] and let $N$ be a [[normal subgroup|0CB0DX5BVV]] of $G$.
The quotient group $G/N$ is the set of [[left cosets|03DEH43F4H]] $\{gN : g \in G\}$ with the operation $(aN)(bN) = (ab)N$.

## Remarks

The operation is well defined because $N$ is normal: if $aN = a'N$ and $bN = b'N$, then $abN = a'b'N$.
The identity of $G/N$ is $N = eN$, and the inverse of $aN$ is $a^{-1}N$.
When $G$ is finite, $|G/N| = [G : N] = |G| / |N|$.
The map $g \mapsto gN$ is a surjective homomorphism from $G$ to $G/N$ with kernel $N$.

## Explanations

### L1 human

A quotient group treats all elements of one coset as one element.
For example, the integers modulo $2$ come from the integers when you treat all even numbers as one element and all odd numbers as another.
The normality of $N$ makes sure that the product of two cosets does not depend on the chosen elements.
