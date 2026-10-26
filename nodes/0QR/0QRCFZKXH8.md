---
tag: 0QRCFZKXH8
kind: statement
role: theorem
name: In a UFD irreducible elements are prime
msc: [13F15]
uses: [06YMXJMXYS, 052SDEPZH7, 0MNHXBSX3M, 0F0K8DB9TD]
sources:
  - url: https://en.wikipedia.org/wiki/Unique_factorization_domain
    locator: Properties
---

## Statement

Let $R$ be a [[unique factorisation domain|06YMXJMXYS]] and let $p \in R$.
Then $p$ is [[irreducible|052SDEPZH7]] if and only if $p$ is [[prime|0MNHXBSX3M]].

## Remarks

[[Prime elements are irreducible|0F0K8DB9TD]] in every integral domain. The other direction needs unique factorisation.
The proof: suppose $p$ is irreducible and $p c = a b$. Factor $a$, $b$ and $c$ into irreducibles. By uniqueness, $p$ is an associate of an irreducible factor of $a$ or of $b$.
Conversely, an integral domain in which every nonzero nonunit is a product of irreducibles, and every irreducible is prime, is a unique factorisation domain.

## Explanations

### L1 human

In the integers, Euclid's lemma says that a prime that divides a product divides a factor.
In a unique factorisation domain, the same thing is true for every irreducible element.
In $\mathbb{Z}[\sqrt{-5}]$ this fails, and so factorisation is not unique there.
