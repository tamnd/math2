---
tag: ESYKDNZF8E
kind: concept
name: Stone algebra
msc: ["06D15"]
specializes: [0HM0HQCK6N]
sources:
  - url: https://en.wikipedia.org/wiki/Stone_algebra
same_as:
  wikidata: Q7619048
  wikipedia: Stone algebra
---

## Summary

A Stone algebra is a bounded [[distributive lattice|0HM0HQCK6N]] in which every element $a$ has a [[pseudocomplement|WMR73J0S26]] $a^*$ and $a^* \vee a^{**} = 1$ holds.
The identity $a^* \vee a^{**} = 1$ is called the Stone identity.
Every [[Boolean algebra|0XADJKM699]] is a Stone algebra, and so is every bounded chain.
Stone algebras lie between Boolean algebras and general pseudocomplemented distributive lattices.

## Explanations

### L1 human

In a Boolean algebra, every element and its complement together fill everything.
A pseudocomplement is a weaker kind of complement, for which this can fail.
A Stone algebra asks for a little less: the pseudocomplement of $a$ and the pseudocomplement of that together fill everything.
The three-element chain $0 < m < 1$ is an example: $m^* = 0$ and $m^{**} = 1$, so $m^* \vee m^{**} = 1$, even though $m \vee m^* = m$.
