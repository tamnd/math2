---
tag: NF2GB0TFEW
kind: definition
name: Premeasure
msc: [28A12]
defines: PV0XXSWFC7
uses: [KWE1DBMN9B, 0GSZ7B0CGR]
sources:
  - url: https://en.wikipedia.org/wiki/Pre-measure
---

## Definition

Let $X$ be a set and let $\mathcal{R}$ be a [[ring of sets|KWE1DBMN9B]] on $X$.
A *premeasure* on $\mathcal{R}$ is a map $\mu_0 \colon \mathcal{R} \to [0, \infty]$, with values in the [[extended real line|0GSZ7B0CGR]], such that:

1. $\mu_0(\varnothing) = 0$.
2. For every sequence $A_1, A_2, \ldots$ of pairwise disjoint sets of $\mathcal{R}$ whose union $\bigcup_n A_n$ lies in $\mathcal{R}$,
$$\mu_0\Big(\bigcup_{n=1}^{\infty} A_n\Big) = \sum_{n=1}^{\infty} \mu_0(A_n).$$

## Remarks

Example: on the ring of finite unions of half-open intervals $(a, b]$ in $\R$, the total length is a premeasure; countable additivity is checked with a compactness argument on closed subintervals.
Non-example: on the ring of finite and cofinite subsets of $\N$, put $\mu_0(A) = 0$ for finite $A$ and $\mu_0(A) = 1$ for cofinite $A$.
It is finitely additive, but $\N = \bigcup_n \set{n}$ gives $1 \ne \sum_n 0$, so clause 2 fails.
A premeasure is monotone on $\mathcal{R}$, and countably subadditive for sequences in $\mathcal{R}$ whose union lies in $\mathcal{R}$.
The same definition is used for a semiring of sets instead of a ring.
A measure is a premeasure whose domain is a $\sigma$-algebra.
