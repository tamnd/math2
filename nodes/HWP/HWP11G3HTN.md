---
tag: HWP11G3HTN
kind: concept
name: Monte Carlo method
msc: [65C05, 11K45]
sources:
  - url: https://en.wikipedia.org/wiki/Monte_Carlo_method
same_as:
  wikidata: Q232207
  wikipedia: Monte Carlo method
---

## Summary

A Monte Carlo method computes a deterministic quantity approximately by drawing random samples.
In its basic form the quantity is the [[expected value|0WQNRCNY3M]] of a [[random variable|0PNRKMRC55]].
It is estimated by the average of many independent copies.
The [[law of large numbers|0ZVEAYVRC3]] makes the estimate converge.
The [[central limit theorem|0EPZC4Z1FC]] shows that the error decreases like $1/\sqrt{n}$ for $n$ samples, whatever the dimension.
This makes Monte Carlo methods the tool of choice for integrals in high dimension and for complex stochastic models.

## Explanations

### L1 human

To estimate the area of a pond, throw many stones at random into a square field around it and count the fraction that land in the water.
That fraction times the area of the field is close to the area of the pond, and closer when more stones are thrown.
This is a Monte Carlo method: a number that has nothing random about it is found by repeated random experiments.
For example, if $10\,000$ random points in the unit square give $7\,850$ points with $x^2 + y^2 \le 1$, the estimate of $\pi/4$ is $0.785$, so $\pi \approx 3.14$.
The price is slow accuracy: to gain one more decimal digit one needs about a hundred times more samples.
