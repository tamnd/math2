---
tag: MYGWT305AB
kind: concept
name: Unit and counit
msc: [18A40]
sources:
  - url: https://en.wikipedia.org/wiki/Adjoint_functors
---

## Summary

The unit and the counit of an adjunction $F \dashv G$ are the two [[natural transformations|KYCPCC57FT]] $\eta \colon \mathrm{Id} \Rightarrow G F$ and $\varepsilon \colon F G \Rightarrow \mathrm{Id}$ that it determines.
They satisfy the two triangle identities, and conversely they determine the [[adjunction|TZHF6ZM92S]].
The unit and the counit give the [[monad|FF6XXA6D1A]] and the comonad of the adjunction.

## Explanations

### L1 human

For the free group and the forgetful functor, the unit sends each element of a set $X$ to the corresponding generator of the free group on $X$.
The counit takes the free group on the elements of a group $H$ and evaluates each word by multiplying in $H$.
So the unit says how to put things in, and the counit says how to compute the result.
The triangle identities say that putting in and then computing gives back what you started with.
