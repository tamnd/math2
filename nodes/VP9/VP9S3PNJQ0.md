---
tag: VP9S3PNJQ0
kind: concept
name: Kriging
msc: [62M30, 62M20, 62H11]
sources:
  - url: https://en.wikipedia.org/wiki/Kriging
same_as:
  wikidata: Q225926
  wikipedia: Kriging
---

## Summary

Kriging is a method to predict the value of a random field at an unobserved location from its values at observed locations.
The prediction is the best linear unbiased predictor: the weighted average of the data with the smallest mean squared prediction error.
The weights come from the spatial dependence of the field, described by its [[variogram|ZF8AA2JVKV]] or its covariance function.
It is named after the mining engineer Danie Krige, and in the language of [[Gaussian processes|22WEM6RTW0]] it is essentially Gaussian process regression.

## Explanations

### L1 human

Suppose you measured the gold content of rock at a few drill holes and want a guess for a new spot.
Nearby holes should count more than far ones, and holes that cluster together should not be counted twice.
Kriging chooses the weights to make the expected squared error of the guess as small as possible.
At a drill hole itself, kriging returns the measured value, so it interpolates the data.
It also gives the size of the expected error, which is larger far from the data.
