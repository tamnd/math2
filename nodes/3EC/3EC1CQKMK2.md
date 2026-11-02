---
tag: 3EC1CQKMK2
kind: definition
name: Regular measure
msc: [28C15]
defines: HQFZQ0F991
uses: [DYR1QFNGNJ, 28E5Q5BM69, 33C1KEK3SC]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_measure
---

## Definition

Let $X$ be a topological space and let $\mu$ be a [[Borel measure|DYR1QFNGNJ]] on $X$.
The measure $\mu$ is *regular* if both of the following hold.

1. $\mu$ is [[inner regular|28E5Q5BM69]]: $\mu(A) = \sup \set{\mu(K) : K \subseteq A, \ K \text{ compact and Borel}}$ for every Borel set $A$.
2. $\mu$ is [[outer regular|33C1KEK3SC]]: $\mu(A) = \inf \set{\mu(U) : U \supseteq A, \ U \text{ open}}$ for every Borel set $A$.

## Remarks

Example: Lebesgue measure on the Borel sets of $\R^n$ is regular.
Outer regularity follows from its construction by covers with open boxes.
For inner regularity, a Borel set $A$ contains a closed set $F$ with $\lambda(A \setminus F)$ arbitrarily small when $\lambda(A) < \infty$.
The sets $F \cap [-k, k]^n$ are compact, and their measures tend to $\lambda(F)$.
The case $\lambda(A) = \infty$ follows by cutting $A$ into bounded pieces.

Non-example: counting measure on $\R$ satisfies clause 1 but not clause 2.
Finite sets are compact, which gives clause 1; the set $\{0\}$ has measure $1$, but every open set around it has measure $\infty$.

Conventions vary.
Many texts use closed sets instead of compact sets in clause 1.
On a metric space, every finite Borel measure is regular in that closed-set sense.
