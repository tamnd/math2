---
tag: TZHF6ZM92S
kind: concept
name: Adjoint functors
msc: [18A40]
sources:
  - url: https://en.wikipedia.org/wiki/Adjoint_functors
same_as:
  wikidata: Q357858
  wikipedia: Adjoint functors
---

## Summary

Two [[functors|28NQ0KRHD3]] $F \colon \mathcal{C} \to \mathcal{D}$ and $G \colon \mathcal{D} \to \mathcal{C}$ are adjoint when maps $F c \to d$ match naturally with maps $c \to G d$.
Then $F$ is the left adjoint and $G$ the right adjoint.
Adjunctions are everywhere in mathematics: free constructions, products, quotients, tensor and hom, and much more.
Each adjunction gives a [[monad|FF6XXA6D1A]], and right adjoints preserve limits.

## Explanations

### L1 human

Many constructions come with a forgetful partner.
The free group on a set $X$ is built from $X$, and every group has an underlying set.
A group homomorphism from the free group on $X$ to a group $H$ is the same as a plain function from $X$ to the set of $H$.
This kind of matching between two sets of maps is an adjunction.
Here the free group functor is the left adjoint and the forgetful functor is the right adjoint.
