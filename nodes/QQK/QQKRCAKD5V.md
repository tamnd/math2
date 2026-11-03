---
tag: QQKRCAKD5V
kind: concept
name: Zinbiel algebra
msc: [17A30, 18M60]
sources:
  - url: https://en.wikipedia.org/wiki/Zinbiel_algebra
same_as:
  wikidata: Q2835946
  wikipedia: Zinbiel algebra
---

## Summary

A Zinbiel algebra is a vector space with a bilinear product $\circ$ such that $(a \circ b) \circ c = a \circ (b \circ c) + a \circ (c \circ b)$.
Its symmetrization $a \circ b + b \circ a$ is always associative and commutative, so a Zinbiel product is a way of splitting a commutative product into two halves.
The half-shuffle product on tensors and the product $f \circ g = \int_0^x f' g$ of functions are the basic examples.
The name is "Leibniz" written backwards: the [[operad|2C5QGNNCAE]] of Zinbiel algebras is Koszul dual to that of [[Leibniz algebras|FGM1ZM3KKN]].

## Explanations

### L1 human

Ordinary multiplication of functions can be cut into two pieces by integration by parts.
For functions $f, g$ with $f(0) = g(0) = 0$, one has $f(x) g(x) = \int_0^x f' g \, dt + \int_0^x f g' \, dt$.
The first piece, viewed as a product of $f$ and $g$, is not commutative or associative.
It still obeys one fixed rule for triple products, and this rule defines a Zinbiel algebra.
Adding the product to its mirror image gives back the usual commutative product.
