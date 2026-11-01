---
tag: W9VYJRBF9N
kind: object
name: Cantor space
msc: [54F65, 54H05]
uses: [0GBG8B49AA, 0TVJZYB6SH, 0RJSBR9GW1, 0BXNDZFQME, 0RQ8DHHR8V, 091GJ3FYD7]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor_space
same_as:
  wikidata: Q616653
  wikipedia: Cantor space
---

## Description

The *Cantor space* is the set $2^{\N} = \set{0, 1}^{\N}$ of all infinite sequences of $0$s and $1$s, with the [[product topology|0GBG8B49AA]] of the discrete space $\set{0, 1}$.
Its basic open sets are the sets of all sequences that begin with a given finite word.
The topology comes from the metric $d(x, y) = 2^{-n}$, where $n$ is the first index with $x_n \neq y_n$, and $d(x, x) = 0$.
The space is [[compact|0TVJZYB6SH]] by Tychonoff's theorem, [[totally disconnected|0RJSBR9GW1]], and has no isolated points.
More generally, a topological space is called a Cantor space when it is homeomorphic to $2^{\N}$.

## Remarks

The [[Cantor set|0BXNDZFQME]] is a Cantor space: it [[is homeomorphic to the space of binary sequences|0RQ8DHHR8V]].
By [[Brouwer's theorem|3NKBCNH5JS]], a space is a Cantor space if and only if it is nonempty, compact, [[metrizable|091GJ3FYD7]], totally disconnected and without isolated points.
For this reason $2^{\N} \times 2^{\N}$ and $(2^{\N})^{\N}$ are again Cantor spaces.
Every nonempty compact metric space is a continuous image of the Cantor space.

## Explanations

### L1 human

A point of the Cantor space is an endless list of yes or no answers.
Two points are close when their lists agree for a long time.
The space looks the same everywhere and is made only of dust, with no two points joined by a connected piece, yet it is compact like a closed interval.
