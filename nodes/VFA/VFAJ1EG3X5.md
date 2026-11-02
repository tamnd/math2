---
tag: VFAJ1EG3X5
kind: concept
name: Nonparametric statistics
msc: [62G05, 62G10]
sources:
  - url: https://en.wikipedia.org/wiki/Nonparametric_statistics
same_as:
  wikidata: Q1097688
  wikipedia: Nonparametric statistics
---

## Summary

Nonparametric statistics is the part of statistics that does not assume the law of the data belongs to a family described by finitely many parameters.
It uses models of infinite dimension, such as all continuous distributions on $\R$ or all smooth densities.
It also includes distribution-free methods, whose behaviour under the null hypothesis does not depend on the unknown law.
Typical tools are the empirical distribution function, rank tests, [[kernel density estimation|ZV65XMJ9A4]] and the bootstrap.

## Explanations

### L1 human

A parametric method assumes, for example, that the data are normal and then only estimates a mean and a variance.
A nonparametric method lets the data speak for the shape of the law.
For instance, a histogram or a kernel density estimate shows the shape of the data without assuming a bell curve.
The price is that more data are needed for the same precision.
