---
tag: ZF8AA2JVKV
kind: concept
name: Variogram
msc: [62M30, 62M40, 62H11]
sources:
  - url: https://en.wikipedia.org/wiki/Variogram
same_as:
  wikidata: Q2269270
  wikipedia: Variogram
---

## Summary

The variogram of a spatial random field measures how different the values at two locations are expected to be.
It is a function of the displacement between the two locations.
It is defined as the variance of the increment $Z(s + h) - Z(s)$, and half of it is called the semivariogram.
It exists under weaker assumptions than a covariance function, so it also describes fields without a constant variance, such as the [[Wiener process|22735FGJV6]].
The variogram is the basic input of [[kriging|VP9S3PNJQ0]] and of most of geostatistics.

## Explanations

### L1 human

Measure soil moisture at many points of a field.
Two points a metre apart usually have similar values, while two points a kilometre apart may be very different.
The variogram records, for each distance, the typical squared difference between the values.
It is small near distance zero and grows with the distance, often levelling off at some range beyond which points are unrelated.
