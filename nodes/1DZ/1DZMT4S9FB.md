---
tag: 1DZMT4S9FB
kind: concept
name: Fiber product of schemes
msc: [14A15, 18A30]
sources:
  - url: https://en.wikipedia.org/wiki/Fiber_product_of_schemes
same_as:
  wikidata: Q49001120
  wikipedia: Fiber product of schemes
---

## Summary

The fiber product $X \times_S Y$ of two [[morphisms of schemes|JXRKH6P1Z4]] $X \to S$ and $Y \to S$ is their [[pullback|Q05K04QJ71]] in the category of schemes.
It always exists, and for affine schemes it is the spectrum of a tensor product of rings.
Fiber products give products of varieties, fibers of morphisms, base change to another field, and the diagonal used to define separatedness.

## Explanations

### L1 human

For sets, the fiber product of $f \colon X \to S$ and $g \colon Y \to S$ is the set of pairs $(x, y)$ with $f(x) = g(y)$.
For schemes one cannot simply take pairs of points, because points of schemes carry more structure.
Instead the fiber product is defined by what maps into it look like.
In the affine case it is concrete: $\operatorname{Spec} B \times_{\operatorname{Spec} A} \operatorname{Spec} C = \operatorname{Spec}(B \otimes_A C)$.
For example, $\mathbb{A}^1_k \times_k \mathbb{A}^1_k = \operatorname{Spec}(k[x] \otimes_k k[y]) = \operatorname{Spec} k[x, y]$ is the plane.
