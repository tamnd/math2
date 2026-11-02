---
tag: P546TSFBK2
kind: concept
name: Mahalanobis distance
msc: [62H30, 62H20]
sources:
  - url: https://en.wikipedia.org/wiki/Mahalanobis_distance
same_as:
  wikidata: Q1334846
  wikipedia: Mahalanobis distance
---

## Summary

The Mahalanobis distance measures how far a point lies from the centre of a multivariate distribution.
Its units are adapted to the spread and the correlations of the distribution.
It is the [[Euclidean distance|0NPPGHQNXQ]] after the data are transformed so that the [[covariance matrix|0V7G6WMFK0]] becomes the identity.
It is used to detect outliers and in [[linear discriminant analysis|ZATS7NV9WD]].
The density of a [[multivariate normal distribution|0XN3K7RSZY]] is constant on the sets of constant Mahalanobis distance.

## Explanations

### L1 human

A point that is two units from the mean is unusual in a direction where the data hardly vary, but ordinary in a direction where they vary a lot.
The Mahalanobis distance takes this into account by dividing each direction by its own spread.
Its level sets are ellipses around the mean instead of circles.
Let the first coordinate have variance $4$ and the second variance $1$, with no correlation.
Then the points $(2, 0)$ and $(0, 1)$ are both at Mahalanobis distance $1$ from the origin.
