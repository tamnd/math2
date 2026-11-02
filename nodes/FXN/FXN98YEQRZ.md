---
tag: FXN98YEQRZ
kind: definition
name: Radon measure
msc: [28C15, 28C05]
defines: HZNEQQBCW4
uses: [0S1FJ8VEX9, DYR1QFNGNJ, YQ5C1SRE0W, 28E5Q5BM69, 0R6EWFKRCF]
sources:
  - url: https://en.wikipedia.org/wiki/Radon_measure
---

## Definition

Let $X$ be a [[Hausdorff space|0S1FJ8VEX9]] and let $\mu$ be a [[Borel measure|DYR1QFNGNJ]] on $X$.
The measure $\mu$ is a *Radon measure* if both of the following hold.

1. $\mu$ is [[locally finite|YQ5C1SRE0W]]: every point has an open neighbourhood of finite measure.
2. $\mu$ is [[inner regular|28E5Q5BM69]]: $\mu(A) = \sup \set{\mu(K) : K \subseteq A, \ K \text{ compact}}$ for every Borel set $A$.

## Remarks

Example: the Dirac measure $\delta_p$ at a point $p$ is a Radon measure.
Every point has a neighbourhood of measure at most $1$; and if $p \in A$ then $K = \{p\}$ is a [[compact|0R6EWFKRCF]] subset of $A$ with $\delta_p(K) = \delta_p(A)$, while if $p \notin A$ both sides are $0$.
Lebesgue measure on $\R^n$ is also a Radon measure.

Non-example: counting measure on $\R$ satisfies clause 2 but not clause 1.

Another common definition, used on locally compact Hausdorff spaces, asks that $\mu$ be finite on compact sets, outer regular on all Borel sets and inner regular on open sets.
On a locally compact Hausdorff space in which every open set is σ-compact, such as $\R^n$, every Borel measure that is finite on compact sets is a Radon measure.
