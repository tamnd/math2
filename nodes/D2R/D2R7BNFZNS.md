---
tag: D2R7BNFZNS
kind: definition
name: Ore extension
msc: [16S36, 16W20, 16W25]
defines: VF3PV13BA1
uses: [0B1261B5ED, 0VTH8KPCG2, 0NZ8JA25WK, 0DZ9DKAKZR, 3J89REV9WQ, 0Q4CBD3HX0]
sources:
  - url: https://en.wikipedia.org/wiki/Ore_extension
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity and let $\sigma \colon R \to R$ be a [[ring endomorphism|0VTH8KPCG2]] with $\sigma(1) = 1$.
A *$\sigma$-derivation* of $R$ is an additive map $\delta \colon R \to R$ with $\delta(ab) = \sigma(a)\delta(b) + \delta(a) b$ for all $a, b \in R$.
Given such $\sigma$ and $\delta$, the *Ore extension* $R[x; \sigma, \delta]$ is the ring $S$ with these properties:

1. $S$ contains $R$ as a subring and contains an element $x$.
2. As a left $R$-[[module|0NZ8JA25WK]], $S$ is [[free|0DZ9DKAKZR]] with basis $1, x, x^2, \dots$.
3. $x a = \sigma(a) x + \delta(a)$ for all $a \in R$.

## Remarks

For every endomorphism $\sigma$ and $\sigma$-derivation $\delta$, such a ring exists and is unique up to an isomorphism fixing $R$ and $x$.
Its elements are written $a_0 + a_1 x + \cdots + a_n x^n$, and rule 3 together with associativity determines all products.
Example: let $k$ be a field, $R = k[y]$, $\sigma = \id$ and $\delta = d/dy$.
The map $\delta$ satisfies $\delta(ab) = a \delta(b) + \delta(a) b$, the Leibniz rule, so it is an $\id$-derivation, and rule 3 reads $x y = y x + 1$; this ring is the first [[Weyl algebra|98QE7KY55W]].
Non-example: take $R = k[y]$, $\sigma = \id$ and $\delta = \id$.
Then $\delta(1 \cdot 1) = 1$ but $1 \cdot \delta(1) + \delta(1) \cdot 1 = 2$, and $1 \ne 2$ in every field, so $\delta$ is not an $\id$-derivation.
No ring as above exists, since rule 3 would give $x = x \cdot 1 = 1 \cdot x + \delta(1) = x + 1$.
When $\delta = 0$ one writes $R[x; \sigma]$, the skew polynomial ring; when $\sigma = \id$ one writes $R[x; \delta]$, a differential polynomial ring.
If $R$ is a [[domain|0Q4CBD3HX0]] and $\sigma$ is injective, then $R[x; \sigma, \delta]$ is a domain.
If $R$ is left Noetherian and $\sigma$ is an automorphism, then $R[x; \sigma, \delta]$ is left Noetherian, a form of the Hilbert basis theorem.
