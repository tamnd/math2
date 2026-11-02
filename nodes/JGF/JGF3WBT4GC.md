---
tag: JGF3WBT4GC
kind: definition
name: Content
msc: [28A12]
defines: PFF8SV6ENB
uses: [PYH82FMXQ2, 0GSZ7B0CGR]
sources:
  - url: https://en.wikipedia.org/wiki/Content_(measure_theory)
---

## Definition

Let $X$ be a set and let $\mathcal{S}$ be a [[semiring of sets|PYH82FMXQ2]] on $X$.
More generally, $\mathcal{S}$ may be any family of subsets of $X$ that contains $\varnothing$.
A *content* on $\mathcal{S}$ is a map $\mu \colon \mathcal{S} \to [0, \infty]$, with values in the [[extended real line|0GSZ7B0CGR]], such that:

1. $\mu(\varnothing) = 0$.
2. If $A_1, \ldots, A_n \in \mathcal{S}$ are pairwise disjoint and $A_1 \cup \cdots \cup A_n \in \mathcal{S}$, then
$$\mu(A_1 \cup \cdots \cup A_n) = \mu(A_1) + \cdots + \mu(A_n).$$

## Remarks

Example: on the semiring of bounded intervals $[a, b)$ in $\R$, length $\mu([a, b)) = b - a$ is a content.
Indeed, if $[a, b)$ is a disjoint union of finitely many such intervals, their lengths add up to $b - a$.
Non-example: on the same semiring, $\mu([a, b)) = (b - a)^2$ fails clause 2, since $[0, 2) = [0, 1) \cup [1, 2)$ but $4 \ne 1 + 1$.
On a ring of sets a content is monotone and finitely subadditive.
A content on a ring is called a [[finitely additive measure|KFWQ24D9M6]] by many authors.
A content that is countably additive is a [[premeasure|PV0XXSWFC7]].
The word content also names a set function used to build Haar measure.
It is defined on the compact subsets of a space; it is monotone and finitely subadditive, and additive on disjoint compact sets.
