---
tag: WPE5Z53QYJ
kind: concept
name: Field trace
msc: [12F05, 11R04]
sources:
  - url: https://en.wikipedia.org/wiki/Field_trace
same_as:
  wikidata: Q2450665
  wikipedia: Field trace
---

## Summary

Let $L/K$ be a [[finite extension|0C1Y04SZ1W]] and let $\alpha \in L$.
Multiplication by $\alpha$ is a $K$-linear map of $L$, and the field trace $\mathrm{Tr}_{L/K}(\alpha)$ is its [[trace|0KZDNGA561]].
It is a $K$-linear map $L \to K$.
For a separable extension it is the sum of the images of $\alpha$ under all embeddings of $L$ into an algebraic closure.
The trace gives the [[trace form|YWX2R53ED6]] and the [[discriminant|3BCYVS9E17]] of an extension.
The trace map is not identically zero exactly when the extension is separable.

## Explanations

### L1 human

Multiplying by a fixed element $\alpha$ is a linear map of the field $L$, seen as a vector space over $K$.
The trace of $\alpha$ is the trace of this map, the sum of the diagonal entries of its matrix.
For Gaussian numbers $a + bi$ over $\Q$, the trace is $(a + bi) + (a - bi) = 2a$.
So the trace adds up all the conjugates of $\alpha$, while the [[norm|KRNFEZWPY0]] multiplies them.
