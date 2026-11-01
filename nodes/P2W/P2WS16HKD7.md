---
tag: P2WS16HKD7
kind: object
name: Baire space of sequences
msc: [54H05, "03E15"]
uses: [0GBG8B49AA, 0MWKJ44V5A, 0BY52JW6NK, 0Z2P41SVDP, 0ZH5AJ2ED7, 0DZXAXEJQ9]
sources:
  - url: https://en.wikipedia.org/wiki/Baire_space_(set_theory)
same_as:
  wikidata: Q803936
  wikipedia: Baire space (set theory)
---

## Description

The *Baire space* $\N^{\N}$ is the set of all infinite sequences of [[natural numbers|0MWKJ44V5A]].
Its topology is the [[product topology|0GBG8B49AA]] of countably many copies of the discrete space $\N$.
Its basic open sets are the sets of all sequences that begin with a given finite sequence.
The topology comes from the metric $d(x, y) = 2^{-n}$, where $n$ is the first index with $x_n \neq y_n$, and $d(x, x) = 0$.
With this metric the space is [[complete|0BY52JW6NK]], and it is [[separable|0Z2P41SVDP]], since the eventually zero sequences are dense.
In descriptive set theory it is written $\mathcal{N}$ or $\omega^\omega$.

## Remarks

The Baire space is homeomorphic to the set of [[irrational numbers|0DZXAXEJQ9]] with the topology of the real line; one homeomorphism uses continued fraction expansions.
It is not locally compact: no basic open set is compact, since the next term of the sequence can take infinitely many values.
It has a base of clopen sets.
Every nonempty Polish space, that is a separable completely metrizable space, is a continuous image of $\N^{\N}$.
As a complete metric space it is a [[Baire space|0ZH5AJ2ED7]] in the sense of Baire category; the two uses of the name are related but different.

## Explanations

### L1 human

A point of the Baire space is an endless list of natural numbers.
Two points are close when their lists agree for a long time.
It is the basic space of descriptive set theory, where sets of reals are studied through the sequences that code them.
