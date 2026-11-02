---
tag: QKWVXJWHP6
kind: concept
name: Prime ideal of a lattice
msc: [06B10, 06D05]
specializes: [5GW2T2AM1A]
sources:
  - url: https://en.wikipedia.org/wiki/Ideal_(order_theory)
---

## Summary

A prime ideal of a [[lattice|WH4SFAACAS]] is a proper [[ideal|5GW2T2AM1A]] that contains one of $x$ or $y$ whenever it contains their meet $x \wedge y$.
It is the lattice analogue of a [[prime ideal|00MHHZ9SNE]] of a commutative ring, with the meet in the role of the product.
The complement of a prime ideal is a prime [[filter|Z15FXM9WM1]].
Prime ideals are the points of the spaces used to represent distributive lattices and Boolean algebras.

## Explanations

### L1 human

An ideal is prime when it cannot catch the common part of two elements without catching one of the two elements.
Fix a point $p$ of a set $X$ and look at all subsets of $X$ that do not contain $p$.
They form a prime ideal of the subsets of $X$: if $A \cap B$ misses $p$, then $A$ or $B$ misses $p$.
Splitting the lattice into this ideal and its complement is like asking the single yes-or-no question "does the set contain $p$?".
