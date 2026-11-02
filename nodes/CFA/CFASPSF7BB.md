---
tag: CFASPSF7BB
kind: concept
name: Composition operator
msc: [47B33]
sources:
  - url: https://en.wikipedia.org/wiki/Composition_operator
same_as:
  wikidata: Q5156798
  wikipedia: Composition operator
---

## Summary

A composition operator acts on a space of functions by precomposing with a fixed map: $C_\varphi f = f \circ \varphi$.
It is always linear.
The questions are when it maps the space into itself, when it is bounded or compact, and how its properties reflect the symbol $\varphi$.
On the [[Hardy space|PNNNFJVF6W]] of the disc, every holomorphic self-map $\varphi$ of the disc gives a bounded composition operator, by Littlewood's subordination principle.
In ergodic theory the same construction is called the Koopman operator.

## Explanations

### L1 human

A composition operator changes a function by first moving the point with a fixed map $\varphi$ and then applying the function.
If $\varphi(z) = z/2$, then $C_\varphi$ turns $f(z)$ into $f(z/2)$, a squeezed copy of $f$.
On power series $\sum a_n z^n$ this multiplies the $n$-th coefficient by $2^{-n}$.
Properties of the operator, such as its norm or its spectrum, then become questions about how $\varphi$ moves points around.
