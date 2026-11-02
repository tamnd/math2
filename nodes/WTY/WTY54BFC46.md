---
tag: WTY54BFC46
kind: concept
name: Regularization of ill-posed problems
msc: [65J20, 65F22, 47A52]
sources:
  - url: https://en.wikipedia.org/wiki/Regularization_(mathematics)
---

## Summary

A problem is ill-posed in the sense of Hadamard when it is not a [[well-posed problem|W09B9NZ9B5]].
This means that a solution does not exist, is not unique, or does not depend continuously on the data.
Regularization replaces an ill-posed problem by a family of nearby well-posed problems, indexed by a parameter.
The parameter is chosen from the noise level so that the regularized solutions converge to the true solution as the noise tends to zero.
It is the basic tool for [[inverse problems|PCMW7KN5P4]] such as image deblurring, tomography and parameter identification.

## Explanations

### L1 human

Some problems amplify small errors in the data enormously, so that the naive answer is useless.
Undoing a blur in a photograph is an example: tiny noise gets magnified into wild patterns.
Regularization adds a mild preference, such as "the answer should not be too large or too rough", which tames this amplification.
The strength of the preference is tuned to the amount of noise.
Too little regularization leaves the noise in, and too much smooths away the real details.
