---
tag: 3GHGFTMFQR
kind: concept
name: Faddeeva function
msc: ["33B20"]
sources:
  - url: https://en.wikipedia.org/wiki/Faddeeva_function
same_as:
  wikidata: Q4027138
  wikipedia: Faddeeva function
---

## Summary

The Faddeeva function is the scaled complex [[complementary error function|TZ3CT1YA9B]] $w(z) = e^{-z^2} \operatorname{erfc}(-iz)$.
It is an [[entire function|0G4F0XB9X2]], and in the upper half-plane it is a Cauchy-type integral of the Gaussian.
On the real line its real part is $e^{-x^2}$ and its imaginary part is a multiple of the [[Dawson function|EQ4QB1QW60]].
It is used to compute the Voigt line profile in spectroscopy and complex error functions in numerical work.

## Explanations

### L1 human

The error function of a complex number can be enormous, because $e^{-z^2}$ is huge for some complex $z$.
The Faddeeva function multiplies by a factor that cancels this growth, so it stays of moderate size in the upper half-plane.
On the real axis it packs two real functions into one complex value.
Its real part is the Gaussian bell curve, and its imaginary part is the Dawson function up to a factor.
