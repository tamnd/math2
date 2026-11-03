---
tag: WS9M7HY0FE
kind: concept
name: Matrix population model
msc: [92D25, 15B48, 39A60]
specializes: [1YEMFQ1H32]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_population_models
same_as:
  wikidata: Q4284947
  wikipedia: Matrix population models
---

## Summary

A matrix population model is a discrete-time [[population model|1YEMFQ1H32]] in which the population is split into classes, such as ages or stages.
A [[nonnegative matrix|JPQCCFCY8X]] maps the class sizes in one time step to those in the next.
The long-run growth rate is the dominant [[eigenvalue|0BQAA2BK3Q]] of the matrix, and the long-run class proportions are given by the corresponding [[eigenvector|0N6960W0BV]].
These models are standard tools in demography, conservation biology and wildlife management.

## Explanations

### L1 human

Split a plant population into seeds, young plants and adult plants, and count each class every year.
Each year, some seeds sprout, some young plants mature, adults make new seeds, and some of each class die.
All these rates fit in a small table, a matrix, and multiplying the vector of counts by this matrix gives next year's counts.
Repeating the multiplication shows the future: after many years the population grows by a fixed factor each year and the shares of the classes settle down.
