---
tag: 06YMXJMXYS
kind: definition
name: Unique factorisation domain
msc: [13F15]
defines: 0W4X9G6263
uses: [09S3PFBEPM, 052SDEPZH7, 053E86NWVK]
sources:
  - url: https://en.wikipedia.org/wiki/Unique_factorization_domain
    locator: Definition
---

## Definition

A unique factorisation domain is an [[integral domain|09S3PFBEPM]] $R$ with these two properties.

1. Every nonzero element $a \in R$ that is not a unit is a product $a = p_1 p_2 \cdots p_n$ of [[irreducible elements|052SDEPZH7]], with $n \ge 1$.
2. The factorization is unique up to order and units. If $p_1 \cdots p_n = q_1 \cdots q_m$ with all $p_i, q_j$ irreducible, then $n = m$. Also, there is a permutation $\sigma$ of $\{1, \dots, n\}$ such that $p_i$ and $q_{\sigma(i)}$ are [[associates|053E86NWVK]] for each $i$.

## Remarks

The integers are a unique factorisation domain: this is the fundamental theorem of arithmetic.
Every [[principal ideal domain is a unique factorisation domain|055HT85T3S]], and so is every [[polynomial ring over a unique factorisation domain|0D6KH8Y59N]].
The ring $\mathbb{Z}[\sqrt{-5}]$ is [[not a unique factorisation domain|0BSJYCG7NM]].
In a unique factorisation domain, [[irreducible elements are prime|0QRCFZKXH8]].

## Explanations

### L1 human

In the integers, $60 = 2 \cdot 2 \cdot 3 \cdot 5$, and every other factorization into primes uses the same primes, up to order and signs.
A unique factorisation domain is a ring where this works for every nonzero nonunit.
Units like $-1$ do not count as a different factorization.
