---
tag: 0FCCTFA275
kind: definition
name: Exponent of a group
msc: [20F50]
defines: 0ZDW0H0VX4
uses: [0JPYSD5E0B]
sources:
  - url: https://en.wikipedia.org/wiki/Torsion_group
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n
    locator: Structure
---

## Definition

Let $G$ be a [[group|G5S1M9]].
The exponent of $G$ is the least positive integer $n$ such that $g^n = e$ for each $g \in G$.
If no such integer exists, then $G$ has infinite exponent.

## Remarks

When the exponent is finite, it is the least common multiple of the [[orders of the elements|0WE2NHZJ7B]] of $G$.
The exponent of a finite group divides the order of the group, by [[Lagrange's theorem|3C53TD]].
The exponent of the cyclic group of order $n$ is $n$, and the exponent of the [[Klein four-group|0PMRQJVTME]] is $2$.
The exponent of $(\mathbb{Z}/n\mathbb{Z})^\times$ is the Carmichael function $\lambda(n)$.

## Explanations

### L1 human

The exponent is the smallest power that sends every element to the identity.
It is a common multiple of all the element orders.
A finite group always has a finite exponent, and the exponent divides the order.
