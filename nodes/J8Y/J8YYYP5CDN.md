---
tag: J8YYYP5CDN
kind: statement
role: theorem
name: Mori–Nagata theorem
msc: ["13F05", "13B22", "13E05"]
uses: [0MVH4Y1CRZ, 09S3PFBEPM, 0VF11ZTTMD, G0V86SJBQW, CB9WJCN9BM]
about: [G0V86SJBQW, CB9WJCN9BM]
sources:
  - url: https://en.wikipedia.org/wiki/Mori–Nagata_theorem
same_as:
  wikidata: Q17099060
  wikipedia: Mori–Nagata theorem
---

## Statement

Let $A$ be a [[Noetherian|0MVH4Y1CRZ]] [[integral domain|09S3PFBEPM]] with [[field of fractions|0VF11ZTTMD]] $K$.
Then the [[integral closure|G0V86SJBQW]] of $A$ in $K$ is a [[Krull domain|CB9WJCN9BM]].

## Remarks

A Noetherian integrally closed domain is a Krull domain, so the theorem says that integral closure keeps part of the Noetherian property, even when it loses the rest.
The integral closure of a Noetherian domain need not be Noetherian, and Nagata gave such examples.
So the class of Krull domains is the natural home for integral closures of Noetherian domains.
In dimension $1$, the [[Krull–Akizuki theorem|FSXA3CF365]] gives more: the integral closure is Noetherian.
For example, the integral closure of $\Z[\sqrt{-3}]$ in $\Q(\sqrt{-3})$ is $\Z[(1 + \sqrt{-3})/2]$, a Dedekind domain and so a Krull domain.

## Explanations

### L1 human

Making a ring integrally closed can destroy the Noetherian property.
The theorem says that something useful survives.
The closed ring is a Krull domain, which means that it still has a good theory of divisors, as in a ring with unique factorisation up to a class group.

### L2 human

Krull domains are the domains that are intersections of discrete valuation rings with a finiteness condition, and they carry a divisor class group.
The theorem lets one use divisor theory on the normalisation of any Noetherian domain, for example on the normalisation of the coordinate ring of a singular affine variety.
Compare the [[Krull–Akizuki theorem|FSXA3CF365]], which in dimension one gives a Noetherian normalisation.
