---
tag: PWZAR115MC
kind: definition
name: Countable additivity
msc: [28A10]
defines: D7KB9HFCGZ
uses: [0SJ3RX9TXA, 0GSZ7B0CGR, 0NM626FH6Q, 07KVB4JSC7]
sources:
  - url: https://en.wikipedia.org/wiki/Sigma-additive_set_function
---

## Definition

Let $X$ be a [[set|0SJ3RX9TXA]] and let $\mathcal{F}$ be a family of subsets of $X$.
Let $\mu \colon \mathcal{F} \to [0, \infty]$ be a function with values in the [[extended real number line|0GSZ7B0CGR]].
The function $\mu$ is *countably additive*, or *σ-additive*, if the following holds.
For every sequence $A_1, A_2, \ldots$ of pairwise disjoint sets in $\mathcal{F}$ whose [[union|07KVB4JSC7]] is in $\mathcal{F}$,
$$\mu\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} \mu(A_n).$$

## Remarks

On the power set of $\N$, the function $\mu(A) = \sum_{n \in A} 2^{-n}$ is countably additive.
The [[series|0NM626FH6Q]] has non-negative terms, so its sum does not depend on how the terms are grouped.
On the family $\mathcal{F}$ of subsets $A \subseteq \N$ such that $A$ or $\N \setminus A$ is finite, let $\nu(A) = 0$ for finite $A$ and $\nu(A) = 1$ otherwise.
This $\nu$ is finitely additive but not countably additive.
Indeed $\N = \bigcup_{n} \set{n}$ is a disjoint union of sets in $\mathcal{F}$, but $\nu(\N) = 1$ and $\sum_n \nu(\set{n}) = 0$.
If $\varnothing \in \mathcal{F}$ and $\mu$ takes at least one finite value, then countable additivity forces $\mu(\varnothing) = 0$: take $A_1 = A$ with $\mu(A) < \infty$ and $A_n = \varnothing$ for $n \ge 2$.
The same definition is used for functions with values in $\R$, $\C$ or a Banach space; then the series must converge.
