---
tag: 3MKM0DKVHS
kind: concept
name: Probabilistic seismic hazard analysis
msc: [86A15, 62P12, 60G55]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_hazard
---

## Summary

Probabilistic seismic hazard analysis is a method to compute how often a given level of ground shaking is expected to be exceeded at a site.
It combines a model of the earthquake sources, with their rates and [[magnitude distributions|9ZEBGCR93V]], and a model of the ground motion they produce.
The result is a hazard curve: the annual rate of exceedance as a function of the shaking level.
Building codes turn it into design values, such as the shaking with a $10\%$ probability of exceedance in $50$ years.
The method was introduced by C. Allin Cornell and is the standard basis of seismic hazard maps.

## Explanations

### L1 human

Engineers want to know how strongly the ground at a site might shake during the life of a building.
The method lists all faults that could produce earthquakes, how often they produce earthquakes of each size, and how strongly each earthquake would shake the site.
It then adds up the chances of all these scenarios to get how often each level of shaking is exceeded.
For example, a level that is exceeded on average once every $475$ years has about a $10\%$ chance of being exceeded in $50$ years.
