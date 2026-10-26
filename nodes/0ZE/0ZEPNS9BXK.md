---
tag: 0ZEPNS9BXK
kind: statement
role: corollary
name: g to the order of the group is the identity
aliases: [power-of-the-group-order-is-identity]
msc: [20D60]
uses: [08V7JHS3QZ, 0F5QC101Q7]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange's_theorem_(group_theory)
    locator: Applications
---

## Statement

Let $G$ be a finite [[group|G5S1M9]] with identity element $e$, and let $g \in G$.
Then $g^{|G|} = e$.

## Remarks

The [[order|0WE2NHZJ7B]] of $g$ divides $|G|$ by [[this corollary|08V7JHS3QZ]], and [[a power is $e$ when the order divides the exponent|0F5QC101Q7]].
For the group $(\mathbb{Z}/p\mathbb{Z})^\times$ of order $p - 1$, with $p$ prime, this gives Fermat's little theorem $a^{p-1} \equiv 1 \pmod p$ for $p \nmid a$.
For the group $(\mathbb{Z}/n\mathbb{Z})^\times$ of order $\varphi(n)$, it gives Euler's theorem.

## Explanations

### L1 human

If a group has $n$ elements, then the $n$th power of each element is the identity.
For example, in a group of order $6$, each element $g$ satisfies $g^6 = e$.
This simple fact proves Fermat's little theorem in number theory.
