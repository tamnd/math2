---
tag: 5MR9ZSC3CX
kind: concept
name: Statistical learning theory
msc: [68Q32, 62H30, 68T05]
sources:
  - url: https://en.wikipedia.org/wiki/Statistical_learning_theory
same_as:
  wikidata: Q7604400
  wikipedia: Statistical learning theory
---

## Summary

Statistical learning theory is the mathematical theory of learning a prediction rule from examples.
It models the data as independent draws from an unknown distribution and measures a rule by its expected [[loss|3BTG6VVCGZ]] on new data, its risk.
Its central results bound the gap between the error on the training data and the true risk.
The bounds depend on the size of the class of rules, measured for example by its [[VC dimension|KCFXR9K3GD]].
It was developed by Vladimir Vapnik and Alexey Chervonenkis among others, and it underlies [[empirical risk minimization|56NVR0SS61]] and support vector machines.

## Explanations

### L1 human

A spam filter is trained on a few thousand labelled emails and must then work on emails it has never seen.
Statistical learning theory asks when doing well on the training emails guarantees doing well on new ones.
The answer depends on how many examples there are and on how flexible the family of possible filters is.
A very flexible family can memorise the training data and still fail on new data; this is overfitting.
The theory gives precise bounds that balance these two effects.
