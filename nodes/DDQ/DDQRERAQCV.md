---
tag: DDQRERAQCV
kind: concept
name: Tor functor
msc: [13D07, 18G15]
sources:
  - url: https://en.wikipedia.org/wiki/Tor_functor
same_as:
  wikidata: Q988381
  wikipedia: Tor functor
---

## Summary

The Tor functors $\operatorname{Tor}_n^R(M, N)$ are the left derived functors of the [[tensor product|F0HQXQ0HCD]] $M \otimes_R N$.
They measure how far tensoring is from being exact.
The vanishing of $\operatorname{Tor}_1^R(M, -)$ characterizes the [[flat modules|73RYYEVDKA]], and Tor groups over $\Z$ appear in the universal coefficient and Künneth theorems of topology.

## Explanations

### L1 human

Tensoring with a module can turn an injective map into one that is not injective.
The Tor groups record what is lost.
To compute them, replace $M$ by a [[projective resolution|HK2AA1YSQ2]], tensor with $N$, and take homology.
For example, $\operatorname{Tor}_1^\Z(\Z/2\Z, \Z/2\Z) \cong \Z/2\Z$, because multiplication by $2$ is injective on $\Z$ but becomes the zero map on $\Z/2\Z$.
The name comes from torsion: $\operatorname{Tor}_1^\Z(\Z/n\Z, A)$ is the set of elements of the abelian group $A$ killed by $n$.
