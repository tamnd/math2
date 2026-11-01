---
tag: NK3CZTVEJD
kind: concept
name: Boolean model
msc: [60D05, 60G55]
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_model_(probability_theory)
same_as:
  wikidata: Q4943358
  wikipedia: Boolean model (probability theory)
---

## Summary

The Boolean model is a random set in $\R^d$.
It is the union of independent random shapes, the grains, placed at the points of a [[Poisson point process|0MTNR28K60]], the germs.
It is the basic germ-grain model of [[stochastic geometry|2J9GB49FHA]].
Many of its mean values have closed formulas.
For example, a given point is covered with probability $1 - e^{-\lambda E[V_d(K)]}$, where $\lambda$ is the intensity and $E[V_d(K)]$ the mean grain volume.
It is used to model porous media, coverage of wireless networks and continuum [[percolation|BH7YPXCYDK]].

## Explanations

### L1 human

Throw points at random over the plane, with no point influencing any other.
Around each point draw a shape, such as a disc whose radius is also chosen at random.
The Boolean model is the union of all these shapes, a random pattern of overlapping blobs.
If all discs have radius $r$ and there are on average $\lambda$ centres per unit area, then each fixed point of the plane is uncovered with probability $e^{-\lambda \pi r^2}$.
With $\lambda \pi r^2 = 1$, about $63\%$ of the plane is covered.
