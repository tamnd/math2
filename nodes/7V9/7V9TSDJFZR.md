---
tag: 7V9TSDJFZR
kind: definition
name: Measure
msc: [28A12, 28A10]
defines: PR11BZQQPG
uses: [N4KDT83V3S, 0GSZ7B0CGR, D7KB9HFCGZ, 0NM626FH6Q, 0ACRGYNHSR]
sources:
  - url: https://en.wikipedia.org/wiki/Measure_(mathematics)
---

## Definition

Let $(X, \Sigma)$ be a [[measurable space|N4KDT83V3S]], and let $[0, \infty]$ be the non-negative part of the [[extended real number line|0GSZ7B0CGR]].
A *measure* on $(X, \Sigma)$ is a function $\mu \colon \Sigma \to [0, \infty]$ such that:

1. $\mu(\varnothing) = 0$.
2. $\mu$ is [[countably additive|D7KB9HFCGZ]]: for every sequence $A_1, A_2, \ldots$ of pairwise disjoint sets in $\Sigma$,
$$\mu\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} \mu(A_n).$$

## Remarks

The [[series|0NM626FH6Q]] in clause 2 has non-negative terms, so it has a value in $[0, \infty]$.
For $x \in X$, the [[Dirac measure|0ACRGYNHSR]] $\delta_x$, with $\delta_x(A) = 1$ if $x \in A$ and $\delta_x(A) = 0$ otherwise, is a measure.
For clause 2, the point $x$ lies in at most one of the disjoint sets $A_n$, so both sides are $1$ or both are $0$.
On the power set of $\N$, the function with $\nu(\varnothing) = 0$ and $\nu(A) = 1$ for $A \ne \varnothing$ is not a measure.
Clause 2 fails: $\nu(\set{1} \cup \set{2}) = 1$, while $\nu(\set{1}) + \nu(\set{2}) = 2$.
A measure is monotone, $\mu(A) \le \mu(B)$ when $A \subseteq B$, and countably subadditive, $\mu(\bigcup_n A_n) \le \sum_n \mu(A_n)$.
A measure with $\mu(X) = 1$ is a probability measure.
