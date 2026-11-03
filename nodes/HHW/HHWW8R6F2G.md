---
tag: HHWW8R6F2G
kind: concept
name: Milnor square
msc: [19B99, 19A49]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Summary

A Milnor square is a commutative square of rings in which one ring is the [[pullback|Q05K04QJ71]] of two others over a third.
In addition, one of the two maps to the third ring is surjective.
Milnor showed that projective modules over the pullback can be built by patching modules over the two corners.
He also showed that $K_0$ and $K_1$ of the four rings fit into a [[Mayer–Vietoris sequence|C2VC3YTG2P]].
It is the algebraic analogue of covering a space by two closed pieces.

## Explanations

### L1 human

Think of a space glued from two pieces along a common part.
Functions on the whole space are pairs of functions on the pieces that agree on the common part.
A Milnor square is the same picture for rings: the big ring consists of pairs that agree after mapping into a third ring.
For example, the ring $k[x, y]/(xy)$ describes two crossing lines; its elements are pairs of polynomials $f(x)$ and $g(y)$ with the same constant term.
