---
tag: KAN07YC9T2
kind: concept
name: Additive functor
msc: ["18E05"]
specializes: [28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/Preadditive_category
---

## Summary

An additive functor is a [[functor|28NQ0KRHD3]] between [[preadditive categories|SC6FD5F4J0]] that respects the addition of morphisms.
Between additive categories, these are exactly the functors that preserve finite biproducts.
Hom functors, tensor products with a fixed module and derived functors are additive.
Additivity is the basic compatibility needed to apply a functor to chain complexes and exact sequences.

## Explanations

### L1 human

In a preadditive category one can add arrows between the same objects.
An additive functor sends a sum of arrows to the sum of their images, just as a linear map sends a sum of vectors to the sum of their images.
For example, tensoring with a fixed abelian group $M$ sends a homomorphism $f$ to $f \otimes \id_M$, and $(f + g) \otimes \id_M = f \otimes \id_M + g \otimes \id_M$.
Additive functors take direct sums to direct sums, so they can be computed piece by piece.
