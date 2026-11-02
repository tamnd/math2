---
tag: 17CW7Z2YDT
kind: definition
name: Finitely additive measure
msc: [28A12, 28A10]
defines: KFWQ24D9M6
uses: [PFMGZ7988V, 0GSZ7B0CGR, D7KB9HFCGZ]
sources:
  - url: https://en.wikipedia.org/wiki/Content_(measure_theory)
---

## Definition

Let $\mathcal{A}$ be an [[algebra of sets|PFMGZ7988V]] on a set $X$.
A *finitely additive measure* on $\mathcal{A}$ is a function $\mu \colon \mathcal{A} \to [0, \infty]$, with values in the [[extended real number line|0GSZ7B0CGR]], such that:

1. $\mu(\varnothing) = 0$.
2. $\mu(A \cup B) = \mu(A) + \mu(B)$ for all $A, B \in \mathcal{A}$ with $A \cap B = \varnothing$.

## Remarks

Let $\mathcal{A}$ be the algebra of subsets $A \subseteq \N$ such that $A$ or $\N \setminus A$ is finite.
Let $\nu(A) = 0$ for finite $A$ and $\nu(A) = 1$ otherwise.
Clause 1 holds, and clause 2 holds since two disjoint sets cannot both have finite complement.
This $\nu$ is not [[countably additive|D7KB9HFCGZ]], since $\nu(\N) = 1$ while $\nu(\set{n}) = 0$ for each $n$.
On the same algebra, the function with $\mu(\varnothing) = 0$ and $\mu(A) = 1$ for $A \ne \varnothing$ is not finitely additive, since clause 2 fails for $A = \set{1}$ and $B = \set{2}$.
By induction, clause 2 gives additivity over any finite disjoint union.
A finitely additive measure is monotone: $\mu(A) \le \mu(B)$ when $A \subseteq B$.
Other names are *content* and *charge*; the word content is also used for the same notion on a ring or a semiring of sets.
