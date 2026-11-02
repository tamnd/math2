---
tag: CTJ5AD8ST5
kind: concept
name: Equalizer
msc: [18A30]
specializes: [CHS5AFJGWE]
sources:
  - url: https://en.wikipedia.org/wiki/Equaliser_(mathematics)
same_as:
  wikidata: Q1224487
  wikipedia: Equaliser (mathematics)
---

## Summary

The equalizer of two parallel morphisms $f, g \colon X \to Y$ in a [[category|A2DE66937D]] is a universal morphism $e \colon E \to X$ with $f \circ e = g \circ e$.
It is the [[limit|CHS5AFJGWE]] of the diagram formed by $f$ and $g$.
In sets it is the subset where $f$ and $g$ agree, and in abelian groups it is the kernel of $f - g$.
Every equalizer is a monomorphism, and products together with equalizers build all limits.

## Explanations

### L1 human

Given two functions $f$ and $g$ from $X$ to $Y$, ask where they give the same answer.
The answer is the set $E = \set{x \in X : f(x) = g(x)}$, which sits inside $X$.
For example, for $f(x) = x^2$ and $g(x) = x$ on the real numbers, the equalizer is $\{0, 1\}$, the set of solutions of $x^2 = x$.
The categorical equalizer describes this "solution set" through maps only: anything mapping into $X$ on which $f$ and $g$ agree must map into $E$.
