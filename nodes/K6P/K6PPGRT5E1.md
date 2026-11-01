---
tag: K6PPGRT5E1
kind: definition
name: Catenary ring
msc: [13C15]
defines: B2CYR292J6
uses: [0310REJJY8, 00MHHZ9SNE, 0S8FE7ZMFM]
sources:
  - url: https://en.wikipedia.org/wiki/Catenary_ring
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]].
A chain of [[prime ideals|00MHHZ9SNE]] $\mathfrak p_0 \subsetneq \mathfrak p_1 \subsetneq \cdots \subsetneq \mathfrak p_n$ has length $n$.
It is saturated if no prime ideal $\mathfrak q$ satisfies $\mathfrak p_{i-1} \subsetneq \mathfrak q \subsetneq \mathfrak p_i$ for some $i$.
The ring $R$ is *catenary* if the following holds for all prime ideals $\mathfrak p \subseteq \mathfrak q$ of $R$.
Every saturated chain of prime ideals from $\mathfrak p$ to $\mathfrak q$ is finite, and all such chains have the same length.

## Remarks

Every principal ideal domain is catenary.
Its nonzero primes are maximal, so the saturated chains are $(0) \subsetneq \mathfrak m$ and the trivial chains, and between two given primes they all have the same length.
Nagata constructed Noetherian local domains that are not catenary: in such a ring there are primes $\mathfrak p \subseteq \mathfrak q$ joined by saturated chains of two different lengths.
Many authors include the condition that $R$ is [[Noetherian|0670T59HGE]] in the definition.
A stronger notion is that of a [[universally catenary ring|5WAFPTH09V]].
