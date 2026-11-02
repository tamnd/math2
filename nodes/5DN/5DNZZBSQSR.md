---
tag: 5DNZZBSQSR
kind: definition
name: Brown–McCoy radical
msc: [16N80]
defines: EWWP84BGSC
uses: [0894J980RK, 0DDA6CY7GJ]
sources:
  - url: https://en.wikipedia.org/wiki/Radical_of_a_ring
---

## Definition

Let $R$ be a [[ring|0894J980RK]] with identity.
A *maximal ideal* of $R$ is a [[two-sided ideal|0DDA6CY7GJ]] $M \ne R$ such that no two-sided ideal $I$ satisfies $M \subsetneq I \subsetneq R$.
The *Brown–McCoy radical* of $R$ is the intersection of all maximal ideals of $R$.

## Remarks

Equivalently, it is the intersection of the ideals $M$ such that $R/M$ is a simple ring.
Example: for $R = \Z$ the maximal ideals are $p\Z$ for primes $p$, and $\bigcap_p p\Z = 0$, so the Brown–McCoy radical of $\Z$ is $0$.
Non-example of a maximal ideal: in $\Z$ the ideal $4\Z$ is not maximal, since $4\Z \subsetneq 2\Z \subsetneq \Z$.
Every maximal ideal is a [[primitive ideal|M0JDQR0V5S]], because a simple ring with identity has a faithful simple module; hence the [[Jacobson radical|XA0DCNH7WY]] is contained in the Brown–McCoy radical.
The inclusion can be strict.
For the ring $R$ of linear maps of a vector space of countably infinite dimension, $J(R) = 0$, while the only maximal ideal is the ideal of maps of finite rank.
