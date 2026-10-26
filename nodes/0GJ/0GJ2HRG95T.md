---
tag: 0GJ2HRG95T
kind: definition
name: Euclidean domain
msc: [13F07]
defines: 0CHS7RBD39
uses: [09S3PFBEPM]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_domain
    locator: Definition
---

## Definition

A Euclidean domain is an [[integral domain|09S3PFBEPM]] $R$ with a function $\delta \colon R \setminus \{0\} \to \mathbb{N}$ with this property.
For all $a, b \in R$ with $b \neq 0$, there are $q, r \in R$ such that $a = b q + r$, and $r = 0$ or $\delta(r) < \delta(b)$.
The function $\delta$ is a Euclidean function of $R$.

## Remarks

The absolute value is a Euclidean function on $\mathbb{Z}$. The degree is a Euclidean function on $K[x]$ for a field $K$.
Some authors also require $\delta(a) \le \delta(a b)$ for all nonzero $a, b$. This changes the class of Euclidean domains only in appearance, because a ring with a Euclidean function has one with this extra property.
Every Euclidean domain is a [[principal ideal domain|0RZYDVZ475]].

## Explanations

### L1 human

In a Euclidean domain, you can always divide with a remainder that is smaller than the divisor.
The function $\delta$ measures what smaller means.
This is all you need to run the Euclidean algorithm.
